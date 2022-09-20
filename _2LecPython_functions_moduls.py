#‘айлы
#’ранение данных
#ѕередача данных в клиент-серверных проектах
#’ранение конфигов
#Ћогирование действий

#  ак работать с файлами:
#—в€зать файловую переменную с файлом,
#определив модификатор работы
#a Ц открытие дл€ добавлени€ данных
#r Ц открытие дл€ чтени€ данных
#w Ц открытие дл€ записи данных
#w+, r+

with open('file.txt', 'w') as data: #означает, что данную конструкцию воспринимаем как переменную дата
    #«ј –џ“»я ƒјЌЌџ’ ¬ Ё“ќћ —Ћ”„ј≈ Ѕ”ƒ≈“ ј¬“ќћј“»„≈— »ћ! «ƒ≈—№ Ќ≈ Ќ”∆Ќј ‘”Ќ ÷»я CLOSE
 data.write('line 1234\n')
 data.write('line 2445\n')

exit()
colors = ['red', 'green', 'blue123']
data = open('file.txt', 'a')
#data.writelines(colors) # разделителей не будет
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()

exit()
colours = ['red', 'green', 'blue3']
data = open('file.txt', 'w')#функи€ open, в file.txt мы передаем аргументы
data.writelines(colours)# разделителей не будет
data.close() #закрываем файл из-за утечек пам€ти



exit()#позвол€ет не проходить тот код, который дальше в скрипте написан
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()