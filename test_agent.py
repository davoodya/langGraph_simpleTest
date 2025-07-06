from schema import BusinessState
from ai_agent import input_node, processing_node

input_data = {
    "today": {
        "revenue": 1200,
        "cost": 800,
        "customers": 40
    },
    "yesterday": {
        "revenue": 1000,
        "cost1": 700,
        "customers": 35
    },
    "metrics": {},
    "recommendation": ""
}

def test_input_node():
    state: BusinessState = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 35}
        },
        "metrics": {},
        "recommendation": ""
    }

    result = input_node(state)
    assert result["input_data"]["today"]["revenue"] == 1200
    print("Input Node(1) Test passed!")

def test_processing_node():
    state: BusinessState = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 600, "customers": 30}
        },
        "metrics": {},
        "recommendation": ""
    }

    # Running node
    result = processing_node(state)
    metrics = result["metrics"]

    assert metrics["profit"] == 400
    assert round(metrics["revenue_change_pct"], 1) == 20.0
    assert round(metrics["cost_change_pct"], 1) == 33.3
    assert round(metrics["today_cac"], 1) == 20.0
    assert round(metrics["yesterday_cac"], 1) == 20.0
    assert round(metrics["cac_change_pct"], 1) == 0.0

    print("Processing Node(2) Test passed!")


if __name__ == "__main__":
    test_input_node()
    test_processing_node()