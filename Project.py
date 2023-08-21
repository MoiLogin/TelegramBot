# from script import Rectangle
#
# rect_1 = Rectangle(3,4)
# rect_2 = Rectangle(12,5)
# #вывод площади наших двух прямоугольников
# print(rect_1.get_area())
# print(rect_2.get_area())
#
# from script import Rectangle, Square
#
# #далее создаем два прямоугольника
#
# rect_1 = Rectangle(3,4)
# rect_2 = Rectangle(12,5)
# #вывод площади наших двух прямоугольников
# print(rect_1.get_area())
# print(rect_2.get_area())
#
# square_1 = Square(5)
# square_2 = Square(10)
#
# print(square_1.get_area_square(),
#       square_2.get_area_square())
#
# figures=[rect_1,rect_2,square_1,square_2]
#
# print(square_1.get_area_square(),
#       square_2.get_area_square())
#
# figures = [rect_1, rect_2, square_1, square_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     else:
#         print(figure.get_area())
#
# from script import Rectangle, Square, Circle
#
# rect_1 = Rectangle(3,4)
# rect_2 = Rectangle(12,5)
# square_1 = Square(5)
# square_2 = Square(10)
# circle_1=Circle(2)
# circle_2=Circle(3)
# figures = [rect_1, rect_2, square_1, square_2,circle_1,circle_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     elif isinstance(figure, Rectangle):
#         print(figure.get_area())
#     else:
#         print(figure.get_area_ci)
#
# class Daughter:
#     def __init__(self) -> None:
#         self.Level=0
#
#     def setLevel (self, Level):
#         self.Level=Level
#
#     def getLevel (self):
#         return self.Level
#
# class Mom:
#     def __init__(self) -> None:
#         pass
#     def moet (self, Daughter):
#         if Daughter.getLevel() >0:
#             Daughter.setLevel(0)
# if __name__=="__main__":
#     masha=Daughter()
#     masha.setLevel(5)
#
#     mom=Mom()
#     mom.moet(masha)
#     print(f"Mom moet Mashu")

# class  PersionCat:
#     breed='persian'
#     age=12.0
#
# class SiberianCat:
#     breed='siberian'
#     age=0.5
#
# class BengalCat:
#     bread='Bengal'
#     age=2
#
# tom=PersionCat()
# garfield=SiberianCat()
# maxim=BengalCat()

# print(type(tom), type(garfield), sep='\n')
# print(isinstance(tom, SiberianCat))

# class Person:
#     age=16
#     name='Max'
#
# # print(getattr(Person, 'x', 'Impos'))
# # setattr(Person, 'name', 'Liza')
# # print(Person.name)
# class D:
#     x=14
#     y=15.6
# del D.x
# print(getattr(D,'x','impass'))
# delattr(D,'y')

# class Person:
#
#     def __init__(self, age:int, name:str):
#         self.age=age
#         self.name=name
#
# p1=Person(15, 'Terovor')
# p2=Person(22, 'Liza')
# print(p1.name, p2.name)

# class KogoMoet:
#     def __init__(self) -> None:
#         self.dLevel=0
#
#     def setPoh(self, level):
#         self.setdLevel=level
#
#     def getPoh(self):
#         return self.setdLevel
#
# class KtoMoet:
#     def __init__(self)->None:
#         pass
#
#     def X(self, KogoMoet):
#         if KogoMoet.getPoh()>0:
#             KogoMoet.setPoh(0)
#
# if __name__=="__main__":
#     masha=KogoMoet()
#     masha.setPoh(1)
#
#     mom=KtoMoet()
#     mom.X(masha)
#
#     print(f'Mom washes Masha')

# import pygame
# import sys
# from Gan import Gun
#
# def run():
#     pygame.init()
#     screen=pygame.display.set_mode((1200,800))
#     pygame.display .set_caption('Космические защитники')
#     bg_color=(0,0,0)
#     gun=Gun(screen)
#     while True:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 sys.exit()
#         screen.fill(bg_color)
#         gun.output()
#         pygame.display.flip()
# run()
#
#










