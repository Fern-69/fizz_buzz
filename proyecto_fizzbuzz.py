def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return(num)  


def run_fizz_buzz():
    for num in range(1, 101):
        print(fizz_buzz(num))


run_fizz_buzz()


















