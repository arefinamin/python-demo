#Task 11

# even_count = 0
# odd_count = 0
#
# for remaining in range(6, 0, -1):
#     number = int(input(f"Type a number ({remaining} remaining): \n"))
#
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Odd total: {odd_count}\n"
#       f"Even total: {even_count}")

#Task 12
total = 0
even_count = 0
odd_count  = 0

for remaining in range(5, 0, -1):
    number = int(input(f"Enter a number ({remaining} remaining): \n"))

    if number % 2 == 0:
        even_count += 1

    else:
        odd_count += 1
    total += number

average = float(total / 5)

print(f"Total: {total} \n"
      f"Average: {average} \n"
      f"Even count: {even_count} \n"
      f"Odd count: {odd_count}     ")