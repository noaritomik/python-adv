age=20
print(age)
after_one_year = age + 1
print(after_one_year)
age_to_str =str(age)
print(age_to_str) #this will give an error because u cant sumn a str and int

#Int to float

mosha = 21
mosha_float=float(mosha)
print(mosha_float)

#implicit type conversion

num1=10
num2=3.14
rezultati=num1+num2
print(rezultati)

vjetet=25
message= "Une jam" + str(vjetet) + "vjeç"
print(message)


rroga1 =input("Shkruani rrogen e pare: ")
rroga2= input("Shkruani rrogen e dyte: ")
rroga1_float=float(rroga1)
rroga2_float=float(rroga2)
rroga_finale = rroga1_float + rroga2_float
print(rroga_finale)


try:
    result=10/0
except ZeroDivisionError:
    print("Nuk mund te ndani me zero")

fruits = {"apple": 5, "banana": 7, "orange": 3}
try:
    print(fruits["grape"])
    except KeyError:
        print("Ky frut nuk eshte ne liste"!)

name='John'
age=30
try:
    biografia=name+age
except Exception as e:
    print("Ka ndodhur nje gabum: " + str(e))
