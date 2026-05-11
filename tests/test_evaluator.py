from app.evaluator import estimate_cost


def test_estimate_cost():

    result = estimate_cost(1000)

    assert result > 0