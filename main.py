from random import randint, shuffle

class Seller:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Buyer:
    def __init__(self, name: str, offered_price: int):
        self.name = name
        self.offered_price = offered_price


if __name__ == '__main__':
    quality = 100
    sellers = list()
    buyers = list()
    for i in range(quality):
        sellers.append(Seller(f'Seller{i + 1}', randint(1, 1000)))
        buyers.append(Buyer(f'Buyer{i + 1}', randint(1, 1000)))

    # shuffle(sellers)
    # shuffle(buyers)

    sellers.sort(key=lambda seller: seller.price)
    buyers.sort(key=lambda buyer: buyer.offered_price, reverse=True)

    for i in range(quality):
        price = sellers[i].price
        offered_price = buyers[i].offered_price
        seller_name = sellers[i].name
        buyer_name = buyers[i].name
        if offered_price >= price:
            print(f'{seller_name} ({price}) -> {buyer_name} ({offered_price})')
        else:
            print(f'{seller_name} ({price}) X {buyer_name} ({offered_price})')
