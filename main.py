from datetime import date, datetime, timedelta

date = datetime(2021, 5, 18)
answer1 = date + timedelta(days=7)
answer2 = answer1 + timedelta(days=7)
answer3 = answer2 + timedelta(days=7)
answer4 = answer3 + timedelta(days=7)
answer5 = answer4 + timedelta(days=7)
answer6 = answer5 + timedelta(days=7)
answer7 = answer6 + timedelta(days=7)
answer8 = answer7 + timedelta(days=7)
answer9 = answer8 + timedelta(days=7)
answer10 = answer9 + timedelta(days=7)
print(answer1, "\n", answer2, "\n", answer3, "\n", answer4, "\n", answer5, "\n", answer6, "\n", answer7, "\n", answer8,
      "\n", answer9, "\n", answer10)

# using for loop

x = 0
while x < 10:
    x += 1
    date = date + timedelta(days=7)
    print(date)

# my age

currentdate = datetime(2021, 5, 18)
year = currentdate.year

my_age = year - 2000
print("I am ", my_age, "years old")


