from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtWidgets, QtCore
from PyQt6.QtCore import Qt
import time

import var
import conexion


class cliente:
    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + "cargar fecha clientes")

    def limpiar(self=None):
        try:
            limpiar = [var.ui.leCodigo, var.ui.leApellidos, var.ui.leNombre, var.ui.leDireccion,
                       var.ui.leFecha, var.ui.leTelefono, var.ui.leEmail]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print(error, "limpiar clientes")

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
            conexion.conexion.mostrarCliente()
        except Exception as error:
            print(error, " alta cliente")

    def cargarTablaClientes(registros):
        try:
            print(registros)
            var.ui.tabCli.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabCli.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla clientes:", error)

    @staticmethod
    def cargarClientes():
        try:
            cliente.limpiar()
            selected_row = var.ui.tabCli.currentRow()
            if selected_row != -1:
                cliente_id = var.ui.tabCli.item(selected_row, 0).text()
                registro = conexion.conexion.onecli(cliente_id)
                if registro:
                    datos = [var.ui.leCodigo, var.ui.leNombre, var.ui.leApellidos,
                             var.ui.leDireccion, var.ui.leFecha,
                             var.ui.leTelefono, var.ui.leEmail]
                    categoria = registro[7]
                    if categoria == "Particular":
                        var.ui.rbtParticular.setChecked(True)
                    elif categoria == "Empresario":
                        var.ui.rbtEmpresario.setChecked(True)
                    for dato, value in zip(datos, registro):
                        dato.setText(str(value))

            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)

    def bajaCliente(self):
        try:
            codigo = var.ui.leCodigo.text()
            conexion.conexion.bajaCliente(codigo)
            conexion.conexion.mostrarCliente()
        except Exception as error:
            print("Error en baja cliente cliente ",error)