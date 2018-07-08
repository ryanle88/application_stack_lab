import time


def age_calc(age):
    new_age = age + (2035 - int(time.strftime("%Y")))
    return(new_age)


while True:
    age = int(input("How old are you? "))
    if age < 100 and age > 0:
        break

print(age_calc(age))
