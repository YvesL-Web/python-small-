from PySide2 import QtWidgets
import currency_converter

class devise(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_default_values()
        self.setup_connection()

    #création des widgets
    def setup_ui(self):
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton(" Inverser Devises ")

        self.Layout.addWidget(self.cbb_devisesFrom)
        self.Layout.addWidget(self.spn_montant)
        self.Layout.addWidget(self.cbb_devisesTo)
        self.Layout.addWidget(self.spn_montantConverti)
        self.Layout.addWidget(self.btn_inverser)

    def set_default_values(self):
      #afficher les différentes devises dans notre fenêtre
      self.cbb_devisesFrom.addItems(sorted(self.c.currencies))
      self.cbb_devisesTo.addItems(sorted(self.c.currencies))
      self.cbb_devisesFrom.setCurrentText("EUR")
      self.cbb_devisesTo.setCurrentText("EUR")

      #le montant maximal qui peut être converti
      self.spn_montant.setRange(1,1000000)
      self.spn_montantConverti.setRange(1, 1000000)
      #les valeurs qui seront affichées par defaut
      self.spn_montantConverti.setValue(1)
      self.spn_montantConverti.setValue(1)

    def setup_connection(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devises)


    #on l'utilise quand on modifie les montants à convertiir
    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        try:
          resultat = self.c.convert(montant,devise_from,devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
          print("Impossible de convertir cette devise!")
        else :
          self.spn_montantConverti.setValue(resultat)

    def inverser_devises(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        # on inverse
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()


app = QtWidgets.QApplication([])
win = devise()
win.show()
app.exec_()
