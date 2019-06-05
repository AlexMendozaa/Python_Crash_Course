robots = ["nomad","Ponginator","Alfred"]

print(robots)
print(robots[0])
print(robots[-1])
print(robots[1:3])

more_bots = robots +['Roomba','Neato','InMoov']
print(more_bots)
more_bots[3] = 'ASIMO'
print(more_bots)
more_bots[3:5] = []
print(more_bots)
a,b = more_bots[0:2]
print(a)
print(b)
print(robots[0].title())
input()
