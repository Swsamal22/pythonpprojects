import random

class Cricket:
    def __init__(self,over,Wicket):
        self.over=over #declaring how many over of match to be played
        self.Wicket=Wicket
        
    def Game(self):
        """
        This function is to start the game
        No parameters is required as the initital parameters passed in the class will act as the parameter for this function
        This returns the total runs for a player
        """
        Total_runs=0
        for i in range(int(self.over)):
            print(f"Over number is: {i} ")
            Total_runs += self.Over()
            if self.Wicket==0:
                print("ALL OUT!")
                break
            print(f"Total runs is {Total_runs}, remaining wickets is {self.Wicket}")
            print("\n")
        return Total_runs
       
    def Over(self):
        """
        This is for an activity within an over
        Returns:
            [int]: [returns the total runs scored in an over]
        """
        runs,balls=0,0
        Category=[1,2,3,4,6,'Wide','No Ball','Wicket']
        while balls<=6:
            x=random.choice(Category)
            if x in [1,2,3,4,6]:
                runs += x
                print(f"ball number {balls} run is {x}")
                balls += 1
            elif x in ['Wide','No Ball']:
                runs += 1
                print(f"ball number {balls} run is {x}, Extra!")
            else:
                print(f"ball number {balls},  {x}")
                self.Wicket -= 1
                balls += 1
                if self.Wicket==0:
                    break
        return runs

        
if __name__ == "__main__":
    """
    main function where we would ask user for the inputs
    """
    overs=input("How many overs of play do you want?\n")
    Yes = input("Do you want the play to be started? 1. Y for yes 2. N for No?\n")
    Wicket=int(input("Enter the number of wickets for each player\n"))
    player_scorecard={}
    #start of the play and one player sets the target for the other player
    if Yes.lower() == 'y':
        #It's toss time
        Player = int(input("Enter how many players wants to play?\n"))
        
        #call the start function for the play to start for a player
        for i in range(Player):
            Player_name = input("Enter the name of the Player\n")
            print(f"It's turn for {Player_name}\n")
            cricket = Cricket(overs,Wicket)
            Team_Score=cricket.Game()
            print(f"{Player_name} has scored {Team_Score} runs\n")
            player_scorecard[Player_name] = Team_Score
        
        print("Player Scorecard:%s \n" %player_scorecard)
        
        #showing the winner of the game
        Winner = max(player_scorecard, key=player_scorecard.get)
        print(f"The winner of the Game is: {Winner}\n")
    else:
        print("Game not started!\n")