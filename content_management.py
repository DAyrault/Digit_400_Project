def Content():
    APP_CONTENT= {
        "Home":[["Add Item","/additem/"], 
                ["View Cart", "/viewcart/"]],
        "Messages":[["Checkout","/checkout/"]],
        "Settings":[["Set Cart Preferences","/setpreferences/"]],
        "Profile":[["User Profile","/profile/"],
                   ["Terms of Service","/tos/"],
                   ["Delete Account","/deleteaccount/"]]
    }
    return APP_CONTENT