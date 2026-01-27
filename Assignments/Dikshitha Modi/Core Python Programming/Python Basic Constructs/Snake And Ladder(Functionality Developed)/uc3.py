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
