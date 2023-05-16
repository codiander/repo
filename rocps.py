#rock, paper and scissors
def rps():
    import random
    comp=["R","P","S"]
    i=0
    compscore=0
    userscore=0
    while i<3:
        print("1.click R for rock")
        print("2.click P for paper")
        print("3.click S for scissors\n")
        compchoice=random.choice(comp)

        userinp=input("KINDLY ENTER YOUR CHOICE:")
        #when both have the same choice
        print("computer chose",compchoice,"against your choice,",userinp)


        if userinp==compchoice:
            pass
            i+=1
        #if both do not have the same choice
        elif userinp!=compchoice:
            #if computer chooses R
            if compchoice=="R":
                if userinp=="P":
                    userscore+=1
                    i+=1
                if userinp=="S":
                    compscore+=1
                    i+=1
            #if computer chooses P
            elif compchoice=="P":
                if userinp=="S":
                    userscore+=1
                    i+=1
                if userinp=="R":
                    compscore+=1
                    i+=1
            #if computer chooses S
            elif compchoice=="S":
                if userinp=="R":
                    userscore+=1
                    i+=1
                if userinp=="P":
                    compscore+=1
                    i+=1

    winningremarks=["YOU WON AGAINST A ROBOT THAT IS TRASH = YOU ARE TRASH TOO!","NOICE!","SMOOTH LIKE BUTTER!"]
    losingremarks=["L STANDS FOR LOSER LIKE YOU!","WAAH, KYA SCENE HAI","NEVER COME BACK NOOBDE, SHHE NOOB YOUR TRASH ON EARTH!"]
    drawremarks=["I WANT SOMETHING JUST LIKE THIS!","WHEN BOTH COPIED THE SAME PAPER THIS HAPPENS!","THE TIE PROTECTS BOTH THE SHIRTS FROM STAINING!"]
    

    if compscore>userscore:
        print(random.choice(losingremarks))
    if compscore<userscore:
        print(random.choice(winningremarks))
    if compscore==userscore:
        print(random.choice(drawremarks))

rps()
                    

                    


                    
                    
                    
                    
            
            
             
                
