#�����
#�������� ������
#�������� ������ � ������-��������� ��������
#�������� ��������
#����������� ��������

# ��� �������� � �������:
#������� �������� ���������� � ������,
#��������� ����������� ������
#a � �������� ��� ���������� ������
#r � �������� ��� ������ ������
#w � �������� ��� ������ ������
#w+, r+

with open('file.txt', 'w') as data: #��������, ��� ������ ����������� ������������ ��� ���������� ����
    #�������� ������ � ���� ������ ����� ��������������! ����� �� ����� ������� CLOSE
 data.write('line 1234\n')
 data.write('line 2445\n')

exit()
colors = ['red', 'green', 'blue123']
data = open('file.txt', 'a')
#data.writelines(colors) # ������������ �� �����
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()

exit()
colours = ['red', 'green', 'blue3']
data = open('file.txt', 'w')#������ open, � file.txt �� �������� ���������
data.writelines(colours)# ������������ �� �����
data.close() #��������� ���� ��-�� ������ ������



exit()#��������� �� ��������� ��� ���, ������� ������ � ������� �������
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()