from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from trading import execute_trade, get_account_info
from models import TradeRequest
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

signals_log = []

@app.post("/trade")
def trade(req: TradeRequest):
    result = execute_trade(req.asset, req.direction, req.amount)
    signals_log.append({
        "asset": req.asset,
        "direction": req.direction,
        "amount": req.amount,
        "result": result,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return result

@app.get("/status")
def status():
    return get_account_info()

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "signals": signals_log})
