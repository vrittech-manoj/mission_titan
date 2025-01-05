# import random
# import datetime
# import time
# class Rocket:
#    def __init__(self):
#      get_rocket = {1: (
#             "   ^   ",
#             "  / \\  ",
#             " /   \\ ",
#             "/     \\",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|     |",
#             "|_____|",
#             "///|\\\  ",
# "-------------------------------------------------------------------------------------------------------------  ",
# )}

#             # Printing each line of the rocket
#      for line in get_rocket[1]:
#         print(line)

#      def rocket_lunch(self,time,earth,sky):
#         self.time = time
#         self.earth = earth
#         self.sky = sky

#      def get_time(self):
#         print("\nStart Time is Starting : ")
#         if self.warnings == 0:
#             print("Your vehicle is in excellent condition!")
#             print("It is ready to launch!")
#             time.sleep(3)
#             for i in range(10, 0, -1):
#                 print(i)
#             time.sleep(1)
#             current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             print(f"Titan has launched successfully at {current_time}....")
# object = Rocket()
# print(object.get_time)
# print(object.get_rocket)            




import datetime
import random
import time


rocket = {1: (
    "    ^    ",
    "   / \\   ",
    "  /   \\  ",
    " /     \\ ",
    "--------- ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|       |  ",
    "|_______|  ",
   "--///|\\-- ",  # Corrected escape sequence for backslashes
"----------------------------------------------------------------------------------------------------------------",
)}

# Printing each line of the rocket
for line in rocket[1]:
    print(line)



current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Start is lucha a Titan {current_time} is time")
print("It is ready to launch!")
# print(f"Titan has launched successfully at {current_time}....")
# print(f"Time is start {time.time()}")
# Countdown from -10 to 0
print("\nStarting countdown...")
for i in range(-10, 1):  # From -10 to 0
    print(i)
    time.sleep(1)  # Pauses for 1 second
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Titan has launched successfully at {current_time}....")
print(f"Titan hes ben go to sky in {current_time} is ")
# If you're trying to print the current time, use this instead:
# Representation of birds attacking the rocket using symbols
bird = """
        ----
    --      --
--            --
----    ----
--      --
        --
"""
print(f"\nBird attack incoming!\n{bird}")
action = input("Do you want to defend your Titen? (yes/no): ").lower()
if action != 'yes':
    print("The birds have damaged the Titen! You lost health points!")
    print("Mission terminated due to some problems....")            

else:
    print("You successfully defended against the birds! No damage done.")

print(f"Titan cross in the earth in {current_time} in space")
print("Titen is go to space and safe leand ")
print("Congralutaion! You are Win ")
print("Level 2 is start")

