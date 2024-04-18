from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_coffee():
  coffee_machine = CoffeeMaker()
  money_machine = MoneyMachine()
  menu = Menu()

  done = False
  while not done:
      options = menu.get_items()
      order = input(f"  What would you like? ({options}): ")
      if order == "report":
          coffee_machine.report()
          money_machine.report()
      elif order == "off":
          done = True
      else:
          drink = menu.find_drink(order)
          if coffee_machine.is_resource_sufficient(drink):
              success = money_machine.make_payment(drink.cost)
              if success:
                  coffee_machine.make_coffee(drink)

make_coffee()