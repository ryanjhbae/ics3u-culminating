# Authors: Ryan Bae and Aayush Dave
# Due Date: January 30, 2018
# Teacher: Mr. Berardi
# File name: crossover.py
# Description: An action and turn-based RPG using characters from different franchises.

from easygui import * #Imports easygui mod/library
import random #Imports random library
import PIL #Imports the python pillow library.
from PIL import Image #Needed to import PIL.

def menu(msg): #Defines a function for the menu that players see.
    
    menu_list = ["Start", "Instructions", "Exit"] #The options that players can choose
    image = "crossover.gif" #The Logo of our game. 
    userinput = buttonbox(msg,title, image = image, choices = menu_list) #Allows the user to choose an option.
    if userinput == "Start": #If user chooses this option, this set of code runs.
        return 1 #Returns 1
    elif userinput == "Exit": #If user chooses to exist, this runs.
        exit() #Kills program
    while userinput == "Instructions": #If user chooses this option, this set of code runs.
        msg = ("This game is an RPG fighting game where the user chooses a character to play as." +
        "This character has a certain amount of HP and three abilities." + 
        "The abilities can either be attack based or defense based.") #Instructions for new players.
        msgbox(msg) #This message above is placed on a separate pop up.
        msg = "The user gets to choose the enemy they face or have it play out as random and then they must fight. The first character to lose all their HP loses." #Instructions part two.
        msgbox(msg) #This message above is placed on a separate pop up.
        msg = "There is also the in game currency that allows character's to make a move: this currency is called mana. Each player gets 100 mana after every turn. If the user chooses to pass, the user gets 100 mana added on to the original amount since a turn has passed." #Instructions for the in game currency.
        msgbox (msg) #Prints out the previous instruction as a separate messagebox.
        msg = "" #Blank message. Used since logo has the name of the game.
        menu_list = ["Start","Instructions","Exit"] #Prompts user to choose an option
        userinput = buttonbox(msg,title, image = image, choices = menu_list) #Allows the user to choose an option.
        if userinput == "Start": #If user chooses this option, this set of code runs.
            return 1 #Returns 1
        elif userinput == "Exit": #If user chooses to exist, this runs.
            exit() #Kills program

def exit_confirm(title): #Confirms user exit.
    msg = "Are you sure you want to exit?" #Asks user if they are sure.
    choices = ["Yes", "No"] #Gives them choices.
    userinput = buttonbox(msg,title,choices = choices) #Allows user to choose.
    if userinput == "Yes": #If they want to leave, this runs.
        exit() #Kills program.
    elif userinput == "No": #If user has made a mistake, this runs.
        return 1 #Returns a value that allows them to go back.
    
def gametype_function(title): #Allows them to choose the AI.
    
    gametype_list = ["Random AI","Pick AI"] #Options for user to choose from.
    msg = "Pick a gametype." #Prompts user to choose.
    gametype = buttonbox(msg,title,choices = gametype_list) #Lets user choose the gametype.
    return gametype #Returns their choice.

def character_name(character): #Function that deciphers the name of the character based on the image chosen.

    name_array = {"darth_vader.gif" : "Darth Vader",
                  "yoda.gif": "Yoda",
                  "boba_fett.gif": "Boba Fett",
                  "thor.gif": "Thor",
                  "hulk.gif": "Hulk",
                  "optimus_prime.gif": "Optimus Prime",
                  "bumblebee.gif": "Bumblebee",
                  "dumbledore.gif": "Dumbledore",
                  "voldemort.gif": "Voldemort"} #Name the character based on the image chosen.
    
    character_name = name_array[character] #Names the character based on the image chose.

    return character_name #Returns the name.

def difficulty_function(title): #Difficulty meter.
    
    difficulty_list = ["Easy","Medium","Hard"] #Gives user options.
    msg = "Pick a difficulty."#Promots user to choose. 
    difficulty = buttonbox(msg,title,choices = difficulty_list)#Lets the user choose a difficulty scale.
    return difficulty #Returns their preferrred difficulty. 

def gametype(title): #Allows them to choose the AI.
    
    gametype_list = ["Random AI","Pick AI"] #Options for user to choose from.
    msg = "Pick a gametype." #Prompts user to choose.
    gametype = buttonbox(msg,title,choices = gametype_list) #Lets user choose the gametype.
    return gametype #Returns their choice.

def moveset_function(character):#When the fight begins, this function allows user to choose their moves. 
    msg = "Pick a move." #Prompts user.

    darth_vader_moves = ["vader_choke.gif","vader_lightsaber.gif","lightsaber_strike.gif","pass.gif"] #Darth vader's moveset.
    yoda_moves = ["yoda_block.gif","yoda_lightsaber.gif","lightsaber_strike.gif","pass.gif"] #Yoda's moveset.
    boba_fett_moves = ["blaster.gif", "flamethrower.gif", "rpg.gif","pass.gif"] #Boba Fett's moveset.
    thor_moves = ["hammer_throw.gif", "lightning_thor.gif", "hammer_block.gif","pass.gif"] #Thor's moveset.
    hulk_moves = ["PUNCH.gif", "SMASH.gif", "sonic_clap.gif","pass.gif"] #Hulk's moveset.
    optimus_prime_moves = ["roll_out.gif", "shield.gif", "truck_slam.gif","pass.gif"] #Optimus Prime's moveset.
    bumblebee_moves = ["roll_out.gif", "need_for_speed.gif", "retreat.gif","pass.gif"] #Bumblebee's moveset.
    dumbledore_moves = ["inferno.gif", "brackium_emendo.gif", "aquamenti.gif","pass.gif"] #Dumbledore's moveset.
    voldemort_moves = ["crucio.gif", "avada_kedavra.gif", "horcrux.gif","pass.gif"] #Voldemort's moveset.

    move_array = {"darth_vader.gif" : darth_vader_moves,
                  "yoda.gif": yoda_moves,
                  "boba_fett.gif": boba_fett_moves,
                  "thor.gif": thor_moves,
                  "hulk.gif": hulk_moves,
                  "optimus_prime.gif": optimus_prime_moves,
                  "bumblebee.gif": bumblebee_moves,
                  "dumbledore.gif": dumbledore_moves,
                  "voldemort.gif": voldemort_moves} #A set of moves is matched to the image/character chosen.

    moveset = move_array[character] #Moveset is based on the moves.
        
    return moveset #Returns the moves.

def player_move_prompt(title,moveset): #Function that prompts user to move.
    msg = "Pick a move." #Prompts user.

    player_move = buttonbox(msg,title,image = moveset,choices = []) #Makes the buttonboxes the moveset.
    return player_move #Returns the move.

def ai_move_function(moveset): #Function for the A.I.'s moves.
    ai_move = random.choice(moveset) #Randomly chooses a move.
    return ai_move #Returns said move.
    
def health_determiner(character): #Determines the character's health at the start.
    
    health_array = {"darth_vader.gif" : 250,
                    "yoda.gif" : 150,
                    "boba_fett.gif" : 250,
                    "thor.gif" : 250,
                    "hulk.gif" : 400,
                    "optimus_prime.gif" : 300,
                    "bumblebee.gif" : 250,
                    "dumbledore.gif" : 200,
                    "voldemort.gif" : 200} #The H.P. for each character. Picture corresponds to the value to the right of it (after the colon).

    health = health_array[character] #Finds the character's health baed on the array above.
    return health #Returns the health.

def cost_determiner(move): #Determines the cost of each move.
    
    cost_array = {"vader_choke.gif" : 200,
                  "vader_lightsaber.gif" : 100,
                  "lightsaber_strike.gif" : 200,
                  "yoda_block.gif" : 150,
                  "yoda_lightsaber.gif" : 100,
                  "lightsaber_strike.gif": 200,
                  "blaster.gif": 100,
                  "flamethrower.gif": 200,
                  "rpg.gif": 300,
                  "hammer_throw.gif": 100,
                  "lightning_thor.gif": 200,
                  "hammer_block.gif": 200,
                  "PUNCH.gif": 200,
                  "SMASH.gif": 300,
                  "sonic_clap.gif": 100,
                  "roll_out.gif": 100,
                  "shield.gif": 200,
                  "truck_slam.gif": 150,
                  "need_for_speed.gif": 200,
                  "retreat.gif": 150,
                  "inferno.gif": 200,
                  "brackium_emendo.gif": 200,
                  "aquamenti.gif": 100,
                  "crucio.gif": 250,
                  "avada_kedavra.gif": 300,
                  "horcrux.gif" : 100,
                  "pass.gif" : 0} #The cost (in Mana) for the usage of each move.

    cost = cost_array[move] #Assigns a cost to each move.
    return cost #Returns the cost.

def player_cost_checker(cost,player_mana): #Function to see whether the user has enough mana to use move.
    value1 = player_mana - cost #Subtracts the cost from the user's total mana.
    if  value1 < 0: #If the mana remaining is less than 0, this runs.
        msg = ("You don't have enough mana for this move. It costs " +
                str(player_move_cost) + " mana but you only have " +
                str(player_mana) + ". Please pick another move.") #Tells user that they cannot use this move due to a lack of mana.
        msgbox(msg) #Prints out the message.
        return 1 #Returns an unconditional value.
        
    else: #If mana is enough, this runs.
        msg = ("Are you sure you want to use this move? It costs " +
                str(player_move_cost) + " mana. You will have " +
                str(player_mana - player_move_cost) + " mana remaining.") #Allows user to reconsider their choice.
        choices = ["Yes","Let me reconsider"] #The choices presented to user.
        userinput1 = buttonbox(msg,title,choices = choices) #Allows user to choose.

        if userinput1 == "Yes": #If they wish to use the move, this runs.
            return 2 #Returns this unconditional value.
        elif userinput1 == "Let me reconsider": #If they do not want to use the move, this runs. 
            return 1 #Returns this unconditional value (1 takes them back to movescreen, 2 continues the code).
    
def ai_cost_checker(cost,ai_mana): #Determines the cost for A.I. since A.I. cannot be prompted to move on their own.
    if ai_mana - cost < 0: #If the amount of mana remaining after cost is subtracted is less than 0, this runs. 
        return 1 #Returns an unconditional value that does the same thing as the return value of 1 from the previous function.
    else: #If there is enough mana, this runs.
        return 2 #Returns the unconditional value that continues the code.

def move_values_function(move): #This function determines the attack power, defensive power and longevity factor of eah move.
    move_values_array = {"vader_choke.gif" : [50,0,2],
                         "vader_lightsaber.gif" : [50,0,1],
                         "yoda_lightsaber.gif" : [0,50,1],
                         "lightsaber_strike.gif" : [60,0,2],
                         "yoda_block.gif" : [0,40,1],
                         "blaster.gif" : [30,0,4],
                         "flamethrower.gif" : [120,0,1],
                         "rpg.gif" : [120,0,1],
                         "hammer_throw.gif" : [50,0,1],
                         "lightning_thor.gif" : [100,0,1],
                         "hammer_block.gif" : [0,40,1],
                         "PUNCH.gif" : [75,0,1],
                         "SMASH.gif" : [200,0,1],
                         "sonic_clap.gif" : [50,0,1],
                         "roll_out.gif" : [75,0,1],
                         "shield.gif" : [0,50,1],
                         "truck_slam.gif" : [100,0,1],
                         "need_for_speed.gif" : [50,0,2],
                         "retreat.gif" : [0,25,2],
                         "inferno.gif" : [100,0,1],
                         "aquamenti.gif" : [40,0,1],
                         "crucio.gif" : [50,0,1],
                         "avada_kedavra.gif" : [120,0,1],
                         "horcrux.gif" : [0,0,0],
                         "brackium_emendo.gif" : [0,0,0],
                         "pass.gif": [0,0,0]} #Values are assigned based on the array.

    move_values = move_values_array[move] #Each move must be properly assigned before the value is returned.
    return move_values #Return move values.

def health_updater1(move_values,prev_moves,character_health,enemy_move_values,enemy_prev_moves,enemy_health): #Function that updates the health of both characters.
     
    no_prev_moves = len(prev_moves) #Determines how long each move will last (the effect it will have on user. If value is 1, it lasts one turn.)
    no_enemy_prev_moves = len(enemy_prev_moves) #Determines how long the effect of the enemy's move will last.
    total_attack = move_values[0] #Assigns the value of the total attack based on the moves array.
    for x in range (0,no_prev_moves): #A for loop used for the amount of time the attack has an affect.
        total_attack += prev_moves[x][0] #Adds the amplitude of the attack each time based on how many turns it lasts.

    current_defense = move_values[1] #Assigns the value for the total attack based on the values from the array previously.
    total_enemy_defense = enemy_move_values[1] #Determines the enemy's move defense based on array.
    for x in range(0,no_enemy_prev_moves): #Creates a for loop for the enemy's defense based on its length.
        total_enemy_defense += enemy_prev_moves[x][1] #Continues adding the amount of defense from each attack based on its factor (length).
    
    return (total_attack,total_enemy_defense,current_defense,enemy_health) #Returns these values.

def health_updater2(return2,health,move,enemy_health,enemy_prev_move,turn,difficulty): #Another function that updates the health of both characters (used for the actual math used to determine the amount of health leftover). 
    total_attack = return2[0] #Finds the attack power based on the array from before.
    total_enemy_defense = return2[1] #Finds the enemy's defense based on the array from before.
    current_defense = return2[2]  #Finds the current defense value by retrieving it from the return values.
    enemy_health = return2[3] #Finds the enemy health by retrieving it from the return values from the function with the health array.
    
    net_attack = total_attack - total_enemy_defense #Net attack is the attack that actually damages the user.
    
    if move == "brackium_emendo.gif": #Used for the special move which does not simply do a set attack or defense but instead adds HP to user.
        health += 50 #Adds 50 to the user's health. 
    if enemy_prev_move == "horcrux.gif": #Used for the special move which blocks out 75% of an attack.
        net_attack = net_attack*0.25 #Attack only does 25% of its original damage.
    
    if net_attack < 0: #If net attack is less than 0, this runs. 
        net_attack == 0 #Makes the attack equal to 0 in order to not add to the enemy's health.
    if net_attack > 0:#If net attack is higher than 0,  this runs.  
        enemy_health -= net_attack #Subtracts the attack from the enemy health. 
        
    if turn%2 != 0: #If the turn is an odd one, it belongs to the user, meaning, based on the difficulty chosen, the attacks do different amounts of damage.
        if difficulty == "Easy": #If difficulty is easy, this runs.
            net_attack = net_attack*1.15 #The attack does 115% damage.
        elif difficulty == "Hard": #If difficulty is hard, this runs.
            net_attack = net_attack*0.85 #Attack only does 85% of damage.
            #Medium = 100% of the attack.

    if health < 0:
        health = 0
    if enemy_health < 0: #Set the health of both the player and AI to 0 if it is in the negatives (prevents negative health values). 
        enemy_health = 0
        
    return (net_attack,total_enemy_defense,health,enemy_health) #Returns these values.
    
def message_function1(return3,current_defense,enemy_prev_move,move,mana): #This function returns the move chosen by the user.
    net_attack = return3[0] #Net attack is called from the previous return values.
    total_enemy_defense = return3[1] #Defense is called from the previous return values.
    health = return3[2] #Health is called from the previous function's return values.
    enemy_health = return3[3] #Enemy health value is called from previous return values.
    
    if move == "brackium_emendo.gif": #If the move is this one, a special message runs.
        msg = ("You have cast a healing charm, and increased your HP by 50! Your health is now " +
               str(health) + ".")  #Message that the user will see when they use this move.
        msgbox(msg) #Printed out message.
    elif move == "horcrux.gif": #If move is this, a special message runs.
        msg = ("You have sacrificed a horcrux, which will allow you to block 75% of the enemy's attack next turn.") #User will see this message.
        msgbox(msg) #Prints out the message.
    
    if net_attack > 0 and enemy_prev_move == "horcrux.gif": #If user uses a move and A.I. blocks it with horcrux, this runs.
        msg = ("The enemy has sacrificed a horcrux and blocked 75% of your attack's damage! They have only taken " +
               str(net_attack) + " damage and their health is now " + str(enemy_health) + ". Maybe next turn!") #This message will be shown.
    elif net_attack > 0 and total_enemy_defense == 0: #If attack hits and the enemy has no defense, this runs.
        msg = ("You have dealt " + str(net_attack) + " damage to the enemy! Their health is now " + str(enemy_health) + ".") #This message will be displayed.
    elif net_attack > 0 and total_enemy_defense > 0: #If the enemy has some defense, this runs.
        msg = ("You have dealt " + str(net_attack) + " damage to the enemy! Unfortunately, they've blocked " +
               str(total_enemy_defense) + " damage. Their health is now " + str(enemy_health) + ".") #This message will be displayed.
    elif net_attack == 0 and total_enemy_defense > 0: #If the net attack is 0, this runs.
        msg = ("The enemy has blocked all of your damage!") #This message will be displayed.
    elif move == "pass.gif": #If user chooses to pass their turn, this runs.
        msg = ("You have chosen to pass this turn, saving 100 mana. You now have " + str(mana) + " mana.")  #This message will be displayed.
    elif net_attack == 0 and total_enemy_defense == 0: #If user has defense, this runs.
        msg = ("Your move will allow you to block " + str(current_defense) + " damage next turn.") #This message will be displayed.
               
    msgbox(msg) #Prints the message based on the choice and circumstances. 
               
def message_function2(return3,current_defense,enemy_prev_move,move,mana): #Function that prints out messages based on the enemy's moves.
    net_attack = return3[0] #Net attack is called from the previous return values.
    total_enemy_defense = return3[1] #Defense is called from the previous return values.
    health = return3[2] #Health is called from the previous function's return values.
    enemy_health = return3[3] #Enemy health value is called from previous return values.
    
    if move == "brackium_emendo.gif": #If enemy chooses this move, this set of code runs.
        msg = ("The enemy has cast a healing charm, which has increased their HP by 50. Their health is now " +
               str(health) + ".") #Prints this message.
        msgbox(msg) #Makes the message come out on a separate messagebox.
    elif move == "horcrux.gif": #If A.I. chooses this move, this set of code runs.
        msg = ("The enemy has sacrificed a horcrux, which will allow them to block 75% of your attack next turn.") #The message user will see.
        msgbox(msg) #Prints out the message. 
  
    if net_attack > 0 and enemy_prev_move == "horcrux.gif": #If user chooses the horcrux move, this runs. 
        msg = ("Your horcrux blocked 75% of the enemy's attack! They have dealt " +
               str(net_attack) + " damage and your health is now " + str(enemy_health) + ".") #This message will be printed.
    elif net_attack > 0 and total_enemy_defense == 0: #If the attack does damage to the user.
        msg = ("The enemy has dealt " + str(net_attack) + " damage to you! Your health is now " + str(enemy_health) + ".") #Prints out this message.
    elif net_attack > 0 and total_enemy_defense > 0: #If some of the attack is blocked out by the user, this runs.
        msg = ("The enemy has dealt " + str(net_attack) + " damage to you! Thankfully, you had some defense so you blocked"
               + str(total_enemy_defense) + " damage. Your health is now " + str(enemy_health) + ".") #Prints out this message.
    elif net_attack == 0 and total_enemy_defense > 0: #If attack does no damage this runs.
        msg = ("You have blocked all of the enemy's damage!") #Prints out this message.
    elif move == "pass.gif": #If A.I. chooses to skip turn, this runs.
        msg = ("The enemy has chosen to pass this turn, saving 100 mana. They now have " + str(mana) + " mana.") #Prints out this message.   
    elif net_attack == 0 and total_enemy_defense == 0: #If enemy has defense, this runs.
        msg = ("The enemy's move will allow them to block " + str(current_defense) + " damage next turn.") #Prints out this message.

    msgbox(msg) #Prints out a different message based on the scenario.

def prev_moves_updater1(player_prev_moves,ai_prev_moves,player_move_values):#Function used to identify the length of the previous move, mainly for the player turn.
    length1 = len(player_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    length2 = len(ai_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    
    for x in range(0,length1): #For loop for the length of the factor and its effects.
        factor = player_prev_moves[x][0] #Calls on the first value in the player_prev_move array.
        factor2 = factor - 1 #Creates a new variable that subtracts one from the factor for as long as the for loop runs.
        if factor > 1: #If the factor is higher than 1, this runs.
            del(player_prev_moves[x][2]) #Deletes the third value from the previously mentioned array.
            player_prev_moves[x].append(factor2) #Adds the new factor in its place.
            
    for x in range(0,length2): #For loop for the A.I.'s factor. 
        factor = player_prev_moves[x][0] #Calls on the first value in the player_prev_move array.
        factor2 = factor - 1 #Creates a new variable that subtracts one from the factor for as long as the for loop runs.
        if factor > 1: #If the factor is higher than 1, this runs.
            del(ai_prev_moves[x][2]) #Deletes the third value from the previously mentioned array.
            ai_prev_moves[x].append(factor2) #Adds the new factor in its place.

    factor = player_move_values[2] #Calls upon the new factor.
    if factor > 1: #If it is higher than 1, this runs.
        player_prev_moves.append(player_move_values) #Adds the player move value to the array.

    return (player_prev_moves,ai_prev_moves) #Returns these values.
        
def prev_moves_updater2(player_prev_moves,ai_prev_moves,ai_move_values): #Function for determining the previous move, mainly for the A.I. turn.  
    length1 = len(player_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    length2 = len(ai_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    
    for x in range(0,length1): #For loop for the length of the factor and its effects.
        factor = player_prev_moves[x][1] #Calls on the second value in the player_prev_move array.
        factor2 = factor - 1 #Creates a new variable that subtracts one from the factor for as long as the for loop runs.
        if factor > 1: #If the factor is higher than 1, this runs.
            del(player_prev_moves[x][2]) #Deletes the third value from the previously mentioned array.
            player_prev_moves[x].append(factor2) #Adds the new factor in its place.
            
    for x in range(0,length2): #For loop for the A.I.'s factor. 
        factor = player_prev_moves[x][0] #Calls on the first value in the player_prev_move array.
        factor2 = factor - 1 #Creates a new variable that subtracts one from the factor for as long as the for loop runs.
        if factor > 1: #If the factor is higher than 1, this runs.
            del(ai_prev_moves[x][2]) #Deletes the third value from the previously mentioned array.
            ai_prev_moves[x].append(factor2) #Adds the new factor in its place.


    factor = ai_move_values[2] #Calls upon the new A.I. factor.
    if factor > 1: #If it is higher than 1, this runs.
        ai_prev_moves.append(ai_move_values)  #Adds the A.I. move value to the array.   
    
    return (player_prev_moves,ai_prev_moves) #Returns these functions.

def universal_moves_updater(return4): #Function that updates both factors based on the previous two functions.
    player_prev_moves = return4[0] #Calls upon the first return value in the previous function's return values.
    ai_prev_moves = return4[1] #Calls upon the second return value from the previous function's returns values. 
    length1 = len(player_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    length2 = len(ai_prev_moves) - 1 #Subtracts one from the length since a turn has passed.
    
    for x in range(0,length1): #Creates for loop for the factor's longevity.
        factor = player_prev_moves[x][1] #Calls upon the factor value from the player's previous moves array.
        if factor <= 0: #If factor is less than or equal to 0, this runs.
            del(player_prev_moves[x]) #Deletes the factor from the player's array.
             
    for x in range(0,length2): #Creates for loop for the factor's longevity.
        factor = ai_prev_moves[x][0] #Calls upon the factor value from the A.I.'s previous moves array.
        if factor <= 0:  #If factor is less than or equal to 0, this runs.
            del(ai_prev_moves[x]) #Deletes the factor from the A.I.'s array.
            
    return (player_prev_moves,ai_prev_moves) #Returns these values.

def endmenu(title): #Function that runs when one player has won the game.
    choices = ["Back to Main Menu", "Exit"] #Gives the user two choices: start again or leave the program.
    msg = "The Game has ended. What would you like to do?" #A message that will be printed.
    userinput = buttonbox(msg,title,choices) #Allows user to make their choice.
    if userinput == "Back to Main Menu": #If user wishes to go back to the menu, this runs.
        return 1 #Returns the unconditional value of 1.
    elif userinput == "Exit": #If user wishes to leave, this runs.
        exit() #User exists.

msg = "" #Blank message  for now.

title = "Crossover" #Name of the Game

character_list = ["darth_vader.gif", "yoda.gif", "boba_fett.gif", "thor.gif", "hulk.gif","optimus_prime.gif","bumblebee.gif","dumbledore.gif","voldemort.gif"] #Allows user to choose a charachter based on their picture.

while menu(msg) == 1: #Code for game. Calls on the menu function and runs it. If the menu function's return is 1, this runs.
    number_of_players = ["Singleplayer","Exit"] #Allows user to choose a gameplay style.
    userinput = buttonbox(msg,title, choices = number_of_players) #Allows user to choose.
    
    while userinput == "Exit": #If they wish to leave, this runs.
        confirmation = exit_confirm(title) #Confirms user's choice.
        if confirmation == 1: #If the return value from the confirmation function is 1, this runs.
            userinput = buttonbox(msg,title, choices = number_of_players) #Brings user back to the original choice.
    
    while userinput == "Singleplayer": #While  user chooses singleplayer, this part of the code runs.
        difficulty = difficulty_function(title) #Calls and runs the difficulty function.
        player_character = buttonbox("Pick a character to play as.", title, image = character_list, choices = "") #Allow user to choose a character.
        player_character_name = character_name(player_character) #Defines the character by calling upon the function that names the character based on the image chosen.
        player_health = health_determiner(player_character) #Determines the user's health based on the array from the function that was called upon.
        player_moveset = moveset_function(player_character)#Calls upon the function that determines the player's moveset and runs it.

        gametype = gametype_function(title) #Calls upon the gametype function, which allows the user to choose an enemy or have the program make a random choice.
        
        if gametype == "Random AI": #If gametype is random A.I., this runs.
            ai_character = random.choice(character_list) #Program chooses a random character from the character list.
            
        elif gametype == "Pick AI": #If user wishes to choose its enemy, this runs. 
            msg = ("Pick the character for the AI.") #Allows user to choose.
            ai_character = buttonbox(msg,title, image = character_list, choices = "") #Character chooses their challenger.
            
        ai_character_name = character_name(ai_character) #Names the A.I.'s character based on the function that is called and run.
        msg = ("The AI has picked " + str(ai_character_name) + ".") #Tells the user what character the A.I. chose.
        msgbox(msg) #Prints the previous message.
        ai_health = health_determiner(ai_character) #Determines the A.I.'s health by using the health_determiner function.
        ai_moveset = moveset_function(ai_character) #Determines the A.I's moveset based on the character chosen by using the function.
        
        player_mana = 0 #As of now, player mana is 0.
        ai_mana = 0 #As of now, A.I. mana is 0.
        player_move_values = [0,0,0] #Sets all the values (attack, defense, factor) to 0.
        player_prev_move = "" #Blank for now.
        player_prev_moves = [[0,0,0]] #Sets all values in the array to 0 as to not confuse the program and to define the variable.
        ai_move_values = [0,0,0] #Sets all values in the array to 0 as to not confuse the program and to define the variable.
        ai_prev_move = "" #Blank for now.
        ai_prev_moves = [[0,0,0]] #Sets all values in the array to 0 as to not confuse the program and to define the variable.
        turn = 0 #Turn is set at 0 as of now.
        
        while True: #Runs until this statement is false.
            turn += 1 #Adds one turn.
            player_mana += 100 #Adds 100 mana for player.
            ai_mana += 100 #Adds 100 mana for A.I.

            player_move = player_move_prompt(title,player_moveset) #Calls and runs the player move prompt function.
            player_move_cost = cost_determiner(player_move) #Calls and runs the cost determiner function, the function that lets the user know if they have enough mana to use a move.
            return1 = player_cost_checker(player_move_cost,player_mana) #Calls and runs the cost determiner function, the function that lets the user know if they have enough mana to use a move.

            while return1 == 1: #While the return value of the function from before is 1, this runs.
                player_move = player_move_prompt(title,player_moveset) #Calls and runs the player move prompter function.
                player_move_cost = cost_determiner(player_move) #Calls and runs the player move cost determiner function.
                return1 = player_cost_checker(player_move_cost,player_mana) #Calls and runs the cost checker function.
                
            player_mana -= player_move_cost #Subtracts cost from the player mana.

            player_move_values = move_values_function(player_move) #Calls and runs the move value function.
            return2 = health_updater1(player_move_values,player_prev_moves,player_health,ai_move_values,ai_prev_moves,ai_health) #Calls and runs the first health updater function.
            return3 = health_updater2(return2,player_health,player_move,ai_health,ai_prev_move,turn,difficulty) #Calls and runs the first health updater function.
            current_defense = player_move_values[1] #Sets the current defense for the player by calling it from the player_move_values array.
            message_function1(return3,current_defense,ai_prev_move,player_move,player_mana) #Calls and runs the message function.
            return4 = prev_moves_updater1(player_prev_moves,ai_prev_moves,player_move_values) #Calls and runs the previous move finder function.
            return5 = universal_moves_updater(return4) #Calls and runs the universal moves updater function.
            player_prev_moves = return5[0] #Sets the player previous move value as the first return value from the previous function's return values.
            ai_prev_moves = return5[1] #Sets the A.I. previous move value as the second return value from the previous function's return values.             

            ai_health = return3[3] #Sets A.I. health as the fourth return value from the health_updater2 function.
            player_health = return3[2] #Sets player health as the third return value from the health_updater2 function.
            
            if ai_health <= 0: #If A.I. has no health, this runs.
                msg = ("Congratulations! You have won the game.") #Informs the user of  their victory.
                msgbox(msg) #Prints this message.
                break #Breaks out of the loop.
            #---------------------------------------------------------

            turn += 1 #Adds one turn. 

            ai_move = ai_move_function(ai_moveset) #Calls and runs the A.I. move function since this is the A.I.'s turn. 
            ai_move_cost = cost_determiner(ai_move) #Calls and runs the A.I. cost deteminer function. 
            return1 = ai_cost_checker(ai_move_cost,ai_mana) #Calls and runs the A.I. cost checker function to make sure A.I. has enough mana to use a move.
            
            while return1 == 1: #While the return value from the ai_cost_checker () function is equal to 1, this runs.
                ai_move = ai_move_function(ai_moveset) #The A.I.'s moves are based on the array that calls on their moveset based on the character the A.I. is playing as.
                ai_move_cost = cost_determiner(ai_move) #Determines the cost of the move by calling and running the cost determiner function. 
                return1 = ai_cost_checker(ai_move_cost,ai_mana) #Runs the cost checker function again to make sure A.I. can use this move.
                
            ai_mana -= ai_move_cost #Subtracts the cost of the move from the A.I.'s mana.
            
            ai_move_values = move_values_function(ai_move) #Calls and runs the move value function.
            return2 = health_updater1(ai_move_values,ai_prev_moves,ai_health,player_move_values,player_prev_moves,player_health) #Calls and runs the first health update function. 
            return3 = health_updater2(return2,ai_health,ai_move,player_health,player_prev_move,turn,difficulty) #Calls and runs the second health updater function.
            current_defense = ai_move_values[1] #Assigns the current defense value from the AI's move value array.
            message_function2(return3,current_defense,player_prev_move,ai_move,ai_mana) #Calls and runs the message function. 
            return4 = prev_moves_updater2(player_prev_moves,ai_prev_moves,ai_move_values) #Calls and runs the second previous move updater function.
            return5 = universal_moves_updater(return4) #Calls and runs the universal previous move function.
            player_prev_moves = return5[0] #Sets the player's previous move value as the first value in the return5 return value's array. 
            ai_prev_moves = return5[1] #Sets the A.I.'s previous move value as the second value in the return5 return value's array.

            ai_health = return3[2] #Finds the A.I. health by calling the third value from the second health updater function's return list.
            player_health = return3[3] #Finds the player health by calling the fourth value from the second health updater function's return list.

            if player_health <= 0: #If the player has no health, this runs.
                msg = ("You have lost the game.") #Informs the user of  their loss.
                msgbox(msg) #Prints this message.
                break #Breaks out of the loop.
            
        endreturn = endmenu(title) #Runs the endmenu function.
        if endreturn == 1: #If user chooses to go back to the main menu, this runs.
            msg = "" #Blank message. 
            menu(msg) #Runs the menu function.  
