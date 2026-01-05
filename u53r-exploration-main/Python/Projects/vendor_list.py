

while True:

    products = {
        "surf": "Unilever",
        "ariel": "P&G",
        "tide": "P&G",
        "rexona": "Unilever",
        "dove": "Unilever",
        "lays": "PepsiCo",
        "coke": "Coca-Cola",
        "sprite": "Coca-Cola",
        "nutella": "Ferrero",
        "ferrero rocher": "Ferrero",
        "kinder": "Ferrero",
        "m&ms": "Mars",
        "snickers": "Mars",
        "mars": "Mars",
        "oreo": "Mondelez",
        "cadbury": "Mondelez",
        "milka": "Mondelez",
        "nivea": "Beiersdorf",
        "head & shoulders": "P&G",
        "colgate": "Colgate-Palmolive",
        "breeze": "Unilever",
        "tops": "Unilever",
        "wings detergent": "Wings Group",
        "pepsi": "PepsiCo",
        "7up": "PepsiCo",
        "delmonte": "Disposal",
        "downy": "P&G",
        "pantene": "P&G",
    }



    item = input("Type product name: ").strip().lower()

    print(products.get(item, "No record found."))
    for i in range(5):
            print(".")