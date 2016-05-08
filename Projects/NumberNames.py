from sys import maxsize

def GetWordFromNum(num):
    simple_change = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    base = 10
    num_of_digits = 1
    while num / base > 1:
        num_of_digits += 1
        base *= 10
    if num_of_digits == 1:
        for number_version, text_version in simple_change.items():
            if num == number_version:
                num_to_word = text_version
                break
        return num_to_word


inp = int(input("Input an integer ({min_value}, {max_value}): ".format(max_value=maxsize, min_value=0)))#-maxsize-1)))

print(GetWordFromNum(inp))
