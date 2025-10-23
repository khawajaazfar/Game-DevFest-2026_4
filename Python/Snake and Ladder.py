import random
from PIL import Image  #importing Image from PIL
end=50
def show_board():    #function to display the image of board
     img = Image.open(r"C:\Users\diyaa\Downloads\snakes.jpg")
     img.show()
def check_ladder(points):  #if the position has ladder
     if(points==5):
         print("LADDER :)")
         return 46
     elif(points==11):
         print("LADDER :)")
         return 66
     elif(points==19):
         print("LADDER :)")
         return 43
     elif(points==24):
         print("LADDER :)")
         return 94
     elif(points==31):
         print("LADDER :)")
         return 73
     elif(points==58):
         print("LADDER :)")
         return 82
     else:
         #if the position has no ladder
         return points
def check_snakes(points):  #checks if the position has snakes
     if(points==34):
         print("SNAKE :(")
         return 7
     elif(points==47):
         print("SNAKE :(")
         return 4
     elif(points==65):
         print("SNAKE :(")
         return 3
     elif(points==87):
         print("SNAKE :(")
         return 22
     elif(points==92):
         print("SNAKE :(")
         return 70
     elif(points==97):
         print("SNAKE :(")
         return 56
     elif(points==99):
         print("SNAKE :(")
         return 40
     else:
         #no change
         return points
def reached_end(points): #checks if the player has reached the end points
     if(points==50):
         return True
     else:
         return False
def play():   #main function
     player1=input("enter the name of the player 1\n")
     player2=input("enter the name of the player 2\n")
     pp1=0
     pp2=0
     turn=0
     while(1): #infinite loop to make the game keep going
         if(turn%2==0):
             print(player1,",your turn")
             c=input("ENTER 1 TO CONTINUE ,0 TO QUIT\n")
             if(c=='0'): #if the player wants to exit
                 print("THE END!!!")
                 print(player1,"You scored:",pp1)
                 print(player2,"You scored:",pp2)
                 print("THANKS FOR PLAYING :)")
                 break
             dice=random.randint(1,6)  #randomly picks one integer from 1-6
             print("THE DICE SHOWED:",dice)
             show_board()
             pp1=pp1+dice
             pp1=check_ladder(pp1)
             pp1=check_snakes(pp1)
             if(pp1>end):
                pp1=100
             print(player1,",YOUR SCORE IS:",pp1)
             if reached_end(pp1):
                print(player1,",YOU WON!!!")
                break
             turn=turn+1   #incrementing the turn value
         else: #for player 2
             print(player2,"your turn")
             c=input("ENTER 1 TO CONTINUE ,0 TO QUIT\n")
             if(c==0): #if the player wants to exit or continue
                 print("THE END!!!")
                 print(player1,",You scored:",pp1)
                 print(player2,",You scored:",pp2)
                 print("THANKS FOR PLAYING :)")
                 break
             dice=random.randint(1,6)  #randomly picks one integer from 1-6
             print("THE DICE SHOWED:",dice)
             show_board()
             pp2=pp2+dice
             pp2=check_ladder(pp2)
             pp2=check_snakes(pp2)
             if(pp2> end): #if points exceeds hundred(max points),the player is given hundred points
                 pp2=100
             print(player2,"YOUR SCORE IS:",pp2)
             if reached_end(pp2):
                 print(player2,"YOU WON!!!")
                 break
             turn=turn+1 #incrementing the turn value
show_board()
play()