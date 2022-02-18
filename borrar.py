import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def ventana():
   app = QApplication(sys.argv)
   w = QWidget()
   boton = QPushButton(w)
   boton.setText("Guardar archivo")
   boton.move(100,50)
   boton.clicked.connect(mostrardialogo)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())

def mostrardialogo():
   dlg = QDialog()
   label = QLabel("Archivo guardado exitosamente")
   label.move(50,50)
   dlg.addWidget(label)
   dlg.setWindowTitle("Dialog") #9. PyQt5 — QDialog Class
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()
   

if __name__ == '__main__':
   ventana()
