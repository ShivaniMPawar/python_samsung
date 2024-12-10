"""Check if it is cloudy or sunny. If sunny and cloudy, then go out with jacket. If only sunny the go out as you wish.
If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy then check if it is lightning.
If it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water. If it is only cloudy and lightning then do not go out.
"""

cloudy = input("Is it cloudy? (Type 'Yes' or 'No') :")
sunny = input("Is it sunny? :")
if cloudy == 'Yes' and sunny == 'Yes':
    print("Go out with jacket")

if cloudy == 'No' and sunny == 'Yes':
    print("Go out as your wish")

if cloudy == 'Yes':
    rain=input("Is it raining? (Type 'Yes' or 'No') :")

    if rain == 'Yes':
        lightning = input("Is it Lightning? (Type 'Yes' or 'No') :")

        if rain == 'Yes' and lightning == 'Yes':
            print("Don't go out")
            
        elif rain == 'Yes' and lightning == 'No':
            print("Either go out with Umbrella or play in water")

        elif cloudy == 'Yes' and lightning == 'Yes':
            print("Don't go out") 

    else:
        print("Go out as you wish")