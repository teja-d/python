def ex1(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION
    is_lower_check = False
    is_upper_check = False
    is_number_check = False
    if len(password)<8:
        return False
    else:
        if '!' in password or '@' in password or '#' in password or '$' in password or '^' in password:
            for i in password:
                if 97 <= ord(i) <= 122:
                    is_lower_check = True
                elif 65 <= ord(i) <= 90:
                    is_upper_check = True
                elif 48<=ord(i)<=57:
                    is_number_check = True
            if is_lower_check and is_number_check and is_upper_check:
                return True
        return False

            
    # END SOLUTION


def ex2(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places

    # BEGIN SOLUTION
    s = sentence
    temp = s.split(' ')
    tot_len = len(temp)
    return round((len(s)-s.count(' '))/tot_len,2)
    # END SOLUTION


def ex3(filename):
    # Complete this function to count the number of lines, words, and chars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # BEGIN SOLUTION
    fp = open('ex3_data.txt','r')
    line_count = 0
    word_count = 0
    char_count = 0
    for line in fp:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)
    fp.close()
    return (line_count,word_count,char_count)

    # END SOLUTION


def ex4(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expressed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    principal = inv_amount = 1
    count = 0
    while principal<(2*inv_amount):
        principal = principal * (1 + apr)
        count += 1
    return count
    pass
    # END SOLUTION


def ex5(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture) given in

    # BEGIN SOLUTION
    count =0
    while n>1:
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n) +1
        count += 1
    return count
    # END SOLUTION


def ex6(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math

    # BEGIN SOLUTION
    if n<=2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True
    # END SOLUTION


def ex7(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers
    # hint use ex6

    # BEGIN SOLUTION
    temp = []
    for i in range(n+1):
        if ex6(i):
            temp.append(i)
    return temp
    # END SOLUTION


def ex8(m, n):
    # Complete this function to determine the greatest common divisor (GCD).
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n.
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # BEGIN SOLUTION
    while m!=0:
        n,m = m, n%m
    return n
    # END SOLUTION


def ex9(filename):
    # Complete this function to read grades from a file and determine the student with the highest average
    # test grades and the lowest average test grades.
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average,
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # BEGIN SOLUTION
    out = ['high_student',0,'low_studnet',100]
    with open(filename) as fp:
        for line in fp:
            if not line.strip():
                continue
            else:
                student_name = line.split(',')[0]
                scores = list(map(float,line.split(',')[1:]))
                avg_score = sum(scores)/len(scores)
                if avg_score > out[1]:
                    out[0] = student_name
                    out[1] = avg_score
                elif avg_score < out[3]:
                    out[2] = student_name
                    out[3] = avg_score
        return tuple(out)

    # END SOLUTION


def ex10(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # result. The order of the elements in the returned list does not have to
    # match the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    # output: list

    # BEGIN SOLUTION
    data.sort()
    return data[num_outliers:(-1*num_outliers)]
    # END SOLUTION


def ex11(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Preserve order

    # BEGIN SOLUTION
    l = []
    for i in words:
        if i not in l:
            l.append(i)
    return l
    # END SOLUTION


def ex12(n):
    # A proper divisor ofa  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only result.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    l = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            l.append(i)
    return l
    # END SOLUTION


def ex13(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28
    # Complete this function to determine if a the number a perfect number or not.
    # input: n (int)
    # output: True or False (bool)

    # BEGIN SOLUTION
    if n == sum(ex12(n)):
        return True
    return False
    # END SOLUTION


def ex14(points):
    # Complete this function to determine the best line.
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # BEGIN SOLUTION
    Xi = 0
    Yi = 0
    for (i,j) in points:
        Xi += i
        Yi += j
    Xbar = Xi/len(points)
    Ybar = Yi/len(points)
    point1 = point2 = 0
    for (i,j) in points:
        point1 += ((i-Xbar)*(j-Ybar))
        point2 += ((i-Xbar)**2)
    return (round(point1/point2,2), (Ybar-round((point1/point2)*Xbar,2)))
    # END SOLUTION


def ex15(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment4.py file
    # Function inputs: 
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on 
    # maximum possible length based on the header and data. This is what makes this problem hard. 
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values. 
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    row_count = len(header)
    row_length = [len(i) for i in header]
    for row in data:
        for i in range(row_count):
            item_len = len(str(row[i]))
            if item_len>row_length[i]:
                row_length[i] = item_len
    header_line = "|"
    for i in range(len(header)):
        header_line += f"{header[i]:^{row_length[i]+2}}"
        header_line += "|"
    lines = []
    for row in data:
        line = "|"
        for i in range(len(row)):
            line += f"{row[i]:^{row_length[i]+2}}"
            line += "|"
        lines.append(line)
    lines = "\n".join(lines)
    sep_line = '+'
    for i in row_length:
        sep_line += '-'*(i+2)
        sep_line += '+'
    title = f"|{title:^{-1+sum(row_length)+(3*len(row_length))}}|"
    title_line = '-' *len(title)
    data = title_line+"\n"+title+"\n"+sep_line+"\n"+header_line+"\n"+sep_line+"\n"+lines+"\n"+sep_line
    fp = open(filename,'w+')
    fp.write(data)

    # END SOLUTION

def ex16(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4. Just complete the list comprehension below.
    # input: `lst` of numbers
    # output: a list of numbers
    
    # BEGIN SOLUTION
    # complete the following line!
    return [ele for ele in lst if ele%3==0 or ele%4==0 ] #complete this line!
    pass # remove this line
    # END SOLUTION



def ex17(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers


    # BEGIN SOLUTION
    # complete the following line!
    return [ele*3 if ele%2==0 else ele*5 for ele in lst] #complete this line!
    pass # remove this line
    # END SOLUTION


def ex18(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value. 
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys

    # BEGIN SOLUTION
    return [i for i in input_dict.keys() if input_dict[i]==test_value]
    pass
    # END SOLUTION


def ex19(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on each data point. 
    Each line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries. 
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function which reads in a file and computes the median 
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN

    The files
    """
    ### BEGIN SOLUTION
    src_list = []
    fp = open(filename)
    for line in fp:
        try:
            src_list.append(float(line.strip()))
        except:
            continue
    src_list.sort()
    n = len(src_list)
    if n==0:
        return "The file does not have any valid number to compute the median"
    if n%2!=0:
        return src_list[n//2]
    return round((src_list[int(n/2)]+src_list[int(n/2)-1])/2,4)
    ### END SOLUTION

def simulateProblem():
    """
    See instructions in exercise_19_instructions.html file
    """
    import random
    ### BEGIN SOLUTION
    configurations = ['a','2a']
    choice1 = random.randint(0,1)
    env = configurations[choice1]
    action = ['stick','switch']
    choice2 = random.randint(0,1)
    act = action[choice2]
    if act == 'switch' and env == '2a':
        return False,True
    elif act == 'stick' and env == '2a':
        return True,True
    elif act == 'switch' and env == 'a':
        return True,False
    return False,False
    ### END SOLUTION


def ex20():
    """
    The function calls the simulateProblem() 10000 times to figure out 
    the empirical (observed) probability of gaining more money when switching 
    and gaining more money when sticking to the original choice.
    Return the probability of win due to sticking and win due to switching
    """
    ### BEGIN SOLUTION
    prob = {"switch":0,"stick":0}
    for i in range(10000):
        value = simulateProblem()
        if (value[0] == value[1]) and value[0] == True:
            prob['stick'] += 1
        elif (value[0] != value[1]) and value[0] == False:
            prob['switch'] += 1

    return prob['stick']/10000,prob['switch']/10000
    ### END SOLUTION