number = int(input("Please write any number : "))

if number == 1:
    print(number,'is not a prime number')
elif number == 2 or number == 3 or number == 5 or number == 7:
    print(number,'is a prime number')
elif number % number == 0 and number % 1 == 0 and number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    print(number,'is a prime number')
else:
    print(number,'is not a prime number')