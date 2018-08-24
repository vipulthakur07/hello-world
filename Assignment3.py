age=int(input("enter age of person"))
sex=input("your sex?")
st=input("your marital status?")
if age>60 and age<20:
    print("error")
else:
    if sex=='female':
        print("you'll work only in urban areas.")
    else:
        if age>20 and age<40:
            print("you can work anywhere")
        else:
            print("you'll work only in urban areas.")
