#Artemio Guerrero
#complete
# Write a class named Pet, which should have the following data attributes:
# *__name(for the name of a pet)
# *__animal_type(for the type of animal that pet is. Example values are 'Dog','Cat',and'Bird')
# *__age(for the pets age)

# The Pet class should have an __init__ method that creates these attributes. It shoul dalso have the following mehtods:

# * set_name
# 	This method assigns a value to the __name filed.

# * set_animal_type
# 	This method assigns a value to the __animal_type filed.

# * set_age
# 	This method assigns a value to the __age filed.

# * get_name
# 	This method returns a value to the __name filed.

# * get_name
# 	This method returns a value to the __name filed.

# * get_name
# 	This method returns a value to the __name filed.

class Pets:
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

# ################################################# #
    
    def set_name(self, name):
        self.__name = name


    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age

# ################################################# #

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age