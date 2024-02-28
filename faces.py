def emoji_converter(user_input):


    happy_emoji = "\U0001F642"
    sad_emoji = "\U0001F641"

    user_input = user_input.replace(":)", happy_emoji)
    user_input = user_input.replace(":(", sad_emoji)
    return user_input

def main():

    user_input = input("Enter an emoticon here: " )

    print(emoji_converter(user_input))

main()