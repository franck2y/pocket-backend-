from pydantic import BaseModel

class TradeRequest(BaseModel):
    asset: str
    direction: str  # "BUY" or "SELL"
    amount: float
