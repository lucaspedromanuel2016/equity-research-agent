"""
Evaluation harness for the Equity Research Agent.

Measures:
- latency
- estimated cost
- memo quality
- prompt version performance
"""

import time
import csv
from datetime import datetime

from agent import generate_research_memo


# ============================================================
# CONFIGURATION
# ============================================================

TEST_TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA"
]

PROMPT_VERSIONS = [
    "v1",
    "v2",
    "v3"
]


# ============================================================
# MANUAL SCORING MOCKS
# (Later you can automate these)
# ============================================================

QUALITY_SCORES = {
    "v1": 1.5,
    "v2": 2.1,
    "v3": 2.6,
}


# ============================================================
# COST ESTIMATION
# ============================================================

def estimate_cost(char_count: int) -> float:
    """
    Rough token cost estimation.

    This is simplified for demo purposes.
    """

    estimated_tokens = char_count / 4

    # Example approximation
    estimated_cost = estimated_tokens * 0.000003

    return round(estimated_cost, 4)


# ============================================================
# MAIN EVALUATION LOOP
# ============================================================

def run_evaluation():
    """
    Run benchmark evaluation across prompt versions.
    """

    results = []

    print("\nStarting Evaluation Harness...\n")

    for version in PROMPT_VERSIONS:

        for ticker in TEST_TICKERS:

            print("=" * 70)
            print(f"Running {ticker} with {version}")
            print("=" * 70)

            start_time = time.time()

            try:

                memo = generate_research_memo(
                    ticker=ticker,
                    prompt_version=version
                )

                end_time = time.time()

                latency = round(end_time - start_time, 2)

                memo_text = memo.investment_thesis

                char_count = len(memo_text)

                estimated_cost = estimate_cost(char_count)

                result = {
                    "timestamp": datetime.now().isoformat(),
                    "ticker": ticker,
                    "prompt_version": version,
                    "latency_seconds": latency,
                    "estimated_cost_usd": estimated_cost,
                    "memo_characters": char_count,
                    "manual_quality_score": QUALITY_SCORES[version],
                    "status": "success"
                }

                print("\nEvaluation Result:")
                print(result)

            except Exception as e:

                result = {
                    "timestamp": datetime.now().isoformat(),
                    "ticker": ticker,
                    "prompt_version": version,
                    "latency_seconds": None,
                    "estimated_cost_usd": None,
                    "memo_characters": 0,
                    "manual_quality_score": 0,
                    "status": f"failed: {str(e)}"
                }

                print("\nFAILED:")
                print(result)

            results.append(result)

    save_results(results)

    print("\nEvaluation Completed.")


# ============================================================
# SAVE CSV RESULTS
# ============================================================

def save_results(results: list):
    """
    Save evaluation results to CSV.
    """

    filename = "evaluation_results.csv"

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:

        fieldnames = [
            "timestamp",
            "ticker",
            "prompt_version",
            "latency_seconds",
            "estimated_cost_usd",
            "memo_characters",
            "manual_quality_score",
            "status"
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in results:
            writer.writerow(row)

    print(f"\nResults saved to {filename}")


# ============================================================
# ENTRYPOINT
# ============================================================

if __name__ == "__main__":
    run_evaluation()