from app.agent import generate_research_memo


def test_generate_research_memo():

    memo = generate_research_memo(
        ticker="AAPL",
        prompt_version="v1"
    )

    assert memo.ticker == "AAPL"

    assert memo.investment_thesis is not None

    assert len(memo.investment_thesis) > 50