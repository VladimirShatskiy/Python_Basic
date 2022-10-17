import random

team1 = [random.randint(500, 1000) / 100 for _ in range(20)]
team2 = [random.randint(500, 1000) / 100 for _ in range(20)]

team_win = [team1[x] if team1[x] > team2[x] else team2[x] for x in range(20)]

print(team1)
print(team2)
print(team_win)

