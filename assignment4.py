class IteratorClass:
    # Complete this class! It takes in three inputs when initializing.
    # input#1 x -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#2 y -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#3 operator -- is a string that can either be 'add', 'sub', 'mul', 'div' -- If the specified operator
    # is not one of these, raise a ValueError.

    # Complete the class by writing functions that will turn it into an iterator class.
    # https://www.programiz.com/python-programming/methods/built-in/iter
    # The purpose of the class is to take two lists(x and y), apply the specified operator and return the output
    # as an iterator, meaning you can do "for ele in IteratorClass(x,y,'add')"
    # NOTE: For the / operator, round to two decimal places
    # Raise ValueError when the length is not the same for both inputs
    # Raise ValueError when the operator is not add, sub, mul, or div.

    # BEGIN SOLUTION
    def __init__(self,x,y,operator) -> None:
        if (operator not in ('add', 'sub', 'mul', 'div')) or (len(x) != len(y)):
            raise ValueError
        self.x = x
        self.y = y
        self.operator = operator
        self.val_len = len(self.x)
        if self.operator=='add':
            self.addition()
        elif self.operator=='sub':
            self.subtraction()
        elif self.operator=='mul':
            self.multiplication()
        else:
            self.division()
        # self.value = 0
        # return self
    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.val_len:
            output = self.my_list[self.value]
            self.value += 1
            return output
        else:
            raise StopIteration

    def addition(self):
        self.my_list = [self.x[i]+self.y[i] for i in range(self.val_len)]
        return iter(self.my_list)

    def subtraction(self):
        self.my_list = [self.x[i]-self.y[i] for i in range(self.val_len)]
        return iter(self.my_list)

    def multiplication(self):
        self.my_list = [self.x[i]*self.y[i] for i in range(self.val_len)]
        return iter(self.my_list)

    def division(self):
        self.my_list = [round(self.x[i]/self.y[i],2) for i in range(self.val_len)]
        return iter(self.my_list)
    # END SOLUTION


class ListV2:
    # Complete this class to fulfill the following requirement
    # 1) The class only takes one input argument which is a list or a tuple;
    #    Raise ValueError if the input is not a list or tuple
    # 2) The class overload loads +,-,*,/ and returns a ListV2 object as the result
    # 3) The class can handle +,-,*,/ for both list and int/float, meaning the thing to the right of the operator
    #    can be a sequence or a number;
    # 4) The class is an iterator
    # HINT: Study the assert statements in the test file to understand how this class is being used and reverse engineer it!
    # NOTE: For the / operator, round to two decimal places

    # BEGIN SOLUTION
    def __init__(self,in_val) -> None:
        if not(isinstance(in_val,list) or isinstance(in_val,tuple)):
            raise ValueError
        self.in_val = in_val
        self.limit = len(self.in_val)
    
    def __iter__(self):
        self.value=0
        return self
    
    def __next__(self):
        if self.value<self.limit:
            out_val = self.in_val[self.value]
            self.value+=1
            return out_val
        else:
            raise StopIteration

    def __add__(obj1,obj2):
        if isinstance(obj2,int) or isinstance(obj2,float):
            return ListV2([obj1.in_val[i]+obj2 for i in range(obj1.limit)])
        if isinstance(obj2,list) or isinstance(obj2,tuple):
            return ListV2([obj1.in_val[i]+obj2[i] for i in range(obj1.limit)])
        return ListV2([obj1.in_val[i]+obj2.in_val[i] for i in range(obj1.limit)])

    def __sub__(obj1,obj2):
        if isinstance(obj2,int) or isinstance(obj2,float):
            return ListV2([obj1.in_val[i]-obj2 for i in range(obj1.limit)])
        if isinstance(obj2,list) or isinstance(obj2,tuple):
            return ListV2([obj1.in_val[i]-obj2[i] for i in range(obj1.limit)])
        return ListV2([obj1.in_val[i]-obj2.in_val[i] for i in range(obj1.limit)])

    def __mul__(obj1,obj2):
        if isinstance(obj2,int) or isinstance(obj2,float):
            return ListV2([obj1.in_val[i]*obj2 for i in range(obj1.limit)])
        if isinstance(obj2,list) or isinstance(obj2,tuple):
            return ListV2([obj1.in_val[i]*obj2[i] for i in range(obj1.limit)])
        return ListV2([obj1.in_val[i]*obj2.in_val[i] for i in range(obj1.limit)])
    
    def __truediv__(obj1,obj2):
        if isinstance(obj2,int) or isinstance(obj2,float):
            return ListV2([round(obj1.in_val[i]/obj2,2) for i in range(obj1.limit)])
        if isinstance(obj2,list) or isinstance(obj2,tuple):
            return ListV2([round(obj1.in_val[i]/obj2[i],2) for i in range(obj1.limit)])
        return ListV2([round(obj1.in_val[i]/obj2.in_val[i],2) for i in range(obj1.limit)])

    def __repr__(self):
        return f'{self.in_val}'
    # END SOLUTION


def ex3(filename):
    # Complete this function to read grades from `filename` and find the minimum
    # student test averages. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and use the min() function to find the student with the minimum
    # test average. The input to the min function should be
    # a list of lines. Ex. ['student1,33,34,35,36,45', 'student2,33,34,35,36,75']
    # input filename
    # output: (lambda_func, line_with_min_student) -- example (lambda_func, 'student1,33,34,35,36,45')

    # BEGIN SOLUTION

    fp = open(filename)
    lines = [i.strip() for i in fp if i.strip()]
    # lambda function
    l_func = lambda x: sum(map(float,x.split(',')[1:]))/len(x.split(',')[1:])
    # min function
    return l_func,min(lines,key=l_func)
    # END SOLUTION


def ex4(filename):
    # Complete this function to read grades from `filename` and map the test average to letter
    # grades using map and lambda. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and map() function.
    # The input to the map function should be
    # a list of lines. Ex. ['student1,73,74,75,76,75', ...]. Output is a list of strings in the format
    # studentname: Letter Grade -- 'student1: C'
    # input filename
    # output: (lambda_func, list_of_studentname_and_lettergrade) -- example (lambda_func, ['student1: C', ...])

    # Use this average to do the grade mapping. Round the average grade.
    # D = 65<=average<70
    # C = 70<=average<80
    # B = 80<=average<90
    # A = 90<=average
    # Define a function that takes in a number grade and returns the letter grade and use
    # it inside the lambda function.
    # HINT: create a function

    # BEGIN SOLUTION
    def grade(average):
        if 65<=average<70:
            return 'D'
        elif 70<=average<80:
            return 'C'
        elif 80<=average<90:
            return 'B'
        return 'A'

    fp = open(filename)
    lines = [i.strip() for i in fp if i.strip()]    
    l_func = lambda x : ": ".join([x.split(',')[0],grade(round(sum(map(float,x.split(',')[1:]))/len(x.split(',')[1:])))])
    final_grades = map(l_func,lines)
    return l_func,list(final_grades)
    pass
    # END SOLUTION


def ex5(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file

    import json
    with open(filename) as infile:
        grades = json.load(infile)
    infile.close()
    # BEGIN SOLUTION
    l_func = lambda ele: float(ele['test3'])
    # grades = sorted(grades,key=l_func)
    grades.sort(key=l_func)
    return l_func, grades
    # END SOLUTION
