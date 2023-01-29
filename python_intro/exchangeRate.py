import httpx
from termcolor import colored


def get_data():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    return httpx.get(url)


def define_rates():
    data = get_data()
    rows = data.text.split("\n")[2:-1]
    res = {}
    for r in rows:
        r_data = r.split("|")
        res[r_data[-2]] = float(float(r_data[-1].replace(",", ".")) / float(r_data[2]))
    return res


def get_start_currency():
    while True:
        try:
            start_curr = input("Zadejte měnu, ze které chcete převádět (nic pro CZK): ")
            if start_curr == "":
                start_curr = "CZK"
            if start_curr != "CZK" and not start_curr in rates.keys():
                raise ValueError()
            break
        except ValueError:
            print(colored("Zadejte platnou měnu", "red"))
    while True:
        try:
            amount = float(input("Zadejte počet " + start_curr + ": "))
            if not amount > 0.0:
                raise ValueError()
            break
        except ValueError:
            print(colored("Zadejte platné množství", "red"))
    return {"curr": start_curr, "amount": amount}


def get_end_currency():
    while True:
        try:
            end_curr = input("Zadejte měnu, na kterou chcete převádět (nic pro EUR): ")
            if end_curr == "":
                end_curr = "EUR"
            if end_curr != "CZK" and not end_curr in rates.keys():
                raise ValueError()
            return end_curr
        except ValueError:
            print(colored("Zadejte platnou měnu", "red"))


def calculate_exchange():
    if end_curr == start_curr["curr"]:
        return start_curr["amount"]

    if end_curr == "CZK":
        return start_curr["amount"] * rates[start_curr["curr"]]
    elif start_curr["curr"] == "CZK":
        return start_curr["amount"] / rates[end_curr]
    else:
        return (start_curr["amount"] * rates[start_curr["curr"]]) / rates[end_curr]


print(colored("Kurzovní lístek", "yellow"))

rates = define_rates()
start_curr = get_start_currency()
end_curr = get_end_currency()
exchange = calculate_exchange()
# if start_curr is stronger than end_curr
stronger = "green" if exchange > start_curr["amount"] else "red"

print(
    colored(str(start_curr["amount"]) + " " + start_curr["curr"], "blue")
    + colored(" =====> ", "yellow")
    + colored(str(exchange) + " " + end_curr, stronger)
)
