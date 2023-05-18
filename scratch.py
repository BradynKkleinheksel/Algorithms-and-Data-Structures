
import random 

i = True 
bootupcall = False
while i is True:
    
    computerscore = 0
    playerscore = 0
    
    
    

    def playerpicksfun():
        rpsvalue = ('rock', 'paper', 'scissors')
        playerpick = input(f"Ok {name}, Rock Paper or Scissors: ")
        playerpicklower = playerpick.lower()
        if playerpicklower not in rpsvalue:
            print('Invalid try again')
            playerpicksfun(name)
        else:
            rpsgenerate(playerpicklower)
                                                                                                   
    
    def rpsgenerate(store):                                                                                     
       rps = random.randint(0, 2)    # 0 is rock, 1 paper, 2 is scissors
    
       if rps == 0:
           computerpick = 'rock'
       elif rps == 1:
           computerpick = 'paper' 
       elif rps == 2:
           computerpick = "scissors"

       truthtable(computerpick, store)
                                                                     

    def truthtable(computerpick1, playerpick1 ):
        global computerscore
        global playerscore

        print(f'Computer chose: {computerpick1} ')
    
        if computerpick1 == 'paper' and playerpick1 == 'rock':
            computerscore += 1
            resultandloop(computerscore, playerscore)
        elif playerpick1 == 'paper' and computerpick1 == 'rock':
            playerscore += 1
            resultandloop(computerscore, playerscore)
        elif computerpick1 == 'scissors' and playerpick1 == 'paper':
            computerscore += 1 
            resultandloop(computerscore, playerscore)
        elif playerpick1 == 'scissors' and computerpick1 == 'paper':
            playerscore += 1
            resultandloop(computerscore, playerscore)
        elif computerpick1 == 'rock' and playerpick1 == 'scissors':
            computerscore += 1
            resultandloop(computerscore, playerscore)
        elif playerpick1 == 'rock' and computerpick1 == 'scissors':
            playerscore += 1
            resultandloop(computerscore, playerscore)
        else:
            print('You Tied!')
            resultandloop(computerscore, playerscore)
        



    def resultandloop(computerscore, playerscore):
        global i
        yesno = ('yes', 'no')
        print(f'Your score is: {playerscore}')
        print(f'The computer score is: {computerscore}')
        loopask = input('Would you like to play again: Yes/No? ')
        loopasklower = loopask.lower()
        if loopasklower not in yesno:
            print('message was invalid') and resultandloop(computerscore, playerscore)
        elif loopasklower == 'no':
            print('Thanks for playing!')
            i = False
        elif loopasklower == 'yes': 
            playerpicksfun()

    
    def bootup():
        global name
        global i
        yesno = input('Would you like to play Rock Paper Scissors? Return Yes/No! ')
        yesnolower = yesno.lower()
        if yesnolower == 'no':
            i = False
        elif yesnolower == 'yes':
            name = input('What is your name? ')
            playerpicksfun()
        else: 
            print('Message was invalid, try again')

    if not bootupcall:
        bootup()
        bootupcall = True    

    
