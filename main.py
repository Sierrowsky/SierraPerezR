import cliente
import eventos
import var, sys
from mainWindow import *
from auxiliar import *
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        #Configuracion de la interfaz de usuario
        var.ui= Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()

        """
        Eventos Botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        """
        Eventos Botones
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionLimpiar_Panel.triggered.connect(cliente.cliente.limpiar)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())