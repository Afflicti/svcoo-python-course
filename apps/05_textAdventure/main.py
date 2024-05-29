rooms = {
    'FOREST': {
        'description': "You are standing in a dark forest. A path leads north and a faint light flickers to the east.",
        'exits': ['NORTH', 'EAST']
    },
    'NORTH': {
        'description': "You reach a clearing. A rickety bridge spans a rushing river to the west.",
        'exits': ['WEST']
    },
    'EAST': {
        'description': "You stumble upon a hidden cave. A single, glowing mushroom illuminates the entrance.",
        'exits': ['SOUTH']
    },
    'SOUTH': {
        'description': "You stumble upon a hidden cave. A single, glowing mushroom illuminates the entrance.",
        'exits': ['UP']
    },
    'WEST': {
        'description': "You cross the bridge and find yourself at the foot of a towering mountain. A narrow path winds upwards.",
        'exits': ['UP']
    },
    'UP': {
        'description': "You reach the mountain peak. A magnificent castle stands before you. The drawbridge is lowered.",
        'exits': ['ENTER']
    },
    'ENTER': {
        'description': "You enter the castle and find yourself in a grand hall. A wise old wizard sits upon a throne.",
        'end': True
    }
}

current_room = 'FOREST'

while True:
  print(rooms[current_room]['description'])
  if 'end' in rooms[current_room]:
    print("You have reached the end of your adventure!")
    break

  exits = rooms[current_room]['exits']
  direction = input("Which direction do you want to go? ").upper()

  if direction in exits:
    current_room = direction
  else:
    print("You can't go that way.")

