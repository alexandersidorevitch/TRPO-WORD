import os


class WorkWithFiles:
    """Работа с файлами"""

    def load_from_file(self, path):
        """
        Выгрузка из файла
        """
        if os.path.exists(path):
            with open(path, encoding='utf-8') as file:
                return file.read()
        else:
            print('Такого файла не существует')
            return None

    def insert_to_file(self, path, text):
        """
        Загрузка в файл
        """
        if text is None:
            print('Вы ничего не загрузили из файла')
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(text)
