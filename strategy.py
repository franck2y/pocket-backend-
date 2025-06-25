import pandas as pd
import ta

def get_signal(candles: list):
    df = pd.DataFrame(candles)
    df = df.rename(columns={"close": "Close", "high": "High", "low": "Low", "open": "Open"})

    df["EMA"] = ta.trend.ema_indicator(df["Close"], window=14)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)

    last_row = df.iloc[-1]

    if last_row["RSI"] < 30 and last_row["Close"] > last_row["EMA"]:
        return "call"
    elif last_row["RSI"] > 70 and last_row["Close"] < last_row["EMA"]:
        return "put"
    else:
        return None