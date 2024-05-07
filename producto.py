import conexion
import var


class producto:
    def limpiarProductos(self):
        try:
            limpiar = [var.ui.leCodigoProd,var.ui.leNombreProd,var.ui.lePrecio,var.ui.leStock]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print("Error al limpiar productos," ,error)
    def crearProducto(self):
        try:
            producto = [var.ui.leNombreProd,var.ui.lePrecio,var.ui.leStock]
            conexion.conexion.crearProducto(producto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print("error al crear productos, ",error)
