import os

from buffer import Buffer
from text_editing import TextEditing
from work_with_files import WorkWithFiles




class Main(WorkWithFiles, Buffer, TextEditing):
    """Класс для задание по ТРПО (поиск и замена)"""
    def __init__(self):
        Buffer.__init__(self)
        self.text = None

    def run(self):
        while True:
            print('\n1. Загрузка из файла')
            print('2. Загрузка в файл')
            print('3. Найти и заменить')
            print('4. Отмена последней операции')
            print('5. Отмена последней отменённой операции')
            print('6. Вывод сохранённого текста\n')

            try:
                input_number = int(input())
            except:
                print('А теперь давай нормально...')
                continue

            if input_number == 1:
                self.text = self.load_from_file(f'{input("Введите название файла: ")}.txt')
                self.append_to_history(self.text)
            elif input_number == 2:
                self.insert_to_file(f'{input("Введите название файла: ")}.txt', self.text)
            elif input_number == 3:

                if self.text is None:
                    print('Загрузите информацию из файла!')
                else:
                    print('1.Воспринимать введенное слово как отдельное слово')
                    print('2.Воспринимать введенное слово как кусок от слова')

                    try:
                        input_number = int(input())
                    except:
                        print('А теперь давай нормально...')
                        continue

                    if input_number == 1:
                        word = fr'\b{input("Введите слово: ")}\b'
                    elif input_number == 2:
                        word = fr'{input("Введите слово: ")}'
                    else:
                        print('Не верный ввод')
                        continue

                    highlighting_text = self.highlighting_text(word, self.text)
                    print(f'{highlighting_text}\n')
                    if highlighting_text == self.text:
                        print('Слово не найдено')
                        continue
                    print('Заменить какое-нибудь слово?')

                    input_number = input()

                    if 'да' == input_number.lower():
                        try:
                            self.text, message = self.replace_text(word, input('На какое словов заменить?\n'), self.text,
                                                          int(input('Под каким номером находиться слово?\n')))
                            if message:
                                self.append_to_history(self.text)
                            print(self.text)
                            print(message)
                        except:
                            print('Введите целое число!!')
                    elif 'нет' == input_number.lower():
                        print('Ну и ладно')
                    else:
                        print('Ничего не понял, но оооооочень интересно')
            elif input_number == 4:
                new_text = self.ctrl_z()

                if new_text is None:
                    pass
                else:
                    self.text = new_text
            elif input_number == 5:
                new_text = self.shift_ctrl_z()

                if new_text is None:
                    pass
                else:
                    self.text = new_text
            elif input_number == 6:
                print(self.text)
            else:
                print('Все фигня, давай по новой')


Class = Main()
Class.run()
