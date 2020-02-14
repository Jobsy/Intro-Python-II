# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:

    def __init__(self, name, current_room, move):
        self.name = name
        self.current_room = current_room
        self.move = move
        # print(self.current_room)

    def __str__(self):
        output = ""
        output += self.name + "\n"
        output += self.current_room.description + ">>>" + "\n"

        return output
