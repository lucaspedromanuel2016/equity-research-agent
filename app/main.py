from agent import generate_research_memo


def main():
    print("Running Equity Research Agent...\n")

    memo = generate_research_memo("AAPL")

    print("\n=== FINAL RESEARCH MEMO ===\n")

    print(memo.model_dump())


if __name__ == "__main__":
    main()