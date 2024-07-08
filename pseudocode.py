def my_max(num_array):
    max_value = num_array[0]
    for elem in num_array:
        if elem > max_value:
            max_value = elem
    return max_value

def my_min(num_array):
    min_value = num_array[0]
    for elem in num_array:
        if elem < min_value:
            min_value = elem
    return min_value

def my_sum(num_array):
    local_counter = 0
    for elem in num_array:
        local_counter += elem
    return local_counter

def my_sort(num_array):
    n = len(num_array)
    for i in range(n):
        sorted = False
        for j in range(n - i - 1):
            if num_array[j] > num_array[j + 1]:
                sorted = True
                num_array[j], num_array[j + 1] = num_array[j + 1], num_array[j]
        if sorted == False:
            return num_array

def validate(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            
            if user_input in list(range(1, 6)):
                return user_input
            else:
                print("Please input a number from 1-5.")
        except ValueError:
            print("Please input a number. ")

def question_1():
    for i in range(1, 101):
        if (i % 5 == 0):
            print(i)

def question_2():
    stopping_point = int(input("Enter stopping point: "))
    counter = 0
    while counter <= stopping_point // 2:
        print(counter * 2)
        counter += 1

def question_3():
    # a. Get 5 inputs
    num_array = []
    counter = 0
    while counter < 5:
        num_array.append(int(input(f"Number {counter + 1}: ")))
        counter += 1

    # b i) Calculate average (in-built function)
    average = round(sum(num_array) / 5, 2)

    # b ii) Calculate average (custom function)
    average_2 = round(my_sum(num_array) / 5, 2)

    # c i) Find min and max number (in-built functions)
    max_value = max(num_array)
    min_value = min(num_array)

    # c.ii) Find min and max number (custom functions)
    max_value_2 = my_max(num_array)
    min_value_2 = my_min(num_array)
    
    # d. Print out all values
    print(f"Average: {average}, Max value: {max_value}, Min value: {min_value}")

def question_4():
    num_array = []
    counter = 0
    while counter < 3:
        user_input = int(input(f"Number {counter + 1}: "))
        num_array.append(user_input)
        counter += 1
    
    # Sorting using in-built functions
    print("Sorted array: ", end="")
    print(*sorted(num_array), sep=", ")

    # Sorting using custom function
    print(my_sort(num_array))

def question_5():
    user_input = int(input("Enter a num: "))
    counter = 0

    while user_input >= 0:
        counter += user_input
        user_input = int(input("Enter a num: "))

    print(counter)

while True:
    print("\nWhich question would you like to see work? \n")
    for i in range(1, 6):
        print(f"Question {i}")
    choose_function = validate("\nEnter a digit from 1-5: ")
    
    match choose_function:
        case 1:
            question_1()
        case 2:
            question_2()
        case 3:
            question_3()
        case 4:
            question_4()
        case 5:
            question_5()
