import cliente
import conexion
import eventos
import informes
import main
import mainWindow
import producto
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
        conexion.conexion.conexion()
        conexion.conexion.mostrarCliente()
        """
        Eventos Botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAlta.clicked.connect(cliente.cliente.altaCliente)
        var.ui.btnBaja.clicked.connect(cliente.cliente.bajaCliente)
        """    
        Eventos Botones
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionLimpiar_Panel.triggered.connect(cliente.cliente.limpiar)
        var.ui.actionLimpiar_Panel.triggered.connect(producto.producto.limpiarProductos)
        """
        Eventos Radio Button
        """
        var.ui.rbtEmpresario.toggled.connect(main.Main.toggleApellidos)

        """
        Eventos tabla
        """
        eventos.Eventos.resiceTabProd()
        eventos.Eventos.resiceTabCli()
        var.ui.tabCli.clicked.connect(cliente.cliente.cargarClientes)
        var.ui.cbHistorico.toggled.connect(conexion.conexion.mostrarCliente)

        """
        Eventos Tool Bar
        """
        var.ui.actionListado_Clientes.triggered.connect(informes.informes.reportCLientes)

    def toggleApellidos(checked):
        # Deshabilita el campo de entrada de apellidos si el radio button está marcado
        var.ui.leApellidos.setEnabled(not checked)
        var.ui.leApellidos.setText(None)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())