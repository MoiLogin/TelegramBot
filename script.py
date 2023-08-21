#Dlina=float(input("Введите длинну:"))
#Schirina=float(input("Введите ширину:"))
#loshad=Dlina*Schirina
#print (f"Площадь равна:{Ploshad}")

# Your_age=int(input ("Сколько тебе лет?-"))
#
# if Your_age < 18:
#     print("Подрости сосунок")
#
# else:
#    print ("Залетай брат")

#print (round(3.1415
#mystr="hello World"
#print (len(mystr))
# s="Hello"
# #r=input()
# s = 'Hello World'
#print (s)
#print (s[:6]+ 'D' +s[7:])
#s=(s[:6]+ 'D' +s[7:])
#print (s)
#s= (input())
#print ("Вы ввели", len(s),"символов")
#s= ('HELLO')
#rint(s.isdigit())
#w='Ivanov Ivan Ivanovich'
#print (w.split('n'))
#s=('1,2,3,4,5,6,7,8,9')
#print (s.split(','))
#print ('     '.join(s))

#a = [
  #  ['Ренат', 'Раушанович', 45.12],
   # ['Эльвина', 'Нурулхаковна', 55.12],
   # ['Тимерлан', 'Ренатович', 65.12],
   # ]
#for name,mid_name,balance in a:
 #   text =f'''Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.'''
   # print(text)

#pi = 31.4159265
#print ("%.4e" % (pi))

# hours= (1)
# minutes= (2)
# ceconds= (3)
#
# #print("%02d:%02d:%02d" % (hours, minutes, ceconds))
#
# letters=[28, 'Lana', 'Xx', 'Anna','Miha']
# letters.append('e')
# letters.append('t')
# print (letters)
# print (len(letters))
# letters.append('i')
# print(letters)
# print(len(letters))
# print(letters [7])
# print(letters)
# letters.pop(1)
# print(letters)
# letters[1]=8
# print(letters)
# letters.sort()
# print(letters)
# letters.append('Igor')
# print(letters)
# letters.sort()
# print(letters)
# letters.extend(['Boris', 'Unis'])
# print(letters)
# letters.sort()
# print(letters)
# letters.insert(2,'Hren')
# print(letters)
# print((','.join (str(letters))))

# a=str ('1 1 2 3 5 8 13 21 34 55')
# L=a.split()
# L = (map(int, L))
# print(sum(L))

# Bakal=map(float,['1','2','3','4.5'])
# Vino= sum(Bakal)
# print(Vino)

# title='Avatar'
# # author='Djek'
# # year='65'
# # Book={'title': title, 'author': author, 'year': int(year)}
# # print(Book)


# ab1={'FIO':'AAA AAA', 'BAL':250}
# ab2={'FIO':'BBB BBB', 'BAL':150}
# ab3={'FIO':'CCC CCC', 'BAL':50}
#
# Spravka= [ab1, ab2, ab3]
# print(Spravka)
# ab4={'FIO':'DDD DDD', 'BAL':350}
# Spravka.append(ab4)
# print(Spravka)


# A=[1,1,2,2,3,3]
# B=set(A)
# C=list(set(B))
# print(C)

# t = input("Введите текст:")
#
# u = list(set(t))
#
# print("Количество уникальных символов: ", len(u))

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
#
# a = 5
# print(a)
# b = 3+2
# print(b)

# a='12345678'
# b=(map(int, a))
# print (b)
# b=list(map(int, a))
# print(b)
# print(b[0]%2==0)

# a=7
# b=9+a
# print("a=F(".b.")")



# cost = int(input('Цена'))
# if cost <= 2500:
#     print("Вы можете купить эти кроссовки!")
# else:
#     print("Увы, кроссовки слишком дорогие!")

# x=int(input('Введите температуру:'))
# if x>=15:
#     if x>=35:
#         print ('Оставайся дома')
#     else:
#         print('Погнали в труханах!')
# else:
#     if x<=-15:
#         print('Одеть зимнюю одежду')
#     else:
#         print('Холодноо!')
# Хорошо = False
# x=int(input('Введите температуру:'))
# if x>15 and not Хорошо:
#     print("Поити на улицу")
# else:
#     print('Не идти')

# one=12
# two=30
# result=int(input())
# if one % result==0 and two % result==0:
#     print('ok')
# else:
#     print()


# speed=int(input())

# if speed <=0:
#     print('Error')
# elif speed in [13,14,15,16]:
#     print('moderate')
# elif speed in [5,6,7,8]:
#     print('strong')
# elif speed in [9,10,11,12]:
#     print('hurricane')
# elif speed in [1,2,3,4]:
#     print('weak')

# if (1<-10 or 1<-1) and (1<2 or 1>15) :
#     print('Правильно')
# else:
#     print('Не правильно')

# temperature=int(input())
# Rain=True
# A='Сильные осадки'
#
# if 20<temperature<30:
#     print('Ok')
#     if Rain:
#         print('Надеть футболку шорты и дождевик')
#     else:
#         print('Футболку и шорты')
# else:
#     print('Не выходить')
#     if temperature>0:
#         if Rain:
#             print('Есть осадки')
#             if A:
#                 print('Надеть пальто')
#             else:
#                 print('Пальто и дождевик')
#         else:
#             print('пальто')
#     else:
#         print('Пуховик')

# temperature = int(input("Input temperature: "))
#
# #для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
#
# #если температура <0 то про дождь спрашивать бессмысленно
# if temperature > 0:
#    rainy = input("Is rainy: ") == "yes"
# #если идет дождь спросим насколько он серьезный
#    if rainy:
#        heavyRain = input("Is heavy rain: ") == "yes"
#
# if (temperature) > 20 and (temperature < 30) :
#    if rainy:
#        decision = "Взять футболку шорты и дождевик"
#    else:
#        decision = "Взять футболку и шорты"
# elif temperature > 0:
#    if rainy:
#        if heavyRain:
#            decision = "Взять пальто, резиновые сапоги и зонт"
#        else:
#            decision = "Взять пальто и дождевик"
#    else:
#        decision = "Взять пальто"
# else:
#    decision = "Взять пуховик"
#
# print(decision)


# n = 10
# while n>=4:
#     print(n)


# объявили функцию для подсчета количества символов в тексте!
# def Simvoli():
#     text=("""
#    У лукоморья дуб зелёный;
#    Златая цепь на дубе том:
#    И днём и ночью кот учёный
#    Всё ходит по цепи кругом;
#    """)
#     text=text.lower()
#     text=text.replace(' ', '')
#     text=text.replace('/n', '')
#
#     count={}
#     for char in text:
#         if char in count:
#             count[char]+=1
#         else:
#             count[char]=1
#     for char, cnt in count.items():
#         print(f'simvol  {char} vstrechaetsya {cnt} raz')
#
# Simvoli()


# def Slozhenie():
#     rezultat=2+2
#     print(rezultat)
# Slozhenie()



# def rec (x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print
#
# rec(5)



# def rec_sum(n):
#    if n == 1:                    #С помощью рекурсивной функции найдите сумму чисел от 1 до n.
#        return 1
#    return n + rec_sum(n - 1)
#
# print(rec_sum(5))



# def reverse_str(string):
#    if len(string) == 0:
#        return ''                                     #С помощью рекурсивной функции развернуть строку.
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('Test'))


# def taran(n):
#     if n<10:
#         return n                                        #Дано натуральное число N. Вычислите сумму его цифр.
#     else:
#         return n%10 + taran(n//10)
#
# print(taran(156))

# def run (start=1, step=1):
#     count=start
#     while True:
#         yield count
#         count+=step
#
# s=run()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# def Yan (start, end):
#     if start>end:
#         end, start=start,end
#     return sum(range(start, end+1))
# print(Yan(1,5))

# str='my TXT'
# str_Wil=iter(str)
#
# print(next(str_Wil))
# print(next(str_Wil))
# print(next(str_Wil))
# print(next(str_Wil))
# print(next(str_Wil))
# print(next(str_Wil))
# print(next(str_Wil))

# a=[1,2,3]
# def qwe (*args):
#     print(*args)
#
# print(*a,',',*a,',')

# def qwe ():
#     for i in range(10):
#         yield i
#         if i ==5:
#             raise StopIteration
# a=qwe()
#
# for _ in range(10):
#     print(next(a))

# import  time
# N=100
# import time
# def a (func):
#     def b ():
#         start=time.time()
#         func()
#         print= (time.time()-start)
#     return b
# @a
# def c():
#     spisok=(i ** 2 for i in range (1000000) if i %2 ==0)
#     print(spisok)
#
# c()

# Rain=True
# Small=True
#
# if Rain:
#     if Small:
#         print('Брать зонт')
#     else:
#         print('Сидеть дома')
# else:
#     print('Не брать зонт')



# name=input('введите название - ')
# if 'Arorat' in name:
#     print(name, 'подделка')
# else:
#     print(f'{name} не подделка')

# coast=5000
# if coast<=2500:
#     print('покупай')
# else:
#     print('дорого')

# class Cat:
#     def __init__(self,name, age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def x_name(self):
#         return self.name
#
#     def x_gender(self):
#         return (self.gender)
#
#     def x_age(self):
#         return self.age
#
# cat_1= Cat("Baron", "Boy",2)
# cat_2= Cat('Murka', 1, 'Gyrl')

# print(cat_1.x_name(),cat_1.x_gender(),cat_1.x_age())

# class Dog(Cat):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# dog_1=Dog("Rex",2)
#
# print(dog_1.self.name(), dog_1.self.age())
#
# # class Cat:
# #     def __init__(self,name):
# #         self.name=name
# #
# # class Dog(Cat):
# #     def __init__(self,name,gender,age):
# #         super().__init__(name)
# #         self.gender=gender
# #         self.age=age
# #
# #     def get_pet(self):
# #         return f'{self.name} {self.age}'
# #
# # dog_1=Dog('Tuzik', 'Boy', 2)
# # print(dog_1.get_pet())
#
# class Rectangle:
#     def __init__(self,a,b):
#         self.a = a
#        	self.b = b
#     def get_area(self):
#         return self.a * self.b
# class Square:
#     def __init__(self,a):
# 	    self.a = a
#     def get_area_square(self):
#         return self.a ** 2
#
# class Circle:
#     def __init__(self,a):
#         self.a=a
#     def get_area_circle (self):
#         return (self.a**2)*3.14

# class Daughter:
#     def __init__(self) -> None:
#         self.Level=0
#
#     def setLevel (self, Level):
#         self.Level=level
#
#     def getLevel (self):
#         return self.Level
#
# class Mom:
#     def __init__(self) -> None:
#         pass
#     def y (self, Daughter):
#         if Daughter.getLevel() >0:
#             Daughter.setLevel(0)
# if __name__=="__main__":
#     masha=Daughter
#     masha.setLevel(5)
#
#     mom=Mom()
#     mom.y(masha)
#     print(f"Mom moet Mashu")

