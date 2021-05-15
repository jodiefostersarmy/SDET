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
### Currently has space and time complexity of O(n)

import operator 

def challenge_2(string):
    dictionary = dict()
    new_string = string.lower()
    for x in new_string:
        dictionary[x] = new_string.count(x)
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


### using counter, which returns a dictionary with element as its key and number of occurrences as its value
from collections import Counter

def challenge_2(string):
    answer = Counter(string)
    return max(answer)

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
### NTS: this can be refactored for sure.
def challenge_4(temp,input,output):
    if input == "C":
        if output == "F":
            return f"{(9*temp)/5 + 32} F"
        elif output == "K":
            return f"{temp + 273.15} K"
        else:
            return f"{temp} C"
    elif input == "F":
        if output == "C":
            return f"{(5*(temp-32))/9} F"
        elif output == "K":
            return f"{(5*(temp-32))/9 + 273.15} K"
        else:
            return f"{temp} F"
    elif input == "K":
        if output == "C":
            return f"{temp - 273.15} C"
        elif output == "F":
            return "{:.2f}".format(f"{(9*(temp-273.15))/5 + 32} F")
        else:
            return f"{temp} K"


### Challenge 5

def challenge_5():
    pass



### Challenge 6

def challenge_6(given_list):
    duplicate_list = given_list
    temp_list = []
    for x in given_list:
        if x["name"] not in temp_list:
            temp_list.append(x)
            duplicate_list.pop(x)
        else:
            continue
    return duplicate_list



the_list = [
                [
                    {
                        "name":"Bob", 
                        "dob": "13/04/1970", 
                        "nationality": "Australian"
                    }
                ],
                [
                    {
                        "name":"Jane", 
                        "dob": "13/04/1970", 
                        "nationality": "Canadian"
                    }
                ],
                [
                    {
                        "name":"Jane", 
                        "dob": "13/04/1971", 
                        "nationality": "French"
                    }
                ]
            ]

print(challenge_6(the_list))