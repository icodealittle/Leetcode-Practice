"""
https://medium.com/javarevisited/25-software-design-interview-questions-to-crack-any-programming-and-technical-interviews-4b8237942db0
You need to write code to implement a Vending machine that has a bunch of products
 like chocolates, candy, cold-drink, and accept some coins like Nickle, Dime, Quarter,
  Cent, etc. Make sure you insert a coin, get a product back, and get your change back.
   Also, write the Unit test to demonstrate that these common use cases work.
   If you get stuck you can read my two-part articles (part1 and part 2) about solving these
    classical system design questions.
"""

products = {'chocolates': 2.0, 'candy': 1.0, 'cold-drink': 3.0, 'chips': 1.50}
coins = {"Twenty": 20, "Ten": 10, "Five": 5.0, "Dollar": 1.0, "Quarter": 0.25}
accepted_tender = ['Quarter', "Dollar", "Five", "Ten", "Twenty"]


def vending_machine(tender, product_choice):
    if product_choice not in products.keys():
        return "This product does not exist"
    if coins.get(tender) < products.get(product_choice):
        return "You are broke."
    # Person gives us $5, "Choco"
    change = coins.get(tender) - products.get(product_choice)
    if change > 0:
        return product_choice, convert_change(change), change
    else:
        return product_choice


def convert_change(change):
    correct_change = []
    while change > 0:
        for key, value in coins.items():
            if change - value >= 0:
                change = change - value
                correct_change.append(key)

    return count_keys(correct_change)


def count_keys(arr):
    l = {}
    for i in arr:
        if i not in l.keys():
            l[i] = 1
        else:
            l[i] += 1
    if l["Quarter"] == 4:
        l["Quarter"] = 0
        l["Dollar"] += 1
    if l['Five'] == 2:
        l["Five"] = 0
        l["Ten"] +=1
    return l


def main():
    user_input = ""
    tender = ""
    while user_input not in products and tender not in accepted_tender:
        user_input = str(input(f"Please enter a product choice. \n {products}"))
        tender = str(input(f"Please enter money choice. \n {accepted_tender}"))
    print(vending_machine(tender, user_input))


if __name__ == '__main__':
    main()
