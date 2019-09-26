from os import listdir


class User:
    def __init__(self, username):
        self.username = username
        self.subscribed_to = []

    def subscribe(self, username):
        """
        subscribes self to username, allowing self to recive notifications about username's posts
        """
        if username in self.subscribed_to:
            print("You are already subscribed to this person")
        else:
            if username in get_all_users():
                self.subscribed_to.append(username)
            else:
                print("Username does not exist")
        return 0

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


def get_all_users():
    users = listdir("./data/")
    new_users = []

    for user in users:
        if user.endswith(".password"):
            user = user.split(sep=".")[0]
            new_users.append(user)

    return new_users


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

        elif action == "pp": # post personal
            with open("./data/" + u.username + ".posts", "a") as messages:
                messages.write(input("$> ") + "\n")

        elif action == "lu": # list users
            users = get_all_users()
            for user in users:
                print(user)

        elif action == "rp": # read personal messages
            with open("./data/" + username + ".posts", "r") as messages:
                print(messages.read())

        elif action == "s": # subscribe
            subscribe_to = input("%> ")
            u.subscribe(subscribe_to)

        elif action == "h":
            help = ["You typed h, the help character",
                    "",
                    "Here is a list of commands:",
                    "\trg\tRead global messages",
                    "\trp\tRead my personal messages",
                    "\tpg\tPost a global message",
                    "\tpp\tPost a personal message",
                    "\tlu\tList all users",
                    "\ts\tSubscribe to an user",
                    "\th\tShow this help message",
                    "",
                    "Here is a list of prompts:",
                    "\t` > `\tWaiting for command",
                    "\t`$> `\tWaiting for message",
                    "\t`%> `\tWaiting for username"]

            for h in help:
                print(h)

        else:
            print("Unkown command, type `h` for a list of commands")


if __name__ == "__main__":
    main()
