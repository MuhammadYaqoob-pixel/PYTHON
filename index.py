# for i in range(1, 6):
#     print(i)




# i=1
# while(i<7):
#     print(i)
#     i+=1



# l=[1, 3, "yaqoob", "hajjan"]
# i=0


# while(i<len(l)):

#       i+=1
# print(l)


# l=[22, 44, 44,77,88]

# for i in  l:
#    print(i)

# for i in range (100):
#     if(i==6):
#         break;
#     print(i)



# for i in range (100):
#     if(i==6):
#         continue;
#     print(i)


# n=int (input("enter any number:"))

# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
    
    #print(i)


# l=["yaqoob", "yasir ", "hajjan", "zameer"]

# for name in l:
#     if(name.startswith ("y")):print(f"hello {name}")


# n=int (input("enter any number:"))
# i=1
# while(i<11):
#     print(f"{n}*{i}={n*i}")
#     i+=1



# n=int (input("enter any number:"))

# for i in range(2, n):
#     if(n%i)==0:
#         print("number is not prime")
#         break
#     else:
# #         print("number is prime")
# n=int (input("enter any number:"))
# product=1

# for i in range(1, n+1):

#     product= product* i

#     print(f"the factorail of{n} is {product}")


n=int (input("enter any number:"))

for i in range(1, n+1):
    print(" "*(n-1), end="")
    print("*"* (2*i-1), end ="")
    print("")