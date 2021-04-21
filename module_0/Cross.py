#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

#Это интерактивная часть с вводом имен игроков, и созданием поля для игры.
print ("Привет, ну что поиграем?!", "Как тебя зовут?", sep='\n\n')
Player1_name=input()
print (Player1_name, "а как зовут твоего соперника?", sep=' ,')
Player2_name=input()
print ("Отлично, приступим!", '\n\n',Player1_name, "ставит крестики", "а", Player2_name, "ставит нолики вот в этом поле:")

Players_Field = "  1  2  3\n1__|__|__\n2__|__|__\n3  |  |  " #создаем игровое поле в виде строковой переменной

print(Players_Field)

#Здесь просто кидаем кости для случайного определения кто ходит первым (используем генератор случайных чисел от 0 до 1)
if np.random.sample()<0.5:
 print (Player1_name, "ходит первым", '\n',Player1_name,"Ваш ход, поставьте координаты по горизонтали и вертикали:")
 Player1_move=1
 Player2_move=0
else:
 print(Player2_name, "ходит первым",'\n',Player2_name,"Ваш ход, поставьте координаты по горизонтали и вертикали:")
 Player2_move=1
 Player1_move=0

#создаем список для ходов игроков (всего будет максимум 9-ть ходов, т.е. максимум 9-ть элементов списка)
move = []

for i in range(9):
 if (Players_Field[12]==Players_Field[15]==Players_Field[18]=="X" or Players_Field[12]==Players_Field[15]==Players_Field[18]=="O"
 or Players_Field[22]==Players_Field[25]==Players_Field[28]=="X" or Players_Field[22]==Players_Field[25]==Players_Field[28]=="O"
 or Players_Field[32]==Players_Field[35]==Players_Field[38]=="X" or Players_Field[32]==Players_Field[35]==Players_Field[38]=="O"
 or Players_Field[12]==Players_Field[22]==Players_Field[32]=="X" or Players_Field[12]==Players_Field[22]==Players_Field[32]=="O"
 or Players_Field[18]==Players_Field[28]==Players_Field[38]=="X" or Players_Field[18]==Players_Field[28]==Players_Field[38]=="O"
 or Players_Field[15]==Players_Field[25]==Players_Field[35]=="X" or Players_Field[15]==Players_Field[25]==Players_Field[35]=="O"
 or Players_Field[12]==Players_Field[25]==Players_Field[38]=="X" or Players_Field[12]==Players_Field[25]==Players_Field[38]=="O"
 or Players_Field[18]==Players_Field[25]==Players_Field[32]=="X" or Players_Field[18]==Players_Field[25]==Players_Field[32]=="O"):
  # объявление о завершении игры и победителя 
  print("Game over")

  if Player1_move ==0:
   print(Player1_name, " победил, он рулит")
  elif Player2_move ==0:
   print(Player2_name, " победил, он рулит")
  break #создали набор условий для прерывания цикла ходов, зменяющих пустые ячейки на Х или О
 
 move.append(input()) #игрок вводит координаты своего Х или О (например, 32 - ячейка 3 по горизонтали и 2 по вертикали, в котрой надо поставить Х или О)
 
 def Replace(Players_Field,x): #функция замены пустой ячейки в игровом поле на Х или О (аргумент x - это индекс строковой переменной, подстроку котрой надо поменять на Х или О)
  p=list(Players_Field)
  if Player1_move==1:
   p[x]="X"   
  else:
   p[x]="O"
  Players_Field="".join(map(str,p))
  return Players_Field
 #это собственно сама замена пустой ячейки в игровом поле на Х или О с помощью функции Replace после того, как игрок ввел координаты замены 
 if move[i] == "11":
  Players_Field = Replace(Players_Field,12)
 elif move[i] == "12":
  Players_Field = Replace(Players_Field,15)
 elif move[i] == "13":
  Players_Field = Replace(Players_Field,18)
 elif move[i] == "21":
  Players_Field = Replace(Players_Field,22)
 elif move[i] == "22":
  Players_Field = Replace(Players_Field,25)
 elif move[i] == "23":
  Players_Field = Replace(Players_Field,28)
 elif move[i] == "31":
  Players_Field = Replace(Players_Field,32)
 elif move[i] == "32":
  Players_Field = Replace(Players_Field,35)
 elif move[i] == "33":
  Players_Field = Replace(Players_Field,38)
 print (Players_Field,"Ходит следующий игрок",'\n\n')
 Player1_move,Player2_move = Player2_move,Player1_move # меняет очередность хода игроков в функции присваивания Х или О.

else:
    print(" Game over", '\n\n',"Ничья, мы крутые программисты!")


# In[ ]:




