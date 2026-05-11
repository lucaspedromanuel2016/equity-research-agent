from pydantic import BaseModel
from typing import List


class EquityResearchMemo(BaseModel):
    ticker: str
    investment_thesis: str
    bullish_signals: List[str]
    bearish_risks: List[str]
    valuation_summary: str
    final_recommendation: str
    citations: List[str]