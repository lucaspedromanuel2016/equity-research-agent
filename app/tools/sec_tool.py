from sec_edgar_downloader import Downloader


def download_sec_filings(ticker: str):
    """
    Download latest SEC filings for a company.
    """

    dl = Downloader(
        company_name="Equity Research Agent",
        email_address="lucaspedromanuel@gmail.com",
        download_folder="sec_data"
    )

    dl.get(
        "10-K",
        ticker,
        limit=1,
    )

    return {
        "status": "success",
        "ticker": ticker.upper(),
    }