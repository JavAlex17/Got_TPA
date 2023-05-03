import pandas as pd
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox, QGridLayout, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem


datos=list(pd.read_csv('character_deaths.csv',header=0))
print(datos[0:13])

class VentanaPersonajes(QMainWindow):
    def __init__(self, archivo):
        super().__init__()
        
        self.table_widget = QTableWidget(self)
        
        n = 0
        for linea in archivo:
            item = QTableWidgetItem(linea)
            self.table_widget.append(item)
            
        self.setWindowTitle("Muertes de Personajes")
        self.setCentralWidget(self.table_widget)
        
app = QApplication(sys.argv)
ventana = VentanaPersonajes(datos)
ventana.show()

sys.exit(app.exec())