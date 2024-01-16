# Задание 2 - Импортируй нужные классы

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    
    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        return markup

# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Вопрос 1", 0, "Ответ1", "Ответ2"),
    Question("Вопрос 1", 1, "Ответ1", "Ответ2", "Ответ3", "Ответ4"),
    Question("Вопрос 1", 2, "Ответ1", "Ответ2", "Ответ3")
]
