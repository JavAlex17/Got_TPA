import sys
import random
import pandas as pd
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton

datos = pd.read_csv('character_deaths.csv')

class VentanaPersonajes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1350, 300)

        self.tablePersonajes = QTableWidget(1, datos.shape[1])
        self.tablePersonajes.setHorizontalHeaderLabels(datos.columns)
        self.mostrarFila()

        self.btnCambiarFila = QPushButton('Personaje al Azar')
        self.btnCambiarFila.clicked.connect(self.mostrarFila)
        layout = QVBoxLayout()
        layout.addWidget(self.tablePersonajes)
        layout.addWidget(self.btnCambiarFila)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.setWindowTitle("Muertes de Personajes")
        
    def mostrarFila(self):
        fila = datos.sample(1)
        for j in range(datos.shape[1]):
            item = QTableWidgetItem(str(fila.iloc[0, j]))
            self.tablePersonajes.setItem(0, j, item)
        
        
app = QApplication(sys.argv)
ventana = VentanaPersonajes()
ventana.show()
sys.exit(app.exec())