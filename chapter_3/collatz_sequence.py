number_input = ''

def collatz(number):
    number_computed = None
    if number % 2 == 0:
        number_computed = number // 2
    else:
        number_computed = 3 * number + 1

    print(number_computed)
    return number_computed

while True:
    number_input = input("Enter an integer: ")
    number_int = None
    try:
        number_int = int(number_input)
        print(number_int)
    except ValueError:
        print(str(number_input)+ " is not an integer")
        continue
    
    number_collatz = number_int
    while True:
        if number_collatz != 1:
            number_collatz = collatz(number_collatz)
            continue
        break
    break