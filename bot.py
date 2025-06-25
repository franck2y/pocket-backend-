from PocketOptionAPI import PocketOptionClient
from strategy import get_signal
from config import *

import time
import random

client = PocketOptionClient(email=EMAIL, password=PASSWORD)
current_amount = MISE_INITIALE

@client.on("connected")
def handle_connected():
    print("✅ Connecté à Pocket Option.")
    start_bot_loop()

def start_bot_loop():
    global current_amount
    while True:
        for symbol in ACTIFS:
            try:
                print(f"🔍 Analyse de l’actif : {symbol}")
                candles = client.get_candles(symbol=symbol, interval=TIMEFRAME, limit=100)
                signal = get_signal(candles)
                if signal:
                    print(f"📈 Signal détecté : {signal} sur {symbol} | montant : {current_amount}$")
                    result = client.buy(symbol, amount=current_amount, direction=signal, duration=DUREE_TRADE)
                    if not result:
                        print("❌ Échec du trade.")
                        continue

                    time.sleep(DUREE_TRADE + 2)
                    trade_result = client.get_last_trade_result()

                    if trade_result and trade_result["profit"] > 0:
                        print("✅ Trade GAGNANT ! Reset martingale.")
                        current_amount = MISE_INITIALE
                    else:
                        print("❌ Trade PERDANT. Martingale...")
                        current_amount *= MARTINGALE_COEFF

                    time.sleep(1)
                else:
                    print(f"⏳ Aucun signal pour {symbol}")
                time.sleep(2 + random.uniform(0, 3))
            except Exception as e:
                print(f"⚠️ Erreur pour {symbol} : {e}")
        time.sleep(5)

client.connect()