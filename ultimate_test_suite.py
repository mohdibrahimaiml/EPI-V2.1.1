"""
Final Comprehensive Verification for EPI v2.1.3
1. Verifies Core Recording (no regressions)
2. Verifies Gemini Patcher SUCCESS case (via mock)
3. Verifies Chat Command SUCCESS case (via integration test)
"""
import sys
import os
import json
import shutil
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add parent dir to path
sys.path.append(os.getcwd())

from epi_recorder import record
from epi_core.container import EPIContainer
from epi_cli.main import app
from typer.testing import CliRunner

runner = CliRunner()

class TestEPIv213(unittest.TestCase):
    
    def setUp(self):
        # Clean up old recordings
        if os.path.exists("epi-recordings"):
            shutil.rmtree("epi-recordings")
        os.makedirs("epi-recordings", exist_ok=True)

    def test_01_core_regression(self):
        """Verify standard python recording still works (No Regressions)"""
        print("\n[TEST] Core Regression: Recording standard script...")
        
        with record("core_test.epi"):
            print("Hello World")
            x = 10 * 10
        
        # Verify file exists
        self.assertTrue(os.path.exists("core_test.epi"))
        
        # Verify integrity
        manifest = EPIContainer.read_manifest(Path("core_test.epi"))
        self.assertEqual(manifest.spec_version, "1.1-json")
        print("   [PASS] Core recording created and verified")

    @patch("google.generativeai.GenerativeModel")
    @patch("google.generativeai.configure")
    def test_02_gemini_patcher_success(self, mock_config, mock_model_cls):
        """Verify patch_gemini captures SUCCESSFUL responses correctly"""
        print("\n[TEST] Gemini Patcher: Verifying SUCCESS capture...")
        
        # Setup Mock
        mock_instance = MagicMock()
        mock_model_cls.return_value = mock_instance
        mock_instance.model_name = "gemini-2.0-flash"
        
        # Mock Response
        mock_response = MagicMock()
        mock_response.text = "This is a successful AI response."
        mock_response.usage_metadata.prompt_token_count = 10
        mock_response.usage_metadata.candidates_token_count = 20
        mock_response.usage_metadata.total_token_count = 30
        mock_instance.generate_content.return_value = mock_response

        # Run recording
        with record("gemini_mock.epi"):
            # We must import inside the patched environment usually, 
            # but here we rely on the patcher having hooked into the sys.modules or imported lib
            # Since epi_recorder imports it, we need to ensure patch_gemini() was called.
            # It is called automatically by @record/with record.
            
            # Simulate user code
            import google.generativeai as genai
            model = genai.GenerativeModel("gemini-2.0-flash")
            model.generate_content("Hello AI")

        # Verify Capture
        temp_dir = EPIContainer.unpack(Path("gemini_mock.epi"))
        steps_file = temp_dir / "steps.jsonl"
        
        with open(steps_file) as f:
            steps = [json.loads(line) for line in f]
            
        # Check Request
        req = next(s for s in steps if s['kind'] == 'llm.request')
        self.assertEqual(req['content']['provider'], 'google')
        self.assertIn("Hello AI", req['content']['contents'])
        
        # Check Response
        res = next(s for s in steps if s['kind'] == 'llm.response')
        self.assertEqual(res['content']['provider'], 'google')
        self.assertEqual(res['content']['response'], "This is a successful AI response.")
        self.assertEqual(res['content']['usage']['total_tokens'], 30)
        
        print("   [PASS] Captured Request, Response, and Token Usage correctly")

    def test_03_chat_command_loading(self):
        """Verify 'epi chat' loads evidence correctly"""
        print("\n[TEST] Chat Command: Verifying loading...")
        
        # Create a dummy epi file first
        with record("chat_test.epi") as ctx:
            ctx.log_step("test.event", {"msg": "hello"})
            
        # We can't easily mock the interactive input in unit test without complex piping,
        # but we can verify it doesn't crash on load.
        # Ideally we'd test the `load_steps_from_epi` logic directly.
        
        from epi_cli.chat import load_steps_from_epi
        steps = load_steps_from_epi(Path("chat_test.epi"))
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0]['content']['msg'], "hello")
        
        print("   [PASS] Chat module loaded steps correctly")

if __name__ == '__main__':
    unittest.main(verbosity=2)
