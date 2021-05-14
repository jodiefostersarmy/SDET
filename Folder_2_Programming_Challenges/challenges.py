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




