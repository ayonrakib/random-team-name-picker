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

rosters = []
for number in range(0,4):
    currentGroup= {}
    for count in range(0,4):
        randomCaptainIndex = randint(0, len(captains)-1)
        randomTeamIndex = randint(0, len(teams)-1)
        currentGroup[captains[randomCaptainIndex]] = teams[randomTeamIndex]
        captains.remove(captains[randomCaptainIndex])
        teams.remove(teams[randomTeamIndex])
    rosters.append(currentGroup)
print(rosters)