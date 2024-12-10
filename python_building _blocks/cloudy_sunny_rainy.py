"""Check if it is cloudy or sunny. If sunny and cloudy, then go out with jacket. If only sunny the go out as you wish.
If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy go out with umbrella."""


cloudy = input("Is it cloudy? (Type 'Yes' or 'No') :")
sunny = input("Is it sunny? :")
if cloudy == 'Yes' and sunny == 'Yes':
    print("Go out with jacket")
if cloudy == 'No' and sunny == 'Yes':
    print("Go out as your wish")
if cloudy =='Yes':
    rain=input("Is it raining? (Type 'Yes' or 'No') :")
    if rain == 'Yes':
        print("Go out with umbrella")
    else:
        print("Go out as you wish")

