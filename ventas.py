from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem, QLineEdit, QSpinBox, QComboBox, QPushButton, QHeaderView

from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var


class ventas:
    """
    Clase que maneja las operaciones relacionadas con las ventas y facturas en la aplicación.
    """
    @staticmethod
    def limpiarFacturas():
        """
        Limpia los campos de entrada relacionados con las facturas en la interfaz de usuario.
        """
        try:
            venta = [var.ui.leFechaFactura, var.ui.leCodigoFactura]
            var.ui.cbCliente.setCurrentIndex(0)
            for i in venta:
                i.setText("")

        except Exception as error:
            print(error)

    def cargarFecha(qDate):
        """
        Carga la fecha seleccionada en el calendario al campo de fecha de factura.
        :param qDate: Fecha seleccionada.
        :type qDate: QDate
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.leFechaFactura.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + "cargar fecha clientes")

    def crearFactura(self):
        """
        Crea una nueva factura con los datos proporcionados en los campos de entrada.
        """
        try:
            fecha_factura = var.ui.leFechaFactura.text().strip()
            cliente = var.ui.cbCliente.currentText().strip()
            if not fecha_factura or not cliente:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Faltan Datos a introducir")
                mbox.exec()
            else:
                codCli = cliente.split(". ")[0]
                registro = [codCli, fecha_factura]
                conexion.conexion.altaFactura(registro)
        except Exception as error:
            print("error en crear factuyra ", error)

    def cargarTablaFacturas(registros):
        """
        Carga los registros de facturas en la tabla de facturas de la interfaz de usuario
        :param registros: Lista de registros de facturas
        :type registros: list
        """
        try:
            print(registros)
            var.ui.tblFactura.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    var.ui.tblFactura.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla facturas:", error)

    @staticmethod
    def cargarFactura():
        """
        Carga los datos de una factura seleccionada en la tabla de facturas a los campos de entrada correspondientes.
        """
        try:
            ventas.limpiarFacturas()
            selected_row = var.ui.tblFactura.currentRow()
            if selected_row != -1:
                idVenta = var.ui.tblFactura.item(selected_row, 0).text()
                registro = conexion.conexion.oneFactura(idVenta)
                print(registro)
                if registro:
                    datos = [var.ui.leCodigoFactura, var.ui.cbCliente, var.ui.leFechaFactura]
                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))
                        elif isinstance(dato, QComboBox):
                            dato.setCurrentIndex(int(value))
                Fact = var.ui.leCodigoFactura.text()
                var.ui.leCodigoFactura2.setText(Fact)
                conexion.conexion.cargarVenta(Fact)
            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)

    #############################################################VENTAS#########################################
    @staticmethod
    def limpiarVentas():
        """
        Limpia los campos de entrada relacionados con las ventas en la interfaz de usuario.
        """
        try:
            venta = [var.ui.leCodigoFactura2, var.ui.leCodigoVenta]
            var.ui.sbCantidad.setValue(0)
            var.ui.cbProducto.setCurrentIndex(0)
            for i in venta:
                i.setText("")

        except Exception as error:
            print(error)

    @staticmethod
    def crearVenta():
        """
        Crea una nueva venta con los datos proporcionados en los campos de entrada.
        """
        try:
            codFac = var.ui.leCodigoFactura2.text().strip()
            idProducto = var.ui.cbProducto.currentText().strip()
            idProdu = idProducto.split(". ")[0]
            sbStock = var.ui.sbCantidad.value()
            if not codFac or not idProducto or sbStock <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Faltan Datos a introducir")
                mbox.exec()
            else:
                registro = [codFac, idProdu, sbStock]
                conexion.conexion.altaVenta(registro)
        except Exception as error:
            print("error en crear factuyra ", error)

    def cargarTablaVentas(registros):
        """
        Carga los registros de ventas en la tabla de ventas de la interfaz de usuario.

        :param registros: Lista de registros de ventas.
        :type registros: list
        """
        try:
            subtotal = 0.0
            var.ui.tblLineaFactura.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    if col_index == 2:
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                        var.ui.tblLineaFactura.setItem(index, col_index, item)
                    else:
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                        var.ui.tblLineaFactura.setItem(index, col_index, item)
                totalViaje = round(float(registro[4]) * float(registro[3]), 2)
                subtotal = subtotal + totalViaje
                iva = subtotal * 0.21
                var.ui.txtSubtotal.setText(str('{:.2f}'.format(round(subtotal, 2))) + " €")
                var.ui.txtIVA.setText(str('{:.2f}'.format(round(iva, 2))) + " €")
                var.ui.txtTotal.setText(str('{:.2f}'.format(round(subtotal + iva, 2))) + " €")

        except Exception as error:
            print("error en cargar tabla facturas:", error)



    @  staticmethod
    def cargarVentas():
        """
        Carga los datos de una venta seleccionada en la tabla de ventas a los campos de entrada correspondientes.
        """
        try:
            ventas.limpiarVentas()
            selected_row = var.ui.tblLineaFactura.currentRow()
            if selected_row != -1:
                idVenta = var.ui.tblLineaFactura.item(selected_row, 0).text()
                registro = conexion.conexion.oneVenta(idVenta)
                if registro:
                    datos = [var.ui.leCodigoVenta, var.ui.leCodigoFactura2, var.ui.cbProducto, var.ui.sbCantidad]
                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))
                        elif isinstance(dato, QComboBox):
                            dato.setCurrentIndex(int(value))
                        elif isinstance(dato, QSpinBox):
                            dato.setValue(int(value))
            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)
    def eliminarVenta(self):
        """
        Elimina la venta seleccionada y actualiza la tabla de ventas.
        """
        try:
            conexion.conexion.borrarLinea(var.ui.leCodigoVenta.text().strip())
            conexion.conexion.cargarVenta(var.ui.leCodigoFactura2.text())
            ventas.limpiarVentas()
        except Exception as error:
            print("Error eliminar Venta: ", error)
    def modifVenta(self):
        """
        Modifica los datos de la venta seleccionada con los nuevos datos proporcionados.


        """
        try:
            idVenta = var.ui.leCodigoVenta.text().strip()
            idProducto = var.ui.cbProducto.currentText().strip()
            idProdu = idProducto.split(". ")[0]
            sbStock = var.ui.sbCantidad.value()
            producto = [
                idVenta,
                idProdu,
                sbStock,
            ]
            conexion.conexion.modifLinea(producto)
            conexion.conexion.cargarVenta(var.ui.leCodigoFactura2.text())
            ventas.limpiarVentas()
        except Exception as error:
            print("Error modificar Venta: ", error)
