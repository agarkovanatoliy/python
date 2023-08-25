def add_person(person):
    data = open('handbook.txt', 'a', encoding='utf-8')
    data.writelines(person)
    data.writelines('\n')
    data.close()

def show_all():
    data = open ('handbook.txt', 'r', encoding = 'utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('handbook.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            if name in line.split():
                print(line)
                break
        else:
            print('Такого нету')

def index_line(name):
    with open('handbook.txt', 'rt', encoding = 'utf-8') as file:
        for index, line in enumerate(file):
            if name in line.split():
                return index
def contact_deletion(name):
    with open(r'handbook.txt', "r", encoding = 'utf-8') as file:
        lines = file.readlines()
        del lines[index_line(name)]
    with open(r'handbook.txt', "w", encoding = 'utf-8') as file:
        file.writelines(lines)


def contact_replacement(name, index, new_element):
    with open('handbook.txt', 'r', encoding ='utf-8') as data:
        for line in data:
            if name in line.split():
                temp = line.split()
                temp_line = line
                new_line = line.replace(temp[index], new_element)
                break
        else:
            print('Такого нету')
    with open('handbook.txt', 'r', encoding = 'utf-8') as data:
        old_data = data.read()
        new_data = old_data.replace(temp_line, new_line)

    with open('handbook.txt', 'w', encoding = 'utf-8') as data:
        data.write(new_data)




