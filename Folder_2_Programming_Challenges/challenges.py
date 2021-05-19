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
    """takes in 3 arguments, one integer and 2 strings.
    returns an f-string
    """
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

def challenge_5(input_string):
    """takes string input, returns string
        using a list containing dictionaries of attributes for each restaurant
        we are able to convert this to a JSON object and store into a database
        to retrieve later if need be.
    """

    restaurants = [
        {
            "cuisine": "pizza",
            "restaurant": "Awesome pizza place",
            "price": "$20"
        },
        {
            "cuisine": "burger",
            "restaurant": "wild burger joint",
            "price": "$15"
        }
    ]
    for restaurant in restaurants:
        if restaurant["cuisine"] in input_string:
            return f"{restaurant['restaurant']}, {input_string}, {restaurant['price']}"

print(challenge_5("pepperoni pizza"))


### Challenge 6


from datetime import date, datetime
from ch6_data import the_list

def challenge_6(given_list):
    """takes a list in the structure of a JSON object
    prints data requested for the dot points, 
    n.b. some variables are hard coded.
    """
    duplicate_list = []
    temp_list = []

    # 1 -- below for loop extracts duplicate names and their attributes into their own list
    for x in given_list:
        if x[0]["name"] not in temp_list:
            temp_list.append(x[0]["name"])
        else:
            duplicate_list.append(x)

    print("Duplicate names list: ", duplicate_list)

    # 2 -- alter the OG list and remove duplicate_list 
    for x in duplicate_list:
        for y in given_list:
            if x == y:
                given_list.pop(given_list.index(y))

    print("Altered original list: ", given_list)

    # 3 -- calculate average age

    count = 0
    ages = 0
    today = date.today()

    N = 51
    younger = []                                                # 4 -- Find all the people with age < N

    for x in given_list:
        date_obj = datetime.strptime(x[0]["dob"], '%d/%m/%Y')   # converting date string to date object
        difference = today - date_obj.date()
        ages += difference.days
        count +=1
        # 4 -- Find all the people with age < N
        if (difference.days)/365 < N:
            younger.append(x)

    average_age = (ages/count)/365                              # 3 -- calculate average age
    avgfloat = "{:.2f}".format(average_age)

    print("The average age is: ", avgfloat)
    print("The people who have an age with less than 51 are: ", younger)
    
    
    # 5 -- Unique countries                                     ---------- still needs work

    import requests
    import json

    unique_countries = []

    with open("countries.json", "r") as data_file:
        raw_json = data_file.readline()
        countries = json.loads(raw_json)

    for person in given_list:
        for country in countries:
            if country["demonym"] == person[0]['nationality']:
                unique_countries.append(country["name"])
            else:
                pass

    print(unique_countries)

    return "End of Testing"


print(challenge_6(the_list))