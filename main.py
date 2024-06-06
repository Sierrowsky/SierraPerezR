import cliente
import conexion
import eventos
import informes
import main
import mainWindow
import producto
import var, sys
import ventas
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
        conexion.conexion.mostrarProducto()
        conexion.conexion.cargarCliente()
        conexion.conexion.cargarProducto()
        conexion.conexion.cargarFactura()
        """
        Eventos Botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAlta.clicked.connect(cliente.cliente.altaCliente)
        var.ui.btnBaja.clicked.connect(cliente.cliente.bajaCliente)
        var.ui.btnCrearProd.clicked.connect(producto.producto.crearProducto)
        var.ui.btnModificar.clicked.connect(cliente.cliente.modifCliente)
        var.ui.btnModifProd.clicked.connect(producto.producto.modifProducto)
        var.ui.btnEliminarProd.clicked.connect(producto.producto.eliminarProducto)
        var.ui.btnFechaFactura.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnCrearFactura.clicked.connect(ventas.ventas.crearFactura)
        var.ui.btnAgregarLinea.clicked.connect(ventas.ventas.crearVenta)
        var.ui.btnEliminarLinea.clicked.connect(ventas.ventas.eliminarVenta)
        var.ui.btnModificarLinea.clicked.connect(ventas.ventas.modifVenta)
        var.ui.btnVerFactura.clicked.connect(informes.informes.reportFacturas)
        """    
        Eventos Botones
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionLimpiar_Panel.triggered.connect(cliente.cliente.limpiar)
        var.ui.actionLimpiar_Panel.triggered.connect(producto.producto.limpiarProductos)
        var.ui.actionLimpiar_Panel.triggered.connect(ventas.ventas.limpiarFacturas)
        var.ui.actionLimpiar_Panel.triggered.connect(ventas.ventas.limpiarVentas)

        """
        Eventos Radio Button
        """
        var.ui.rbtEmpresario.toggled.connect(main.Main.toggleApellidos)

        """
        Eventos tabla
        """
        eventos.Eventos.resiceTabProd()
        eventos.Eventos.resiceTabCli()
        eventos.Eventos.resicetblLineaFactura()
        var.ui.tabCli.clicked.connect(cliente.cliente.cargarClientes)
        var.ui.tabProd.clicked.connect(producto.producto.cargarProducto)
        var.ui.cbHistorico.toggled.connect(conexion.conexion.mostrarCliente)
        var.ui.tblFactura.clicked.connect(ventas.ventas.cargarFactura)
        var.ui.tblLineaFactura.clicked.connect(ventas.ventas.cargarVentas)

        """
        Eventos Tool Bar
        """
        var.ui.actionListado_Clientes.triggered.connect(informes.informes.reportCLientes)
        var.ui.actionListado_Productos.triggered.connect(informes.informes.reportProductos)

    def toggleApellidos(checked):
        # Deshabilita el campo de entrada de apellidos si el radio button está marcado
        var.ui.leApellidos.setEnabled(not checked)
        var.ui.leApellidos.setText(None)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())