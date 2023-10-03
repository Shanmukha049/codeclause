n1=eval(input("enter the 1st operand"))
n2=eval(input("enter the 2nd operand"))
op=input("choose any of the operators:'+,-,*,/,//,^,%' ")
if op=='+':
    print("Sum=",n1+n2)
elif op=='-':
    print("Difference=",n1-n2)
elif op=='*':
    print("Product=",n1*n2)
elif op=='/':
    print("Division=",n1/n2)
elif op=='//':
    print("Floor Division=",n1//n2)
elif op=='^':
    print("power=",n1**n2)
else:
    print("enter a valid operator")