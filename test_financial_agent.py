#!/usr/bin/env python3
"""
Financial Trading Agent - High-Stakes AI Decision Simulator

This agent demonstrates a realistic financial AI workflow:
1. Market data analysis
2. Risk assessment
3. Compliance checks
4. Trade execution

All steps are captured by EPI Recorder for audit trails.
"""

import time
import json
from datetime import datetime

def print_step(emoji, message, delay=0.3):
    """Print a step with visual formatting"""
    print(f"{emoji} {message}")
    time.sleep(delay)

def main():
    print("\n" + "="*70)
    print("🏦 FINANCIAL AI AGENT - LIVE TRADING SIMULATION")
    print("="*70 + "\n")
    
    # Step 1: Market Analysis
    print_step("📊", "Analyzing real-time market data...")
    print_step("   ", "└─ Fetching AAPL stock price: $185.43")
    print_step("   ", "└─ Analyzing 50-day moving average: $178.21")
    print_step("   ", "└─ Sentiment analysis score: +0.847 (bullish)")
    print_step("✓", "Market analysis complete\n", 0.5)
    
    # Step 2: Risk Assessment
    print_step("⚖️", "Running risk assessment models...")
    print_step("   ", "└─ Portfolio exposure check: PASSED")
    print_step("   ", "└─ Volatility index (VIX): 14.2 (acceptable)")
    print_step("   ", "└─ Maximum drawdown limit: WITHIN BOUNDS")
    print_step("✓", "Risk check PASSED\n", 0.5)
    
    # Step 3: Compliance Verification
    print_step("🔐", "Verifying regulatory compliance...")
    print_step("   ", "└─ SEC Rule 15c3-1 (Net Capital): COMPLIANT")
    print_step("   ", "└─ FINRA 4210 (Margin Requirements): COMPLIANT")
    print_step("   ", "└─ MiFID II transaction reporting: ENABLED")
    print_step("✓", "Compliance verification PASSED\n", 0.5)
    
    # Step 4: Trade Execution
    trade_data = {
        "timestamp": datetime.now().isoformat(),
        "action": "BUY",
        "symbol": "AAPL",
        "quantity": 500,
        "price": 185.43,
        "total_value": 92715.00,
        "confidence": 0.847,
        "rationale": "Strong bullish momentum + low volatility + compliance verified"
    }
    
    print_step("🚀", "EXECUTING TRADE...")
    print("\n" + "─" * 70)
    print(f"   ACTION:     {trade_data['action']}")
    print(f"   SYMBOL:     {trade_data['symbol']}")
    print(f"   QUANTITY:   {trade_data['quantity']} shares")
    print(f"   PRICE:      ${trade_data['price']}")
    print(f"   TOTAL:      ${trade_data['total_value']:,.2f}")
    print(f"   CONFIDENCE: {trade_data['confidence']*100:.1f}%")
    print("─" * 70)
    
    time.sleep(0.8)
    
    # Save trade record
    with open('trade_record.json', 'w') as f:
        json.dump(trade_data, f, indent=2)
    
    print("\n✅ TRADE EXECUTED SUCCESSFULLY")
    print("📄 Trade record saved to: trade_record.json")
    
    print("\n" + "="*70)
    print("🔒 All actions captured by EPI Recorder for audit trail")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
