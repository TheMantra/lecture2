year=int(input("please enter year\n"))
temp_year=year
while year>=2029:
    year*=4
    print(year)

print("inside for loop")

year=int(input("please enter year\n"))
for x in range(temp_year,2029):
    print(x)
