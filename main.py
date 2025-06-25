from fastapi import FastAPI
from trading import execute_trade, get_account_info
from pydantic import BaseModel

app = FastAPI()

# Modèle de requête pour les trades
class TradeRequest(BaseModel):
    asset: str
    direction: str  # "call" ou "put"
    amount: float

# Endpoint pour vérifier le compte
@app.get("/status")
def status():
    return get_account_info()

# Endpoint pour exécuter un trade
@app.post("/trade")
def trade(req: TradeRequest):
    result = execute_trade(req.asset, req.direction, req.amount)
    return {"result": result}
