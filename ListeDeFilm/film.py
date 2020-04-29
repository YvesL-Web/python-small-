import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "Film.json")


def get_films():
    with open(DATA_FILE, 'r') as f:
        titre_film = json.load(f)

    film = [Film(films) for films in titre_film]
    return film


class Film:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_film(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def _write_film(self, films):
        with open(DATA_FILE, 'w') as f:
            json.dump(films, f,indent=4)

    def add_to_film(self):
        # on recupère la liste de film
        films = self._get_film()
        # on vérifie si le film est dans la liste
        if self.title not in films:
            films.append(self.title)
            self._write_film(films)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà dans la liste.")
            return False

    def del_to_film(self):
        # on recupère la liste
        films = self._get_film()
        # on vérifie si le film est dans la liste
        if self.title in films:
            films.remove(self.title)
            self._write_film(films)
