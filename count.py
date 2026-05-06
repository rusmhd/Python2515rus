#Rushil Mohamed
#Count how many numbers in [3, 7, 12, 18, 5, 20] are greater than 10.
lst = [3, 7, 12, 18, 5, 20]
count = 0
for x in lst:
    if x > 10:
        count += 1

print("Count > 10:", count)