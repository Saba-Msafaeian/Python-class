#age = input("please enter your age : ")
count = 0
while count < 4:
    age = input("please enter your age : ")
    try:
        age = int(age)
        if (age <= 0 or age >= 120):
            # print("age must between 1 to 120")
            raise Exception('age must between 1 to 120')
    except ValueError as e:
        print("Some thing wrong", e)
    except Exception as e:
        print(e)
    else:
        print('age imported succesfuly')
        break
    finally:
        print("-----------------------")
        count +=1
    
# x = 12
# try:
#     print(x)
# except:
#     print("x is not defined")
# else:
#     print('in the else estatment')
# finally:
#     print('in the filnally estatment')

