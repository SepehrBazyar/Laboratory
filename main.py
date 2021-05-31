import menu
import user.menu_view as user_view
import Lab.Lab_view as Lab_view
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
         "access_dict": {"patient": "1", "operator": ["1", "2"], "doctor": ["1", "3"], "manager": ["1", "3", "4"],
                         "admin": ["1", "2", "5"]},
         "children_with_authorization": [

             {"name": "patient",
              "children": [
                  {"name": "new test",
                   "children": [
                       {"name": "Covid19 test",
                        "function": Lab_view.cv19_view,
                        "description": "Covid19 test",
                        },
                   ],
                   "description": "patient new test",
                   },
                  {"name": "result",
                   "function": Lab_view.result,
                   "description": "patient result",
                   },
              ],
              "description": "patient menu",
              },

             {"name": "operator",
              "children": [
                  {"name": "new test",
                   "children": [
                       {"name": "Covid19 test",
                        "function": Lab_view.cv19_view,
                        "description": "Covid19 test",
                        },
                   ],
                   "description": "register new test",
                   },
                  {"name": "update test",
                   "function": Lab_view.update_test,
                   "description": "operator update test",
                   },
                  {"name": "all tests",
                   "function": Lab_view.repr_all_test,
                   "description": "all tests list",
                   },
                  {"name": "all patients",
                   "function": user_view.repr_all_patients,
                   "description": "all patients list",
                   },
              ],
              "description": "operator menu",
              },

             {"name": "doctor",
              "children": [
                  {"name": "update test",
                   "function": Lab_view.update_test,
                   "description": "doctor update test",
                   },
                  {"name": "all tests",
                   "function": Lab_view.repr_all_test,
                   "description": "all tests list",
                   },
                  {"name": "all patients",
                   "function": user_view.repr_all_patients,
                   "description": "all patients list",
                   },
              ],
              "description": "doctor menu",
              },

             {"name": "manager",
              "children": [
                  {"name": "confirm test",
                   "function": Lab_view.update_test,
                   "description": "manager confirm test",
                   },
                  {"name": "all tests",
                   "function": Lab_view.repr_all_test,
                   "description": "all tests list",
                   },
                  {"name": "all patients",
                   "function": user_view.repr_all_patients,
                   "description": "all patients list",
                   },
                  {"name": "all doctors",
                   "function": user_view.repr_all_doctors,
                   "description": "all doctors list",
                   },
                  {"name": "all operators",
                   "function": user_view.repr_all_operators,
                   "description": "all operators list",
                   },
              ],
              "description": "manager menu",
              },

             {"name": "admin",
              "children": [
                  {"name": "register doctor",
                   "function": user_view.register_doctor,
                   "description": "register new doctor",
                   },
                  {"name": "register operator",
                   "function": user_view.register_operator,
                   "description": "register new operator",
                   },
                  {"name": "manage tests",
                   "function": Lab_view.manage_test,
                   "description": "managing tests",
                   },
                  {"name": "manage users",
                   "function": user_view.manage_users,
                   "description": "managing users",
                   },
              ],
              "description": "admin menu",
              },
         ],
         "description": "Login Users",
         },

        # This is for Register Menu
        {"name": "Register",
         "function": user_view.register,
         "description": "Register Users",
         },
    ],
    "description": ""
}
# initialize setup(create admin, ...)
initialize_setup()

menu = menu.utility.generate_menu(menu_dic)
menu()
