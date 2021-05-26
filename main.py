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
         "function": hello_world,
         "description": "Login Users",
         },

        # This is for Register Menu
        {"name": "Register",
         "children": [
             {"name": "Register as a Patient",
              "description": "Register Patients",
              "function": user_view.patient_register},
             {"name": "Register as a Doctor",
              "description": "Register Doctors",
              "function": user_view.doctor_register},
             {"name": "Register as a Operator",
              "description": "Register Operators",
              "function": user_view.operator_register},
             {"name": "Register as a Managers",
              "description": "Register Managers",
              "function": user_view.manager_register},
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
