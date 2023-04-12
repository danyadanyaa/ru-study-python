from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        filtered_movies = [
            movie
            for movie in list_of_movies
            if movie["rating_kinopoisk"]
            and float(movie["rating_kinopoisk"]) != 0
            and len(movie["country"].split(",")) >= 2
        ]
        return sum(map(lambda x: float(x["rating_kinopoisk"]), filtered_movies)) / len(
            filtered_movies
        )

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        filtered_films = [
            movie
            for movie in list_of_movies
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating
        ]
        count_in_names = map(lambda x: x["name"].count("и"), filtered_films)
        return sum(count_in_names)
