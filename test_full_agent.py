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

    # 1. Calculate profit
    expected_profit = 1500 - 1300
    assert metrics["profit"] == expected_profit, f"Expected profit: {expected_profit}, Got: {metrics['profit']}"

    # 2. Calculate the percentage of revenue change
    revenue_change = ((1500 - 1000) / 1000) * 100
    assert math.isclose(metrics["revenue_change_pct"], revenue_change, abs_tol=0.1)

    # 3. Calculate the percentage of cost change
    cost_change = ((1300 - 900) / 900) * 100
    assert math.isclose(metrics["cost_change_pct"], cost_change, abs_tol=0.1)

    # 4. Today & Yesterday CAC
    today_cac = 1300 / 50
    yesterday_cac = 900 / 45
    cac_change_pct = ((today_cac - yesterday_cac) / yesterday_cac) * 100
    assert math.isclose(metrics["today_cac"], today_cac, abs_tol=0.1)
    assert math.isclose(metrics["yesterday_cac"], yesterday_cac, abs_tol=0.1)
    assert math.isclose(metrics["cac_change_pct"], cac_change_pct, abs_tol=0.1)

    # 5. Check the recommendations
    # if profit is low assert the Profit is negative
    if expected_profit < 0:
        assert "Profit is negative" in recommendations

    # if CAC is growing assert CAC has increased significantly in recommendations
    if cac_change_pct > 20:
        assert "CAC has increased significantly" in recommendations

    # If revenue_change is growing, assert Sales have grown in recommendations
    if revenue_change > 0:
        assert "Sales have grown" in recommendations

    print("Full Agent Logic & Recommendation Test passed!")


if __name__ == "__main__":
    test_full_agent()