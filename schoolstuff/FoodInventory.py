def main():
    product_names = ["hamburger", "cheeseburger", "small fries"]
    product_costs = [0.99, 1.29, 1.49]
    quants = [10, 5, 20]

    mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

    while mode != "q":
        if mode == "s":
            prod = input("Enter a product nsme: ")
            if prod in product_names:
                print("We sell", prod, "at", product_costs[product_names.index(prod)])
            print()
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        elif mode == "l":
            print("Product", format("Price", ">20"), format("Quantity", ">10"))
            for i in range(len(product_names)):
                print(format(product_names[i], "<22"), format(format(product_costs[i], ".2f"), "<7"), format(quants[i], "<5"))
            print()
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        elif mode == "a":
            item = input("Enter a new product name: ")
            while item in product_names:
                print("Sorry, we already sell that product. Try again.")
                item = input("Enter a new product name: ")
            cost = float(input("Enter a product cost: "))
            while cost <= 0:
                print("Invalid cost. Try again.")
                cost = float(input("Enter a product cost: "))
            quantity = int(input("How many of these products do we have? "))
            while quantity <= 0:
                print("Invalid quantity. Try again.")
                quantity = int(input("How many of these products do we have? "))
            product_names.append(item)
            product_costs.append(cost)
            quants.append(quantity)
            print("Product added!\n")
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        elif mode == "r":
            prod = input("Enter a product nsme: ")
            while prod not in product_names:
                print("Product doesn't exist. Can't remove.")
                prod = input("Enter a product nsme: ")
            else:
                i = product_names.index(prod)
                del product_names[i]
                del product_costs[i]
                del quants[i]
                print("Product removed!\n")
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        elif mode == "u":
            prod = input("Enter a product nsme: ")
            while prod not in product_names:
                print("Product doesn't exist. Can't update.")
                prod = input("Enter a product nsme: ")
            print("What would you like to update?")
            prodattr = input("(n)ame, (c)ost or (q)uantity: ")
            i = product_names.index(prod)
            if prodattr == "n":
                new_name = input("Enter a new name: ")
                while new_name == prod:
                    print("Duplicate name!")
                    new_name = input("Enter a new name: ")
                product_names[i] = new_name
                print("Product name has been updated\n")
            elif prodattr == "c":
                new_cost = float(input("Enter a new cost: "))
                while new_cost <= 0:
                    print("Invalid cost!")
                    new_cost = float(input("Enter a new cost: "))
                product_costs[i] = new_cost
                print("Product cost has been updated\n")
            elif prodattr == "q":
                new_quant = int(input("Enter a new quantity: "))
                while new_quant <= 0:
                    print("Invalid quantity!")
                    new_quant = int(input("Enter a new quantity: "))
                quants[i] = new_quant
                print("Product quantity has been updated\n")
            else:
                print("Invalid option\n")
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        elif mode == "e":
            total = 0
            for i in product_costs:
                total += i * quants[product_costs.index(i)]
            print(format("Most expensive product:", "<28"), max(product_costs), "(" + str(product_names[product_costs.index(max(product_costs))]) + ")")
            print(format("Least expensive product:", "<28"), min(product_costs), "(" + str(product_names[product_costs.index(min(product_costs))]) + ")")
            print(format("Total value of all products:", "<28"), format(total, ".2f"))
            print()
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        else:
            print("Invalid option, try again")
            mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    else:
        print("See you soon!")


main()


