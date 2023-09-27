def ex1(name):
    # Complete this function to use the `name` input parameter/argument to create the following string and return it:
    # Hello, <name>, nice to meet you!
    # Example: name = Brian
    # Output: "Hello, Brian, nice to meet you!"
    # You must use f-string!!!

    # BEGIN SOLUTION
    return f"Hello, {name}, nice to meet you!"
    # END SOLUTION


def ex2(x, y, z):
    # Complete this function to use the inputs x, y, and z to return the quoted string.
    # You must use f-string to create each line, but you can use the + operator to join each line
    # or use the new line character inside the f-string to add new lines. 
    """
    The value of x is: <x>.
    The value of y is: <y>.
    The value of z is: <z>.
    """

    # BEGIN SOLUTION
    return f"""The value of x is: {x}.\nThe value of y is: {y}.\nThe value of z is: {z}."""
    # END SOLUTION


def ex3(length, width):
    # Complete this function to use the inputs length and width to
    # calculate the area of a rectangle and return the following string:
    # "The area of a rectangle with length <length> and width <width> is <area>."
    # Make sure to round the area to two decimal places.

    # BEGIN SOLUTION
    return f"The area of a rectangle with length {length} and width {width} is {round(length*width,2)}."
    # END SOLUTION


def ex4(radius):
    # Complete this function to return the surface area of a sphere given a radius.
    # Use the input `radius` as the radius
    # round the surface area to two decimals
    # Use the PI from the math module

    import math
    PI = math.pi

    # BEGIN SOLUTION
    return round(4*PI*radius*radius,2)
    # END SOLUTION


def ex5(radius):
    # Complete this function to return the volume of a sphere given a radius.
    # Use the input `radius` as the radius
    # round the volume to two decimals
    # Use the PI from the math module

    import math
    PI = math.pi

    # BEGIN SOLUTION
    return round(4*PI*radius*radius*radius/3,2)
    # END SOLUTION


def ex6(weight, height):
    # The body mass index (BMI) is calculated as a peron's weight (in pounds) times 703, divided by the square
    # of the person's height (in inches). A BMI in the range 19-25, inclusive, is considered healthy.
    # Complete this function to calculate and return a person's BMI
    # Round the BMI to two decimals places using the round function

    # BEGIN SOLUTION
    return round((weight*703)/(height*height),2)
    # END SOLUTION


def ex7(no_one_liter_bottles, no_more_than_one_liter_bottles):
    # When you buy soda bottles, you deposit a small amount to encourage recycling.
    # For one liter bottle the deposit is $0.10.
    # For a bottle larger than one liter, the deposit is $0.25.
    # Complete this function to print a refund message like follows:
    # The refund amount is $<amount>.
    # Round the refund to two decimal places using f-string format specifier

    # BEGIN SOLUTION
    amount = no_one_liter_bottles/10 + no_more_than_one_liter_bottles/4
    return f"The refund amount is ${amount:.2f}."
    # END SOLUTION


def ex8(a, b):
    # Complete this function to return the following string given two numbers a and b
    """
    The sum of <a> and <b> is <result>.
    The difference when <b> is subtracted from <a> is <result>.
    The product of <a> and <b> is <result>.
    The quotient when <a> is divided by <b> is <result>.
    The remainder when <a> is divided by <b> is <result>. 
    The result of <a>^<b> is <result>. 
    """

    # Return just one string that has multiple lines. use f-string and + to concatenate lines

    # BEGIN SOLUTION
    return f"""The sum of {a} and {b} is {a+b}.
The difference when {b} is subtracted from {a} is {a-b}.
The product of {a} and {b} is {a*b}.
The quotient when {a} is divided by {b} is {a//b}.
The remainder when {a} is divided by {b} is {a%b}.
The result of {a}^{b} is {a**b}."""
    # END SOLUTION


def ex9(P, r, t):
    # The formula for simple interest is A = P(1+rt), where P is
    # the principle amount, r is the annual rate of interest,
    # t is the number of years the amount is invested, and A
    # is the amount at the end of the investment.
    # Complete this function to return the following string:
    # After <t> years at <r>%, the investment will be worth $<A>.
    # Round the amount to two decimal places using f-string
    # Hint: rate is a percentage!

    # BEGIN SOLUTION
    return f"After {t} years at {r}%, the investment will be worth ${P*(1 + (r/100*t)):.2f}."
    # END SOLUTION


def ex10(P, r, t, n):
    # The formula for compound interest is
    # A = P(1 + r/n)^nt
    # where:
    # P is the principle amount.
    # r is the annual rate of interest.
    # t is the number of years the amount is invested.
    # n is the number of times the interest is compounded per year.
    # A is the amount at the end of the investment.
    # Complete this function to return the following string:
    # $<P> invested at <r>% for <t> years compounded <n> times per year is $<A>.
    # round to two decimal places using f-string formatting

    # BEGIN SOLUTION
    return f"${P} invested at {r}% for {t} years compounded {n} times per year is ${P*(1 + (r/(100*n)))**(n*t):.2f}."
    # END SOLUTION


def ex11(input_string):
    """
    This function takes in one input string. Complete this function to return
    the input string and the number of characters in the input string.
    Sample Input: Amherst
    Expected return string: The input string 'Amherst' has 7 characters. 
    - Use f-string
    """

    # BEGIN SOLUTION
    return f"The input string '{input_string}' has {len(input_string)} characters."
    # END SOLUTION


def ex12(noun, verb, adjective, adverb):
    """
    This function takes in four input strings. Complete this function to return
    a sentence using the four input strings
    Input Strings: noun, verb, adjective, adverb
    Expected print Statement: Do you <verb> your <adjective> <noun> <adverb>? That's hilarious!
    - Use f-string
    """

    # BEGIN SOLUTION
    return f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    # END SOLUTION


def ex13(current_age, age_at_retirement, current_year):
    """
    This function takes in three numbers as input arguments: current_age, age_at_retirement, and current_year. 
    Complete this function to return the expected output string. 

    If current_age = 36, age_at_retirement = 72, and current_year = 2021

    Expected output:
    Your current age is: 36.
    You would like to retire at: 72.
    You have 36 years left until you can retire.
    It's 2021, so you can retire in 2057.

    - Use f-string
    """

    # BEGIN SOLUTION
    return f"""Your current age is: {current_age}.
You would like to retire at: {age_at_retirement}.
You have {age_at_retirement-current_age} years left until you can retire.
It's {current_year}, so you can retire in {current_year+(age_at_retirement-current_age)}."""
    # END SOLUTION


def ex14(length, width):
    """
    This function takes in the length and width in feet. 
    Complete this function to return the expected output string. 
    Use formula -- m^2 = f^2 * 0.09290304 to convert feet^2 to meter^2

    If length = 15 and width = 20

    Expected output:
    The length of the room in feet is 15.
    The width of the room in feet is 20.
    The dimension of the room is 15 by 20 feet.
    The area is
    300 square feet
    27.87 square meters

    - Use f-string
    """

    # BEGIN SOLUTION
    return f"""The length of the room in feet is {length}.
The width of the room in feet is {width}.
The dimension of the room is {length} by {width} feet.
The area is
{length*width} square feet
{length*width*0.09290304:.2f} square meters"""
    # END SOLUTION


def ex15(number_of_people, number_of_pizzas):
    """
    This function takes in the number of people and the number of pizzas. Assume each pizza has 8 slices. 

    Complete this function to return the expected output string. 

    If number_of_people = 8 and number_of_pizzas = 2

    Expected output:
    There are 8 with 2 pizzas.
    Each person gets 2 pieces of pizza.
    There are 0 leftover pieces.

    - Use f-string
    """

    # BEGIN SOLUTION
    return f"""There are {number_of_people} with {number_of_pizzas} pizzas.
Each person gets {(number_of_pizzas*8)//number_of_people} pieces of pizza.
There are {(number_of_pizzas*8)%number_of_people} leftover pieces."""
    # END SOLUTION


def ex16(length, width):
    """
    This function takes in the length and width in feet of a ceiling. You need to calculate the number
    of gallons needed to paint the ceiling. Assuming one gallon can paint 350 square feet. 

    Complete this function to return the expected output string. 

    If length = 12 and width = 30

    Expected output:
    You will need to purchase 2 gallons of paint to cover 360 square feet.

    - Use f-string
    - HINT: You need to use the math.ceil function to round up
    """

    import math
    # BEGIN SOLUTION
    return f"You will need to purchase {math.ceil(length*width/350)} gallons of paint to cover {length*width} square feet."
    # END SOLUTION


def ex17(value):
    """
    You must use f-string formatting to get the output string: "The value is: 3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not use the round
    function. Rather, use f-string for rounding. Make sure to return the output string!
    """

    # BEGIN SOLUTION
    return f"The value is: {value:.4f}."
    # END SOLUTION


def ex18(value):
    """
    You must use f-string formatting to get the following string output: "The value is:     3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not just put
    spaces inside the f-string. Use f-string format specifiers to adjust justification and width. 
    """

    # BEGIN SOLUTION
    return f"The value is: {value:>10.4f}."
    # END SOLUTION


def ex19(value):
    """
    You must use f-string formatting to get the following string output: "The value is: 3.141590--.". This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. 
    """

    # BEGIN SOLUTION
    return f"The value is: {value:-<10.6f}."
    # END SOLUTION


def ex20(value):
    """
    You must use f-string formatting to get the following output string: "The value is: --3.141590--." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """
    # BEGIN SOLUTION
    return f"The value is: {value:-^12.6f}."
    # END SOLUTION

def ex21(hours, wage):
    # Many companies pay time-and-a-half for any hours worked above 40 in a given week.
    # Complete this function whose inputs are hours worked (hours) and the hourly rate (wage) to
    # calculate the total wages for the week.
    #
    # BEGIN SOLUTION
    tot = hours*wage
    if hours>40:
        tot += (hours-40)*wage/2
    return tot
    # END SOLUTION


def ex22(score):
    # A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
    # Complete this function which accepts a quiz score as an input and uses a decision structure to calculate the corresponding
    # grade.
    # BEGIN SOLUTION
    dict1 = {"5":'A', "4":'B', "3":'C', "2":'D', "1":'F', "0":'F'}
    return dict1[str(score)]
    # END SOLUTION


def ex23(score):
    # A certain CS professor gives 100-point exams that are graded on the scale 90-100: A, 80-89: B, 70-79: C,
    # 69-69: D, < 60: F. Complete this function which accepts an exam score as input and uses a decision structure
    # to calculate the corresponding grade.

    # BEGIN SOLUTION
    # 90-100: A, 80-89: B, 70-79: C,
    # 69-69: D, < 60: F
    if score>90:
        return 'A'
    elif score>80:
        return 'B'
    elif score>70:
        return 'C'
    elif score>60:
        return 'D'
    return 'F'
    # END SOLUTION


def ex24(credits):
    # A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman.
    # At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classified as Senior.
    # Complete this function which calculates the class standing from the number of credits earned.
    # BEGIN SOLUTION
    if credits>=26:
        return 'Senior'
    elif credits>=16:
        return 'Junior'
    elif credits>=7:
        return 'Sophomore'
    return 'Freshman'
    # END SOLUTION


def ex25(limit, speed):
    # The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a
    # penalty of $200 for any speed over 90 mph. Complete this function which accepts a speed limit and a clocked
    # speed and either return the string `Legal` or the amount of fine, if the speed is illegal.
    # BEGIN SOLUTION
    if speed>limit:
        fine = 50 + (speed-limit)*5
        if speed<90:
            return fine
        return fine+200
    return 'Legal'
    # END SOLUTION


def ex26(input_string):
    # Complete this function to determine if the input_string is a palindrome. Return True or False
    # Use square brackets to reverse the input_string! Make sure to lower the input string before testing!
    # BEGIN SOLUTION
    if input_string.lower() == input_string[::-1].lower():
        return True
    return False
    # END SOLUTION


def ex27(month, day):

    # The year is divided into four season: spring, summer, fall (or autumn) and winter.
    # While the exact dates that the seasons change vary a little bit from year to
    # year because of the way that the calender is constructed, we will use the following
    # dates for this exercise:

    # Season  -- First Day
    # Spring  -- March 20
    # Summer  -- June 21
    # Fall  -- September 22
    # Winter    -- December 21

    # Complete this function which takes in as inputs a month and day. It should
    # output the season.
    # input 1: month -- str
    # input 2: day -- int

    # output: month -- str (Spring, Summer, Fall, Winter)

    # BEGIN SOLUTION
    # if month in ('January','February','December','March'):
    if (month=='December' and day>=21) or (month=='March' and day<20) or month in ('January','February'):
            return "Winter"
    # if month in ('April','May','March','June'):
    # if (month=='March' and day>=20) or (month=='June' and day<21):
    if (month=='March' and day>=20) or (month=='June' and day<21) or month in ('April','May'):
            return "Spring"
    # if month in ('July','August','June','September'):
    #     if (month=='June' and day>=21) or (month=='September' and day<22):
    if (month=='June' and day>=21) or (month=='September' and day<22) or month in ('July','August'):
            return "Summer"
    # if month in ('October','November','September','December'):
        # if month=='September' and day>22:
    # if (month=='June' and day>=21) or (month=='September' and day<22) or month in ('July','August'):
    else:
        return "Fall"
    # END SOLUTION


def ex28(year):
    # Complete this function to check if year is a leap year
    # Input: year
    # Output: True or False (Boolean)

    # BEGIN SOLUTION
    if year%400 == 0 and year%100 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    return False
    # END SOLUTION


def ex29(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # IMPORTANT: Use the function ex28() to determine if year is leap year

    # BEGIN SOLUTION
    if ex28(year):
        if (month in (1,3,5,7,8,10,12) and day<32) or (month==2 and day<30) or (month!=2 and day<31):
            return True
    else:
        if (month in (1,3,5,7,8,10,12) and day<32) or (month==2 and day<29) or (month!=2 and day<31):
            return True
    return False
    # END SOLUTION


def ex30(month, day, year):
    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # IMPORTANT: use the functions you wrote previous, namely, ex28 and ex29.
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid.

    # BEGIN SOLUTION
    if ex29(month, day, year):
        day_num = 31 * (month - 1) + day
        if month>2:
            day_num -= (4*(month)+23)//10
        if ex28(year) and month>2:
            day_num+=1
        return day_num
    return False
    # END SOLUTION


def ex31(plate):

    # In a particular jurisdiction, older license plates consist of three uppercase
    # letters followed by three digits. When all of the license plates following
    # that pattern had been used, the format was changed to four digits followed by
    # three uppercase letters.

    # Complete this function whose only input is a license plate and its output
    # is: 1) Older/Valid 2) Newer/Valid 3) Invalid
    # input: plate (str)
    # output: 'Older/Valid' or 'Newer/Valid' or 'Invalid'
    # HINT: Use the comparator operators (>=, <=)!

    # BEGIN SOLUTION
    if len(plate)==6 and (plate[:3]>='AAA' and plate[:3]<='ZZZ') and (int(plate[3:])>=000 and int(plate[3:])<=999):
        return "Older/Valid"
    elif len(plate)==7 and (int(plate[:4])>=0000 and int(plate[:4])<=9999) and (plate[4:]>='AAA' and plate[4:]<='ZZZ'):
        return "Newer/Valid"
    return "Invalid"
    # END SOLUTION


def ex32(date):
    # A magic date is a date where the day multiplied by the month is equal
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year) -- e.g., 06/01/2022 -- will have leading zero before month and day
    # output: True or False (bool)
    # Hint: use string indexing to extract the month, day, and year from the date string

    # BEGIN SOLUTION
    [month,day,year] = date.split('/')
    if int(month)*int(day) == int(year[-2:]):
        return True
    return False
    # END SOLUTION

