class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def ImpureFormula(self, products):
        answer = 0
        for k, v in products.items():
            answer += float(v['unit_price']) * int(v['qnt'])
        return answer

    def totalImpurePrice(self, products):
        total_impure_price = round(self.ImpureFormula(products), 2)
        return total_impure_price

    def DcountFormula(self,products):
        answer = 0
        for k, v in products.items():
            answer += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        return answer

    def totalDiscount(self, products):
        total_discount = round(self.DcountFormula(products), 2)
        return total_discount


    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products)-self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
