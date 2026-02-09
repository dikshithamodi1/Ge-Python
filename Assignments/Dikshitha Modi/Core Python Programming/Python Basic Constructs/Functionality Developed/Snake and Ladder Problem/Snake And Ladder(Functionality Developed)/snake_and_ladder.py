import random

#UC1
player1_position=0
player2_position=0

#UC6
dice_count=0

#UC2
def roll_dice():
    return random.randint(1,6)

#UC3
def check_option(position,dice):
    option=random.choice(["No Play","Ladder","Snake"])
    if option=="Ladder":
        position+=dice
    elif option=="Snake":
        position-=dice
    elif option=="No Play":
        pass

    if position<0:
        position=0

    return position,option


#UC5
def exact_position(old_position,new_position):
    if new_position>100:
        return old_position
    return new_position

#UC7
current_player=1

while True:
    dice=roll_dice()
    dice_count+=1
    
    if current_player==1:
        old_position=player1_position
        new_position,option=check_option(player1_position,dice)
        player1_position=exact_position(old_position,new_position)

        print("Player 1 rolled:", dice,"|", option, "| Position:",player1_position)
        if player1_position==100:
            print("Player 1 won")
            break

        current_player=2

    else:
        old_position=player2_position
        new_position,option=check_option(player2_position,dice)
        player2_position=exact_position(old_position,new_position)

        print("Player 2 rolled:", dice,"|", option, "| Position:",player2_position)
        if player2_position==100:
            print("Player 2 won")
            break
        current_player=1
print("Total dice rolls:",dice_count)
