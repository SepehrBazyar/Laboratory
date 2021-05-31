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

        # This is for Login Menu
        {"name": "Login",
         "authorization_function": core_utility.login_authorization,
         "children_with_authorization": [
                  {"name": "patient",
                    "children":[
                        {"name": "new test",
                            "function":user_view.repr_all_users,
                            "description": "patient new test",
                            },
                    ],
                    "description": "patient menu",
                    },
                    {"name": "doctor",
                    "children":[
                        {"name": "update test",
                            "function":user_view.repr_all_users,
                            "description": "doctor update test",
                            },
                    ],
                    "description": "doctor menu",
                    },
                    {"name": "admin",
                    "children":[
                        {"name": "update test",
                            "function":user_view.repr_all_users,
                            "description": "doctor update test",
                            },
                    ],
                    "description": "admin menu",
                    },
                    {"name": "manager",
                    "children":[
                        {"name": "update test",
                            "function":user_view.repr_all_users,
                            "description": "doctor update test",
                            },
                    ],
                    "description": "manager menu",
                    },

              # todo: add all options for highest priority user(admin) as children and delete function
         ],
         "description": "Login Users",
         },

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
