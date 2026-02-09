player_position=0
dice_count=0
while player_position<100:
    dice=roll_dice()
    dice_count+=1

    old_pos=player_position
    new_pos,option=check_option(player_position,dice)
    player_position=exact_position(old_pos,new_pos)

    print("Dice:",dice, "| Option: ",option, "| Position: ",player_position)

print("Total Dice Rolls:",dice_count)
