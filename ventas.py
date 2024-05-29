from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtWidgets, QtCore, QtGui

import conexion
import var
class ventas:
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