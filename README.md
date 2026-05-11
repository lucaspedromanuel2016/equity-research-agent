# Autonomous Equity Research Agent

An autonomous AI-powered equity research system that generates institutional-style investment memos using Anthropic Claude, financial APIs, SEC EDGAR filings, and structured tool orchestration.

Built as a production-style AI engineering project demonstrating:
- LLM orchestration
- Claude Tool Use
- Financial data integration
- Prompt engineering
- Evaluation harnesses
- Typed schemas
- Production-grade architecture

---

# Features

- Autonomous equity research memo generation
- Prompt versioning system
- Structured Pydantic validation
- SEC EDGAR filing analysis
- Financial statement analysis
- News aggregation + summarization
- Evaluation benchmarking system
- Latency + cost tracking
- pytest testing suite
- Modular architecture
- GitHub Actions CI-ready

---

# Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.11+ |
| LLM | Anthropic Claude API |
| Financial Data | yfinance |
| SEC Filings | sec-edgar-downloader |
| Validation | Pydantic |
| Testing | pytest |
| Env Management | python-dotenv |
| Data Analysis | pandas |
| CLI Output | rich |

---

# Project Architecture

```text
equity-research-agent/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── prompts.py
│   ├── evaluator.py
│   ├── models.py
│   │
│   ├── tools/
│   │   ├── company_overview.py
│   │   ├── financials_tool.py
│   │   ├── news_tool.py
│   │   ├── sec_tool.py
│   │   └── citations.py
│   │
│   ├── schemas/
│   │   ├── memo_schema.py
│   │   └── tool_schema.py
│   │
│   └── utils/
│       ├── logger.py
│       ├── timers.py
│       └── cost_tracker.py
│
├── tests/
├── examples/
├── requirements.txt
├── README.md
└── .env