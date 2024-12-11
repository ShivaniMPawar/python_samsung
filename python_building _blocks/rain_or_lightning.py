#Read 2 string input from user, whether it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water

raining=input("Is it raining?(Type 'yes' or 'no'):")
lightning=input("Is it lightning?(Type 'Yes' or 'No'):")
if raining.lower() == 'yes':
    print("Go out with umbrella or play in water")
    if lightning.lower() == 'yes':
        print("Don't go out!")
    else:
        print("Go out with umbrella or play in water")


else:
    print("Go out without umbrella")
