# def print_usman():
#     print("learning with usman")
#     print("learning with usman")
#     print("learning with usman")
# print_usman() 

# #2
# def print_usman():
#     text = "learning with usman"
#     print(text)
#     print(text)
#     print(text)

   
# print_usman()    

# #3
# def print_usman(text):
#     print(text)
#     print(text)
#     print(text)

# print_usman("learning with usman")

#defining a function with if , elif and else statements
def school_calculator(age,text):
    if age==5:
        print("congratulations! hammad can join the school.")
    elif age>5:
        print("hammad should join the higher secondry school") 
    else:
        print("still hammad is a baby")

school_calculator(5,"hammad")              


#defining a function of future
def future_age(age):
    new_age=age+20
    return new_age
    print (new_age)

future_predicted_age= future_age(18)
print(future_predicted_age)