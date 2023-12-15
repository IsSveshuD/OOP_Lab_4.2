#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Один тестовый вопрос представляет собой словарь Task со
# следующими ключами: вопрос,пять вариантов ответа, номер
# правильного ответа, начисляемые баллы за правильный ответ.
# Для моделирования набора тестовых вопросов реализовать класс
# TestContent,содержащий список тестовых вопросов. Реализовать
# методы добавления и удаления тестовых вопросов, а также метод
# доступа к тестовому заданию по его порядковому номеру в списке.
# В списке не должно быть повторяющихся вопросов. Реализовать операцию
# слияния двух тестовых наборов, операцию пересечения и вычисления разности.
# Дополнительно реализовать операцию генерации конкретного объекта
# Test объемом не более К вопросов из объекта типа TestContent.

class Test:
    def __init__(self, question, options, correct_answer, points):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.points = points


class TestContent:
    # Максимальный размер списка
    Max_size = 100

    def __init__(self, size=Max_size):
        self.questions = []
        self.size = size
        self.count = 0

    def add_question(self, question):
        if self.count < self.size:
            if question not in self.questions:
                self.questions.append(question)
                self.count += 1
            else:
                print("Вопрос уже есть в списке.")
        else:
            print("Достигнут максимально возможный размер списка.")

    def remove_question(self, question):
        if question in self.questions:
            self.questions.remove(question)
            self.count -= 1
        else:
            print("Вопрос не найден в списке.")

    def get_question(self, index):
        if 0 <= index - 1 < self.count:
            return self.questions[index - 1]
        else:
            print("Неверный номер вопроса.")

    def merge_tests(self, other_test):
        new_test = TestContent(size=self.size)
        new_test.questions = self.questions + other_test.questions
        new_test.count = len(new_test.questions)
        return new_test

    def intersect_tests(self, other_test):
        new_test = TestContent(size=self.size)
        new_test.questions = list(set(self.questions)
                                  & set(other_test.questions))
        new_test.count = len(new_test.questions)
        return new_test

    def diff_tests(self, other_test):
        new_test = TestContent(size=self.size)
        new_test.questions = list(set(self.questions)
                                  - set(other_test.questions))
        new_test.count = len(new_test.questions)
        return new_test

    def generate_test(self, k):
        import random
        if k > self.size - self.count:
            print("Запрошенное количество вопросов больше,"
                  " чем доступное количество для добавления.")
            return None
        else:
            selected_questions = random.sample(self.questions, k)
            new_test = TestContent(size=self.size)
            new_test.questions = selected_questions
            new_test.count = len(selected_questions)
            return new_test

    def size(self):
        return self.size


if __name__ == "__main__":
    q1 = Test("Какой язык программирования вы изучаете?",
              ["Python", "Java", "C++", "JavaScript", "Ruby"], 0, 10)
    q2 = Test("Что такое ООП?",
              ["Объектно-ориентированное программирование",
               "Объектно-ориентированный протокол",
               "Объективно-ориентированное программирование",
               "Объектно-ориентированный процессор",
               "Объектно-ориентированная парадигма"], 0, 15)

    test_content1 = TestContent(size=5)
    test_content1.add_question(q1)
    test_content1.add_question(q2)

    # Печать размера и количества элементов
    print(f"Размер: {test_content1.size}, \
          Количество элементов: {test_content1.count}")

    question3 = Test("Что такое GIT?",
                     ["Глобальный информационный трекер",
                      "Графический интернет-трансфер",
                      "Общий интернет-текст",
                      "GNU интерактивные инструменты",
                      "Объектно-ориентированное программирование"], 4, 20)
    test_content1.add_question(question3)

    # Пример добавления существующего вопроса
    test_content1.add_question(q2)

    # Пример получения вопроса по номеру
    get_q = test_content1.get_question(1)
    print(get_q.question)

    # Пример удаления вопроса
    test_content1.remove_question(q1)

    # Печать размера и количества элементов после изменений
    print(f"Размер: {test_content1.size}, \
          Количество элементов: {test_content1.count}")

    # Примеры слияния, пересечения и вычитания списков
    q4 = Test("Столица России?",
              ["Лондон", "Воронеж", "Москва",
               "Ставрополь", "Пекин"], 2, 50)
    test_content2 = TestContent(size=5)
    test_content2.add_question(q1)
    test_content2.add_question(q4)
    test_content1.merge_tests(test_content2)
    test_content1.intersect_tests(test_content2)
    test_content1.diff_tests(test_content2)
