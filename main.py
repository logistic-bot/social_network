class User:
    def __init__(self, username):
        self.username = username

    def ask_yes_no(self):
        got_response = False
        while not got_response:
            response = input("[y/n]: ").strip().lower()
            if response[0] in ('y', 'n'):
                got_response = True
            else:
                got_response = False
                print("Please answer yes or no.")

        if response[0] == 'y':
            return True
        else:
            return False

    def login(self, password):
        """
        Logs in the user using the given password.
        Loads the password from a file.
        """
        try:
            filename = "./data/" + self.username + ".password"
            with open(filename, "r") as passwordfile:
                if password == passwordfile.read():
                    return True
                else:
                    raise Exception("Invalid password for user {}".format(self.username))
        except FileNotFoundError:
            print("User {} does not exist. Create new user?".format(self.username))
            response = self.ask_yes_no()

            if response: # create new user
                with open("./data/" + self.username + ".password", "w") as passwordfile:
                    passwordfile.write(password)
            else:
                exit()


def main():
    username = input("Username: ")
    password = input("Password: ")
    u = User(username)
    u.login(password)

    while True:
        action = input(" > ")

        if action == "rg": # read global
            with open("./messages/global.txt", "r") as messages:
                print(messages.read())

        elif action == "pg": # post global
            with open("./messages/global.txt", "a") as messages:
                messages.write("<" + u.username + "> " + input("$> ") + "\n")


if __name__ == "__main__":
    main()
