import menu
import user.menu_view as user_view


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
    "children": [{
        "name": "register",
        "description": "register user",
        "function": user_view.register
    },
        {
            "name": "list users",
            "description": "list users",
            "function": user_view.repr_all_users
        }
    ],
    "description": ""

}
menu = menu.utility.generate_menu(menu_dic)
menu()
