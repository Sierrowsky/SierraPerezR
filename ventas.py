from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtWidgets, QtCore, QtGui

import conexion
import var
class ventas:
    @staticmethod
    def limpiarVentas():
        try:
            venta = [var.ui.leFechaFactura,var.ui.leCodigoFactura]
            var.ui.cbCliente.clear()
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
            print("error en crear factuyra " , error)

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
"""
    @staticmethod
    def cargarProducto():
        try:
            ventas.limpiarVentas()
            selected_row = var.ui.tabProd.currentRow()
            if selected_row != -1:
                id_producto = var.ui.tabProd.item(selected_row, 0).text()
                registro = conexion.conexion.oneproducto(id_producto)
                if registro:
                    datos = [var.ui.leCodigoPrd, var.ui.leNombreProd, var.ui.lePrecio, var.ui.sbStock]
                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))
                        elif isinstance(dato, QSpinBox):
                            dato.setValue(int(value))


            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)"""