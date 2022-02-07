# num=[1,2,3,4,5,6,7]
# list=len(num)
# i=0
# while i<=list:
#     i=i+1
# print(i*i)

# def num(a,b,c,d,e,f,g):
#     num=a*b*c*d*e*f*g
#     print(num)
# num(1,2,3,4,5,6,7)


def multiply(mylist):
    result=1
    for x in mylist:
        result=result*x
    return result
number=[1,2,3,4,5,6,7]
print(multiply(number))