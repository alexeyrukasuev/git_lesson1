#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Airplane():
    def __init__(self,name,cabin,distance,weigh,fuel,speed):
#Иниалиазиция атрибутов: наименование, загруженность салона , расстоянное расстояние полета в один конец , вес , уровень топлива,
# скорость самолета на высоте 5 км.
        self.name = name
        self.cabin = cabin
        self.distance = distance
        self.weigh = weigh
        self.fuel = fuel
        self.speed = speed
    
    def refuel(self):
        #Дозаправить
        print("Самолет", self.name + " необходимо дозаправить")

    def eat(self):
        #снабжение рационами питания
        print("Самолет", self.name + " необходимо снабдить рационами питания")
        
    def cleaning(self):
        #Убрать салон
        print("Салон самолета", self.name + " необходимо убрать салон")

    def chassis(self):
        #Проверить шасси
        print("Самолету", self.name + " необходимо проверить шасси")
        
    def bloker(self):
        #Провести проверку блокираторов
        print("Самолету", self.name + " необходимо провести проверку блокираторов")

    def glidepath(self):
        #Проверить глиссадное оборудование
        print("Самолету", self.name  +  " необходимо проверить глиссадное оборудование")
        
    def accessories(self):
        #Проверить все коплектующие 
        print("Самолету", self.name + " необходимо проверить все коплектующие")
        
class Frazil(Airplane):
    def sqr(self):
        if self.speed>= 800:
            print("невозможно")
        else:
            print("возможо")
        
airplane = Airplane("Airbus A380",525,15400,500,296,895)
airplane_2 = Frazil("Airbus A380",525,15400,500,296,895)
print("Наименование:",airplane.name)
print("Загруженность салона:",airplane.cabin, " человек.")
print("Посстоянное расстояние полета в один конец:",airplane.distance," км.")
print("Вес:",airplane.weigh," т.")
print("Уровень топлива:",airplane.fuel," т.")
print("Скорость самолета на высоте 5 км:",airplane.speed," км/ч.")
print("Образования наледи: ",airplane_2.sqr())
airplane.glidepath()

#Пример полиморфизма:
a=8+8
b= "8"+"8"
print(a)
print(b)


# In[ ]:




