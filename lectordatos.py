#Integrantes: 
#Javiera Cabezas
#Annais Caro
#Natalia Carrillanca
#Franco Comas
#Felipe Delgado

import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton

#Importa la base de datos y la lee
datos = pd.read_csv('character_deaths.csv')

class VentanaPersonajes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1350, 200)
        
        #Crea la tabla utilizando la primera linea como nombres para las columnas
        self.tablePersonajes = QTableWidget(1, datos.shape[1])
        self.tablePersonajes.setHorizontalHeaderLabels(datos.columns)
        self.mostrarPersonaje()
        
        #Crea el boton para cambiar de personaje y le asigna la accion
        self.botonAzar = QPushButton('Personaje al Azar')
        self.botonAzar.clicked.connect(self.mostrarPersonaje)
        layout = QVBoxLayout()
        layout.addWidget(self.tablePersonajes)
        layout.addWidget(self.botonAzar)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        
        self.setWindowTitle("Muertes de Personajes")
    
    #Define la funcion mostrar personaje   
    def mostrarPersonaje(self):
        fila = datos.sample(1)
        for j in range(datos.shape[1]):
            item = QTableWidgetItem(str(fila.iloc[0, j]))
            self.tablePersonajes.setItem(0, j, item)
        
        
app = QApplication(sys.argv)
ventana = VentanaPersonajes()
ventana.show()
sys.exit(app.exec())