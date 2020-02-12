# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, move):
        self.name = name
        self.current_room = current_room
        self.move = move

    def __str__(self):
        output = ""
        output += self.name + "\n"
        output += self.current_room + "\n"
        for m in self.move:
            output += f"{m}\n"

        output += f"Exit"

        return output


j = Player("Jobsy", "Room 1", ["n", "e", "s", "w"])

print(j)
