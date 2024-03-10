import random


# Creates the Battleship board.
def build_board():
    ''' Creates an 11 x 11 numbered board.
       Then fills the grid with ~ symbol.'''
    
    
    grid_size = 11
    
    board = []
    
    for row in range(grid_size):
        
        # When creating the list add the row numbers.
        grid = [row]
        
        for col in range(grid_size):
            
            # On the first row add the column numbers.
            if row == 0:
                if col > 0:
                    grid.append(col)
            else:
                if col > 0:     
                    grid.append("~")
            
        board.append(grid)
        
    
    return board


# Displays the inserted board (player or blank).
def display_board(board):
    # Allows me to quickly call what board I want the user to see.
    
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
    print()
    

# Checks the user input to see if its acceptable.
def valid_move(board, n, ship_r, ship_c, direction):
    
    ''' After user input, this checks to see if the move is valid,
    and within the grid dimensions, along with any other ships in its place.
    It then goes on to place the ship where the user selected
    or return an error message.'''
    
    
    # Grid size minus ship size. max placement position.
    a = 11 - n
    
    error = False
    
    
    if direction == "down":
        
        # If row selection greater than max placement, error = True.
        if ship_r > a:
            error = True
            
        else:
            
            # Checks to see if ship is already placed there.
            for i in range(n):
                if board[ship_r+i][ship_c] == "0":
                    error = True
            
            # If the error variable hasnt changed continue to place ship.        
            if error == False:
                for i in range(n):
                    board[ship_r+i][ship_c] = "0"
                            
    
    elif direction == "up":
        
        # If row selection is less than the size of the ship (min distance).
        # Change error variable.
        
        if ship_r < n:
            error = True
            
        else:
            
            for i in range(n):
                if board[ship_r -i][ship_c] == "0":
                    error = True
                    
            if error == False:
                for i in range(n):
                    board[ship_r -i][ship_c] = "0"
                
                
    elif direction == "right":
        
        if ship_c > a:
            error = True
            
        else:
            
            for i in range(n):
                if board[ship_r][ship_c +i] == "0":
                    error = True
                    
            if error == False:
                for i in range(n):
                    board[ship_r][ship_c +i] = "0"
                
    elif direction == "left":
        
        if ship_c < n:
            error = True
            
        else:
            
            for i in range(n):
                if board[ship_r][ship_c - i] == "0":
                    error = True
            
            if error == False:
                for i in range(n):
                    board[ship_r][ship_c - i] = "0"
                
    
    # If error comes back as false make the function return false.
    # Else return the edited board with ship placement.
        
    if error == True:
        return False
    else:
        return board
               

# Checks to see if the ship has already been placed.
def check_piece(piece):

    
    if piece == "aircraft carrier":
        if a_c == 0:
            return True
        


    elif piece == "battleship":
        if bat == 0:
            return True
            
   
    elif piece == "cruiser":
        if cru == 0:
            return True
        
      
    elif piece == "destroyer":
        if des == 0:
            return True
              
    else:
        return False


# Allows the user to input what row, column and direction to place ship.
def user():
   
     
   
    print(f"""Ships to place.
    {a_c} Aircraft Carrier
    {bat} Battleship
    {cru} Cruiser
    {des} Destroyer
    """)

    select_ship = input("Which ship do you want to place: ").lower()

        
    
    while True:    
        ship_r = input("Row placement for ship: ")
        ship_c = input("Column placement for ship: ")
        
        if ship_r.isdigit() and ship_c.isdigit() == True:
            break
        else:
            print("\nPlease input a correct placement.\n")


        
    ship_r = int(ship_r)
    ship_c = int(ship_c)
        
    direction = input("Direction. (Up/Down/Left/Right): ").lower()
    print()

    return [select_ship, ship_r, ship_c, direction]


# Allows the computer to place its ships.
def computer():
    
    directions = ("down", "left", "up", "right")

    
    ship_r = random.randint(1,10)
    ship_c = random.randint(1,10)
    direction = random.choice(directions)
    
    
    
    return [ship_r, ship_c, direction]
    
  
# Checks to see if the user input has hit a ship.  
def attack(board, blank, attack_r, attack_c):
    '''This looks at the wether the user has hit a ship,
    and replace 0 with an X.
    It will also check to see if you have already selected
    that area.
    and finally it will mark a miss with _. '''
    
    while True:
        

        if board[attack_r][attack_c] == "0":
            blank[attack_r][attack_c] = "X"
            print("\nHIT!!!!\n")
            return False
            break
            
        elif blank[attack_r][attack_c] == "X":
            print("Already Selected.")
            return False
            
        elif blank[attack_r][attack_c] == "_":
            print("Already Selected.")
            return False
            
        else:
            blank[attack_r][attack_c] = "_"
            print("\nMISS!!!!\n")
            break
            
    # This will return the blank board with the up to date markers.    
    return blank   
        
        
# This will allow the computer to attack.       
def comp_attack(board, ship):
    '''This will select two random numbers for row and column.
    It will then check that to see if it has hit or missed.
    if a row and column has already been hit it will then try again.'''
    

    while True:

        placed = False

        hit = True


        for i, boat in enumerate(ship):
            

            boat_count = 0

            for mark in boat:

                row = mark[0]
                col = mark[1]

                if board[row][col] == "X":

                    boat_count = boat_count + 1


                if boat_count == len(boat):

                        ship.pop(i)




            for mark in boat:

                moves = ["up", "down", "left", "right"]

                row = mark[0]
                col = mark[1]

                if board[row][col] == "X":


                    while True:

                        move = random.choice(moves)

                        
                        if move == "down":
                            
            
                            if row + 1 < 11:

                                pos = board[row + 1][col]

                                if pos == "~" or pos == "0":

                                    attack_r = row + 1 
                                    attack_c = col

                                    placed = True
                                    
                                    break

                            



                                

                        if move == "up":
                            if row - 1 > 0:
                                
                                pos = board[row-1][col]

                                if pos == "~" or pos == "0":

                                    attack_r = row - 1 
                                    attack_c = col

                                    placed = True
                                    break
                            

                        if move == "right":
                            if col + 1 < 11:
                                
                                pos = board[row][col + 1]

                                if pos == "~" or pos == "0":

                                    attack_r = row 
                                    attack_c = col + 1

                                    placed = True
                                    break
                                

                        if move == "left":
                            if col - 1 > 0:
                                
                                pos = board[row][col - 1]

                                if pos == "~" or pos == "0":

                                    attack_r = row
                                    attack_c = col - 1

                                    placed = True
                                    break
                        



                        if len(moves) == 1:
                            break


                        moves.remove(move)

                    

                if placed == True:
                    break
                




     
        if placed == False:

            attack_r = random.randint(1,10)
            attack_c = random.randint(1,10)



        
        if board[attack_r][attack_c] == "0":
            board[attack_r][attack_c] = "X"
            print("\nYou've been HIT!!!!\n")

            hit = False
            break
            
        elif board[attack_r][attack_c] == "X":
            error = "Invalid" 

            
        elif board[attack_r][attack_c] == "_":
            error = "Invalid"

            
        
        else:
            board[attack_r][attack_c] = "_"
            print("\nTHEY MISSED!!!!\n")
            break
        




        




    ''' This will return the players board,
    which has been edited with the new markers.'''
    return [board, attack_r, attack_c, hit]  


# This checks to see if a ship has been sunk.
def check_ship(board, ship, attack_r, attack_c):
    '''This looks in the ship list to check,
    if each ship has been hit the correct number of times.
    Once a ships has been hit the correct number of times,
    it will be removed from the list.'''
        
        
    # Runs through the ship list.
    for i in range(len(ship)):
        
        # i will select what ship its looking at.
        # 1 and 2 are the indexes of row and column.
        row = ship[i][1]
        col = ship[i][2]
        
        direction = ship[i][3]
        
        number = ship[i][0]
        
        # This allows me to see which ship has been sunk.
        counter = 0
        

        if board[attack_r][attack_c] == "X":
            # When it looks at the first ship, 
            # iterate over it the number of markers it has.
            for k in range(number):
                

                # Check the direction to determine which way it has to look.
                
                if direction == "up":

                    # If up then iterate over row minus the number.
                    if board[row-k][col] == "X":

                        # If it finds an X add one to the counter and go again.
                        counter = counter + 1
                        
                        
                
                elif direction == "down":
                    
                        
                    if board[row+k][col] == "X":

                        counter = counter + 1
                    
                    
                    
                elif direction == "left":
                    
                    if board[row][col-k] == "X":
                        
                        counter = counter + 1
                        
                        
                        
                    
                elif direction == "right":
                    
                    
                    if board[row][col+k] == "X":

                            counter = counter + 1
                    
            

            # After it checks one ship, 
            # If counter is equal to the ships marker number,
            # Remove that ship from the list and return true.   
            if counter == number:
                
                sunk = number

                ship.pop(i)
                
                return [True, sunk]
            
            

            
def ship_location(ship):

    ship_list = []
    
        
    # Runs through the ship list.
    for i in range(len(ship)):
        
        # i will select what ship its looking at.
        # 1 and 2 are the indexes of row and column.
        row = ship[i][1]
        col = ship[i][2]
        
        direction = ship[i][3]
        
        number = ship[i][0]
    
        ship_number = []


        # When it looks at the first ship, 
        # iterate over it the number of markers it has.
        for k in range(number):
            
            ship_place = []

            # Check the direction to determine which way it has to look.
            
            if direction == "up":

                ship_place.append(row-k)
                ship_place.append(col)

                            
            elif direction == "down":

                ship_place.append(row+k)
                ship_place.append(col)
                
            
                
            elif direction == "left":

                ship_place.append(row)
                ship_place.append(col-k)
                
                        
                
            elif direction == "right":

                ship_place.append(row)
                ship_place.append(col+k)
            
            ship_number.append(ship_place)

        ship_list.append(ship_number)

    return ship_list

            
          
            
        

# Start of program.

# Placement phase.

print("""Welcome to Battleship!!!
Please Position your ships.\n""")

# Displays empty board.
display_board(build_board())

# Creates a board for the player.
player = build_board()

# Monitors what ships are available.
a_c = 1
bat = 1
cru = 1
des = 2
        
# Stores the ships that have been placed.
player_ship_storage = []

while True:
    
    
    # Stores user inputted ship selection, row, col and direction.
    user_move = user()
    
    
    # Checks ship placement.
    if check_piece(user_move[0]) == True:
        print("Ship already placed\n")
        
    elif check_piece(user_move[0]) == False:
        print("Please select a ship\n")
        
    else:
        
        # Checks to see if user input is vaild and able to place on board.
        
        if user_move[0] == "aircraft carrier":
            
            move = valid_move(player, 5, user_move[1], user_move[2], user_move[3])
            
            if move == False:
                print("Invalid Placement!")
                
            else:
                # Remove 1 from a_c.
                # Create an aircraft list and add it to storage.
                a_c = a_c - 1
                aircraft = [5, user_move[1], user_move[2], user_move[3]]
                player_ship_storage.append(aircraft)
            

                
        elif user_move[0] == "battleship":
            
            move = valid_move(player, 4, user_move[1], user_move[2], user_move[3]) 
            
            if move == False:
                print("Invalid Placement!")
            else:    
                bat -= 1
                battleship = [4, user_move[1], user_move[2], user_move[3]]
                player_ship_storage.append(battleship)
                
                
                
        elif user_move[0] == "cruiser":
            
            move = valid_move(player, 3, user_move[1], user_move[2], user_move[3])
            
            if move == False:
                print("Invalid Placement!")
            else:
                cru -= 1
                cruiser = [3, user_move[1], user_move[2], user_move[3]]
                player_ship_storage.append(cruiser)
        
        
                
        elif user_move[0] == "destroyer":
            
            move = valid_move(player, 2, user_move[1], user_move[2], user_move[3])
            
            if move == False:
                print("Invalid Placement!")
            else:
                des -= 1
                
                destroyer = [2, user_move[1], user_move[2], user_move[3]]
                
                player_ship_storage.append(destroyer)
        



        player_storage = ship_location(player_ship_storage)



        # Displays up to date board with placed ship.   
        display_board(player)
        
        # Updates the amount of ships that have been placed.
        total = a_c + bat + cru + des
        
        # Once all ships have been placed, break the loop.
        if total == 0:
            break
    

#------------------------------------------------------------------------------

# Builds a board for computer.
comp = build_board()

# Creates a list ready to store computer ships.
comp_ship_storage = []

# Allows computer to place ships on board.
for i in range(5):
    
      
    if i == 0:
        
        while True:
            
            # Loops round until a valid move is accepted.
            
            comp_move = computer()
            
            move = valid_move(comp, 5, comp_move[0], comp_move[1], comp_move[2])
            
            if move != False:
                
                # Once a move is valid store computer ship in storage.
                aircraft = [5, comp_move[0], comp_move[1], comp_move[2]]

                comp_ship_storage.append(aircraft)
                
                break

                
    if i == 1:

        while True:
            
            comp_move = computer()
            
            move = valid_move(comp, 4, comp_move[0], comp_move[1], comp_move[2])
            

            if move != False:
                
                battleship = [4, comp_move[0], comp_move[1], comp_move[2]]
            
                comp_ship_storage.append(battleship)
                break
        

            
    if i == 2:

        while True:
            
            comp_move = computer()
            
            move = valid_move(comp, 3, comp_move[0], comp_move[1], comp_move[2])
            
            
            if move != False:
                
                cruiser = [3, comp_move[0], comp_move[1], comp_move[2]]
            
                comp_ship_storage.append(cruiser)
                
                break

        
    # This allows the last two to place the 2 destroyers.     
    if i > 2:

        while True:
            
            comp_move = computer()
            
            move = valid_move(comp, 2, comp_move[0], comp_move[1], comp_move[2])
            

            if move != False:
                
                destroyer = [2, comp_move[0], comp_move[1], comp_move[2]]
            
                comp_ship_storage.append(destroyer)
                
                break

#------------------------------------------------------------------------------

# This is the start of the attack phase.


# Creates a blank board to show the user when they hit or miss.
blank_board = build_board()

# Tallies up how many ships have been sunk.
comp_ships = 0

player_ships = 0

# Loops over the attack phase until all ships are sunk.
while True:
        
    print("Player Attack\n")
    
    # Displays blank board to user.
    display_board(blank_board)
    
    # Loops over if user doesnt input number.
    while True:
        attack_r = input("Which row do you want to attack: ")
            
        attack_c = input("Which column do you want to attack: ")

        # Checks user input to see if number.
        if attack_r.isdigit() and attack_c.isdigit() == True:
            break
        else:
            print("\nPlease input a correct placement.\n")
    
    attack_r = int(attack_r)
    
    attack_c = int(attack_c)  
        
    
    # checks the computer board to see if anything is hit 
    # and places the result on blank board.
    player_move = attack(comp, blank_board, attack_r, attack_c)
    
    # Checks the blank board to see if it has the select number of hits.
    # If the hit markers == ship markers then run code.
    sunk_ship = check_ship(blank_board, comp_ship_storage, attack_r, attack_c)


    try:
        if sunk_ship[0] == True:

            ship = ""

            if sunk_ship[1] == 5:
                print("Aircraft Carrier has been sunk!\n")
            elif sunk_ship[1] == 4:
                print("Battleship has been sunk!\n")
            elif sunk_ship[1] == 3:
                print("Cruiser has been sunk!\n")
            elif sunk_ship[1] == 2:
                print("Destroyer has been sunk!\n")

            
            comp_ships = comp_ships + 1

    except TypeError:
        pass
        
        # If 5 ships have been sunk then end the loop.
    if comp_ships == 5:
        break
    
    # Displays updated board.
    display_board(blank_board)
    
    # Shows that user input was incorrect move or they hit a target.
    # So go again.
    if player_move == False:
        
        input("Press enter to Go Again!!")
    
    # This then lets the computer have a turn.   
    else:
        input("Press enter to continue.")
    
    
    
        print("\n Computer Attack")
        
        # This will attack the player and place markers on their board.
        comp_move = comp_attack(player, player_storage)
        
        # This will show the outcome.
        display_board(player)
        
        # This will check the players ships hit markers.
        sunk_ship = check_ship(player, player_ship_storage, comp_move[1], comp_move[2])

        try:
            if sunk_ship[0] == True:

                ship = ""

                if sunk_ship[1] == 5:
                    print("Aircraft Carrier has been sunk!")
                elif sunk_ship[1] == 4:
                    print("Battleship has been sunk!")
                elif sunk_ship[1] == 3:
                    print("Cruiser has been sunk!")
                elif sunk_ship[1] == 2:
                    print("Destroyer has been sunk!")
            
            
            
                player_ships = player_ships + 1

        except TypeError:
            pass
            

        # This will allow the computer to go again,
        # when a ship has been hit.
        while comp_move[3] == False:

            if player_ships == 5:
                break
            
            comp_move = comp_attack(player, player_storage)
            
            display_board(player)
            
            sunk_ship = check_ship(player, player_ship_storage, comp_move[1], comp_move[2])

            try:

                if sunk_ship[0] == True:

                    ship = ""

                    if sunk_ship[1] == 5:
                        print("Aircraft Carrier has been sunk!")
                    elif sunk_ship[1] == 4:
                        print("Battleship has been sunk!")
                    elif sunk_ship[1] == 3:
                        print("Cruiser has been sunk!")
                    elif sunk_ship[1] == 2:
                        print("Destroyer has been sunk!")
            
            
                    player_ships = player_ships + 1

            except TypeError:
                pass
        
        
        if player_ships == 5:
            break
        
        #display_board(player)
        input("Press enter to continue.")
         


# Once the loop has been exited this will check to see who won.
# Then print the following.
if comp_ships == 5:
    print("\nCongratulations YOU WON!!!!")

elif player_ships == 5:
    print("\nSorry YOU LOSE!!!!!")
    

print("\nTHANKS FOR PLAYING")
        
    
     
            
  

    
    
    
    
    