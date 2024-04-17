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
                var.ui.leNombre.text(),
                var.ui.leApellidos.text(),
                var.ui.leDireccion.text(),
                var.ui.leFecha.text(),
                var.ui.leTelefono.text(),
                var.ui.leEmail.text()
            ]
            if var.ui.rbtEmpresario.isChecked():
                categoria = "Empresario"
            elif var.ui.rbtParticular.isChecked():
                categoria = "Particular"

            cliente.append(categoria)
            print(cliente)
            conexion.conexion.guardarCliente(cliente)
        except Exception as error:
            print(error, " alta cliente")

