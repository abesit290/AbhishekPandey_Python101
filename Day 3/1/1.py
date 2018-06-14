for number in range(100):  

    if number % 3 == 0: 

        print("Fizz")                                         

        continue

    elif number % 5 == 0:     

        print("Buzz")                                         

        continue

    elif number % 15 == 0:         

        print("FizzBuzz")                                     

        continue
        
    print(number)
