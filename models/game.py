class Game:
    def play_rps(p1_choice, p2_choice):
        if p1_choice == "rock":
            if p2_choice == "rock":
                return 2
            if p2_choice == "paper":
                return 0
            if p2_choice == "scissors":
                return 1
        if p1_choice == "paper":
            if p2_choice == "rock":
                return 1
            if p2_choice == "paper":
                return 2
            if p2_choice == "scissors":
                return 0
        if p1_choice == "scissors":
            if p2_choice == "rock":
                return 0
            if p2_choice == "paper":
                return 1
            if p2_choice == "scissors":
                return 2
