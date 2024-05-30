from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QSpinBox,QLineEdit

import conexion
import var


class producto:
    @staticmethod
    def limpiarProductos():
        try:
            limpiar = [var.ui.leCodigoPrd,var.ui.leNombreProd,var.ui.sbStock]
            var.ui.lePrecio.setText("0.00")
            for i in limpiar:
                if isinstance(i, QLineEdit):
                    i.setText(None)
                elif isinstance(i, QSpinBox):
                    i.setValue(0)
        except Exception as error:
            print("Error al limpiar productos," ,error)

    def crearProducto(self):
        try:
            nombre_producto = var.ui.leNombreProd.text().strip()
            precio = var.ui.lePrecio.text().strip()
            stock = var.ui.sbStock.value()

            print(nombre_producto, precio, stock)

            if not nombre_producto or not precio or not stock:
                print("Faltan Datos")
            else:
                newproducto = [nombre_producto.title(), precio,int(stock)]
                conexion.conexion.crearProducto(newproducto)
                conexion.conexion.mostrarProducto()
        except Exception as error:
            print("Error al crear productos,", error)

    def cargarTablaProductos(registros):
        try:
            print(registros)
            var.ui.tabProd.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabProd.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla clientes:", error)
    @staticmethod
    def cargarProducto():
        try:
            producto.limpiarProductos()
            selected_row = var.ui.tabProd.currentRow()
            if selected_row != -1:
                id_producto = var.ui.tabProd.item(selected_row, 0).text()
                registro = conexion.conexion.oneproducto(id_producto)
                if registro:
                    datos = [var.ui.leCodigoPrd,var.ui.leNombreProd,var.ui.lePrecio,var.ui.sbStock]
                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))
                        elif isinstance(dato, QSpinBox):
                            dato.setValue(int(value))


            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)
    def modifProducto(self):
        try:
            producto = [
                var.ui.leCodigoPrd,
                var.ui.leNombreProd,
                var.ui.lePrecio,
                var.ui.sbStock
            ]
            modifProducto = []
            for i in producto:
                modifProducto.append(i.text().title())
            conexion.conexion.modficarProducto(modifProducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print(error," modif Producto")
    def eliminarProducto(self):
        try:
            idProducto = var.ui.leCodigoPrd.text().title()
            conexion.conexion.borrarProducto(idProducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print(error, " eliminar Producto")