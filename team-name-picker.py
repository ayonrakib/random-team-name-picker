# random team name picker
# input: team names, captains
# return: dict of captains as keys and team names as values
# method:
#   1. jotokkhon na 1st argument er length 0 theke bor hoy:
#       2. get random captain name from captains list
#       3. get random team name from teams list
#       4. assign team name to captain as dict
#       5. captain name list theke captain name remove
#       6. team name list theke team name remove
#       7. recursive call of same method with the captains names and team names
#   8. return  team name generator var
from random import randint
captainsToTeamNames = {}
def getCaptainsTeamNames(*args):
    while(len(args[0])>0):
        randomCaptainName = getRandomCaptainName(args[0])
        randomTeamName = getRandomTeamName(args[1])
        captainsToTeamNames[randomCaptainName] = randomTeamName
        args[0].remove(randomCaptainName)
        args[1].remove(randomTeamName)
        getCaptainsTeamNames(args[0],args[1])
    return captainsToTeamNames

# method: pick captain name randomly
# input: team names
# return: name of team captain as string
# method:
#   1. randomly captain name pick korbo
#   2. return captains name

def getRandomCaptainName(captainNames):
    # print(randint(1,10))
    randomCaptainName = captainNames[randint(0,len(captainNames)-1)]
    return randomCaptainName

# method: pick team name randomly
# input: team names and captain names and dict of team captains and names
# return: dict of team captains as keys and names as values and new names and captains
# method:
#   1. randomly captain name pick korbo
#   2. return captains name
def getRandomTeamName(teamNames):
    while(len(teamNames)>0):
        randomTeamName = teamNames[randint(0,len(teamNames)-1)]
        return randomTeamName
        

# method: assign team name to dict
# input: team name, captain name and dict
# return: dict
# method:
#   1. dict[captain name] = team anme
#   2. return dict
def assignTeamNameToCaptain(captainName, teamName, captainToTeamName):
    captainToTeamName[captainName] = teamName
    return captainToTeamName


# print(getRandomCaptainName(["Ayon","Rashed","Rupom"]))
# print(getRandomTeamName(["A","B","C"]))
# print(assignTeamNameToCaptain("Ayon","A",{}))
print(getCaptainsTeamNames(["Mona","Rashed","Rupom","Abu Sohel","Zahedul","Moinul","Omar","Shajal","Munna","Nafis","Sami","Mashu","Rezwan","Shaheen", "Manar", "Polin"],
["Austin Spikers",
"Austin Crushers",
"Austin Hitters",
"Austin Blockers",
"Austin Tornadoes",
"Austin Twisters",
"Austin Typhoons",
"Austin Blasters",
"Austin Dynamites",
"Austin Challengers",
"Austin Raiders",
"Austin Jaguars",
"Austin Eagles",
"Austin Falcons",
"Austin Wildcats",
"Austin Hawks"
]))