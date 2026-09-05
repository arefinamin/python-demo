#Task 8
largest = 0
for _ in range(5):
    number = int(input("Enter 5 numbers: \n"))

    if number > largest:
        largest = number
print(largest)


#Task 9
count = 0
vowels = ["a","e","i","o","u"]
word = input("Enter a word: \n")
for letter in word:
    if letter in vowels:
     count += 1

print(f"total: {count}")


#Task 10
negative_count = 0
positive_count = 0
zero_count = 0

for remaining in range(5,0,-1):
    number = int(input(f"Type a number: {remaining} left \n"))

    if number < 0:
        negative_count += 1
    else:
        positive_count += 1
print(f"Positive number: {positive_count}\n"
      f"Negative number: {negative_count}  ")
