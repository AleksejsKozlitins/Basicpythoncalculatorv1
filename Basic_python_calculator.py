import re #importing RegEX

print("Basic Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath(): #define custom function
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit': #type quit to exit
        print("Goodbye,\nThank you for using basic python calculator") #printing message when you type 'quit'
        run = False
    else:
       equation = re.sub('[a-zA-Z,.:()" "]',  '', equation) #removing anything what is not equation by using RegEX

       if previous == 0:
           previous = eval(equation)
       else:
           previous = eval(str(previous) + equation)


while run:
    performMath()