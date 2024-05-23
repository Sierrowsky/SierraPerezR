from PyQt6.uic.properties import QtWidgets, QtCore

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
            cliente=  var.ui.cbCliente.currentText()
            codCli = cliente.split(" ")[0]
            registro = [codCli,var.ui.leFechaFactura.text()]
            conexion.conexion.altaFactura(registro)
        except Exception as error:
            print("error en crear factuyra " , error)

    def cargarTablaFacturas(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tblFactura.setRowCount(index + 1)
                var.ui.tblFactura.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tblFactura.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tblFactura.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tblFactura.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tblFactura.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tblFactura.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablafacturas", error)
        except Exception as error:
            print("Error en cargarTablaFacturas:", error)

