import menu
import user.menu_view as user_view
from core.service import initialize_setup
import core.utility as core_utility


class Manage:
    "ertebat beyne baqie class ha"
    pass


class Output:
    pass


class Input:
    pass


menu_dic = {
    "name": "Main Menu",
    "children": [

        # This is for Register Menu
        {"name": "Register",
         "function": user_view.register,
         "description": "Register Users",
         },

        # {
        #     "name": "list users",
        #     "description": "list users",
        #     "function": user_view.repr_all_users
        # }
    ],
    "description": ""

}
# initialize setup(create admin, ...)
initialize_setup()

menu = menu.utility.generate_menu(menu_dic)
menu()
