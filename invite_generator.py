class InviteGenerator:
    def __init__(self):
        self.invitee_names = []

    def accessing_names(self):
        names = open("invited_names.txt").readlines()  # accessing all lines from the .txt file
        for _ in range(len(names)):
            self.invitee_names.append(names[_].strip()) # strip nextline "\n"

    def generating_invites(self):
        text_to_replace = "[name]"

        # Accessing template letter:
        template = open("starting_letter.txt").read()

        # Creating new letters with names from names_to_add:
        for _ in range(len(self.invitee_names)):
            open(f"./ReadyToSend/Invite_for_{self.invitee_names[_]}.txt", "w").write(template.replace(text_to_replace, self.invitee_names[_]))
