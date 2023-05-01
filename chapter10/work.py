import random

# class Coin:
#     def __init__(self):
#         self.sideup = 'Heads'

#     def toss(self):
#         if random.randint(0,1) == 0:
#             self.sideup = 'Heads'
#         else:
#             self.sideup = 'Tails'
#     def get_sideup(self):
#         return self.sideup
        

# def main():
#     mycoin = Coin()

#     print('This sideis up :', mycoin.get_sideup())

#     print('I am tossing the coin...')

#     mycoin.toss()

#     print('This side is up:' , mycoin.get_sideup())

# main()


# Exercise:
# Create a class named "Person" with two data attributes, "name" and "age". Then create two methods, "greet" and "celebrate_birthday". The "greet" method should print a greeting message that includes the person's name, while the "celebrate_birthday" method should increase the person's age by 1 and print a message acknowledging the new age.

# Next, create two instances of the "Person" class named "Alice" and "Bob". Set Alice's name to "Alice" and age to 25, and set Bob's name to "Bob" and age to 30. Call the "greet" method for each person, and then call the "celebrate_birthday" method for each person. Finally, call the "greet" method for each person again to see their updated ages.
# nums = [1,3,7,9,2]
# target = 11
# def findTwoSum(nums,target):
#     for i in range(len(nums)):
#         numTwofind = target - nums[i]

#         for j in range(i + 1, len(nums)):
#             if nums[j] == numTwofind:
#                 print([i,j])
#     return None
# findTwoSum(nums,target)


# nums = []
# target = 7
# def findTwoSums(nums,target):
#     for i in range(len(nums)):
#         num_to_find = target - nums[i]

#         for j in range(i + 1,len(nums)):
#             if nums[j] == num_to_find:
#                 print([i,j])
#             else:
#                 print("Null")

# findTwoSums(nums,target)