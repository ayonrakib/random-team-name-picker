# team picker

# team names to captains names
# a list

# assigned team fixtures empty list
# iterate 4 times:
#   current group empty dict
#   random team index from the team names list
#   random captain index from the team names list
#   current group[team names[team index]] = captains[captains index]
#   remove the captain from captains and team from teams
#   return current group
from random import randint

teams = ["Austin Spikers",
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
]

captains = ["Mona","Rashed","Rupom","Abu Sohel","Zahedul","Moinul","Omar","Shajal","Munna","Nafis","Sami","Mashu","Rezwan","Shaheen", "Manar", "Polin"]
groupA = {}
rosters = []
# for count in range(0,4):
for number in range(0,4):
    randomCaptainIndex = randint(0, len(captains)-1)
    randomTeamIndex = randint(0, len(teams)-1)
    groupA[captains[randomCaptainIndex]] = teams[randomTeamIndex]
    captains.remove(captains[randomCaptainIndex])
    teams.remove(teams[randomTeamIndex])
# rosters.append(groups)
print(groupA)
# print(teams)
# print(captains)

groupB = {}

for number in range(0,4):
    randomCaptainIndex = randint(0, len(captains)-1)
    randomTeamIndex = randint(0, len(teams)-1)
    groupB[captains[randomCaptainIndex]] = teams[randomTeamIndex]
    captains.remove(captains[randomCaptainIndex])
    teams.remove(teams[randomTeamIndex])
# rosters.append(groups)
print(groupB)
# print(teams)
# print(captains)

groupC = {}

for number in range(0,4):
    randomCaptainIndex = randint(0, len(captains)-1)
    randomTeamIndex = randint(0, len(teams)-1)
    groupC[captains[randomCaptainIndex]] = teams[randomTeamIndex]
    captains.remove(captains[randomCaptainIndex])
    teams.remove(teams[randomTeamIndex])
# rosters.append(groups)
print(groupC)
# print(teams)
# print(captains)

groupD = {}

for number in range(0,4):
    randomCaptainIndex = randint(0, len(captains)-1)
    randomTeamIndex = randint(0, len(teams)-1)
    groupD[captains[randomCaptainIndex]] = teams[randomTeamIndex]
    captains.remove(captains[randomCaptainIndex])
    teams.remove(teams[randomTeamIndex])
# rosters.append(groups)
print(groupD)
# print(teams)
# print(captains)