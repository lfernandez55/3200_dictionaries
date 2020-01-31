top_room = {}
middle_room = {}
bottom_room = {}

top_room = {'adjacent_rooms':[middle_room]}
middle_room = {'adjacent_rooms':[top_room,bottom_room]}
bottom_room = {'adjacent_rooms':[middle_room]}

rooms = {'top_room':top_room, 'middle_room': middle_room, 'bottom_room': bottom_room}

current_room = 'middle_room'
request = ""
print(rooms[current_room])

while request != 'quit':
    print("U r in the ", current_room)
    request = input("What room would u like to go to?")
    if rooms[request] in rooms[current_room]['adjacent_rooms']:
        current_room = request
    elif request == 'quit':
        break
    else:
        print("U can't get thar from here!!!!!")