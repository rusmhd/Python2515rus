#Rushil Mohamed
#Write a function that calculates the average of numbers in a list.Example list: [12, 18, 25, 30]
def calculate_average(lst):
    return sum(lst) / len(lst)

numbers = [12, 18, 25, 30]
avg = calculate_average(numbers)

print("Average:", avg)