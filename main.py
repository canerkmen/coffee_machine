import data

order = ""
money = 0

def printResources(money):
  
  waterAmount = data.resources.get("water")
  milkAmount = data.resources.get("milk")
  coffeeAmount = data.resources.get("coffee")
  
  print(f"Water : {waterAmount} ml \nMilk : {milkAmount} ml")
  print(f"Coffee {coffeeAmount} gr \nMoney : ${money}")

def printMoney(orderType):
  print("Please insert coins.")
  quarters = int(input("How many quarters ? :"))
  dimes = int(input("How many dimes ? :"))
  nickles = int(input("How many nickles ? :"))
  pennies= int(input("How many pennies ? :"))
  
  amount = amountCalc(quarters, dimes, nickles, pennies)
  cost = costReturner(orderType)
  
  if  amount >= cost:
    return amount - cost
  
  return -1

def amountCheck(orderType):
  
  if data.resources["water"] >= data.MENU[orderType]["ingredients"]["water"] and                             data.resources["coffee"] >= data.MENU[orderType]["ingredients"]["coffee"]:
    if orderType != "espresso":
      data.resources["milk"] >= data.MENU[orderType]["ingredients"]["milk"]
      return True
    return True
  return False

def amountUpdate(orderType):
  
  data.resources["water"] -= data.MENU[orderType]["ingredients"]["water"]
  data.resources["coffee"] -= data.MENU[orderType]["ingredients"]["coffee"]
  if orderType != "espresso":
    data.resources["milk"] -= data.MENU[orderType]["ingredients"]["milk"]

def costReturner(orderType):
  return data.MENU[orderType]["cost"]

def amountCalc(quarters, dimes, nickles, pennies):
  amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
  return amount

def moneyCheck(orderType, quarters, dimes, nickles, pennies):
  
  amount = amountCalc(quarters, dimes, nickles, pennies)
  
  if costReturner(orderType) >= amount:
    return True

  return False

def orderFunc():
  order = input("What would you like? (espresso/latte/cappuccino):")
  while order.lower() != "espresso" and order.lower() != "latte" and order.lower() != "cappuccino" and order.lower() != "off":
    order = input("Invalid Process!Try Again!\nWhat would you like? (espresso/latte/cappuccino):")
  return order

while order != "off":
  
  order = orderFunc()
  
  if order == "report":
    printResources(money)
  elif order != "off":
    if amountCheck(order) == True :
      cost = printMoney(order)
    
      if cost == -1:
        print("You don't have enough money.")
      
      else:
        amountUpdate(order)
        print(f"Here is your ${cost:.2f} change.\nEnjoy your drink!")
        money += costReturner(order)
    else:
      print("We don't have enough ingredients.")
  