from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem, QLineEdit, QSpinBox, QComboBox
from PyQt6.uic.properties import QtWidgets, QtCore, QtGui

import conexion
import var


class ventas:
    @staticmethod
    def limpiarFacturas():
        try:
            venta = [var.ui.leFechaFactura, var.ui.leCodigoFactura]
            var.ui.cbCliente.setCurrentIndex(0)
            for i in venta:
                i.setText("")

        except Exception as error:
            print(error)

    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.leFechaFactura.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + "cargar fecha clientes")

    def crearFactura(self):
        try:
            fecha_factura = var.ui.leFechaFactura.text().strip()
            cliente = var.ui.cbCliente.currentText().strip()
            if not fecha_factura or not cliente:
                print("Faltan Datos")
            else:
                codCli = cliente.split(" ")[0]
                registro = [codCli, fecha_factura]
                conexion.conexion.altaFactura(registro)
        except Exception as error:
            print("error en crear factuyra ", error)

    def cargarTablaFacturas(registros):
        try:
            print(registros)
            var.ui.tblFactura.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tblFactura.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla facturas:", error)

    @staticmethod
    def cargarFactura():
        try:
            ventas.limpiarFacturas()
            selected_row = var.ui.tblFactura.currentRow()
            if selected_row != -1:
                idVenta = var.ui.tblFactura.item(selected_row, 0).text()
                registro = conexion.conexion.oneFactura(idVenta)
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
        try:
            codFac = var.ui.leCodigoFactura2.text().strip()
            idProducto = var.ui.cbProducto.currentText().strip()
            idProdu = idProducto.split(". ")[0]
            sbStock = var.ui.sbCantidad.value()
            if not codFac or not idProducto or sbStock <= 0:
                print("Faltan Datos")
            else:
                registro = [codFac, idProdu, sbStock]
                conexion.conexion.altaVenta(registro)
        except Exception as error:
            print("error en crear factuyra ", error)

    def cargarTablaVentas(registros):
        try:
            print(registros)
            var.ui.tblLineaFactura.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tblLineaFactura.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla facturas:", error)
    @  staticmethod
    def cargarVentas():
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