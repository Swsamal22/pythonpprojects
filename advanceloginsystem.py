import resetpassword
import time

username="Swapnadeep"
password="doggo369"
turn=3

while turn > 0:
    user_name=input("Enter Username: ")
    pass_word=input("Enter the password: " + "If you forget password and want to reset it enter 0: ")
    
    if pass_word != '0':
        if (user_name!=username and pass_word != password):
            print("Wrong username and password ")
            turn -= 1
            print("you have", turn ,"attempts left")
            
        elif(user_name == username and pass_word != password):
            print("Wrong Password ")
            turn -= 1
            print("you have", turn ,"attempts left")
            
        elif(user_name != username and pass_word == password):
            print("Wrong Username ")
            turn -= 1
            print("you have", turn ,"attempts left")
            
        else:
            print(" Access Granted ")
            time.sleep(10)
            print("...........loading.......Please wait!.......")
            time.sleep(10)
            print("Transfering to the main page ")
            break
                 
    else:
        x=resetpassword.resetpassword()
        password=x
        print("Your password has been updated")
        print(f"Your User name is {username} and password is {password}")
        break
    
