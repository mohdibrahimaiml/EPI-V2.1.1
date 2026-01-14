import time
from epi_recorder import record

print("Running agent with auto_sign=True...")

with record("test_signing.epi", workflow_name="SEC-Compliant Trading", auto_sign=True) as epi:
    print("Recording...")
    
    epi.log_step("MARKET_DATA", {"symbol": "AAPL", "price": 185.43})
    time.sleep(0.1)
    
    epi.log_step("RISK_VAR", {"VaR_95": 12500.00})
    time.sleep(0.1)
    
    epi.log_step("EXECUTION", {"action": "BUY", "total": 92715.00})
    time.sleep(0.1)
    
    print("Recording complete")

print("\nAgent finished. Checking signature...")
