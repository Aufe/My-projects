a = {"January": 31,
     "February": 28,
     "Marth": 31,
     "April": 30,
     "May": 31,
     "June": 30,
     "July": 31,
     "August": 31,
     "September": 30,
     "October": 31,
     "November": 30,
     "December": 31
}

day = 7
days_sunday = 0
for i in range(1900, 2001):
    for j in a:
        if i % 4 == 0 and j == "February" and i != 1900:
            day = (day + a[j] + 1) % 7
            if day == 6:
                days_sunday += 1
        else:
            day = (day + a[j]) % 7
            if i > 1900 and day == 6:
                days_sunday += 1


print(days_sunday)