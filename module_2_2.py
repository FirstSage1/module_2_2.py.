#Условная конструкция
#===========================
first=input("Введите цифру 1: ")
second=input("Введите цифру 2: ")
third=input("Введите цифру 3: 1")
print(first,second,third)
if first==second==third:
    print("3")
elif first == second or second == third or first == third:
        print("2")
else:
            print("0")
