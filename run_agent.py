from ai_agent import build_agent
from schema import BusinessState
import json

# Create the agent
agent = build_agent()

# Test Data
state: BusinessState = {
    "input_data": {
        "today": {"revenue": 1400, "cost": 1100, "customers": 50},
        "yesterday": {"revenue": 1200, "cost": 900, "customers": 45}
    },
    "metrics": {},
    "recommendations": ""
}