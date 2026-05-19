# # class Student:
# #     def __init__(self, name):
# #         self.name = name

# #         s1 = Student("ravan")
# #         print(s1.name)
# #         del s1

# #private methods  and public 

# # class Student:
# #     def __init__(self, name):
# #         self.name = name

# #         s1 = Student("ravan")
# #         print(s1.name)  # public attribute
# #         del s1

# # class Account:
# #     def __init__(self,  acc_no, acc_psw):
# #        self.account_number = acc_no
# #        self.__account_password = acc_psw  # private attribute we put __ before the variable name to make it private

# #        def reset_password(self, new_password):
# #            self.__account_password = new_password  # method to reset the password


# # acc1  = Account(12345, "abc")

# # print(acc1.account_number)  # Accessing public attribute

# # print(acc1.__account_password)  # Attempting to access private attribute (will raise an error)
# # print(acc1.reset_password("new_password"))  # Attempting to reset password (will raise an error)
# # acc1




# class Student:
#     def __init__(self, name):
#         self.name = name   # public attribute


# s1 = Student("Ravan")
# print(s1.name)

# del s1   # deletes the object


# class Account:
#     def __init__(self, acc_no, acc_psw):
#         self.account_number = acc_no          # public attribute
#         self.__account_password = acc_psw    # private attribute

#     def reset_password(self, new_password):
#         self.__account_password = new_password
#         print("Password changed successfully")


# acc1 = Account(12345, "abc")

# print(acc1.account_number)   # accessible

# # print(acc1.__account_password)
# # This will give an error because it is private

# acc1.reset_password("new_password")


class Person:
    __name = "mitsu"

    def __hello(self):
        print("Hello, my name is", self.__name)

        def welcome(self):
            print("Welcome to the world of Python!")