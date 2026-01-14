
import time
from epi_recorder import record

# "Evidence Container" - Portable, Immutable, Verifiable.
evidence_file = "SEC_Compliant_Trade_AAPL.epi"

# We use 'notary' to emphasize this is a LEGAL/CRYPTOGRAPHIC act, not a logging act.
with record(evidence_file, workflow_name="Algorithmic_Trade_Audit", auto_sign=True) as notary:
    print()
    print(">> [PROTOCOL] Session started. Sealing state transitions...")
    print("=" * 60)

    # 1. STATE: Market Context (What did the AI see?)
    print(">> [AGENT] Ingesting OPRA market feed...")
    notary.log_step("STATE_INGEST", {
        "symbol": "AAPL", 
        "price": 185.43, 
        "volume": "45.2M", 
        "sentiment": "POSITIVE"
    })
    time.sleep(0.2)

    # 2. STATE: The Logic Fork (Why did it decide?)
    print(">> [AGENT] Computing Technical Indicators (SMA-50)...")
    notary.log_step("STATE_REASONING", {
        "indicator": "SMA_50", 
        "value": 178.21, 
        "signal": "BUY_SIGNAL", 
        "confidence": 0.94
    })
    time.sleep(0.2)

    # 3. STATE: The Regulatory Gate (The Rainmatter/Fintech Hook)
    print(">> [AGENT] Verifying SEC 15c3-1 Net Capital Rule...")
    notary.log_step("COMPLIANCE_GATE", {
        "rule": "15c3-1", 
        "check": "Net_Capital_Adequacy", 
        "result": "PASS",
        "timestamp": time.time()
    })
    time.sleep(0.2)

    # 4. STATE: Execution (The Action)
    print(">> [AGENT] Committing Trade Order...")
    trade = {"action": "BUY", "symbol": "AAPL", "qty": 500, "notional": 92715.00}
    notary.log_step("STATE_COMMIT", trade)
    time.sleep(0.2)
    
    print("=" * 60)
    print(f">> [PROTOCOL] Evidence Sealed: {evidence_file}")
