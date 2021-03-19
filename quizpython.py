
import datetime
import os                                 # sysytem() function
import random                      # random() function to generate questions in random order
from time import sleep         # time() function


print("------------LET'S PLAY THE QUIZ------------")
print("____________________________________________________________")
print("____________________________________________________________")
print("............CHECK YOUR KNOWLEDGE HERE....!!!!............")
print( )
print( )
print("...............HELP MENU..................")                 # instructions for quiz game
print("This is a Quiz Game, it contains 10 Questions")
print("There will be 4 options, You have to choose  only Correct option")
print("For Each correct answer, you will be awarded with 1 Point")
print("You can't see the Previous question, 1 Questuon will be dispalyed at a time ")
print("You have to play all the 10 Questions, you can't Skip any of them")
print("____________________________________________________________")

print(".............. BEST OF LUCK..............")
print( )
print( )

print("--------------------------------------------------------------------------------------------------------------")
choice=str(input("Press S to Start/ Q to quit the Game :"))
if choice.upper()=="S":
    name=str(input("Register your name:"))       #name of the player
    print(name)
elif choice.upper()=="Q":
    sleep(1)                                                                # game will be ended within 1 second
    quit()

    



os.system('cls')                                                #it will clear the screen



print("-----------------------------------------------------------------------------------")
dn=datetime.datetime.now()
print("Game Starts at:",dn.strftime("%c"))                          #TIME when Game Begins

print("Q1) Which of these is a palindrome number?")

s={1:'1234',2:'2341',3:'12321',4:'5434'}  #options

k="Correct.......!"


for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():

    a=int(input("Option:"))
    
    if a==3:
        print(k)
        
        
    elif a<1 or a>4:                    # it restricts the option boundary
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print( "Your Option  is Incorrect")

if a==3:
    print(k)
    
elif a<1 or a>4:
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")


sleep(1.0)                   #next question will appear after 1.0 second 
os.system('cls')
print("-----------------------------------------------------------------------------------")


print("Q2) Which aniaml laughs like Human being?")

s={1:'Deer',2:'Heyna',3:'Tiger',4:'Monkey'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def use_input():
    a=int(input("Option:"))
    if a==2:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        use_input()
    else:
        print(" Your Option  is Incorrect")

if a==2:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    use_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")


print("Q3) How many times a piece of a paper can be folded at most?")

s={1:'3',2:'5',3:'7',4:'Depends on the size of the Papers'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))
def u_i():
    a=int(input("Option:"))
    if a==3:
        print(k)
    
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        u_i()
    else:
        print("  Your Option  is Incorrect")

if a==3:
    print(k)
    
elif a<1 or a>4:
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print("Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")

print("Q4) What is the Capital city of karnataka?")

s={1:'Mysore',2:'Bengaluru',3:'Mangalore',4:'Vijaynagar'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==2:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==2:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")

print("Q5) In which city 'WANKHADE STADIUM' is located?")

s={1:'Mumbai',2:'Delhi',3:'Chennai',4:'Hyderabad'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==1:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==1:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")

print("Q6) What is the square of 49?")

s={1:'2201',2:'2011',3:'2421',4:'2401'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==4:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==4:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")
print("Q7) If A+B=7& A-B=3, then AxB=?")

s={1:'9',2:'6',3:'10',4:'14'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==3:
        print(k)
    
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==3:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')
print("-----------------------------------------------------------------------------------")
print("Q8) Who is the All Time Top Scorer in International ODI Cricket ?")

s={1:'Ricky Ponting',2:'Sachin Tendulkar',3:'Kumar Sangakkara',4:'Brian Lara'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==2:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==2:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')

print("-----------------------------------------------------------------------------------")
print("Q9) How many states in India have  Ocean Boundaries ?")

s={1:'9',2:'10',3:'7',4:'6'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==1:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==1:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")

sleep(1.0)
os.system('cls')

print("-----------------------------------------------------------------------------------")
print("Q10) The Crossbreed of Male Lion & Female Tiger  is called .............?")

s={1:'Jaguar',2:'Tigon',3:'Cheetah',4:'Liger'}

k="Correct.......!"

for i in s:
    print(i,":",s.get(i))
    
a=int(input("Option:"))

def user_input():
    a=int(input("Option:"))
    if a==4:
        print(k)
        
    elif a<1 or a>4:
        print("Invalid Choice!! Please enter between 1 and 4.")
        user_input()
    else:
        print(" Your Option  is Incorrect")

if a==4:
    print(k)
    
elif a<1 or a>4 :
    print("Invalid Choice!! Please Re-enter between 1 and 4.")
    user_input()
else:
    print(" Your Option  is Incorrect")
   
    



sleep(2.0)
os.system('cls')


score=str(input("The no. of Correct answers are :"))
outof="/ 10"
print("Your Score is ",score,outof)

print("-----------------------------------------------------------------------------------")

print(" ANSWER KEY")   # answers to all the above questions
st={1:'Q1-12321',2:'Q2-Heyna',3:'Q3-7',4:'Q4-Bengaluru',5:'Q5-Mumbai',6:'Q6-2401',7:'Q7-10',8:'Q8-Sachin Tendulkar',9:'Q9-9',10:'Q10-Liger'}
st.get(i)

for i in st:
    print(st.get(i))

    

sleep(5)
os.system('cls')
print("-----------------------------------------------------------------------------------")

x=datetime.datetime.now()
print(name.upper(),",you have succesfully started playing at",dn.strftime("%X"),"hrs"," & finished the game at",x.strftime("%X"),"hrs")    # Ending time of the Game also displayed here
sleep(5)           #after 5 seconds, screen will be cleared


os.system('cls')

print(".................................................")
print("...PLAYER DETAILS...")          # Database of the Player
print("|","NAME        :",name.upper())
print("|","SCORE      :",score,outof)
print("|","END-TIME :",x.strftime("%c"))
      

sleep(6)
exp=str(input("How is your experience ?"))
print(exp)
os.system('cls')
    

        

sleep(2)













