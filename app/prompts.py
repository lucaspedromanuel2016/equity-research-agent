"""
Prompt management system for the Equity Research Agent.

This module provides:
- Prompt versioning
- System prompts
- Memo formatting templates
- Prompt builder helpers

The architecture is designed for:
- prompt experimentation
- evaluation benchmarking
- A/B testing
- production-grade prompt engineering
"""

# ============================================================
# PROMPT VERSION REGISTRY
# ============================================================

PROMPT_VERSIONS = {
    "v1": "baseline",
    "v2": "structured_institutional",
    "v3": "strict_grounded_agent",
}

ACTIVE_PROMPT_VERSION = "v3"


# ============================================================
# SYSTEM PROMPTS
# Controls Claude behavior / reasoning style
# ============================================================

SYSTEM_PROMPTS = {
    "v1": """
You are an equity research analyst.

Provide basic investment insights based on financial data.

Keep responses simple and direct.
""",

    "v2": """
You are a Senior Equity Research Analyst at a top-tier investment firm.

You produce structured, professional investment research.

Rules:
- Be analytical and concise
- Focus on financial performance and risks
- Avoid hype or speculation
- Use institutional tone
""",

    "v3": """
You are a Senior AI Engineer, Quantitative Research Engineer,
and Institutional Equity Research Analyst operating inside a
production-grade financial intelligence system.

Your role is to generate institutional-quality equity research
using structured financial data, SEC filings, and news sources.

STRICT RULES:
- Use ONLY provided tool data
- Never hallucinate financial metrics
- Clearly separate facts vs interpretation
- Prioritize risk analysis over optimism
- Think like a top-tier institutional analyst
- Maintain concise and professional writing
- Ensure all claims are grounded in source data
- Produce structured markdown-ready output
- Include citation awareness in reasoning
"""
}


# ============================================================
# MEMO FORMATS
# Controls output structure / formatting
# ============================================================

MEMO_FORMATS = {
    "v1": """
Simple format:

- Summary
- Opinion
""",

    "v2": """
1. Investment Thesis
2. Bull Case
3. Bear Case
4. Recommendation
""",

    "v3": """
1. Executive Summary
2. Business Overview
3. Recent News Analysis
4. Financial Performance Analysis
5. SEC Filing Insights
6. Bull Case
7. Bear Case
8. Key Risks
9. Valuation Commentary
10. Final Investment Conclusion
11. Source Citations
"""
}


# ============================================================
# GLOBAL MEMO INSTRUCTIONS
# Shared formatting + quality rules
# ============================================================

MEMO_INSTRUCTIONS = """
You must generate a structured equity research memo.

Rules:
- Use concise institutional writing
- Use bullet points where appropriate
- Do NOT fabricate financial numbers
- Clearly distinguish facts from analysis
- Highlight both upside and downside risks
- Keep reasoning grounded in provided tool data
- If information is missing, explicitly state:
  "Data not available"
- Maintain production-quality formatting
- Ensure all major insights are citation-aware
"""


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_prompt(version: str = ACTIVE_PROMPT_VERSION) -> dict:
    """
    Returns prompt configuration for a given version.

    Args:
        version (str): Prompt version key.

    Returns:
        dict: Contains system prompt and memo format.
    """

    if version not in PROMPT_VERSIONS:
        raise ValueError(
            f"Invalid prompt version: {version}"
        )

    return {
        "version": version,
        "name": PROMPT_VERSIONS[version],
        "system": SYSTEM_PROMPTS[version],
        "format": MEMO_FORMATS[version],
    }


def build_research_prompt(
    ticker: str,
    data: dict,
    version: str = ACTIVE_PROMPT_VERSION,
) -> str:
    """
    Builds the main research prompt sent to Claude.

    Args:
        ticker (str): Stock ticker symbol.
        data (dict): Aggregated tool data.
        version (str): Prompt version.

    Returns:
        str: Fully formatted research prompt.
    """

    if version not in PROMPT_VERSIONS:
        raise ValueError(
            f"Invalid prompt version: {version}"
        )

    memo_format = MEMO_FORMATS[version]

    return f"""
[TICKER]
{ticker}

[PROMPT VERSION]
{version} - {PROMPT_VERSIONS[version]}

[MEMO STRUCTURE]
{memo_format}

[GLOBAL INSTRUCTIONS]
{MEMO_INSTRUCTIONS}

[TOOL DATA]
{data}

[CRITICAL RULES]
- Never hallucinate financial data
- Only use provided tool outputs
- Clearly separate facts vs interpretation
- Maintain institutional investment tone
- Prioritize risk-aware analysis
- Use structured markdown formatting
- Ensure conclusions are evidence-based
"""


def get_system_prompt(
    version: str = ACTIVE_PROMPT_VERSION,
) -> str:
    """
    Returns system prompt only.

    Args:
        version (str): Prompt version.

    Returns:
        str: System prompt text.
    """

    if version not in PROMPT_VERSIONS:
        raise ValueError(
            f"Invalid prompt version: {version}"
        )

    return SYSTEM_PROMPTS[version]