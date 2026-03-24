first_score = 0

while True:
    user = input(" + yoki stop kiriting!")

    first_score += 10
    if user == "+":
        print("total score:", first_score)
    elif user == "stop":
        print("finished: ", first_score)
        break
    else:
        print("only + or stop!")


    