
#Purpose: Making a Choose Your Own Adventure game Using Lists, Functions, Loops, Variables, and Conditionals
#hint = attacking and exploring stance will make this game greater



"Status: Working"





y=1
f_player_health=250
f_king_health=250
player_health=100
dragon_health=100
king_health=500
collected=False
here_dine=False
here_lib=False
here_jail=False
here_obs=False
here_guard=False
here_arm=False
here_dock=False
def credits():
  print("Coding By:abdurrahman")

def end():
  again=input("Would you like to play again? (y/n) ").lower()
  if again == "n":
    clear()
    print("Thank you for playing!")
    credits()
    time.sleep(2)
    exit()
  


import time
import random

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class text:
  End="\033[0m"
  Underlined="\033[4m"
  Italic="\033[3m"
  Bold="\033[1m"
  Red="\033[31m"
  Pink="\033[91m"
  Green="\033[32m"
  Yellow="\033[33m"
  Blue="\033[34m"
  Magenta="\033[35m"
  Cyan="\033[36m"
  White="\033[97m"
  Black="\033[90m"
  Background="\033[40m"
  Background_Red="\033[41m"
  Background_Green="\033[42m"

#Lists:
actions = ["Run","Fight","Scream"]

found = ["sowrd","bow","spear","rock","stick","bone"]

troll_name = ["COLBEY","BEN","EMMA","ASHLEY","KYLE","STOLEB","BILLY","LIAM","JOHN"]

barn_animal = ["Polish Chicken","Rooster","Turkey","Pig","Cow"]

dragon_attacks=["Fire","Lighting","Step","Slam","Swoop"]

king_attacks=["Vision","Terraformation","Fling","Sword"]

weapons=["1. Sword","2. Bow","3. Spear"]

succsess=["1","2"]

heal_stuff=[]

defense_stuff=[]

food_stuff=[]

boom_stuff=[]

battle_stuff=[]
#Functions written below:
def bear_encounter():
  global choice
  print(text.Bold+"Instructions: If a decision pops up, type the number of the option you want to select. If there is no number, write the name of the optain you want to select. If you do it incorrectly you will either die, or get a message telling you to try again."+text.End)
  time.sleep(2)
  print("You gain consciousness. Unsure of where you are. You sit up as the pain of the brush you were laying on hits you. You open your eyes and find yourself in a"+text.Green+" Forest"+text.End+
 ".")
  time.sleep(2)
  print("After getting on your feet you look around. All of a sudden you hear a loud rumbling and rustling in the bushes.")
  time.sleep(2)
  print(text.Bold+"A Bear runs out of the brush! What do you do?"+text.End)
  while True:
    for x in range(len(actions)):
      print("\t"+actions[x])
    choice=input().lower()
    if choice =="run" or choice == "fight" or choice == "scream":
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

  action_consequense1()

def action_consequense1():
  global choice

  if choice == "run":
    clear()
    print("You try to run away but the bear catches you and eats you. "+text.Red+"Game Over."+text.End)
    end()
  elif choice == "fight":
    clear()
    print(text.Bold+"You decide to fight the Bear. You look around for weapons."+text.End)
    time.sleep(2)
    print(text.Underlined+"You find the following:"+text.End)
    time.sleep(1)
    print(text.Red+"1. A Stick")
    time.sleep(1)
    print("2. A Rock")
    time.sleep(1)
    print("3. A Pile of Dirt"+text.End)

    choice=input(text.Bold+"What do you choose? "+text.End+text.Italic+"(enter the number)"+text.End)
    if choice == "1":
      clear()
      print(text.Blue+"You decide to use the stick."+text.End)
      time.sleep(1)
      print("You jab the bears eyes with the stick, blinding it. The bear runs off!")
    elif choice == "2":
      clear()
      print(text.Blue+"You decide to use the rock."+text.End)
      time.sleep(1)
      print("You throw the rock at the bear,\nThe bear runs off!")
    elif choice == "3":
      clear()
      print(text.Blue+"You shove your hand into the ground pulling up a pile of dirt."+text.End)
      time.sleep(1)
      print("You throw the dirt at the bear, it doesnt work and he eats you. "+text.Red+"Game Over"+text.End)
      end()
    else:
      print("That is not a valid Choice. You take too long and the bear eats you. "+text.Red+"Game Over"+text.End)
      end()
  if choice == "scream":
    clear()
    print("You scream, the bear get aggervated by the noise and attacks you. "+text.Red+"Game Over"+text.End)
    end()
  time.sleep(3)
  path_split()

def path_split():
  global choice
  if choice == "1":
    clear()
    print("After that close encounter of the bear you cautiously walk \nthrough the woods, tightly Clutching your stick.")
    time.sleep(2)
    print("You walk for a while, eventually feeling safe enough to drop \nyour stick.")
    time.sleep(2)
  elif choice == "2":
    clear()
    print("After that close encounter of the bear you cautiously walk \nthrough the woods, tightly clutching your rock.")
    time.sleep(2)
    print("You walk for a while, eventually feeling safe enough to drop \nyour rock.")

  path_decision()

def path_decision():
  global choice

  print("You come across a fork in the path.")

  choice = input(text.Bold+"Do you want to go left or right? (left/right)"+text.End)
  if choice == "left":
    print("You decide to take the left path.")
    path_consequense()
  elif choice == "right":
    print("You decide to take the right path.")
    path_consequense()

def path_consequense():
  global choice

  if choice == "left":
    clear()
    print("You walk for a long time. Eventually coming into a clearing about 3 miles down the path. You are very tired after the fight and the long walk.")

    choice = input(text.Bold+"Do you want to stay for a little in the clearing? (yes/no)"+text.End).lower()
    if choice == "yes":
      clear()
      clearing()
    if choice == "no":
      print("You opt out of staying in the clearing. With no other way to go. You turn back.")
      time.sleep(4)
      clear()
      path_decision()

  if choice == "right":
    print("You walk for a little bit down the right path eventually coming across a deep cavern.")   
  choice = input(text.Bold+"Do you want to explore the cavern? (yes/no)"+text.End).lower()
  if choice == "yes":
    clear()
    cavern()
  if choice =="no":
    clear()
    print("You opt out of exploring the cavern. With no other way to go. You turn back.")
    time.sleep(4)
    clear()
    path_decision()

def clearing():
  print("You setup in the clearing")
  clearing_fight()

def cavern():
  print("You decide to explore the cavern.")
  time.sleep(4)
  clear()
  cavern_fight()

def cavern_fight():
  global choice
  tn= random.choice(troll_name)

  print("As you walk into the cavern you get an overwhelming feeling of dread set in. You feel as if your not alone in the cavern.")
  time.sleep(2)
  print("You stop in the middle of an opening. To your left there is a human skeleton on the ground. Shivers go down your spine. Suddenly a entire cave shakes and a huge troll steps into the exit of the cavern.")
  time.sleep(4)

  print(f"The troll opens his mouth an speaks in a loud booming voice that reverbarates off the barren walls. The troll says, I AM  {tn}! THE TROLL GUARDIAN OF THIS PASS. YOU MUST ANSWER MY RIDDLE OR FIGHT ME TO THE DEATH.")
  time.sleep(2)
  print(text.Bold+text.Underlined+"What do you Do:"+text.End)
  options = ["1. Answer The Riddle","2. Fight The Troll"]
  for x in range(len(options)):
    print("\t"+options[x])
  choice=input().lower()

  if choice == "1":
    clear()
    print("You dedide to try the riddle.")
    time.sleep(2)
    print("You walk up to the troll and begin to speak.")
    time.sleep(2)
    print(text.Bold+text.Underlined+"What do you say:"+text.End)
    speech=["1. I shall do your riddle.","2. Tell me your riddle now!"]
    for x in range(len(speech)):
      print("\t"+speech[x])
    choice=input().lower()
    if choice == "1" or "2":
      clear()
      print("VERY WELL THEN. YOU HAVE ONE TRY TO ANSWER MY RIDDLE. IF FAIL YOU SHALL BE KILLED! IF YOU SUCCEED. I WILL LET YOU OUT OF MY CAVERN.")
      time.sleep(3)
      print(text.Underlined+text.Bold+"MY RIDDLE IS THIS."+text.End+text.Red+"\nYOU CAN SEE NOTHING ELSE\nWHEN YOU LOOK IN MY FACE,\nI WILL LOOK YOU IN THE EYE,\nAND I WILL NEVER LIE.\nWHAT AM I?"+text.End)
      time.sleep(3)
      print("You consider the riddle. You come up with three possible answers.")
      riddle=["1. A Statue","2. Your Reflection","3. Glasses"]
      for x in range(len(riddle)):
        print("\t"+riddle[x])
      pick=input().lower()
      if pick == "2":
        print("VERY GOOD! YOU HAVE BESTED ME. YOU MAY EXIT MY CAVERN.")
      else:
        print("YOU FOOL! THE CORRECT ANSWER WAS YOUR REFLECTION. The troll laughs at you before crushing you under its fist."+text.Red+"GAME OVER"+text.End)

    the_countryside()

  if choice == "2":
    clear()
    print("SO YOU HAVE CHOSEN DEATH.. VERY WELL THEN. WE SHALL FIGHT!")
    time.sleep(2)
    print("You have made the decision to fight the troll. You remember the battle with the bear. And get an idea. You quickly look around at the bones you saw earler and see the skeleton has weapons. Just then the troll lifts its arm and swings its fist at the ground.")
    time.sleep(5)
    clear()
    print("You sprint over to the skeleton just missing the huge fist of the troll. You quiclky scavenge the body.")
    print(text.Underlined+text.Bold+"You Find the folowing weapons:"+text.End)
    for x in range(len(weapons)):
      print("\t"+weapons[x])
    weapon_choice=input()
  if weapon_choice == "1":
    print("You have chosen the sword.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()

    if attack_spot=="1":
      clear()
      print("You run and jump onto the trolls arm. You climb up the arm and stab the troll in the eye.")
      print("The troll screams in pain and is now blinded. However, it is not enough to kill the troll. The troll stumbles around and crushes you under its foot."+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="2":
      clear()
      print("You sprint across the cave and jump onto the troll's leg. You slice its leg in half! The troll falls off balance and dies on impact with the floor.")
      print("You arise vicotrius and run as fast as you can out of the exit.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="3":
      clear()
      print("Holding tight to the hilt of your sword, you run and hit the troll in the arm. You fall to the ground still holding on to the trolls severed limb. You look up to see the troll cover its wound with its other hand.")
      print("The troll is very aggervated. It bellows a mighty roar and falls to the ground. It has bled out.")
      print("You arise victourius and run as fast as you can out of the exit.")
      time.sleep(4)
      the_countryside()
    else:
      print("That is not a vaild choice. You take to long and get slain by the troll."+text.Red+"GAME OVER"+text.End)
      end()
  if weapon_choice=="2":
    clear()
    print("You have chosen to use the bow.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()
    if attack_spot=="1":
      clear()
      print("You pull back your bow and fire an arrow into the trolls eye. It misses and hits hit forehead instead. The troll keels over and slams into the floor. Lifeless.")
      print("You arise vicourius and run as fast as you can out of the exit.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="2":
      clear()
      print("You pull back your bow and shoot the troll in hit leg. The troll is unaffected by such a small attack. He pulls the arrow out and steps on you. "+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="3":
      print("You pull your bow back and shoot the troll in the arm. The troll is unaffected by your attack. It scoffs and crushes you under his fist. "+text.Red+"GAME OVER"+text.End)
      end()
    else:
      print("That is not a valid choice. You take to long and get slain by the troll. "+text.Red+"GAME OVER"+text.End)
      end()
  if weapon_choice=="3":
    clear()
    print("You have chosen to use the spear.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()
    if attack_spot=="1":
      clear()
      print("You run and jump up to the arm of the troll. You climb up and stab the troll in the eye. The spear goes all the way though the trolls head. It falls to the ground, Dead.")
      print("You arise vicourius and run as fast as you can out of the exit.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="2":
      clear()
      print("You run up to the troll and thrust the spear into it's leg. You try to retrive your spear but it is stuck. The aggervated troll crushes you under its foot. "+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="3":
      clear()
      print("You decide to attack the troll in its arm. Getting a running start you jump up onto the trolls arm pushing the spear all the way through. You try to retrive your spear but it is stuck in its arm. The agervated troll swings its arm and you go flying and hit the hard rock wall of the cave. You are dead. "+text.Red+"GAME OVER"+text.End)
      end()

def clearing_fight():
  global choice
  tn= random.choice(troll_name)

  print("You grab a few sticks and leaves and setup a small tent. After a few hours of scavengering the clearing. You decide your ready to leave the clearing, as you see a building off to the distance.")
  time.sleep(3)
  print("Just as you are about to leave the clearing you hear a loud *SNAP*! As a tree comes crashing down on the boarder of the clearing. In its wake walks a mighty troll. It moves in front of you blocking the only way out of the clearing!")
  time.sleep(3)
  print(f"The troll opens its mouth an speaks in a loud booming voice that reverbarates off through the surrounding trees. The troll says, I AM  {tn}! THE TROLL GUARDIAN OF THIS PASS. YOU MUST ANSWER MY RIDDLE OR FIGHT ME TO THE DEATH.")
  time.sleep(2)
  print(text.Bold+text.Underlined+"What do you Do:"+text.End)
  options = ["1. Answer The Riddle","2. Fight The Troll"]
  for x in range(len(options)):
    print("\t"+options[x])
  choice=input().lower()

  if choice == "1":
    clear()
    print("You dedide to try the riddle.")
    time.sleep(2)
    print("You walk up to the troll and begin to speak.")
    time.sleep(2)
    print(text.Bold+text.Underlined+"What do you say:"+text.End)
    speech=["1. I shall do your Riddle.","2. Tell me your riddle now!"]
    for x in range(len(speech)):
      print("\t"+speech[x])
    choice=input().lower()
    if choice == "1" or "2":
      clear()
      print("VERY WELL THEN. YOU HAVE ONE TRY TO ANSWER MY RIDDLE. IF YOU FAIL WE SHALL FIGHT! IF YOU SUCCEED. I WILL LET YOU OUT OF THIS FOREST.")
      time.sleep(3)
      print(text.Underlined+text.Bold+"MY RIDDLE IS THIS."+text.End+text.Red+"\nYOU CAN SEE NOTHING ELSE\nWHEN YOU LOOK IN MY FACE,\nI WILL LOOK YOU IN THE EYE,\nAND I WILL NEVER LIE.\nWHAT AM I?"+text.End)
      time.sleep(3)
      print("You consider the riddle. You come up with three possible answers.")
      riddle=["1. A Statue","2. Your Reflection","3. Glasses"]
      for x in range(len(riddle)):
        print("\t"+riddle[x])
      pick=input().lower()
      if pick == "2":
        print("VERY GOOD! YOU HAVE BESTED ME. YOU MAY EXIT THIS FOREST.")
        the_countryside()
      else:
        print("YOU FOOL! THE CORRECT ANSWER WAS YOUR REFLECTION. The troll laughs at you before crushing you under its fist."+text.Red+"GAME OVER"+text.End)

  if choice == "2":
    clear()
    print("SO YOU HAVE CHOSEN DEATH.. VERY WELL THEN. WE SHALL FIGHT!")
    time.sleep(2)
    print("You have made the decision to fight the troll. You remember the battle with the bear. And get an idea. You quickly look around. Within an instant you realize that there is a skeleton of another traveler just off the treeline of the clearing.")
    time.sleep(5)
    print("You sprint over to the skeleton just missing the huge fist of the troll. You quiclky scavenge the body.")
    print(text.Underlined+text.Bold+"You Find the folowing weapons:"+text.End)
    for x in range(len(weapons)):
      print("\t"+weapons[x])
    weapon_choice=input()
  if weapon_choice == "1":
    print("You have chosen the sword.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()

    if attack_spot=="1":
      clear()
      print("You run and jump onto the trolls arm. You climb up the arm and stab the troll in the eye.")
      print("The troll screams in pain and is now blinded. However, it is not enough to kill the troll. The troll stumbles around and crushes you under its foot."+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="2":
      clear()
      print("You sprint across the clearing and jump onto the troll's leg. You slice its leg in half! The troll falls off balance and dies on impact with the tree it knocked over.")
      print("You arise vicotrius and run as fast as you can out of the clearing.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="3":
      clear()
      print("Holding tight to the hilt of your sword, you run and hit the troll in the arm. You fall to the ground still holding on to the trolls severed limb. You look up to see the troll cover its wound with its other hand.")
      print("The troll is very aggervated. It bellows a mighty roar and falls to the ground. It has bled out.")
      print("You arise victourius and run as fast as you can out of the clearing.")
      time.sleep(4)
      the_countryside()
    else:
      print("That is not a vaild choice. You take to long and get slain by the troll."+text.Red+"GAME OVER"+text.End)
      end()
  if weapon_choice=="2":
    clear()
    print("You have chosen to use the bow.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()
    if attack_spot=="1":
      clear()
      print("You pull back your bow and fire an arrow into the trolls eye. It misses and hits hit forehead instead. The troll keels over and slams into the ground. Lifeless.")
      print("You arise vicourius and run as fast as you can out of the clearing.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="2":
      clear()
      print("You pull back your bow and shoot the troll in hit leg. The troll is unaffected by such a small attack. It pulls the arrow out and steps on you. "+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="3":
      print("You pull your bow back and shoot the troll in the arm. The troll is unaffected by your attack. It scoffs and crushes you under its fist. "+text.Red+"GAME OVER"+text.End)
      end()
    else:
      print("That is not a valid choice. You take to long and get slain by the troll. "+text.Red+"GAME OVER"+text.End)
      end()
  if weapon_choice=="3":
    clear()
    print("You have chosen to use the spear.")
    print(text.Bold+text.Underlined+"Where do you attack the troll at?"+text.End)
    text.Red
    print("1. Go for the eyes")
    print("2. Go for the legs")
    print("3. Go for the arms")
    text.End
    attack_spot=input()
    if attack_spot=="1":
      clear()
      print("You run and jump up to the arm of the troll. You climb up and stab the troll in the eye. The spear goes all the way though the trolls head. It falls to the ground, Dead.")
      print("You arise vicourius and run as fast as you can out of the exit.")
      time.sleep(4)
      the_countryside()
    elif attack_spot=="2":
      clear()
      print("You run up to the troll and thrust the spear into it's leg. You try to retrive your spear but it is stuck. The aggervated troll crushes you under its foot. "+text.Red+"GAME OVER"+text.End)
      end()
    elif attack_spot=="3":
      clear()
      print("You decide to attack the troll in its arm. Getting a running start you jump up onto the trolls arm pushing the spear all the way through. You try to retrive your spear but it is stuck in its arm. The agervated troll swings its arm and you go flying and hit the hard rock wall of the cave. You are dead. "+text.Red+"GAME OVER"+text.End)
      end()

def the_countryside():
  global choice
  clear()
  print("You quickly run out of the forset. Still in shock from the troll that could have killed you. You look around. Realziing you find yourslef in a feild. A farm is on the horizon.")
  print("After a long walk you arrive at the farm. There are 3 places you can go on the farm.")
  time.sleep(1)
  print("Straight ahead is the Barn.") 
  time.sleep(1)
  print("To the left is a empty stable.")
  time.sleep(1)
  print("To the right is a farmhouse.")
  time.sleep(1)
  direction()

def direction():
  global choice
  print(text.Bold+text.Underlined+"Where do you go?"+text.End)
  places = ["1. Barn", "2. Stable", "3. Farmhouse"]
  while True:
    for x in range(len(places)):
      print("\t"+places[x])
    choice=input().lower()
    if choice =="1" or choice == "2" or choice == "3":
      country_location()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def barn_choice():
  global choice
  print(text.Bold+text.Underlined+"Where do you go?"+text.End)
  go = ["1. Left", "2. Right","3. Forward"]
  while True:
    for x in range(len(go)):
      print("\t"+go[x])
    choice=input().lower()
    if choice =="1" or choice == "2" or choice == "3":
      clear()
      barn_way()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def country_location():
  global choice
  ran_out_of_names()

def ran_out_of_names():
  global choice

  if choice == "1":
    e = random.choice(barn_animal)
    if open != True:
      print("You walk up to the barn. You try the door and it is locked. The key must be somewhere else on the farm. You go somewhere else.")
      direction()
    if open == True:
      print("You walk up to the barn and use the key to open the door. You walk in and get hit with the smell of the barn. There is a map and note on the wall. It is a map with a outlined route that leads to a village. The note is a list fo suppiles that would have been delivered on the route.")
      print(f"You look around and see several things. To the left is a tractor. To the right is a dirtbike. Straght ahead there is a horse, and a {e}.")
      time.sleep(1)
      barn_choice()
  if choice == "2":
    print("You walk up to the stable. You notice there is an open gate. You walk up and look inside. It is empty. On the floor there is hoof prints, a water trough is up against the back of the stall.")
    time.sleep(2)
    print("Its obvious a horse was here. Although it must be somewhere else on the farm.")
    time.sleep(2)
    print("Discovering there is nothing esle to see here, you walk somwhere else.")
    direction()
  if choice == "3":
    print("You walk up to the farmhouse.")
    way()

def way():
  global choice
  global key
  time.sleep(1)
  print("There are 3 doors you can go through. The rest are barracaded for an unknown reason.")
  print(text.Bold+text.Underlined+"Where do you go?"+text.End)
  doors = ["1. Left", "2. Right", "3. Forward"]
  while True:
    for x in range(len(doors)):
      print("\t"+doors[x])
    choice=input().lower()
    if choice =="1" or choice == "2" or choice == "3":
      doors_paths()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def doors_paths():
  global open
  global choice
  if choice == "1":
    open = True
    print("You go over to the left door. Its jammed. You back up and slam your arm into the door. Within an instant it gives way revaling the master bedroom. The room is destoryed. With the wardrobe knocked over, the sheets to the bed an utter mess. You notice a key on the nightstand. You pick it up and examine it. The tag says 'BARN KEY' There is nothing else in this room.")
    time.sleep(5)
    print("You exit the room")
    time.sleep(3)
    print(text.Bold+text.Underlined+"Do you want to explore the other rooms or exit the house?"+text.End)
    place = ["1. Explore", "2. Exit"]
    while True:
      for x in range(len(place)):
        print("\t"+place[x])
      choice=input().lower()
      if choice =="1" or choice == "2":
        clear()
        place_int()
        break
      else:
       print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)
  if choice == "2":
    print("You go over to the right door. It opens noisly and reveals a kitchen. You walk in and find that it has been ransakced. The drawers are pulled out and broken. Shattered china litters the floor. It is too dangerous to explore.")
    time.sleep(3)
    way()
  if choice == "3":
    print("You walk forward and open the door. It is a bathroom., Walking in you get an overwhelming stench that almost casues you to pass out. There is a gass leak in that room. You quiclky close the door before you collapse.")
    time.sleep(3)
    way()

def place_int():
  if choice == "1":
    way()
  if choice == "2":
    direction()

def barn_way():
  global choice
  if choice == "1":
    print("You go over to the tractor and notice the key is still in the ignition. You try to start it but it is out of gas.")
    barn_choice()
  if choice == "2":
    print("You walk up to the dirtbike. The frame is extremely rusted, but it has gas. It would be risky to use it.")
    print(text.Bold+text.Underlined+"Do you take the risk?"+text.End)
    bike = ["Yes", "No"]
    while True:
      for x in range(len(bike)):
        print("\t"+bike[x])
      choice=input().lower()
      if choice =="yes" or choice == "no":
        clear()
        bike_out()
        break
      else:
        print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)
  if choice == "3":
    print("You walk forward and pet the horses mane.")
    time.sleep(1)
    print("You look over and see a number for things hung on a hook on the wall. You see the saddle, the girth and the stirrup and bridle.")
    time.sleep(1)
    print("Suddenly an idea strikes you. This horse could help you travel to the nearby village.")
    print(text.Bold+text.Underlined+"Do you take the horse?"+text.End)
    honse = ["Yes", "No"]
    while True:
      for x in range(len(honse)):
        print("\t"+honse[x])
      choice=input().lower()
      if choice =="yes" or choice == "no":
        clear()
        pre_village()
        break
      else:
        print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

  else:
      print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def bike_out():
  global choice
  if choice == "yes":
    print("You hop on the dirt bike and turn the key. The engine roars to life. The bike starts to shake and you hear the engine start rattling.")
    print("Not 5 seconds after you start the engine it backfires and the bike falls apart.")
    time.sleep(5)
    barn_choice()
  if choice == "no":
    print("You decide not to take the risk of trying the bike and walk away.")
    time.sleep(3)
    barn_choice()

def pre_village():
  global choice
  if choice == "yes":
    print("You grab the equipment and gear up prepare the horse for the ride.")
    time.sleep(1)
    print("Once you are ready. You mount the horse and get started at a light trot out of the barn and accelerate to a gallop once you reach open feilds.")
    time.sleep(2)
    into_the_village()

def into_the_village():
  global choice
  clear()
  print("You ride on for about 30 minutes before you see the village coming up.")
  time.sleep(1)
  print("You arrive at the village and see a group of villagers standing at the village gates.")
  print("The villagers are wearing aromour and are brandishing weapons defesnsivly in your direction.")
  time.sleep(2)
  print("You slow down and dismount your steed.")
  print("You walk up to the villagers and ask them what is going on.")
  time.sleep(3)
  print("A villager responds snidely,"+text.Magenta+"We are defensing our home from the dragon of course!"+text.End)
  time.sleep(2)
  print(text.Magenta+"If you wish to enter to saftey you may, once you enter you cannot leave. Or you can stay out there where the risk of death is constant!"+text.End)
  print(text.Bold+text.Underlined+"What do you decide?"+text.End)
  honse = ["1. Enter the Village", "2. Offer to defeat the dragon"]
  while True:
    for x in range(len(honse)):
      print("\t"+honse[x])
    choice=input().lower()
    if choice =="1" or choice == "2":
      clear()
      ending1()
      break
    else:
      print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def ending1():
  global choice
  if choice == "1":
    print("You tell the villagers you wish to enter the village.")
    print(text.Magenta+"Very well then traveler. Welcome to your new home."+text.End)
    print(text.Blue+"You have gotten the Ending: Member or the Village"+text.End)
    end()

  if choice == "2":
    print("I shall not stay in your village. But I can defeat the dragon for you.")
    print(text.Magenta+"And how do you plan to do that?"+text.End)
    time.sleep(1)
    print("I have defeated many beasts in my travels. Surley I can defeat a dragon.")
    time.sleep(1)
    print(text.Magenta+"Very well then traveler. I offer you my sword and armour for your quest. Once you defeat the dragon. Retrurn here, we will be waiting.."+text.End)
    time.sleep(2)
    to_the_keep()

def to_the_keep():
  global choice
  print("You give your thanks to the villagers and mount your horse. With a crack of the reins the horse gallops away towards the dragons keep.")
  time.sleep(1)
  print("You ride into the night. Just as you are about to stop to rest you see a massive tower looming over the darkened skyline.")
  print("There is a sense a fear and dispair that sets over you as you draw nearer.")
  time.sleep(2)
  print("A defaning roar erupts from the tower. Your horse bucks you off and runs off to the night due to the roar.")
  time.sleep(1)
  print("You stand up and spit dirt out of your mouth. Looking up to the top of the tower, you see a dragons tail swish through the air into the top balcony.")
  time.sleep(2)
  climbing_the_tower()

def climbing_the_tower():
  print("You walk up to the tower door and use your sword to slash the lock open. With a great effort you pull the heavy oak door open.")
  time.sleep(1)
  print("As you walk into the tower you see a grand golden statue of a king sitting on a throne of bones. An inscription is written on the throne.")
  print("The inscription reads: "+text.Yellow+"The King of Dreams"+text.End)
  print("You closley examine the statue. Something catches your eye, underneath the word dreams the word nightmares has been carved.")
  time.sleep(3)
  print("The writing looks hurried and trails off at the end, as if the person was pulled away while writing.")
  time.sleep(1)
  print("Deep gashes in the stone walls show that the dragon is at least the size of a semi truck")
  time.sleep(1)
  print("You look back at the door but realize it is sealed shut. The only way to go is up.")
  time.sleep(2)
  the_climb()

def the_climb():
  global choice
  print("You walk over and start up the spiral stairs. Its going to be a long walk to the top, but you must not let your guard down.")
  print("After 5 minutes of walking you hear something running down the stairs ")
  time.sleep(2)
  action = ["1. Push It Over the Edge", "2. Stab It", "3. Dodge It"]
  print(text.Bold+"A skeleton runs at you! What do you do?"+text.End)
  while True:
    for x in range(len(action)):
      print("\t"+action[x])
    choice=input().lower()
    if choice =="1" or choice == "2" or choice == "3":
      skeleton()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def skeleton():
  global choice
  if choice == "1":
    print("You reach out and push the skeleton over the edge of the staircase. The skeleton grabs your wrist and pulls you down with it."+text.Red+text.Underlined+"GAME OVER"+text.End)
    end()
  if choice == "2":
    print("You try to stab the skeleton but ti just goes right through. The skeleton kills you."+text.Red+text.Underlined+"GAME OVER"+text.End)
  if choice == "3":
    print("You step slightly to the left and the skeleton goes right passed you.")
    time.sleep(1)
    continue_climbing()

def continue_climbing():
  time.sleep(2)
  clear()
  print("You continue up the stairs laughing to yourslef at how easy it was to get passed the skeleton.")
  time.sleep(1)
  print("As you climb higher, a crippling sense of fear sets in and the air begins to smell heavily of smoke.")
  print("The steps grow steeper and become charred. The walls are cracked and crumbling.")
  time.sleep(2)
  print("You reach the top of the stairs. You come into a gigantic room. A ruined tapsestry of angels lines the domed ceiling.")
  print("You grab onto the hilt of your sword as you look around.")
  time.sleep(2)
  print("You see that the circular room is lined with pillars that open out to a balcony. In the center of the room, lies a large red dragon, deep in slumber..")
  dragon_battle()

def dragon_battle():
  global choices
  print("With one swift movement, you unsheathe your sword. The metalic ring reverberates into the night. The moonlight reflecting off your shiny blade. As you prepare to take your first step forward, the dragon stops snoring. The eyes of the dragon open revealing radiant green slit pupils that guide their way to gaze as you. As if the dragon is x-raying you with its icy stare.")
  time.sleep(3)
  print("The dragon stands onto its hind legs and belows a mighty roar that shakes the building.")
  time.sleep(1)
  print("The dragon opens its maw and begins to speak in a low hoarse voice.")
  print(text.Background_Red+"I AM THE DRAGON GUARDIAN OF THIS PLACE. I HAVE BEEN SUMMONED TO GUARD THE ALTER OF THE KING OF DREAMS."+text.End)
  time.sleep(1)
  print("You tighten your grip on the sword.")
  time.sleep(1)
  print("The dragon begins to speak once more.\n"+text.Background_Red+"NOW I MUST KILL YOU LIKE I HAVE DONE TO EVERY TRAVELER THAT ENTERS MY KEEP."+text.End)
  print(text.Bold+text.Underlined+"THE DRAGON MAKES HIS ATTACK!"+text.End)
  dragon = ["1. Begin The Fight", "2. Run","3. Try to negoriate with the dragon."]
  while True:
    for x in range(len(dragon)):
      print("\t"+dragon[x])
    choices=input().lower()
    if choices =="1" or choices == "2" or choices == "3":
      clear()
      fight_the_dragon()
      break
    else:
      print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def fight_the_dragon():
  global choices
  global dragon_health
  global player_health

  player_health=100
  dragon_health=100

  if choices == "1":
    print("You let out a mighty scream as you raise your sword. The dragon retruns with a roar as it beats is gigantic wings. The room becomes engulfed in flame as the dragon creates a ring of fire trapping you in the room.")
    print("Instructions: You must pick an attack from the list. The dragon will make its attack at the same time. There is a 50% chance your attack will work. If you use a defensive attack, there is a 50% chance it will work, if it works only the dragon will be damaged. If it fails, only you will be damaged. Both fighters start with 100% health.")
    player()
  if choices == "2":
    print("You attempt to run away from the dragon. The dragon snarls and burns you alive."+text.Red+"GAME OVER"+text.End)
    end()
  if choices == "3":
    print("You attempt to negotiate with the dragon. It does nothing and the dragon kills you."+text.Red+"GAME OVER"+text.End)
    end()

def player():
  global dragon_attack
  global player_attack
  dragon_attack=random.choice(dragon_attacks)
  time.sleep(5)
  clear()
  print ("Opponent Health: "+str(dragon_health))
  print ("Your Health: "+str(player_health))
  print(text.Bold+text.Underlined+"What do you do?"+text.End)
  act = ["1. Stab","2. Slash","3. Parry","4. Dodge"]
  while True:
    for x in range(len(act)):
      print("\t"+act[x])
    player_attack=input().lower()
    if player_attack =="1" or player_attack == "2" or player_attack == "3" or player_attack == "4":
      fight_results()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def fight_results():
  global player_attack
  global dragon_health
  global player_health
  global dragon_attack
  attack_succsess=random.choice(succsess)

  if attack_succsess == "1" and player_attack == "4":
    print(f"The dragon uses its {dragon_attack} attack but you dodge it. Nobody takes damage.")
    am_i_dead()
  elif attack_succsess == "2" and player_attack == "4":
    print(f"The dragon uses its {dragon_attack} attack. You attempt to dodge it but it strikes you. You take 5 damage.")
    player_health-=5 
    am_i_dead()

  if attack_succsess == "1" and player_attack == "3":
    print(f"The dragon uses its {dragon_attack}  attack but you parry it back at the dragon.")
    dragon_health-=30
    print("You take no damage as the attack was sent back at the dragon.")
    am_i_dead()

  elif attack_succsess == "2" and player_attack == "3":
    print(f"The dragon uses its {dragon_attack} attack! You Attempt to pary the dragons attack but it fails.")
    player_health-=9
    am_i_dead()

  if attack_succsess == "1" and player_attack == "2":
    print(f"The dragon uses its {dragon_attack} attack. You take 10 damage. You return the attack with a Slash attack! The dragon takes 11 damage.")
    player_health-=10
    dragon_health-=11
    am_i_dead()

  elif attack_succsess == "2" and player_attack == "2":
    print(f"The dragon uses its {dragon_attack} attack. You take 11 damage. You attempt to retrun the attack with a slash attack but you fail.")
    player_health-=11
    am_i_dead()


  elif attack_succsess == "1" and player_attack == "1":
    print(f"The dragon uses its {dragon_attack} attack! You take 9 damage. You return the attack with a Stab attack! The dragon takes 15 damage.")
    player_health-=9
    dragon_health-=15
    am_i_dead()


  elif attack_succsess == "2" and player_attack == "1":
    print(f"The dragon uses its {dragon_attack} attack! You take 10 damage. You attempt to retrun the attack with a stab attack but you fail.")
    player_health-=10
    am_i_dead()

def dragon_victory():
  global choice
  clear()
  print("You charge at the dragon, landing the final blow. As your sword pireces the dragons throat it rithes in pain. Falling to the ground. A lifeless pile of scales.")
  time.sleep(1)
  print("You take a look around and notice a chest in the corner of the room.")
  print(text.Bold+text.Underlined+"Do you open the chest or leave for the village?"+text.End)
  to_end = ["1. Open", "2. Leave"]
  while True:
    for x in range(len(to_end)):
      print("\t"+to_end[x])
    choice=input().lower()
    if choice =="1" or choice == "2":
      ending_2()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def am_i_dead():
  if player_health <= 0:
    print("The dragon lands the final blow and you collapse. The last thing you hear is the laugh of the dragon before it all fades to black. "+text.Red+"GAME OVER"+text.End)
    end()
  elif dragon_health <= 0:
   dragon_victory()
  else:
    player()

def ending_2():
  global choice
  if choice == "2":
    print("You decide to exit the tower. Before you leave you cut a piece off the dragon and make your way to the village.")
    time.sleep(1)
    print("Without a horse you are walking on foot for the next day or so.")
    time.sleep(1)
    print("You arrive at the village and see the same guards from before.")
    time.sleep(1)
    print("You hold up the peice of the dragon as proof you have slain the beast.")
    print("They smile and guide you into the village.")
    print(text.Blue+"You have unlokced the ending: Hero of the Village"+text.End)
    end()
  if choice == "1":
    print("You decide to open the chest. You walk up and lift the lid.")
    print("Inside there is nothing but a scroll of paper.")
    print("You lift the scroll out of the chest and read it.")
    time.sleep(1)
    print("The scroll reads as follows, "+text.Italic+text.Bold+"If you are reading this note it means you have surrvied the dragon just as I have. I don't know how this place got to me. I tired to stay overnight in the tower but the dragon regenerated itself somehow. I belive it has something to do with the King of Dreams.. Could we be trapped in a dream? Maybe thats why I don't recognize my own voice and strength. I must go before the dragon comes back.."+text.End)
    time.sleep(2)
    print("You think back to the skeleton from earlier. Could that have been the traveler that wrote this?")
    print("Just as your about to leave you realize there is a second item in the chest. It is a map.")
    print("The map shows a path to a huge castle. Above it shows the name. 'THE PALACE OF DREAMS'. That must be where the king is.")
    to_end = ["1. Go to the Castle", "2. Retrun to the Village"]
    while True:
      for x in range(len(to_end)):
        print("\t"+to_end[x])
      choice=input().lower()
      if choice =="1" or choice == "2":
        ending_2_cont()
        break
      else:
       print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def ending_2_cont():
  global choice
  if choice == "2":
    print("You decide to exit the tower. Before you leave you cut a piece off the dragon and make your way to the village.")
    time.sleep(1)
    print("Without a horse you are walking on foot for the next day or so.")
    time.sleep(1)
    print("You arrive at the village and see the same guards from before.")
    time.sleep(1)
    print("You hold up the peice of the dragon as proof you have slain the beast.")
    print("They smile and guide you into the village.")
    print(text.Blue+"You have unlokced the ending: Hero of the Village"+text.End)
    end()
  if choice == "1":
    print("You stand up and pocket the map. As you start walking you realize what you are about to do. The king could kill you. But you've come to far to turn back now..")
    time.sleep(1)
    across_the_feilds()

def across_the_feilds():
  global choice
  print("Without your horse you must set out on foot. It will take several days to reach the castle. Who knows what may happen on your way over.")
  print("You walk on without stopping for at least a day, until you come across a river bank.")
  print("It is too wide and too deep to swim across. You must find another way across.")
  print("You walk along the river bank for a few hours until you come across a draw bridge. However, the lever is on the other side of the river.")
  time.sleep(4)
  print("It seems the only way across is on the bridge. You must find a way to lower the bridge from this side.")
  bridge()

def bridge():
  global choice
  print("You look around and see several things.")
  to_end=["1. A Rope", "2. A Rock","3. A Bow"]
  while True:
    for x in range(len(to_end)):
      print("\t"+to_end[x])
    choice=input().lower()
    if choice == "1" or choice == "2" or choice == "3":
      river_bank()
      break
    else:
      print(text.Red+"That is not an option. Please choose a action:"+text.End)

def river_bank():
  global choice
  if choice == "1":
    print("You grab the rope and throw it across the river. The end of the rope wraps it self around the lever. With a hard pull the lever slides back and the bridge begins to lower.")
    time.sleep(3)
    back_on_track()
  if choice == "2":
    print("You take the rock and try to throw it at the lever. It does not make it across. You must try again.")
    bridge()
  if choice == "3": 
    bow()

def bow():
  global choice
  clear()
  print("You grab the bow. Now you must find something to load it with.")
  print("You look around and see a few things to load it with.")
  arrow=["1. A Stick", "2. A Broken Arrow","3. A Sharp Rock"]
  while True:
    for x in range(len(arrow)):
      print("\t"+arrow[x])
    choice=input().lower()
    if choice == "1" or choice == "2" or choice == "3":
      bow_output()
      break
    else:
        print(text.Red+"That is not an option. Please choose a action:"+text.End)

def bow_output():
  global choice
  if choice == "1":
    print("You load the stick into the bow and draw. 'WHOOSH'! The stick flies across the river and strikes the lever. The bridge begins to lower.")
    time.sleep(3)
    back_on_track()
  if choice == "2":
    print("You load the broken arrow into the bow and draw. 'WHOOSH'! The arrow flies out of the bow but spirals into the river before it reaches the other side.")
    arrow()
  if choice == "3":
    print("You load the rock into the bow and draw. 'WHOOSH'! The rock flies across barely clearing the river. It strikes the lever. The bridge begins to lower.")
    time.sleep(3)
    back_on_track()

def arrow():
  print("You can pick a new projectile or a new stratagey.")
  print("1. New Stratagey")
  print("2. New Projectile")
  choice2=input().lower()
  if choice2=="1":
    bridge()
  if choice2=="2":
    bow()
  else:
    clear()
    print(text.Red+"That Is not a vaild option. Please try again."+text.End)
    arrow()

def back_on_track():
  clear()
  print("You walk across the bridge.")
  time.sleep(1)
  print("You contiue to walk through the seemingly endless feilds until you see a huge black castle on the horizon. Looking at the castle you get a powerful sense of nostalgia. But nothing about this castle seems familiar to you.")
  print("You walk up to the castle and begin your accent up the grand staircase.")
  print("Once you reach the top you are greeted by a towering exterior wall. The gate has been knocked off its hinges.")
  print("Marching into the castle grounds you notice there is a tower that looks almost identical to the dragon's keep in the grounds. There must be another dragon here. But you are here for the king, not to get sidetracked.")
  time.sleep(2)
  print("You walk over to the main castle gate and push it open. You must make your way though the castle and find the throne room.")
  time.sleep(1)
  castle_pick()

def castle_pick():
  global castle_pick
  print("There is a curved path leading up to the throne room. You can go straight to the throne room, or explore the castle. There could be items that will help you here.")
  castle = ["1. Straight to the throne room", "2. Explore the castle"]
  while True:
    for x in range(len(castle)):
      print("\t"+castle[x])
    castle_pick = input().lower()
    if castle_pick == "1" or castle_pick == "2":
        story_split()
        break
    else:
        print(text.Red+"That is not a vaild choice. Please Select an option:"+text.End)

def story_split():
  global castle_pick
  if castle_pick=="1":
    king_battle()
  if castle_pick=="2":
    the_castle()

def the_castle():
  global castle_explore
  print("There are several places you can go.")
  go = ["1. Observation Room", "2. Guards' Chamber", "3. Dining Hall", "4. Library", "5. Lockup", "6. Armory", "7. Docks", "8. Throne Room"]
  while True:
    for x in range(len(go)):
      print("\t"+go[x])
    castle_explore = input().lower()
    if castle_explore == "1" or castle_explore == "2" or castle_explore == "3" or castle_explore == "4" or castle_explore == "5" or castle_explore == "6" or castle_explore == "7" or castle_explore == "8":
        places()
        break
    else:
        print(text.Red+"That is not a vaild choice. Please Select an option:"+text.End)

def places():
  global collected
  global castle_explore
  global book
  global boats
  global here_dine
  global here_jail
  global here_lib
  global here_obs
  global here_guard
  global here_arm
  global here_dock
  #Observation Room v
  if castle_explore=="1":
    clear()
    if here_obs==False:
      print("You walk forward and start your way up the spiral stairs.")
      time.sleep(1)
      print("When you reach the top, you are entered into a huge room with large windows that give a spectacular view of the castle grounds.")
      print("In this room there is a pile of medical supplies againt the wall. You grab them. There is nothing else here.")
      heal_stuff.append("1. Bandages")
      heal_stuff.append("2. Bandaid")
      heal_stuff.append("3. Mysterious Potion")
      here_obs=True
      collected=True
      print("You walk back down the stairs onto the main grounds.")
      the_castle()
    if here_obs==True:
      clear()
      print(text.Bold+"You have already already been here."+text.End)
      the_castle()
  #Guards' Chamber v
  if castle_explore=="2":
    clear()
    if here_guard==False:
      print("You walk into the castle and begin your way down the stairs. Eventually, you end up in the guards' chamber.")
      print("To your suprise, there is nobody in the room. You see a sheild on the wall. You take it and sling it against your Back.")
      here_guard=True
      defense_stuff.append("1. Sheild")
      collected=True
      print("There is nothing else here. You exit the room.")
      the_castle()
    if here_guard==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
      the_castle()
  #Dining Hall v
  if castle_explore=="3":
    clear()
    if here_dine==False:
      print("You walk into the castle into the barren hallways. You wander around until you find the Dining Hall. Inside there is a long table loaded with food. On the celling there is a tapestry of a short man with wavy black hair riding a horse. You walk up to the table and grab some food. There is nothing else here.")
      food_stuff.append("1. Steak")
      food_stuff.append("2. Bread")
      food_stuff.append("3. Mushrooms")
      collected=True
      print("There is nothing else here. You exit the room.")
      here_dine=True
      the_castle()
    if here_dine==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
      the_castle()
  #Library v
  if castle_explore=="4":
    clear()
    if here_lib==False:
      print("You walk into the castle and wander through the halls until you find a Library. There is a bookshelf with a glowing book. The title is just 'DO NOT OPEN'.")
      print(text.Bold+text.Underlined+"Do you open the book?"+text.End)
      book = ["1. Open", "2. Leave it"]
      while True:
        for x in range(len(book)):
          print("\t"+book[x])
        book = input().lower()
        if book == "1" or book == "2":
            books()
            break
        else:
            print(text.Red+"That is not a vaild choice. Please Select an option:"+text.End)   
    if here_lib==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
      the_climb()
  #Lockup v
  if castle_explore=="5":
    clear()
    if here_jail==False:
      print("You walk into the castle and wander around until you see a grate in the floor. Beneath the grate is a set of stairs. You lift up the grate and make your way down the stairs. You find yourself in the Lockup of the castle. Empty prison cells line the wall. However, there is nothing of intrest here.")
      here_jail=True
      the_castle()
    if here_jail==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
      the_castle()
  #Armory v 
  if castle_explore=="6":
    clear()
    if here_arm==False:
      print("You walk into the guards' chamber and see the Armory. You take a few wepons left on a rack. Mysteriously, the rest of the armory is empty. As if the soldiers went out to battle and never returned..")
      print("There is nothing else here.")
      battle_stuff.append("1. Broad Sword")
      battle_stuff.append("2. Dagger")
      battle_stuff.append("3. Bow & Arrows")
      battle_stuff.append("4. Spear")
      collected=True
      here_arm=True
      the_castle()
    if here_arm==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
      the_castle()
  #Docks v
  if castle_explore=="7":
    clear()
    if here_dock==False:
      print("You walk around the grounds until you find yourself at the ship docks of the castle. There is a ship docked here. You get an idea. You could look around, or take the boat and sail away.")
      print(text.Bold+text.Underlined+"Whay do you do?"+text.End)
      boat = ["1. Take The Boat", "2. Keep Focused on the king"]
      while True:
        for x in range(len(boat)):
          print("\t"+boat[x])
        boats = input().lower()
        if boats == "1" or boats == "2":
            dock()
            break
        else:
            print(text.Red+"That is not a vaild choice. Please Select an option:"+text.End)   
    if here_dock==True:
      clear()
      print(text.Bold+"You have already been here."+text.End)
  #Throne Room v
  if castle_explore=="8":
    clear()
    king_battle()

def books():
  global book
  if book =="1":
    print("You see a flash of light and find yourslef back at the gate. You are unable to controll your own body.")
    king_battle()
  if book =="2":
    clear()
    print("You decide to leave the book. After wandering around the library to find nothing else in here. You exit the library.")
    here_lib=True
    the_castle()

def dock():
  global boats
  global here_dock
  clear()
  if boats == "1":
    print("You get on the boat and hoist the sails. You take to the seas, never to be bothered by the troubles of man again.")
    print(text.Blue+"You have unlocked the Ending: Adrift at Sea"+text.End)
    end()
  if boats == "2":
    print("You take your eyes off the boat and look around the docks. You find a box marked, 'EXPLOSIVES'. These could be useful. You pocked a few sticks of dynamite.")
    boom_stuff.append("1. Dynamite")
    collected=True
    here_dock=True
    print("There is nothing else here. You exit the docks.")
    the_castle()

def king_battle():
  global castle_explore
  if collected==False:
      print("You walk through the grounds up the winding paths until you arrive at a set of marble stairs. You triumphantly march your way into the throne room. sitting smuggly upon his throne sat the king. The statue did not quite capture the terrefying image of the real king. His eyes had no color, they were just black dots on his face. Yet you could still tell they are staring right at you.")
      print("The king stands up from his throne an opens his arms wide.")
      print(text.Yellow+"There you are! I've been waiting for you. I am very impressed by your preformance here. You are the only one to ever even make it to the castle! I've been waiting for this battle for eons.. "+text.End)
      print("You reach over and grab the hilt fo yuor sword prepared for an attack at any moment.")
      print(text.Yellow+"Now now, don't get ahead of yourself. There is a few things I must get set straight first.."+text.End)
      print("The king snaps his fingers and the walls of the throne room begin to melt away, replacing themselves with a stadium. The seats are filled with skeletons. Millions of them.")
      time.sleep(2)
      print(text.Yellow+"I cannot express enough how extraordinary it was that you made it here! This stadium is filled with every person that has ever sliped into my realm. After all, we need an audience.. I expect you'll be joining them soon."+text.End)
      print("As the stadium builds itself you can't help but feel a crippling sense of fear wash over you. You look at the king and the fear worsens. When you try to focus on the king, his image becomes distorted and hazy. How are you supposed to fight somthing you can't see?")
      print(text.Yellow+"Have you connected the dots yet? Perhaps your not as smart as I thought.. Let me clue you in. I am holding you prisoner in your own mind. This place is a collection of all that you fear and loathe. I am simply a projection of the fears that you claim aren't there. I am all you fear, I AM ATHURA KING OF KINGS, LOOK UPON MY WORKS ALL MIGHTY AND DESPAIR"+text.End)
      sword_player()
  if collected==True:
    print("You walk through the grounds up the winding paths until you arrive at a set of marble stairs. You triumphantly march your way into the throne room. sitting smuggly upon his throne sat the king. The statue did not quite capture the terrefying image of the real king. His eyes had no color, they were just black dots on his face. Yet you could still tell they are staring right at you.")
    print("The king stands up from his throne an opens his arms wide.")
    print(text.Yellow+"There you are! I've been waiting for you. I am very impressed by your preformance here. You are the only one to ever even make it to the castle! I've been waiting for this battle for eons.. "+text.End)
    print("You reach over and grab the hilt fo yuor sword prepared for an attack at any moment.")
    print(text.Yellow+"Now now, don't get ahead of yourself. There is a few things I must get set straight first.."+text.End)
    print("The king snaps his fingers and the walls of the throne room begin to melt away, replacing themselves with a stadium. The seats are filled with skeletons. Millions of them.")
    time.sleep(2)
    print(text.Yellow+"I cannot express enough how extraordinary it was that you made it here! This stadium is filled with every person that has ever sliped into my realm. After all, we need an audience.. I expect you'll be joining them soon."+text.End)
    print("As the stadium builds itself you can't help but feel a crippling sense of fear wash over you. You look at the king and the fear worsens. When you try to focus on the king, his image becomes distorted and hazy. How are you supposed to fight somthing you can't see?")
    print(text.Yellow+"Have you connected the dots yet? Perhaps your not as smart as I thought.. Let me clue you in. I am holding you prisoner in your own mind. This place is a collection of all that you fear and loathe. I am simply a projection of the fears that you claim aren't there. I am all you fear, I AM ATHURA KING OF KINGS, LOOK UPON MY WORKS ALL MIGHTY AND DESPAIR"+text.End)
    boss_player()

def sword_player():
  global player_attack
  global king_attacks
  king_attacks=random.choice(king_attacks)
  time.sleep(5)
  clear()
  print ("Opponent Health: "+str(king_health))
  print ("Your Health: "+str(player_health))
  print(text.Bold+text.Underlined+"What do you do?"+text.End)
  act = ["1. Stab","2. Slash","3. Parry","4. Dodge"]
  while True:
    for x in range(len(act)):
      print("\t"+act[x])
    player_attack=input().lower()
    if player_attack =="1" or player_attack == "2" or player_attack == "3" or player_attack == "4":
      sword_results()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def sword_results():
  global player_attack
  global king_health
  global player_health
  global king_attacks
  attack_succsess=random.choice(succsess)

  if attack_succsess == "1" and player_attack == "4":
    print(f"The king uses his {king_attacks} attack but you dodge it. Nobody takes damage.")
    am_i_dead2()
  elif attack_succsess == "2" and player_attack == "4":
    print(f"The king uses his {king_attacks} attack. You attempt to dodge it but it strikes you. You take 5 damage.")
    player_health-=5 
    am_i_dead2()

  if attack_succsess == "1" and player_attack == "3":
    print(f"The king uses his {king_attacks} attack but you parry it back at him.")
    king_health-=50
    print("You take no damage as the attack was sent back at the king.")
    am_i_dead2()

  elif attack_succsess == "2" and player_attack == "3":
    print(f"The king uses his {king_attacks} attack! You Attempt to pary the king's attack but it fails.")
    player_health-=9
    am_i_dead2()

  if attack_succsess == "1" and player_attack == "2":
    print(f"The king uses his {king_attacks} attack. You take 10 damage. You return the attack with a Slash attack! The king takes 47 damage.")
    player_health-=10
    king_health-=47
    am_i_dead2()

  elif attack_succsess == "2" and player_attack == "2":
    print(f"The king uses his {king_attacks} attack. You take 11 damage. You attempt to retrun the attack with a slash attack but you fail.")
    player_health-=11
    am_i_dead2()


  elif attack_succsess == "1" and player_attack == "1":
    print(f"The king uses his {king_attacks} attack! You take 9 damage. You return the attack with a Stab attack! The king takes 79 damage.")
    player_health-=9
    king_health-=79
    am_i_dead2()


  elif attack_succsess == "2" and player_attack == "1":
    print(f"The king uses his {king_attacks} attack! You take 10 damage. You attempt to retrun the attack with a stab attack but you fail.")
    player_health-=10
    am_i_dead2()

def am_i_dead2():
  if player_health <= 0:
    print("The king lands the final blow and you collapse.")
    print(text.Yellow+"Now, now, you couldn't have possibly throught you would actually win.. Its better this way."+text.End)
    print("The king summons chains from the ground that wrap around you like snakes. With the snap of the kings fingers the chains tighten, and you die."+text.Red+" GAME OVER"+text.End)
    end()
  elif king_health <= 250:
   final_halfway()
  else:
    sword_player()

def boss_player():
  global y
  global player_attack
  global king_health
  global player_health
  global king_attacks
  king_attacks=random.choice(king_attacks)
  print ("Opponent Health: "+str(king_health))
  print ("Your Health: "+str(player_health))
  print(text.Bold+text.Underlined+"What do you use?"+text.End)
  inventory = ["1. Weapons","2. Health","3. Defense","4. Explosives","5. Food"]
  while True:
    for x in range(len(inventory)):
      print("\t"+inventory[x])
    player_attack=input().lower()
    if player_attack =="1" or player_attack == "2" or player_attack == "3" or player_attack == "4" or player_attack == "5":
      boss_results()
      break
    else:
      print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def boss_results():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  attack_succsess=random.choice(succsess)
  if player_attack == "1":
    int_bat()
  if player_attack == "2":
    int_heal()
  if player_attack == "3":
    int_def()
  if player_attack == "4":
    int_boom()
  if player_attack == "5":
    int_food()

def int_def():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  while True:
    if defense_stuff == []:
      print("You have no items in this catagory.")
      boss_player()
    if player_attack == "3":
      for x in range(len(defense_stuff)):
        print("\t"+defense_stuff[x])
      choices =input().lower()
      if choices =="1":
        defense()
        break
      else:
        print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def int_boom():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  while True:
    if boom_stuff == []:
      print("You have no items in this catagory.")
      boss_player()
    if player_attack == "4":
      for x in range(len(boom_stuff)):
        print("\t"+boom_stuff[x])
      choices =input().lower()
      if choices =="1":
        boom()
        break
      else:
        print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def int_food():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  while True:
      if food_stuff == []:
        print("You have no items in this catagory.")
        boss_player()
      if player_attack == "5":
        for x in range(len(food_stuff)):
          print("\t"+food_stuff[x])
        choices =input().lower()
        if choices =="1" or choices =="2" or choices =="3":
          food()
          break
        else:
          print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def int_heal():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  while True:
      if heal_stuff == []:
        print("You have no items in this catagory.")
        boss_player()
      if player_attack == "2":
        for x in range(len(heal_stuff)):
          print("\t"+heal_stuff[x])
        choices =input().lower()
        if choices =="1" or choices =="2" or choices =="3":
          heal()
          break
        else:
          print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def int_bat():
  global king_attacks
  global player_attack
  global king_health
  global player_health
  global attack_succsess
  global choices
  while True:
      if battle_stuff == []:
        print("You have no items in this catagory.")
        boss_player()
      if player_attack == "1":
        for x in range(len(battle_stuff)):
          print("\t"+battle_stuff[x])
        choices =input().lower()
        if choices =="1" or choices =="2" or choices =="3" or choices =="4":
          weapon()
          break
        else:
          print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def defense():
  global choices
  global attack_succsess
  global king_attacks
  global player_health
  if attack_succsess=="1" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You use your sheild and deflect the damage!")
    print("Nobdoy takes damage.")
    boss_player()
  if attack_succsess=="2" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You attempt to use the sheild but it fails.")
    print("You take 10 damage.")
    player_health -= 10
    time.sleep(5)
    clear()
    boss_am_i_dead()

def boom():
  global choices
  global attack_succsess
  global king_attacks
  global player_health
  global king_health
  if attack_succsess=="1" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You ignite a stick of dynamite and throw it at the king.")
    print("The blast deals 75 damage to the king and deflects his attack!")
    king_health -= 75
    boss_am_i_dead()
  if attack_succsess=="2" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You attempt to ignite a stick of dynamite but it turn out as a dud.")
    print("You take 12 damage.")
    player_health -= 12
    boss_am_i_dead()

def food():
  global choices
  global player_health
  if choices == "1":
    print("You eat the steak and gain 5 health.")
    print("Nobody takes damage as not attacks were dealt.")
    player_health += 5
    boss_player()
  if choices =="2":
    print("You eat the bread and gain 2 health.")
    print("Nobody takes damage as no attacks were dealt.")
    player_health += 2
    boss_player()
  if choices =="3":
    print("You eat the mushrooms and gain 4 health.")
    print("Nobody takes damage as no attacks were dealt.")
    player_health += 4
    boss_player()

def heal():
  global choices
  global player_health
  if choices == "1":
    print("You use the bandage and gain 5 health.")
    print("Nobody takes damage as not attacks were dealt.")
    player_health += 5
    boss_player()
  if choices =="2":
    print("You use the bandaid and gain 2 health.")
    print("Nobody takes damage as no attacks were dealt.")
    player_health += 2
    boss_player()
  if choices =="3":
    print("You drink the potion and gain 4 health.")
    print("Nobody takes damage as no attacks were dealt.")
    player_health += 4
    boss_player()

def weapon():
  global choices
  global attack_succsess
  global player_health
  global king_health
  if attack_succsess=="1" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You use your Broad Sword and swing at the king!")
    print("You take 10 damage.")
    print("The king takes 50 damage")
    player_health -= 10
    king_health -= 50
    boss_am_i_dead()
  elif attack_succsess=="2" and choices =="1":
    print(f"The king uses his {king_attacks} attack on you! You attempt to use the Broad Sword but the king dodges it.")
    print("You take 10 damage.")
    player_health -= 10
    boss_am_i_dead()

  if attack_succsess=="1" and choices =="2":
    print(f"The king uses his {king_attacks} attack on you! You use your dagger and stab the king!")
    print("You take 5 damage.")
    print("The king take 43 damage")
    player_health -= 5
    king_health -= 43
    boss_am_i_dead()
  elif attack_succsess=="2" and choices =="2":
    print(f"The king uses his {king_attacks} attack on you! You attempt to stab the king with the dagger but you can't get close enough.")
    print("You take 10 damage from the kings attack.")
    player_health -= 10
    boss_am_i_dead()

  if attack_succsess=="1" and choices =="3":
    print(f"The king uses his {king_attacks} attack on you! You use your bow to shoot the king! It hits him in the eye.")
    print("The king takes 70 damage.")
    print("You take no damage, the king missed")
    king_health -= 70
    boss_am_i_dead()
  elif attack_succsess=="2" and choices =="3":
    print(f"The king uses his {king_attacks} attack on you! You attempt to shoot the king with your bow but it misses.")
    print("You take 10 damage from the kings attack.")
    player_health -= 10
    boss_am_i_dead()

  if attack_succsess=="1" and choices =="4":
    print(f"The king uses his {king_attacks} attack on you! You use your spear and hurl it at the king.")
    print("The king is hit and takes 30 damage.")
    print("You take 10 damage from the kings attack.")
    king_health -= 30
    player_health-= 10
    boss_am_i_dead()
  elif attack_succsess=="2" and choices =="4":
    print(f"The king uses his {king_attacks} attack on you! You attempt to hit the king with your spear but you miss.")
    print("You take 10 damage.")
    player_health -= 10
    boss_am_i_dead()

def boss_am_i_dead():
  if player_health <= 0:
    print("The king lands the final blow and you collapse.")
    print(text.Yellow+"Now, now, you couldn't have possibly throught you would actually win.. Its better this way."+text.End)
    print("The king summons chains from the ground that wrap around you like snakes. With the snap of the kings fingers the chains tighten, and you die."+text.Red+" GAME OVER"+text.End)
    end()
  elif king_health <= 250:
    final_halfway()
  else:
    time.sleep(5)
    clear()
    boss_player()

def final_halfway():
  print("The king withdrawls.")
  print(text.Yellow+("You.. You drained half of my health... Now, its time i finish this once and for all!"+text.End))
  print("In that moment, you get an idea. This is YOUR mind. So you could do whatever you want..")
  print("You focus really hard on the ground and it begins to crack.")
  print("Now, you and the king are even. Its time to take back your mind..")
  final_player()

def final_player():
  global king_attacks
  global player_attack
  king_attacks=random.choice(king_attacks)
  time.sleep(5)
  clear()
  print ("Opponent Health: "+str(f_king_health))
  print ("Your Health: "+str(f_player_health))
  print(text.Bold+text.Underlined+"What do you use?"+text.End)
  act = ["1. Terraformation","2. Chain Slash","3. Nightmares","4. Fling"]
  while True:
    for x in range(len(act)):
      print("\t"+act[x])
    player_attack=input().lower()
    if player_attack =="1" or player_attack == "2" or player_attack == "3" or player_attack == "4":
      final_fight_results()
      break
    else:
     print(text.Red+"That is not an option. \nPlease choose a action:"+text.End)

def final_fight_results():
  global player_attack
  global f_king_health
  global f_player_health
  global king_attacks
  attack_succsess=random.choice(succsess)

  if attack_succsess == "1" and player_attack == "4":
    print(f"The King uses his {king_attacks} attack but you fling the king back into the stands. Nobody takes damage.")
    final_am_i_dead()
  elif attack_succsess == "2" and player_attack == "4":
    print(f"The King uses his {king_attacks} attack. You attempt to fling the king but he is faster, it strikes you. You take 5 damage.")
    f_player_health-=5 
    final_am_i_dead()

  if attack_succsess == "1" and player_attack == "3":
    print(f"The King uses his {king_attacks}  attack but you use create a nightmare in the kings mind. He becomes distracted and his attack is rebound.")
    f_king_health-=30
    print("You take no damage.")
    print("The King takes 30 damage")
    final_am_i_dead()

  elif attack_succsess == "2" and player_attack == "3":
    print(f"The King uses his {king_attacks} attack! You Attempt to give the king a nightmare but he closes his mind and rebounds it on you. You become distracted and the king attacks.")
    print("You take 9 damage.")
    f_player_health-=9
    final_am_i_dead()

  if attack_succsess == "1" and player_attack == "2":
    print(f"The King uses his {king_attacks} attack. You take 10 damage. You return the attack with a Chain Slash attack! The king takes 20 damage.")
    f_player_health-=10
    f_king_health-=20
    final_am_i_dead()

  elif attack_succsess == "2" and player_attack == "2":
    print(f"The King uses his {king_attacks} attack. You take 11 damage. You attempt to retrun the attack with a chain slash attack but you fail.")
    f_player_health-=11
    final_am_i_dead()


  if attack_succsess == "1" and player_attack == "1":
    print(f"The King uses his {king_attacks} attack! You raise the ground infornt of you and create a sheild that rebounds the kigns attack.! The king takes 20 damage.")
    f_king_health-=20
    final_am_i_dead()

  elif attack_succsess == "2" and player_attack == "1":
    print(f"The King uses his {king_attacks} attack! You take 10 damage. You attempt to terraform the arena but the king is faster and hits you.")
    print("You take 10 damage.")
    f_player_health-=10
    final_am_i_dead()

def final_am_i_dead():
  if f_player_health <= 0:
    print("The dragon lands the final blow and you collapse. The last thing you hear is the laugh of the dragon before it all fades to black. "+text.Red+"GAME OVER"+text.End)
    end()
  elif f_king_health <= 0:
   final_ending()
  else:
    final_player()

def final_ending():
  print("You scream at the king. Your face about an inch from his. I KNOW YOUR WEAKNESS, YOU HAVE NO DOMINION IN THIS WORLD, I NO LONGER FEAR YOU. The king let out screams of rage. The scream fades to nothing as you deliver the final blow to the fallen king. The very fabric of reality begins to crack. Everything beigns to fragment and a brilliant bright light shines through the cracks. All feeling evacuates your body. You begin to float. As the world caves in, you start to drift off to the heavens. As you close your eyes. An overwhelming sense of peace floods your senseless body. You begin to fall back to earth. Your eyes fly open.")
  print("You wake with a start, in a cold sweat. Then, you lay back down again, with a sigh of relif. After all, it was just a dream...")
  print(text.Blue+"You have unlocked the Final Ending: Back To Reality"+text.End)
  end()

#---------------------------------------------------------------

bear_encounter()
