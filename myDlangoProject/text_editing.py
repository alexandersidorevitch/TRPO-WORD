import re


class TextEditing:
    """Цвета
    Цвет	Текст	Фон
    Чёрный	30	40
    Красный	31	41
    Зелёный	32	42
    Жёлтый	33	43
    Синий	34	44
    Фиолетовый	35	45
    Бирюзовый	36	46
    Белый	37	47

    Эффекты
    Код	Значение
    0	Сброс к начальным значениям
    1	Жирный
    2	Блёклый
    3	Курсив
    4	Подчёркнутый
    5	Редкое мигание
    6	Частое мигание
    7	Смена цвета фона с цветом текста"""

    def searching_words(self, search_word, text):
        """
        Возврат позиций искомого слова
        """
        return map(lambda el: el.span(), re.finditer(search_word, text, re.IGNORECASE))

    def highlighting_text(self, search_word, text, higlight='\033[31m\033[1m\033[4m'):
        """
        Возрат текста с выделенными словами
        """
        new_text = ''
        last = 0
        for i, start in enumerate(self.searching_words(search_word, text), 1):
            start, end = start
            new_text += f'{text[last:start]} {higlight}{i}. {text[start:end]}\033[0m '
            last = end
        new_text += text[last:]
        return new_text

    def replace_text(self, search_word, repl, text, position):
        """
        Замена заданного слова на другое заданное слово
        """
        nabor = tuple(self.searching_words(search_word, text))
        if 1 <= position <= len(nabor):
            start, end = tuple(self.searching_words(search_word, text))[position - 1]
            new_text = text[:start]
            new_text += re.sub(search_word, repl, text[start:], count=1, flags=re.IGNORECASE)
            return new_text, ''
        else:
            return text, '\033[31m\033[1m\033[4mТакого индекса нет\033[0m'
