from random import randint


class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name


class Seller(Person):
    def __init__(self, name: str, price: int):
        super().__init__(name)
        self._price = price

    def get_price(self) -> int:
        return self._price


class Buyer(Person):
    def __init__(self, name: str, offered_price: int):
        super().__init__(name)
        self._offered_price = offered_price

    def get_offered_price(self) -> int:
        return self._offered_price


if __name__ == '__main__':
    N = 10
    MIN_SELLER_PRICE = 1
    MIN_BUYER_OFFERED_PRICE = 1
    MAX_SELLER_PRICE = 1000
    MAX_BUYER_OFFERED_PRICE = 700

    sellers = list()
    buyers = list()

    for i in range(N):
        sellers.append(Seller(f'Seller{i + 1}', randint(MIN_SELLER_PRICE, MAX_SELLER_PRICE)))
        buyers.append(Buyer(f'Buyer{i + 1}', randint(MIN_BUYER_OFFERED_PRICE, MAX_BUYER_OFFERED_PRICE)))

    sellers.sort(key=lambda seller: seller.get_price())
    buyers.sort(key=lambda buyer: buyer.get_offered_price(), reverse=True)

    for i in range(N):
        price = sellers[i].get_price()
        offered_price = buyers[i].get_offered_price()
        seller_name = sellers[i].get_name()
        buyer_name = buyers[i].get_name()
        if offered_price >= price:
            print(f'{seller_name} ({price}) -> {buyer_name} ({offered_price})')
        else:
            print(f'{seller_name} ({price}) X {buyer_name} ({offered_price})')
