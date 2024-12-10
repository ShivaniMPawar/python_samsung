#Read 2 string input from user, whether it is raining and lightning, then do not go out. If it is only #raining then either go out with umbrella or play in water
raining=input("Is it raining?(Type 'Yes' or 'No'):")
lightning=input("Is it lightning?(Type 'Yes' or 'No'):")
if raining == 'Yes':
    print("Go out with umbrella or play in water")
if raining== 'Yes'and lightning == 'Yes':
    print("Don't go out!")
