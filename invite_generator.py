class InviteGenerator:
    def __init__(self):
        self.names_to_add = []

    def accessing_names(self):
        names = open("invited_names.txt").readlines()  # accessing all lines from the .txt file
        for _ in range(len(names)):
            self.names_to_add.append(names[_].strip()) # strip nextline "\n"

    def adding_names_to_letter(self):
        text_to_replace = "[name]"

        # Accessing template letter:
        template = open("starting_letter.txt").read()

        # Creating new letters with names from names_to_add:
        for _ in range(len(self.names_to_add)):
            open(f"./ReadyToSend/Letter_{self.names_to_add[_]}.txt", "w").write(template.replace(text_to_replace, self.names_to_add[_]))
