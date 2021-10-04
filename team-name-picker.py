# random team name picker
# input: team names, captains
# return: dict of captains as keys and team names as values
# method:
#   1. team names of captains and team names
#   2. jotokkhon na argument length 0 hocche:
#       2.1. recursive call of same method with both params and dict and assign it to team name generator var
#   3. return  team name generator var
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
    # print(randint(1,10))
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
print(getCaptainsTeamNames(["Ayon","Rashed","Rupom"],["A","B","C"]))