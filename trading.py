from bs4 import BeautifulSoup
import requests
from config import POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD

# Client fictif pour exécution de trade
class PocketOptionAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0.0

    def trade(self, asset, direction, amount):
        # Simulation : random gagnant/perdant
        import random
        success = random.choice([True, False])
        if success:
            self.balance += amount * 0.8
        else:
            self.balance -= amount
        return {"success": success, "balance": self.balance}

    def get_info(self):
        session = requests.Session()

        # Connexion
        login_url = "https://pocketoption.com/en/login/"
        data = {
            "email": self.email,
            "password": self.password
        }
        session.post(login_url, data=data)

        # Récupération du solde depuis la page mobile
        account_url = "https://m.pocketoption.com/fr/cabinet/demo-quick-high-low/"
        res = session.get(account_url)
        soup = BeautifulSoup(res.text, "html.parser")

        # Extraction du texte contenant "RECHARGER LE COMPTE"
        balance_text = soup.find(text=lambda t: "RECHARGER LE COMPTE" in t)

        if balance_text:
            raw = balance_text.strip().split("RECHARGER")[0]
            try:
                self.balance = float(raw.replace(",", ".").strip())
            except:
                self.balance = 0.0
        else:
            self.balance = 0.0

        return {"email": self.email, "balance": self.balance}

# Instance unique de l’API
client = PocketOptionAPI(POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD)

def execute_trade(asset, direction, amount):
    return client.trade(asset, direction, amount)

def get_account_info():
    return client.get_info()
