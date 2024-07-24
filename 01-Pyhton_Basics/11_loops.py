# # while and For loops
# #while loop
x=0
while (x<5):
    print(x)
    x=x+1


# # for loop
for x in range(5,10):
    print(x)


#Array
days =("mon","tue","wed","thu","fri","sat","sun")
for d in days:
    print(d)
    if (d=="fri"):break #loops stop
    if (d=="fri"):continue #skips d
    print(d)