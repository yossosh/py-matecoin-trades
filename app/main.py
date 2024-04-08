import json
from decimal import Decimal


def calculate_profit(trades_information_file: str) -> None:
    with open(trades_information_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])
        if bought:
            bought_volume = Decimal(bought)
            earned_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume
        elif sold:
            sold_volume = Decimal(sold)
            earned_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)
