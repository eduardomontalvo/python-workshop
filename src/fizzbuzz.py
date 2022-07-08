numRange = range(25, 151, 4)

def fizzbuzz(nums):
    print("-------------------------------")
    for x in nums:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")    
        else:
            print(x)

fizzbuzz(numRange)
