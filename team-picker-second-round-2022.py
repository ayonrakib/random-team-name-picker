from random import randint

teams = ["X1",
        "X2",
        "X3",
        "X4",
        "Y1",
        "Y2",
        "Y3",
        "Y4"
]

captains = ["Sami","Shajal","Polin","Rupom","Zahedul","Moinul","Omar","Mashu"]
assignedTeams = {}

for number in range(8):
    randomTeamIndex = randint(0, len(teams)-1)
    randomCaptainIndex = randint(0, len(captains)-1)
    assignedTeams[teams[randomTeamIndex]] = captains[randomCaptainIndex]
    teams.remove(teams[randomTeamIndex])
    captains.remove(captains[randomCaptainIndex])
print(assignedTeams)