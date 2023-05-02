import pandas as pd
import random as random
datos=list(pd.read_csv('character_deaths.csv',header=0))

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem     


#class TablaPersonajes(QMainWindow):
#    def __init__(self, lista):
#        super().__init__(lista)
#        
#        self.table_widget = QTableWidget(self)
#        
#        for elemento in lista:
#            item = QTableWidgetItem(elemento)
#            self.table_widget.addItem(item)
#            
#        self.setWindowTitle("Personajes")
#        self.setCentralWidget(self.table_widget)
            
class ListaGUI(QMainWindow):
    def __init__(self, lista):
        super().__init__()
        
        # Crea el widget QListWidget y lo llena con los elementos de la lista
        self.list_widget = QListWidget(self)
        
        for elemento in lista:
            item = QListWidgetItem(elemento)
            self.list_widget.addItem(item)
        
        # Establece la ventana principal
        self.setWindowTitle("Elementos de la lista")
        self.setCentralWidget(self.list_widget)

        
if __name__ == '__main__':
    # Crea una lista de elementos de ejemplo
    lista_ejemplo = ["elemento 1", "elemento 2", "elemento 3"]
    #datos = datos[0]
    # Crea la aplicación y la ventana principal
    app = QApplication(sys.argv)
    ventana = ListaGUI(datos)
    ventana.show()
    
    # Ejecuta el bucle de eventos
    sys.exit(app.exec())