from app.tools.company_overview import get_company_overview


def test_company_overview():

    result = get_company_overview("AAPL")

    assert result.ticker == "AAPL"

    assert result.company_name is not None

    assert result.market_cap is not None