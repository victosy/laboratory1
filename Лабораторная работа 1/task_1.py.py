from typing import Union
import doctest

class Door:
    def __init__(self, height: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Дверь"

        :param height: Высота двери
        :param material: Материал двери

        Примеры:
        >>> door = Door(2100, "Дерево")
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота двери должна быть типа int или float")
        if not height > 0:
            raise ValueError("Высота двери должна быть положительным числом")
        self.height = height
        if not isinstance(material, str):
            raise TypeError("Материал двери должен быть типа str")
        if not material.strip():
            raise ValueError("Материал двери не может быть пустой строкой")
        self.material = material

    def is_door_useful(self) -> bool:
        """
        Проверяет, подходит ли дверь для прохода взрослого человека
        (минимальная рекомендуемая высота — 1800 мм)

        :return: True, если высота >= 1800 мм, иначе False

        Примеры:
        >>> door = Door(1500, "Пластик")
        >>> door.is_door_useful()
        False
        """
        ...

    def change_material(self, new_material: str) -> None:
        """
        Изменяет материал двери с валидацией

        :param new_material: Новый материал (непустая строка)

        Примеры:
        >>> door = Door(2100, "Дерево")
        >>> door.change_material("Стекло")
        """
        if not isinstance(new_material, str):
            raise TypeError("Новый материал должен быть типа str")
        if not new_material.strip():
            raise ValueError("Материал не может быть пустой строкой")
        ...

class Music:
    def __init__(self, name: str, author: str, genre: str):
        """
        Создание и подготовка к работе объекта "Музыкальное произведение"

        :param name: Название произведения (непустая строка)
        :param author: Исполнитель/композитор (непустая строка)
        :param genre: Музыкальный жанр (непустая строка)

        Примеры:
        >>> song = Music("Bohemian Rhapsody", "Queen", "Рок")
        """
        for param_name, param_value in [("name", name), ("author", author), ("genre", genre)]:
            if not isinstance(param_value, str):
                raise TypeError(f"Параметр '{param_name}' должен быть типа str")
            if not param_value.strip():
                raise ValueError(f"Параметр '{param_name}' не может быть пустой строкой")
        self.name = name
        self.author = author
        self.genre = genre

    def change_genre(self, new_genre: str) -> None:
        """
        Изменяет музыкальный жанр с валидацией

        :param new_genre: Новый жанр (непустая строка)

        Примеры:
        >>> song = Music("Все пройдет", "Михаил Боярский", "Поп")
        >>> song.change_genre("Альтернатива")
        """
        if not isinstance(new_genre, str):
            raise TypeError("Жанр должен быть типа str")
        if not new_genre.strip():
            raise ValueError("Жанр не может быть пустой строкой")
        ...

    def get_info(self) -> str:
        """
        Возвращает полную информацию о музыкальном произведении

        :return: Строка с названием, автором и жанром

        Примеры:
        >>> song = Music("Mockingbird", "Eminem", "Хип-хоп")
        >>> song.get_info()
        'Название: Mockingbird, Исполнитель: Eminem, Жанр: Хип-хоп'
        """
        ...

class Capybara:
    def __init__(self, cuteness_level: int, emotions: str):
        """
        Создание и подготовка к работе объекта "Капибара"

        :param cuteness_level: Уровень милоты (целое число от 1 до 10)
        :param emotions: Эмоциональное состояние (непустая строка)

        Примеры:
        >>> capy = Capybara(9, "Спокойствие")
        """
        if not isinstance(cuteness_level, int):
            raise TypeError("Уровень милоты должен быть типа int")
        if not 1 <= cuteness_level <= 10:
            raise ValueError("Уровень милоты должен быть в диапазоне от 1 до 10")
        self.cuteness_level = cuteness_level

        if not isinstance(emotions, str):
            raise TypeError("Эмоции должны быть типа str")
        if not emotions.strip():
            raise ValueError("Эмоции не могут быть пустой строкой")
        self.emotions = emotions

    def express_emotion(self) -> str:
        """
        Возвращает текущее эмоциональное состояние капибары

        :return: Строка с описанием эмоции

        Примеры:
        >>> capy = Capybara(10, "Радость")
        >>> capy.express_emotion()
        'Капибара чувствует: Радость'
        """
        ...

    def is_happy(self) -> bool:
        """
        Проверяет, счастлива ли капибара (эмоция содержит "радость" или "счастье", регистронезависимо)

        :return: True, если эмоция связана со счастьем, иначе False

        Примеры:
        >>> capy1 = Capybara(8, "Радость")
        >>> capy1.is_happy()
        True
        >>> capy2 = Capybara(6, "Грусть")
        >>> capy2.is_happy()
        False
        """

if __name__ == "__main__":
    doctest.testmod()
    pass
