first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x in y, first, second)))



from pprint import pprint

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for i in range(len(data_set)):
            file.write(str(data_set[i]))
            file.write('\n')
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        win = random.choice(self.words)
        return win


first_ball = MysticBall('Да', 'Нет', 'Наверное','верблюд')
print(first_ball())
print(first_ball())
print(first_ball())