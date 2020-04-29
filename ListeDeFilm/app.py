from PySide2 import QtWidgets, QtCore
from ListeDeFilm import film

class Interface(QtWidgets.QWidget):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("Film à Voir")
       self.setup_ui()
       self.populate_film()
       self.setup_connections()

    def setup_ui(self):
        self.Layout = QtWidgets.QVBoxLayout(self)

        self.LineEdit_titre = QtWidgets.QLineEdit()
        self.btn_AjoutFilm = QtWidgets.QPushButton("Ajouter un film")
        self.ListW_film = QtWidgets.QListWidget()
        self.ListW_film.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_suppFilm = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.Layout.addWidget(self.LineEdit_titre)
        self.Layout.addWidget(self.btn_AjoutFilm)
        self.Layout.addWidget(self.ListW_film)
        self.Layout.addWidget(self.btn_suppFilm)

    def setup_connections(self):
        self.btn_AjoutFilm.clicked.connect(self.add_movies)
        self.btn_suppFilm.clicked.connect(self.remove_movies)
        self.LineEdit_titre.returnPressed.connect(self.add_movies)

    def populate_film(self):
        movies = film.get_films()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            # lw_item.setData(QtCore.Qt.UserRole, movie)
            self.ListW_film.addItem(lw_item)

    def add_movies(self):
       titre = self.LineEdit_titre.text()
       if not titre :
           return False
       movie = film.Film(titre)
       resultat = movie.add_to_film()
       if resultat:
           lw_item = QtWidgets.QListWidgetItem(movie.title)
           lw_item.movie = movie
           # lw_item.setData(QtCore.Qt.UserRole, movie)
           self.ListW_film.addItem(lw_item)
           self.LineEdit_titre.setText("")

       self.LineEdit_titre.setText("")


    def remove_movies(self):
        for selected_item in self.ListW_film.selectedItems():
            movie = selected_item.movie
            # movie = selected_item.data(QtCore.Qt.UserRole)
            movie.del_to_film()
            self.ListW_film.takeItem(self.ListW_film.row(selected_item))


app = QtWidgets.QApplication([])
win = Interface()
win.show()
app.exec_()