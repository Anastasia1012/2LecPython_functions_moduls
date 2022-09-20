#Файлы
#Хранение данных
#Передача данных в клиент-серверных проектах
#Хранение конфигов
#Логирование действий

# Как работать с файлами:
#Связать файловую переменную с файлом,
#определив модификатор работы
#a – открытие для добавления данных
#r – открытие для чтения данных
#w – открытие для записи данных
#w+, r+


#with open('file.txt', 'w') as data: #означает, что данную конструкцию воспринимаем как переменную дата
#    #ЗАКРЫТИЯ ДАННЫХ В ЭТОМ СЛУЧАЕ БУДЕТ АВТОМАТИЧЕСКИМ! ЗДЕСЬ НЕ НУЖНА ФУНКЦИЯ CLOSE
# data.write('line 1234\n')
# data.write('line 2445\n')


#colors = ['red', 'green', 'blue123']
#data = open('file.txt', 'a')
##data.writelines(colors) # разделителей не будет
#data.write('\nLINE 2\n')
#data.write('LINE 3\n')
#data.close()


#colours = ['red', 'green', 'blue3']
#data = open('file.txt', 'w')#функия open, в file.txt мы передаем аргументы
#data.writelines(colours)# разделителей не будет
#data.close() #закрываем файл из-за утечек памяти



#exit() позволяет не проходить тот код, который дальше в скрипте написан
#path = 'file.txt' #путь к папке
#data = open(path, 'r') #режим чтения
#for line in data:
#    print(line)#оператор пустой строки, задвоение пустой строки
#data.close()

#exit() #позволяет не проходить тот код, который дальше в скрипте написан, разрывать связь

#Функции
#Это фрагмент программы, используемый
#многократно
#def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

#Функция
#при которой можно использовать и символ, и число

def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5)) # !!!!!
#print(new_string('!')) # TypeError missing I required

def new_string(symbol, count=3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!'))  
print(new_string(4)) #12

#Функция
def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) #asdw
print(concatenatio('a', '1', 'd', '2')) #a1d2
#print(concatenatio('1', '2', '3', '4')) #TypeError

#Функция Рекурсии

def fib(n): #указали название, указали аргументы
    if n in [1, 2]:# если n содержится в списке , состоящем из элементов 1 и 2
        return 1
    else:
        return fib(n-1) + fib(n-2)#иначе возвращаем рекурсивный вызов для n-1 и n-2

list = [] 
for e in range(1, 10):#проделываем это среди 10 чисел
    list.append(fib(e))
    print(list)#1,1,2,3,5,8,13,21,24

#Функция Кортежи
# Это неизменяемый список
t = ()
print(type(t)) #tuple

t = ()
print(type(1,)) #tuple

t = ()
print(type(1)) #int

t = ()
print(type(28, 9, 1990)) #tuple

colourc = ['red', 'green', 'blue']
print(colours) #['red', 'green', 'blue']

t = tuple(colours)
print(t)#['red', 'green', 'blue']

#Например

a = (3, 5)
print(a) #3,4
print(a[0])#3
print(a[-1])#по аналогии работы со списками получаем последний элемент, то есть 4

# с циклом for
a = (3, 5)
for item in a:
    print(item)

#Можно распаковать кортеж в отдельные переменные

t  = tuple(['red', 'green', 'blue']) #достатчно сложная функия двух преобразований, мы создаем список, превращаем его в кортеж
#далее в три переменные


red, green, blue = t
print('r:{} g:{} blue:{}',format(red, green, blue)) #r: red g:green b:blue

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

#Словари
#Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \ 
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

#Можно обратиться только к values и появятся только значения {'↑', '←', '↓', '→'}

#Функция Множества

#Неупорядоченная совокупность элементов
a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

colors.add('red')
print(colors) # {'red', 'green', 'blue'}

colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}

colors.remove('red')
print(colors) # {'green', 'blue','gray'}

# colors.remove('red') # KeyError: 'red'

colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}

colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))

#Неизменяемое множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

#Списки

#Просто так копировать данные не нужно

#метод pop удаляет последний элемент
#метод insert помогает вставлять
#append добавляет в конец
