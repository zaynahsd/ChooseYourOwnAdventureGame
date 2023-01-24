def begin_game():
    input("Welcome to the Year 3000, a choose your own adventure game! Press enter to begin.")
    name = input("What is your name?  ")

    print("Welcome " + name + "!" + " The year is 3000 and a hologram appears before you. The hologram says: " + name + " which pill do you wish to take?")
    choice = input("Do you take the red pill or the blue pill (red/blue)")

    if choice == "red":
        print("You chose the red pill. Two paths appear before you.")
        choice = input("Do you take the left path or the right path (left/right)")

        if choice == 'left':
            print("A group of holograms begin to shoot at you. What do you do?")
            choice = input("Do you dodge the bullets or shoot back? (dodge/shoot)")

            if choice == 'dodge':
                print("You tried to dodge but were hit with a stray bullet. GAME OVER!")

            elif choice == 'shoot':
                print("You were able to eliminate all of the targets. MISSION SUCCESSFUL!")


        elif choice == 'right':
            print("A portal opens and a pack of robo dogs comes rushing out. Now what?")
            choice = input("Do you distract them or run? (distract/run)")

            if choice == 'distract':
                print("You were able to distract the dogs and get away. MISSION SUCCESSFUL!")

            elif choice == 'run':
                print("You tried to run but the robo dogs caught up with you and attacked. GAME OVER!")


    elif choice == "blue":
        print("You chose the blue pill. A set of stairs and an elevator appears before you.")
        choice = input("Do you take the stairs or the elevator (stairs/elevator)")

        if choice == 'stairs':
            print("A computer is at the top of the stairs and needs to be hacked to proceed.")
            choice = input("Do you hack the computer or destroy it? (hack/destroy)")

            if choice == 'hack':
                print("You were able to hack the computer and infiltrate the room. MISSION SUCCESSFUL!")

            elif choice == 'destroy':
                print("Destroying the computer set off alarms and you were eliminated. GAME OVER!")


        elif choice == 'elevator':
            print("You reach the top floor and get off the elevator. You are met with a cyber army. Now what?")
            choice = input("Do you sneak around them or fight back? (sneak/fight)")

            if choice == 'fight':
                print("You were able to fight them all. MISSION SUCCESSFUL!")

            elif choice == 'sneak':
                print("You tried to sneak but a cyber soldier caught you and eliminated you. GAME OVER!")

begin_game()
