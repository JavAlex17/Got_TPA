import pandas as pd
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton


datos=pd.read_csv('character_deaths.csv')


class VentanaPersonajes(QMainWindow):
    def __init__(self, archivo):
        super().__init__()
        self.resize(1350,300)
        
        self.tablePersonajes = QTableWidget(archivo.shape[0], archivo.shape[1])
        self.tablePersonajes.setHorizontalHeaderLabels(archivo.columns)
        
        self.setWindowTitle("Muertes de Personajes")
        self.setCentralWidget(self.tablePersonajes)
        
        for i in range(archivo.shape[0]):
            for j in range(archivo.shape[1]):
                item = QTableWidgetItem(str(archivo.iloc[i,j]))
                self.tablePersonajes.setItem(i, j, item)


        
        
app = QApplication(sys.argv)
ventana = VentanaPersonajes(datos)
ventana.show()

sys.exit(app.exec())