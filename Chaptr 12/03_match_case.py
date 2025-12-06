def match_case(statuse):
    match statuse:
        case 200:
            return "ti is 200"
        case 300:
            return "it is 300"
        case 400:
            return "it is 400"
        case 500:
            return "it is 500"
        case _:
            return "Unknown input"

print(match_case(int(input("Enter Your choice : "))))