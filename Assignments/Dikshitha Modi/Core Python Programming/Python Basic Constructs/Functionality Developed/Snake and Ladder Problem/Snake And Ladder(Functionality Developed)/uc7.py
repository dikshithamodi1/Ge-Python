player1_position=0
player2_position=0
dice_count=0
current_player=1

while True:
    dice=roll_dice()
    dice_count+=1
    
    if current_player==1:
        old=player1_position
        new,option=check_option(player_position,dice)
        player1_position=exact_position(old,new)

        print("Player 1 rolled:", dice,"|", option, "| Position:",player1_position)
        if player1_position==100:
            print("Player 1 won")
            break

        current_player=2

    else:
        old=player2_positio
        new,option=check_option(player_position,dice)
        player2_position=exact_position(old,new)

        if player2_position==100:
            print("Player 2 won")
            break
        current_player=1
print("Total dice rolls:",dice_count)
