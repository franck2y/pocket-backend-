from config import POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD

# Simulation - remplace ça par l'import réel de ton API
class PocketOptionAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 100.0

    def trade(self, asset, direction, amount):
        # logique fictive, à remplacer par API WebSocket ou HTTP réelle
        import random
        success = random.choice([True, False])
        if success:
            self.balance += amount * 0.8
        else:
            self.balance -= amount
        return {"success": success, "balance": self.balance}

    def get_info(self):
        return {"email": self.email, "balance": self.balance}

# Crée un seul client global
client = PocketOptionAPI(POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD)

def execute_trade(asset, direction, amount):
    return client.trade(asset, direction, amount)

def get_account_info():
    return client.get_info()
