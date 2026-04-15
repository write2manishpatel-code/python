buy_amount = float(input("please enter the actual product price: ")) #20
sale_amount = float(input("please enter the sale price amount: ")) #40



if sale_amount > buy_amount:

    profit = sale_amount - buy_amount
    print("total profit ", profit)

else:
    print("NO PROFIT!!!!")