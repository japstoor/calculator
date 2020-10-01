x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
op = [(x+y),(x-y),(x*y),(x/y),(x%y)]
tag = ["Addition:","Subtraction:","Multiplication:","Division:","Modulation:"]
i=0
op_index=0
tag_index=0
while i<5:
    print(tag[tag_index],op[op_index])
    tag_index += 1
    op_index += 1
    i+=1
