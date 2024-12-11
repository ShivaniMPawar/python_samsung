#Accept the average score from the user and print the result 

avg_score=int(input("Enter your average score : "))

# if the user gives number less than -1 then after checking the if condition of and it fails.All other statements are skipped and else part is executed 

if avg_score <= 49 and avg_score >= 0:
    print("Fail")

elif avg_score <= 79:
    print("Second class")

elif avg_score <= 95:
    print("First class")

elif avg_score <= 100:
    print("Distinction")

else:
    print("Invalid avg score")