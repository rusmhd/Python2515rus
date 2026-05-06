#Rushil Mohamed
#Write Python programs for the following:  Count how many numbers in [3, 7, 12, 18, 5, 20] aregreater than 10.
ls=[7,12,18,5,20]
c=0
for i in ls:
  if i>10:
    c+=1
print("Count > 10:",c)