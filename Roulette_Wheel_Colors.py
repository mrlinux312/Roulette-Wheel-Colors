print("Roulette wheel colors")
pocket = int(input("Please enter pocket number from 0-36:"))
odd = (pocket % 2 != 0)
even = (pocket % 2 == 0)

if pocket == 0:
    pcolor = "green"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 1 and pocket <= 10 and odd:
    pcolor = "red"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 1 and pocket <= 10 and even: 
    pcolor = "black"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 11 and pocket <= 18 and odd:
    pcolor = "black"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 11 and pocket <= 18 and even:
    pcolor = "red"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 19 and pocket <= 28 and odd:
    pcolor = "red"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 19 and pocket <= 28 and even:
    pcolor = "black"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 29 and pocket <= 36 and odd:
    pcolor = "black"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket >= 29 and pocket <= 36 and even:
    pcolor = "red"
    print(f"The color for pocket {pocket} is {pcolor}")
elif pocket < 0 or pocket > 36:
    print("Error! You have entered a number out of range!")
    print("\nPlease enter a number between 0-36")
