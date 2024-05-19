def palindrum(word):
    word = input("write something")

    if word == word[::-1]:
        return "can be reverse"
    else:
        return "can't be reverse"

Try = palindrum("Race car")
print(Try)