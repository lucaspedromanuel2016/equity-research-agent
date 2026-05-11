from pydantic import BaseModel
from typing import Optional


class CompanyOverview(BaseModel):
    ticker: str
    company_name: Optional[str]
    sector: Optional[str]
    industry: Optional[str]
    market_cap: Optional[int]
    current_price: Optional[float]
    pe_ratio: Optional[float]
    business_summary: Optional[str]