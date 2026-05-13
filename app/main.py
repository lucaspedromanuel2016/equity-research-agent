from pathlib import Path
from agent import generate_research_memo


def save_memo(ticker: str, memo):
    """
    Save generated memo to markdown file.
    """

    memo_dir = Path("memo")
    memo_dir.mkdir(exist_ok=True)

    file_path = memo_dir / f"{ticker.lower()}_memo.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(memo.investment_thesis)

    print(f"\nMemo saved to: {file_path}")


def main():
    """
    Main application entry point.
    """

    print("Running Equity Research Agent...\n")

    ticker = "AAPL"

    memo = generate_research_memo(ticker)

    print("\n========== GENERATED MEMO ==========\n")
    print(memo.investment_thesis)

    save_memo(ticker, memo)


if __name__ == "__main__":
    main()