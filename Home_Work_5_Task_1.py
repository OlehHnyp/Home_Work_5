numbers_divisible_by_2 = []
numbers_divisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []

for i in range(1,11):
    if all([i%2 != 0, i%3 != 0]):
        numbers_not_divisible_by_2_and_3.append(i)
    elif not i%2:
        numbers_divisible_by_2.append(i)
    elif not i%3:
        numbers_divisible_by_3.append(i)

print(
    f"Even numbers in range from 1 to 10 that are divisible by 2: \
{numbers_divisible_by_2}."
)
print(
    f"Odd numbers in range from 1 to 10, which are divisible by 3: \
{numbers_divisible_by_3}."
)
print(
    f"Numbers in range from 1 to 10 that are not divisible by 2 and 3: \
{numbers_not_divisible_by_2_and_3}."
)