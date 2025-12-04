def get_next(n):
    return sum(int(digit) ** 2 for digit in str(n))


def is_happy(n):
    slow = n
    fast = get_next(get_next(n))
    while True:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        print(slow, fast)
        if slow == 1 or fast == 1:
            return True
        if slow == fast:
            #print(slow, fast)
            return False

#input_number = 12345678
number_list = [8]

for input_number in number_list:
    result = is_happy(input_number)
    print(f"{'yes' if result else 'NO'}, {input_number} is {'----------------------------------------------------------' if result else 'not'} a Happy Number")
