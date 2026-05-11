import yfinance as yf

from schemas.company_schema import CompanyOverview


def get_company_overview(ticker: str) -> CompanyOverview:
    """
    Fetch basic company overview data.
    """

    stock = yf.Ticker(ticker)

    info = stock.info

    return CompanyOverview(
        ticker=ticker.upper(),
        company_name=info.get("longName"),
        sector=info.get("sector"),
        industry=info.get("industry"),
        market_cap=info.get("marketCap"),
        current_price=info.get("currentPrice"),
        pe_ratio=info.get("trailingPE"),
        business_summary=info.get("longBusinessSummary"),
    )