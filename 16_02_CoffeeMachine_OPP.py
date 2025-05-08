from D_16_Menu import Menu
from D_16_coffee_maker import CoffeeMaker
from D_16_MoneyMachine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()

is_on= True
my_menu = Menu()

while is_on:
  options = my_menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    my_money_machine.report()
    my_coffee_maker.report()
  else:
    drink = my_menu.find_drink(choice)
    if my_coffee_maker.is_resource_sufficient(drink) and (
      my_money_machine.make_payment(drink.cost)):
      my_coffee_maker.make_coffee(drink)

