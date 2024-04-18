from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtWidgets, QtCore

import var
import conexion
class cliente:
    def cargarFecha(qDate):
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + "cargar fecha clientes")
    def limpiar(self=None):
        try:
            limpiar = [var.ui.leCodigo,var.ui.leApellidos,var.ui.leNombre,var.ui.leDireccion,
                       var.ui.leFecha,var.ui.leTelefono,var.ui.leEmail]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print (error , "limpiar clientes")

    def altaCliente(self):
        try:
            cliente = [
                var.ui.leNombre,
                var.ui.leApellidos,
                var.ui.leDireccion,
                var.ui.leFecha,
                var.ui.leTelefono,
                var.ui.leEmail
            ]
            newCliente = []
            for i in cliente:
                newCliente.append(i.text().title())
            if var.ui.rbtEmpresario.isChecked():
                categoria = "Empresario"
            elif var.ui.rbtParticular.isChecked():
                categoria = "Particular"

            newCliente.append(categoria)
            print(newCliente)
            conexion.conexion.guardarCliente(newCliente)
        except Exception as error:
            print(error, " alta cliente")
    def cargarTablaClientes(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabCli.setRowCount(index+1)
                var.ui.tabCli.setItem(index,0,QTableWidgetItem(str(registro[0])))


