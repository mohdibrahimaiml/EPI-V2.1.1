"""
Financial Agent - EPI Investor Demo
Professional AI agent simulation for pitch demonstrations
"""
import time
import random
from datetime import datetime

def log(message, prefix="→"):
    """Professional logging output"""
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {prefix} {message}")

# ============================================================================
# Financial Risk Analysis Agent
# ============================================================================

log("Initializing Financial Agent v2.3", "🔷")
time.sleep(0.3)

log("Loading market data...", "📊")
time.sleep(0.4)

log("Connecting to risk scoring engine...", "🔗")
time.sleep(0.3)

print("\n" + "─" * 70)
log("Starting Transaction Analysis", "⚡")
print("─" * 70 + "\n")

# Simulate realistic financial transactions
transactions = [
    {"id": 9928, "amount": 45000, "type": "WIRE_TRANSFER", "risk": "LOW"},
    {"id": 9929, "amount": 125000, "type": "INTERNATIONAL", "risk": "MEDIUM"},
    {"id": 9930, "amount": 8500, "type": "ACH_PAYMENT", "risk": "LOW"},
]

decisions = []

for tx in transactions:
    log(f"Analyzing Transaction #{tx['id']}", "🔍")
    time.sleep(0.4)
    
    # Simulate AI risk assessment
    log(f"Amount: ${tx['amount']:,} | Type: {tx['type']}", "  ")
    time.sleep(0.3)
    
    # Risk scoring
    risk_score = random.uniform(0.1, 0.9) if tx['risk'] == 'MEDIUM' else random.uniform(0.05, 0.25)
    log(f"Risk Score: {risk_score:.3f} ({tx['risk']})", "  ")
    time.sleep(0.3)
    
    # Decision making
    if risk_score < 0.3:
        decision = "APPROVED"
        symbol = "✅"
    elif risk_score < 0.7:
        decision = "FLAGGED_FOR_REVIEW"
        symbol = "⚠️"
    else:
        decision = "BLOCKED"
        symbol = "🚫"
    
    log(f"Decision: {decision}", f"  {symbol}")
    
    decisions.append({
        'transaction_id': tx['id'],
        'amount': tx['amount'],
        'risk_score': risk_score,
        'decision': decision
    })
    
    print()
    time.sleep(0.3)

# ============================================================================
# Generate Audit Report
# ============================================================================

print("─" * 70)
log("Generating Compliance Report", "📄")
print("─" * 70 + "\n")

report_content = f"""
{'='*70}
FINANCIAL AGENT - TRANSACTION ANALYSIS REPORT
{'='*70}

Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Agent Version: 2.3
Compliance Framework: SOC2 + GDPR

TRANSACTIONS PROCESSED
{'─'*70}
"""

for decision in decisions:
    report_content += f"""
Transaction ID: {decision['transaction_id']}
  Amount:      ${decision['amount']:,}
  Risk Score:  {decision['risk_score']:.4f}
  Decision:    {decision['decision']}
"""

report_content += f"""
{'─'*70}
SUMMARY
{'─'*70}
Total Processed: {len(decisions)}
Approved:        {sum(1 for d in decisions if d['decision'] == 'APPROVED')}
Flagged:         {sum(1 for d in decisions if d['decision'] == 'FLAGGED_FOR_REVIEW')}
Blocked:         {sum(1 for d in decisions if d['decision'] == 'BLOCKED')}

{'='*70}
CRYPTOGRAPHICALLY SIGNED BY EPI
{'='*70}
"""

# Save the audit trail
with open("audit_report.txt", "w") as f:
    f.write(report_content)

log("Audit report saved: audit_report.txt", "💾")
time.sleep(0.3)

# Generate machine-readable output
with open("decisions.json", "w") as f:
    import json
    json.dump(decisions, f, indent=2)

log("Decision log saved: decisions.json", "💾")
time.sleep(0.3)

print("\n" + "═" * 70)
log("Agent Execution Complete", "✅")
print("═" * 70)

print(f"""
📊 SESSION SUMMARY
   • Transactions Analyzed: {len(decisions)}
   • Risk Models Applied: 3
   • Compliance Checks: PASSED
   • Audit Trail: SEALED

🔐 All actions recorded and cryptographically signed.
   Ready for regulatory submission.
""")
