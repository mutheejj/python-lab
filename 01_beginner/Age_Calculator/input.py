# this askes user to enter the year of birth

year = int(input("Enter the year of birth: "))

print(f"You were born in {year}")

def agecalc(year): 
    age = 2020 - year
    return age

result = agecalc(year)
print(f"Your age is: {result}")
