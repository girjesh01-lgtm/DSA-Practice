"""
You are going on a camping trip, but before you leave you need to buy groceries. To optimize your time spent in the store, instead of buying the items from your shopping list in order, you plan to buy everything you need from one department before moving to the next.

Given an unsorted list of products with their departments and a shopping list, return the time saved in terms of the number of department visits eliminated.

Example:
products = [
    ["Cheese",          "Dairy"],
    ["Carrots",         "Produce"],
    ["Potatoes",        "Produce"],
    ["Canned Tuna",     "Pantry"],
    ["Romaine Lettuce", "Produce"],
    ["Chocolate Milk",  "Dairy"],
    ["Flour",           "Pantry"],
    ["Iceberg Lettuce", "Produce"],
    ["Coffee",          "Pantry"],
    ["Pasta",           "Pantry"],
    ["Milk",            "Dairy"],
    ["Blueberries",     "Produce"],
    ["Pasta Sauce",     "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
5-3=2
For example, buying the items from list1 in order would take 5 department visits, whereas your method would lead to only visiting 3 departments, a difference of 2 departments.

Produce(Blueberries)->Dairy(Milk)->Pantry(Coffee/Flour)->Dairy(Cheese)->Produce(Carrots) = 5 department visits
New: Produce(Blueberries/Carrots)->Pantry(Coffee/Flour)->Dairy(Milk/Cheese) = 3 department visits

list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"] => 2
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"] => 0
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"] => 2
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"] => 0

All Test Cases:
shopping(products, list1) => 2
shopping(products, list2) => 2
shopping(products, list3) => 0
shopping(products, list4) => 2
shopping(products, list5) => 0

Complexity Variable:
n: number of products
"""

products = [
    ["Cheese", "Dairy"],
    ["Carrots", "Produce"],
    ["Potatoes", "Produce"],
    ["Canned Tuna", "Pantry"],
    ["Romaine Lettuce", "Produce"],
    ["Chocolate Milk", "Dairy"],
    ["Flour", "Pantry"],
    ["Iceberg Lettuce", "Produce"],
    ["Coffee", "Pantry"],
    ["Pasta", "Pantry"],
    ["Milk", "Dairy"],
    ["Blueberries", "Produce"],
    ["Pasta Sauce", "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"]
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"]
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"]
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"]


def min_visits(products, input_list):
    # create a dictionary for department and product compile
    dept_prod_dict = {}
    for item in products:

        if (item[1] in dept_prod_dict):
            print("inside if")
            dept_prod_dict[item[1]].append(item[0])

        else:
            dept_prod_dict[item[1]] = [item[0]]

    max_visits = 0
    min_visits = 0
    prev_dep = ""
    for product in input_list:
        current_dep = dept_prod_dict[product]
        if (prev_dep != current_dep):
            max_visits += 1


min_visits(products, list1)