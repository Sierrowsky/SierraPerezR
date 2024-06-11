from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QSpinBox,QLineEdit
from PyQt6 import QtWidgets

import conexion
import var


class producto:
    """
    Clase que maneja las operaciones relacionadas con los productos de la aplicacion
    """
    @staticmethod
    def limpiarProductos():
        """
        Limpiar los campos de entrada relacionados con los productos en la interfaz de usuario
        :return:
        """
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
        """
        Crea un producto con los datos proporcionados en los campos de entrada
        :return:
        """
        try:
            nombre_producto = var.ui.leNombreProd.text().strip()
            precio = var.ui.lePrecio.text().strip()
            stock = var.ui.sbStock.value()

            print(nombre_producto, precio, stock)

            if not nombre_producto or not precio or not stock:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Faltan Datos a introducir")
                mbox.exec()
            else:
                newproducto = [nombre_producto.title(), precio,int(stock)]
                conexion.conexion.crearProducto(newproducto)
                conexion.conexion.mostrarProducto()
        except Exception as error:
            print("Error al crear productos,", error)

    def cargarTablaProductos(registros):
        """
        Carga los registros de productos en la tabla de productos de la interfaz de usuario
        :param registros: Lista de registros
        :type registros: list
        :return: None
        """
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
        """
        Carga los datos de un producto seleccionado en la tabla de productos a los campos de entrada correspondientes.
        :return: None
        """
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
        """
        Modifica los datos del producto seleccionado con los nuevos datos proporcionados.
        :return: None
        """
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
        """
        Elimina el producto seleccionado y actualiza la tabla de productos.
        :return:  None
        """
        try:
            idProducto = var.ui.leCodigoPrd.text().title()
            conexion.conexion.borrarProducto(idProducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print(error, " eliminar Producto")