from __future__ import division
import random

def montyHall(toSwitch):
  doors = [0, 0, 1]
  random.shuffle(doors)
  firstDoorIndex = random.randint(0, 2)
  behindFirstDoor = doors[firstDoorIndex]
  del doors[firstDoorIndex]

  if doors[0] == 0:
    del doors[0]
  elif doors[1] == 0:
    del doors[1]

  if toSwitch:
    return doors[0]
  else:
    return behindFirstDoor

def simulate(toSwitch):
  wins = 0
  for i in range(0, 100000):
    result = montyHall(toSwitch)
    if result == 1:
      wins = wins + 1
  return wins


numStay = simulate(False)
numSwitch = simulate(True)

stayPercentage = (numStay / 100000) * 100
print 'Stay with first door: ' + str(stayPercentage) + '%'
switchPercentage = (numSwitch / 100000) * 100
print 'Switch to other door: ' + str(switchPercentage) + '%'
