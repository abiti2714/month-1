#  Task_2 = Write a function that sums numbers in a list.


import random
number = []

for x in range(20):
    random_num = random.randint(0, 10)
    number.append(random_num)


def sum_numbers():
    """
    Sums all the numbers in the global 'number' list and prints the total sum.
    """
    previous_sum = 0
    for num in number:
        current_number = num
        total_sum = previous_sum + current_number
        previous_sum = total_sum
    print(f"The total sum is {total_sum}")


sum_numbers()
