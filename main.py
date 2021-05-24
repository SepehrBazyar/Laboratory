import menu


class Manage:
    "ertebat beyne baqie class ha"
    pass


class Output:
    pass


class Input:
    pass

def hello_world():
    print("hello")

menu_dic = {
    "name": "main menu",
    "children": [{"name": "register",
                  "description": "register user",
                  "function": hello_world
                  }],
    "description": ""

}
menu = menu.utility.generate_menu(menu_dic)
menu()

