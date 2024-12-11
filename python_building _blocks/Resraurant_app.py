#Show the menu to the consumer and accept the food number from the coustomer and serve the food to the customer of his/her choice
menu = {
    1 : "Roti",
    2 : "Naan Roti",
    3 : "Chicken Soup",
    4 : "kheema",
    5 : "Mutton gravy",
    6 : "Yedami",
    7 : "Chicken Biryani",
    8 : "Fish Fry"
}
print("Welcome to our Savji restaurant")

print("\n\n-------------------MENU----------------------\n\n")

print(menu)

food_number = int(input("Enter the food number of your choice :"))

food = menu.get(food_number,'invalid_choice')

if food == 'invalid_choice':
    print("Sorry, You have chosen a invalid food item")
else:
    print(f"Here is your food {food}")

