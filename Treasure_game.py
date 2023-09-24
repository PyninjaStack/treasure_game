
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right":\n').lower() #("\ backslash in the line means it escape the string and see as text")
#nroad = road.lower()
if road == "left":
        lake = input("you come to a lake. There is an island in the middle of the lake. Tpye 'wait' to wait for the boat.Type 'swim' to swim across:\n").lower()
        #nlake = lake.lower()
        if lake == "wait":
                doar = input("You arrive at the island unharmed. There is a house with 3 doors. 'one red', 'one yellow' and 'one blue'. which colour do you choose?\n").lower()
                #ndoar = doar.lower()
                if doar == "red":
                    print("Burned by fire.\nGame Over")
                elif doar == "blue":
                    print("Eaten by beasts.\nGame Over")
                elif doar == "yellow":
                    print("You have found the Treasure.\nYou win")
                else:
                     print("You have choose the wrong Door.\n")
                #else:
                    #print("You Win")
        else:
            print("Attacked by trout.\nGame Over")
else:
    print("Fall into a hole.\nGame Over")
                      

                     
  