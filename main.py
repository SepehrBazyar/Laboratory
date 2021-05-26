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
    "name": "Main Menu",
    "children": [
        # This is for Login Menu
        {"name": "Login",
         "children": [
             {"name": "Login as a Patient",
              "description": "Login Patients",
              "function": print("hello Patient")},
             {"name": "Login as a Doctor",
              "description": "Login Doctors",
              "function": print("hello Doctor")},
             {"name": "Login as a Operator",
              "description": "Login Operators",
              "function": print("hello Operator")},
             {"name": "Login as a Managers",
              "description": "Login Managers",
              "function": print("hello Managers")},
         ],
         "description": "Login Users",
         },

        # This is for Register Menu
        {"name": "Register",
         "children": [
             {"name": "Register as a Patient",
              "description": "Register Patients",
              "function": user_view.register},
             {"name": "Register as a Doctor",
              "description": "Register Doctors",
              "function": user_view.register},
             {"name": "Register as a Operator",
              "description": "Register Operators",
              "function": user_view.register},
             {"name": "Register as a Managers",
              "description": "Register Managers",
              "function": user_view.register},
         ],
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

menu = menu.utility.generate_menu(menu_dic)
menu()
