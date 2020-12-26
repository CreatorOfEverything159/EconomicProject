from random import randint


class Seller:  # seller's structure
    def __init__(self, name: str, price: int, quantity_of_goods: int):
        self.name = name  # the seller name
        self.price = price  # the price offered by the seller
        self.quantity_of_goods = quantity_of_goods  # quantity of goods from the seller


class Buyer:  # Buyer's structure
    def __init__(self, name: str, offered_price: int):
        self.name = name  # the buyer name
        self.offered_price = offered_price  # the price offered by the buyer


if __name__ == '__main__':
    quality = 100  # number of iterations
    sellers = list()  # array of sellers
    buyers = list()  # array of buyers

    for i in range(quality):
        sellers.append(Seller(f'Seller{i + 1}', randint(1, 1000), randint(1, 100)))  # creating the seller and assigning a random price
        buyers.append(Buyer(f'Buyer{i + 1}', randint(1, 1000)))  # creating the buyer and assigning a random price

    sellers.sort(key=lambda seller: seller.price)  # sorting in ascending order all sellers from the array by price
    buyers.sort(key=lambda buyer: buyer.offered_price, reverse=True)  # sorting in descending order of all buyers from the array by price

    for i in range(quality):
        price = sellers[i].price  # take the offered price from the seller[i]
        offered_price = buyers[i].offered_price  # take the offered price from the buyer[i]
        seller_name = sellers[i].name  # take the name from the seller[i]
        buyer_name = buyers[i].name  # take the name from the buyer[i]
        quantity = sellers[i].quantity_of_goods  # take the quantity of goods from the seller[i]
        outcome = offered_price // price  # goods outcome
        outcome_price = outcome * price  # buyer can buy total

        if offered_price >= price:
            print(f'\033[32m\033[1m{seller_name} {price}$/paper -> {buyer_name} have {offered_price}$, TOTAL: {outcome} pieces for {outcome_price}$\033[1m')
        else:
            print(f'\033[0m\033[31m{seller_name} {price}$/paper X {buyer_name} have {offered_price}$')
