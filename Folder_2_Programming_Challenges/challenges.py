### Challenge 1

def challenge_1():
    """
    Prints numbers from 1 - 100.
    Returns nothing.
    """

    start = 1
    end = 100
    answer = ""

    for x in range(start, end+1):
        if x != 100:
            if x % 15 == 0:
                answer += "PlanitTesting "
            elif x % 3 == 0:
                answer += "Planit "
            elif x % 5 == 0:
                answer += "Testing "
            else:
                answer += f"{x} "
        else:
            answer += "Testing"
    print(answer)

challenge_1()



### Challenge 2



### Challenge 3 

def challenge_3_a(input_string):
    """Replaces spaces with hypen and reverses the string using slice index syntax 
    This solution uses build in Methods
    """
    new_string = ""
    for char in input_string[::-1]:         # using index syntax for slicing we're able to start from the end of the string to the front
        new_string += char
    answer = new_string.replace(" ", "-")   # using the string replace() method, we can produce the answer.
    print(answer)

challenge_3_a("reverse order")

def challenge_3_b(input_string):
    """Replaces spaces with hypen and reverses the string using slice index syntax 
    This solution uses a control flow aka "Naive" approach
    """

    answer = ""
    for char in input_string[::-1]:
        if char == " ":
            answer += "-"
        else:
            answer += char
    
    print(answer)

challenge_3_b("reverse order")



### Challenge 4
