player_position=0
while player_position<100:
    dice=roll_dice()
    player_position,option=check_option(player_position,dice)
