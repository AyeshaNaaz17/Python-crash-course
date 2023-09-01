while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a age higher than zero')
    else:
        print('Thank you!')
        break
    finally:
        print("Okay! I'm finally done!")