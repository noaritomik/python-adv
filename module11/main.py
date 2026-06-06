file_path = 'main.txt'
file = open(file_path,'r')

olti = file.read()
print(olti)
file.close()
'''with open('main.txt','w') as file:
    file.write('Sot eshte dite me diell')
    
'''


line = ['Hello World \n','Digital School \n']
with open('main.txt','w') as file:
    file.writelines(line)

with open('main.txt', 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)