import yfinance as yf

from schemas.news_schema import NewsArticle


def get_company_news(ticker: str) -> list[NewsArticle]:
    """
    Fetch recent company news.
    """

    stock = yf.Ticker(ticker)

    news_items = stock.news

    articles = []

    for item in news_items[:5]:
        article = NewsArticle(
            title=item.get("title"),
            publisher=item.get("publisher"),
            link=item.get("link"),
        )

        articles.append(article)

    return articles