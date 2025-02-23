import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it's a free instance for 60 hours per month")
elif type == "t2.medium":
    print(" it charges $2 per hour")
elif type == "t3.large":
    print("it charges $3 per hour")
else:
    print("instance type is not valid")