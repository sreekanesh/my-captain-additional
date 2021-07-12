#getting the number values


first_num=int(input('enter the first number  :'))
second_num=int(input('enter the second number :'))

#operator
print("")
print("")
print('+ represents addition')
print('- represents subraction')
print('* represents multiplication')
print('/ represents division')
print("")
print("")
operator=input('assign a operator {+  -  *  /}  : ')


#addition
if operator=="+":
    print(first_num+second_num)

#subraction
if operator=='-':
    print(first_num-second_num)

#multiplication
if operator=='*':
    print(first_num-second_num)

#division

if operator=="/":
    print(first_num/second_num)    