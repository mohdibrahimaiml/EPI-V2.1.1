#!/usr/bin/env python3
"""Test agent using EPI Python API"""
import time
from epi_recorder import record

# This uses the EPI Python API to properly record steps
with record("test_structure.epi", workflow_name="Structure Test") as session:
    print("Testing EPI structure...")
    
    # Log some test steps
    session.log_step("MARKET", {
        "message": "Test market data",
        "price": 185.43
    })
    time.sleep(0.1)
    
    session.log_step("RISK_CHECK", {
        "message": "Test risk check",
        "status": "PASS"
    })
    time.sleep(0.1)
    
    session.log_step("EXECUTION", {
        "message": "Test execution",
        "value": 92715.00
    })
    
    print("Recording complete")
