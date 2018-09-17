def BasketBall():
    stats=open("bball.txt","a")
    NewStats=input("Would you like to enter new stats? ")
    yess=["YES", "yes","Yes","y","Y"]
    nos=["No", "NO","no","n","N"]
    if NewStats in yess:
        n=int(input("How many players stats do you want to enter? "))
        for i in range(n):
            bball=open("bball.txt", "a")
            date=input("DATE: ")#ex. 02-01-2017 is Feb 1st, 2017
            #numb=(input("NUMBER: "))
            name=input("PLAYER: ")
            team=input("TEAM: ")
            #Games Stats
            minut=(input("Minutes: ")) #Minutes played
            fgm=int(input("FGM: "))
            fga=int(input("FGA: "))
            threefgm=int(input("3FGM: "))#3 ponters made
            threefg=int(input("3FGA: ")) #3 pointers attempted
            twofg=fga-threefg
            twofgm=fgm-threefgm
            freetm=int(input("FTM: ")) #Free throws made
            freet=(input("FTA: ")) #Free throws attempted
            points=((twofgm*2)+(threefgm*3)+freetm) #total points
            oreb=int(input("OREB: "))
            dreb=int(input("DREB: "))
            reb=oreb+dreb
            ast=(input("AST: "))
            tov=(input("TOV: "))
            stl=(input("STL: "))
            blk=(input("BLK: "))
            pf=(input("PF: "))
            stats.write(date + ","+ name + "," + team + ","+ minut + "," 
                             +str(fgm)+ "," +str(fga)+ "," +str(threefgm)+ ","+ str(threefg)+","+str(freetm)+","+freet+","+str(points)
                             +","+ str(oreb)+","+str(dreb)+","+str(reb)+","+ast+","+tov+","+stl+","+blk+","+ pf+"\n")
            bball.close()
    while NewStats in nos:
            stats=open("bball.txt","r")
            a=stats.read().split("\n")
            date=input("What days games do you want to see? ")
            player=input("Who's stats do you want to see? ")
            for line in a:
                b=line.split(",")
                if date == b[0] and player ==b[1]:
                    print("General Information:"+"\n"+"Player name: ",b[1],",","Team: ",b[2],"\n",
                    "Game Stats:","\n","Minutes Played: ",b[3],",","FGM: ",b[4],",","FGA: ",b[5],",","3FGM: ",b[6],",","3FGA: ",b[7],",","FTM: ",b[8],",","FTA: ",b[9],",","Total Points: ",b[10],
                    "\n","Offensive Rebounds: ",b[11],",","Defensive Rebounds: ",b[12],",","Total Rebounds: ",b[13],",","Assists: ",b[14],",","Turnovers: ",b[15],",","Steals: ", b[16],",","Blocks: ",b[17],",","PF: ",b[18])

BasketBall()



