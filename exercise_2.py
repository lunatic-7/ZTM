# Password checker (EXERCISE)

user_id = input("Type your user_id: ")
password = input("Set your password: ")

ps_length = len(password)
hidden = "*" * ps_length

print(f"Hello {user_id}, your password - {hidden} is {ps_length} digit long!")
