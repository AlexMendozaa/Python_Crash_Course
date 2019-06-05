Nomad = {'type':'rover','color':'black','processor':'Jetson TX1'}
print(Nomad['type'])
BARB = {'type':'test-bed','color':'black','type':'wheeled'}
print(BARB)
myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
print(myRobots)
myRobots['Llamabot'] = 'Getting to it'
print(myRobots)
del myRobots['Llamabot']
print(myRobots)
workingRobots = myRobots.copy()
print(workingRobots)
otherRobots = {'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}
myRobots.update(otherRobots)
print(myRobots)
input()
