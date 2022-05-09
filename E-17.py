lst = [99, 1993, 1771, 3]
def print_big_enough(num):
    lst.sort()
    if num > lst[-1]:
        a = "Big enough"
    else:
        a = "Not big enough"
    return a

input1 = int(input("Please enter a number: "))

print(print_big_enough(input1))