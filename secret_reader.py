def read_token():
    with open("bot_secret_token.txt") as file:
        token = file.read().strip()
    return token
