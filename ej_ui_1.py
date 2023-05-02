from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(696, 524)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        VentanaPrincipal.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 681, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.texto = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(28)
        self.texto.setFont(font)
        self.texto.setObjectName("texto")
        self.verticalLayout.addWidget(self.texto)
        self.entrada = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.entrada.setObjectName("entrada")
        self.verticalLayout.addWidget(self.entrada)
        self.boton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.boton.setFont(font)
        self.boton.setObjectName("boton")
        self.verticalLayout.addWidget(self.boton)
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 22))
        self.menubar.setObjectName("menubar")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=VentanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        
        #Controlar evento desde Vista
        #self.boton.clicked.connect(self.saludar)

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)
        
    #def saludar(self):
    #    self.texto.setText(f"Bienvenido {self.entrada.text()}")
    #    self.entrada.setText("")

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Es la aplicación utilizando Qt Designer"))
        self.texto.setText(_translate("VentanaPrincipal", "Este es un texto de Bienvenida"))
        self.boton.setText(_translate("VentanaPrincipal", "OK"))