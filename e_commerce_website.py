users={}
def register():
    username=input("enter user name")
    password=input("enter password")

    if username in users:
        print("user name already exsists")
    else:
        users[username]=password
        print("registratoin successful")
def login():
    global logged_in
    username=input("enter user name")
    password=input("enter password")
    if username in users:
        if users[username] == password:
            print("login successful")
            logged_in=True
        else:
            print("enter valid credentials")
    else:
        print("user does not exsists ,register")




products={'electronics':{'laptop':55000,'mobile':10000,'head phones':1000},
             'clothing':{ "shirt": 800,"jeans": 1200,"jacket": 2500},
             'accessories':{"watch": 3000,"Bag": 1500,"sunglasses": 1000}
             }

cart=[]
logged_in=False
while True:
    print("menu")
    print("1.register")
    print("2.login")
    print("3.view categories")
    print("4.search product")
    print("5.add to cart")
    print("6.remove from cart")
    print("7.place order")
    print("8.Exit")
    n=int(input())
    match n:
        case 1:
            register()
        case 2:
            login()
        case 3:
            if not logged_in:
                print("please login first")
            else:
                print("view all the categories")
                for category in products:
                    print(category ,":",end=" ")
                    for item in products[category]:
                        print(item,end=" ")
                    print()
            
        case 4:
             if not logged_in:
                print("please login first")
             else:
                print("serach for your product what would you like to search")
                found=False
                item=input().strip()
                for category in products:
                    if item in products[category]:
                        print("product found and price is",products[category][item])
                        found=True
                        break
                if not found:
                    print("item not in the category list")
        case 5:
             if not logged_in:
                print("please login first")
             else:
                found=False
                item=input("enter item to add to cart")
                for category in products:
                    if item in products[category]:
                        cart.append(item)
                        found=True
                        print("added to cart")
                        break
                if not found:
                    print("item not in the category")
        case 6:
             if not logged_in:
                print("please login first")
             else:
                item=input("enter item you would like to remove from cart")
                if item in cart:
                    cart.remove(item)
                    print("item removed fom the cart")
                else:
                    print("item not found")
        case 7:
             if not logged_in:
                print("please login first")
             else:
                if not cart:
                    print("cart empty")
                else:
                    tot=0
                    print("items in cart")
                    for item in cart:
                        print(item)
                        for category in products:
                            if item in products[category]:
                                tot+=products[category][item]
                    print("tot bill",tot)
                    print("order placed successfully")
                    cart.clear()
        case 8:
            print("thankyou visit again")
            break
        case _:
            print("enter valid choice")
            
                
