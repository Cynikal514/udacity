def gameMode(level):
    # Input: Level chosen by user input
    # Output: list containing string and a list of the answers.
    # Description: Determine game level and return appropriate starting text and answers in list form.
    if level =="easy":
        game_text_start = ['''The Open Systems Interconnect (OSI) model has 7 layers.  They are ___1___ - Layer 7; ___2___ - Layer 6; __3___ - Layer 5; ___4___ - Layer 4; ___5___ - Layer 3; ___6___ - Layer 2; ___7___ - Layer 1.
        ''', ["Application", "Presentation", "Session", "Transport", "Network", "Data", "Physical"]]
    elif level == "medium":
        game_text_start = ['''While there has been a lot of crossover between device functionality, the two main networking devices are ___1___ and ___2___. Routers are typically used
        as the ___3___ device between networks, allowing routing decisions to be made and forwarding traffic as needed. Switches hubs provide higher port density than the typical router
        provides, however this brings along its own problems. Hubs put all ports on it in what's known as a ___4___ domain, where each device has to take turns talking on the network or their
        traffic will overlap. Switches don't have this problem, as they only have a ___5___ domain, which means each device can communicate bi-directionally at the same time but are only allowed
        to send broadcast traffic to devices connected to the same switch as them.''', ["routers", "switches", "gateway", "collision", "broadcast"]]
    elif level == "hard":
        game_text_start = ['''BGP is an ___1___ gateway protocol, meant to be used between different networks. It is the protocol used between Internet service providers (ISPs) and also can be used between an ___2___ and an ISP. BGP was built for ___3___, ___4___, and ___5___, not speed. Because of this, it behaves differently from the protocols like ___6___,___7___, and ___8___
        ''', ["external", "Enterprise", "reliability", "scalability", "control", "RIP", "OSPF", "EIGRP"]]
    else:
        return "Please choose an appropriate level to continue"

    return game_text_start


def wordReplace(text_input,guess):
    # Input: string that was determined based on difficult chosen.
    # Output: print statements to the screen as the user interacts with the game.
    # Description: Function that takes in a string, finds a blank and asks the user for an answer.
    # If the provided answer is correct, the function replaces the indexed list item with answer.
    # If answer is wrong, the function will increment the guess counter and prompt again for same question.
    game_text = text_input[0].split( )
    answers = text_input[1]
    index, answer_index = 0, 0
    guess = int(guess)
    while (index < len(game_text)) and ( 0 < guess):
        word = game_text[index]
        if "___" in word:
            print textJoin(game_text,guess)
            var_answer = raw_input("What goes in spot "+word+"? ")
            if var_answer == answers[answer_index]:
                game_text[index] = var_answer
                index += 1
                answer_index += 1
            else:
                guess -= 1
        else:
            index += 1


def textJoin(input,guess):
    # Input: Current list that needs to be joined and the num. of guesses used so far.
    # Output: Returns joined list as a string and number of guesses remaining.
    # Description: Joins given list into a string using a space between list elements and appends num of guesses left.
    input = " ".join(input)
    input += "\nGuesses left: " + str(guess)
    return input


def gameStart():
    # Input: User input only
    # Output: Calls other functions with either user input value or a list
    # Description: Function that is initially called when the program starts.
    # Asks user to select a difficulty and hands that off to another function.
    # Once other function returns with appropriate list based on level chosen, passes that list
    # to another function to start the find/replace.
    # Bonus: Asks for number of guesses the user would like to attempt
    game_level = ""
    while game_level not in ('easy', 'medium', 'hard'):
        game_level = raw_input("Please select game difficulty - easy / medium / hard: ")
        game_text = gameMode(game_level)
        num_guess = raw_input("How many guesses would you like(1-10)? ")
        min_guess = 0
        max_guess = 11
        while not num_guess < max_guess and not min_guess < num_guess:
            num_guess = raw_input("Sorry, number entered not in range. Please try again.\nHow many guesses would you like(1-10)? ")
        wordReplace(game_text,num_guess)


gameStart()
