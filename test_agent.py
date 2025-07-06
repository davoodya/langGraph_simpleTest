from schema import BusinessState
from ai_agent import input_node, processing_node, recommendation_node

input_data = {
    "today": {
        "revenue": 1200,
        "cost": 800,
        "customers": 40
    },
    "yesterday": {
        "revenue": 1000,
        "cost": 700,
        "customers": 35
    },
    "metrics": {},
    "recommendations": ""
}

def test_input_node():
    state: BusinessState = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 35}
        },
        "metrics": {},
        "recommendations": ""
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
        "recommendations": ""
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

def test_recommendation_node():
    state: BusinessState = {
        "input_data": {},
        "metrics": {
            "profit": -200,
            "revenue_change_pct": 10,
            "cost_change_pct": 15,
            "today_cac": 25,
            "yesterday_cac": 20,
            "cac_change_pct": 25
        },
        "recommendations": ""
    }

    result = recommendation_node(state)
    rec = result["recommendations"]

    assert "Profit" in rec
    assert "CAC" in rec
    assert "Sales" in rec
    print("Recommendation Node(3) Test passed!")

def test_negative_values():
    # New test for Negative Values in processing_node
    negative_state: BusinessState = {
        "input_data": {
            "today": {"revenue": -500, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 35}
        },
        "metrics": {},
        "recommendations": ""
    }

    result = processing_node(negative_state)
    assert result["metrics"]["profit"] == -1300
    assert result["metrics"]["revenue_change_pct"] == -150.0  # (-500 - 1000)/1000 * 100
    print("Processing Node(2) with Negative Value Test passed!")

if __name__ == "__main__":
    test_input_node()
    test_processing_node()
    test_negative_values()
    test_recommendation_node()