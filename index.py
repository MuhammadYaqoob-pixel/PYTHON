# def avg():
#     a=int ( input("enter a "))
#     b=int ( input("enter b "))
#     c=int ( input("enter c "))
#     average=(a+b+c)/3
#     print(average)

# avg()

# def goodday():
#     a=int(input("enter value of a"))
#     b=int(input("enter value of b"))
#     print(a+b)   

# goodday()
# goodday()
# print("thank you for using fuctions")


# def goodday(name):
#     print("soory you are fail," + name)
    
# goodday("hajjan") 

# goodday("yaqoob")
# goodday("janii")




def factorial():
    if(n==1 or n==0):
        return 1
    
    return n*factorial(n-1)
n=int(input("enter a number:"))

print(f"the factorial is :{factorial (n)}")

