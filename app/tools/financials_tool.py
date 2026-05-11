import yfinance as yf


def get_financial_statements(ticker: str) -> dict:
    """
    Fetch financial statement data using yfinance.
    """

    stock = yf.Ticker(ticker)

    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow

    return {
        "ticker": ticker.upper(),
        "income_statement": financials.to_dict(),
        "balance_sheet": balance_sheet.to_dict(),
        "cash_flow": cashflow.to_dict(),
    }