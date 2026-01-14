"""
Create a Sample EPI File for Public Distribution
This generates a professional demo .epi file to showcase on GitHub and website
"""

import sys
import io
import time

# Force UTF-8 encoding for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from epi_recorder import record
from pathlib import Path

def main():
    print("\n" + "="*70)
    print("  CREATING PUBLIC SAMPLE .EPI FILE")
    print("  This will be uploaded to GitHub and epilabs.org")
    print("="*70 + "\n")
    
    # Create the public sample
    with record(
        "sec_compliant_aapl_trade.epi",
        workflow_name="SEC-Compliant Algorithmic Trade",
        goal="Demonstrate EPI's capabilities for regulatory compliance",
        notes="Public sample showing cryptographically signed trading evidence",
        metadata_tags=["demo", "finance", "sec-compliance", "public-sample"]
    ) as session:
        
        print("[OK] EPI Recording started!\n")
        
        # Step 1: Market Analysis
        print("[STEP 1] Market Analysis")
        session.log_step("market.analysis", {
            "symbol": "AAPL",
            "price": 178.25,
            "rsi": 62.5,
            "volume_delta": "+15%",
            "signal": "bullish"
        })
        print("  Symbol: AAPL")
        print("  Current Price: $178.25")
        print("  RSI: 62.5 (Bullish)")
        print("  Volume: +15% above average")
        print()
        time.sleep(1)
        
        # Step 2: Risk Assessment
        print("[STEP 2] Risk Assessment")
        session.log_step("risk.assessment", {
            "portfolio_exposure": 0.12,
            "max_drawdown_risk": 0.032,
            "sharpe_ratio": 1.85,
            "decision": "WITHIN_LIMITS"
        })
        print("  Portfolio Exposure: 12%")
        print("  Max Drawdown Risk: 3.2%")
        print("  Sharpe Ratio: 1.85")
        print("  Decision: WITHIN RISK LIMITS ✓")
        print()
        time.sleep(1)
        
        # Step 3: Trade Execution
        print("[STEP 3] Trade Execution")
        trade_details = {
            "action": "BUY",
            "quantity": 500,
            "order_type": "LIMIT",
            "limit_price": 178.20,
            "expected_value": 89100.00,
            "trade_id": "TR-2026-01-0278"
        }
        session.log_step("trade.execution", trade_details)
        print("  Action: BUY")
        print("  Quantity: 500 shares")
        print("  Order Type: LIMIT")
        print("  Limit Price: $178.20")
        print("  Expected Value: $89,100.00")
        print()
        time.sleep(1)
        
        # Step 4: Compliance
        print("[STEP 4] Compliance Check")
        session.log_step("compliance.validation", {
            "framework": ["MiFID II", "Dodd-Frank"],
            "wash_sale_rule": "PASS",
            "circuit_breaker": "PASS",
            "pre_trade_risk": "PASS"
        })
        print("  Regulatory Framework: MiFID II + Dodd-Frank")
        print("  Wash Sale Rule: PASS ✓")
        print("  Circuit Breaker: PASS ✓")
        print("  Pre-Trade Risk: PASS ✓")
        print()
        time.sleep(1)
        
        # Final Result
        print("[RESULT] Trade Approved and Logged")
        print("  Trade ID: TR-2026-01-0278")
        print(f"  Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print("  Status: EXECUTED")
        print()
        
        session.log_step("workflow.completed", {
            "status": "success",
            "trade_id": "TR-2026-01-0278",
            "total_value": 89100.00
        })
    
    print("="*70)
    print("  ✅ PUBLIC SAMPLE CREATED!")
    print("  📦 File: sec_compliant_aapl_trade.epi")
    print("  🔐 Status: Cryptographically Signed")
    print("="*70)
    print()
    print("Next Steps:")
    print("  1. Verify:  epi verify sec_compliant_aapl_trade.epi")
    print("  2. View:    epi view sec_compliant_aapl_trade.epi")
    print("  3. Upload to GitHub Releases and epilabs.org")
    print()

if __name__ == "__main__":
    main()
