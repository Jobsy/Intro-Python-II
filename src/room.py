# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description,
                 n_to=None,
                 s_to=None,
                 e_to=None,
                 w_to=None
                 ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        output = ""
        output += self.name + "\n"
        output += self.description + "\n"
        # output += str(self.n_to)
        # output += str(self.s_to)
        # output += str(self.e_to)
        # output += str(self.w_to)
        # output += f"{self.n_to if self.n_to else ' '}" + "\n"
        # output += f"{self.s_to if self.s_to else ' '}" + "\n"
        # output += f"{self.e_to if self.e_to else ' '}" + "\n"
        # output += f"{self.w_to if self.w_to else ' '}" + "\n"

        # for r in roo

        return output
