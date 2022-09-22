#1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from array import array

n = int(input())
i = 2
while n > 1:
    while n % i == 0:
        print(i, end=' ')
        n //= i
    i += 1

#    2 - Задайте последовательность чисел. Напишите программу, 
#    которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

a = [1,2,2,2,3,4,5,5,5]
print(tuple(sorted(filter(lambda x : a.count(x) == 1, a))))
(1, 3, 4)

#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
#Нужно перезаписать файл.
#Пример:
#Ангела Меркель 5
#Андрей Валетов 5
#Фредди Меркури 3
#Анастасия Пономарева 4

#Программа выдаст:
#АНГЕЛА МЕРКЕЛЬ 5
#АНДРЕЙ ВАЛЕТОВ 5
#Фредди Меркури 3
#Анастасия Пономарева 4
file = open('home_ed.txt','w')
file.write('\
Ангела Меркель 5\n\
Андрей Валетов 5\n\
Фредди Меркури 3\n\
Анастасия Пономарева 4\n')
file.close()
arr=[]
with open(r'home_ed.txt','r') as file:
    for line in file:
        arr.append(line)
print(arr)
j=0
for i in arr:
    if i[-2]=='5':
        arr[j]=i.upper()
    j+=1
with open('home_ed.txt','w') as file:
    for line in arr:
        file.write(line)
print(arr)

#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
#При расшифровке происходит обратная операция. 
#К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
#а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.
def enigma(text,key)->str:
    """шифрование сдвигом букв"""
    world=[]
    for i in text:
        world.append(ord(i)+key)
    
    del text
    text=[]
    for i in world:
        text.append(chr(i))
    result =''.join(map(str,text))
    return result
def encryption(text,key)->str:
    """расшифровка с помощью сдвига и ключа"""
    world=[]
    for i in text:
        world.append(ord(i)-key)
    del text
    text=[]
    for i in world:
        text.append(chr(i))
    result=''.join(map(str,text))
    return result

string=input('шифр Цезаря\nВведите текст->')
string=enigma(string)
print(string)
with open('encr_text','w') as file2:
file2.write(string)
file2=open('encr_text')
string=file2.read()
file2.close
string=encryption(string)
print(string)

#5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
#Входные и выходные данные хранятся в отдельных текстовых файлах.
#файл первый:
#AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
#файл второй:
#сжатый текст.
# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def rle_encode(data):
   encoding = ''
   prev_char = ''
   count = 1
   if not data: 
       return ''
   for char in data:
      if char != prev_char:
          if prev_char:
             encoding += str(count) + prev_char
          count = 1 
          prev_char = char 
      else:
          count += 1
   else:
         encoding += str(count) + prev_char
   return encoding
def rle_decode(data):
   decode = ''
   count = '' 
   for char in data: 
      if char.isdigit(): 
         count += char
      else:
          decode += char * int(count)
          count = '' 
   return decode

val=rle_encode('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
with open('файл.txt','w') as file3:
    file3.write(val)
#print(val)
with open('файл.txt','r') as file3:
    cripto=file3.read()
with open('файл1.txt','w') as file3:
    file3.write(rle_decode(cripto))
