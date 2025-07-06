from ai_agent import build_agent
from schema import BusinessState
import math


def test_full_agent():
    agent = build_agent()

    # add test data for a process all things say in resume
    input_data: BusinessState = {
        "input_data": {
            "today": {
                "revenue": 1500,
                "cost": 1300,
                "customers": 50
            },
            "yesterday": {
                "revenue": 1000,
                "cost": 900,
                "customers": 45
            }
        },
        "metrics": {},
        "recommendations": ""
    }

    # Run the agent and get the result & recommendations
    result = agent.invoke(input_data)

    metrics = result["metrics"]
    recommendations = result["recommendations"]