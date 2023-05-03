import pandas as pd
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget , QTableWidget, QTableWidgetItem


datos=list(pd.read_csv('character_deaths.csv',header=0))
print(datos[0:13])

class VentanaPersonajes(QMainWindow):
    def __init__(self, archivo):
        super().__init__()
        
        self.tablePersonajes = QTableWidget(10,13)
        
        self.tablePersonajes.setHorizontalHeaderLabels(['Name','Allegiances','Death Year','Book of Death','Death Chapter','Book Intro Chapter','Gender','Nobility','GoT','CoK','SoS','FfC','DwD'])
        
        
        #self.table_widget = QTableWidget(self)
            
        self.setWindowTitle("Muertes de Personajes")
        self.setCentralWidget(self.tablePersonajes)
        
app = QApplication(sys.argv)
ventana = VentanaPersonajes(datos)
ventana.show()

sys.exit(app.exec())