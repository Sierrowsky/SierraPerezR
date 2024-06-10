from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtWidgets, QtCore
from PyQt6.QtCore import Qt
import time

import var
import conexion


class cliente:
    def cargarFecha(qDate):
        """
        Carga la fecha seleccionada en el widget de fecha.

        :param qDate: Fecha seleccionada.
        :type qDate: QDate
        """

        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + "cargar fecha clientes")

    def limpiar(self=None):
        """
        Limpia los widgets del panel de clientes.

        Limpia los textos y checkboxes del panel de clientes.
        """

        try:
            limpiar = [var.ui.leCodigo, var.ui.leApellidos, var.ui.leNombre, var.ui.leDireccion,
                       var.ui.leFecha, var.ui.leTelefono, var.ui.leEmail]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print(error, "limpiar clientes")

    def altaCliente(self):
        """
        Da de alta a un cliente en la base de datos.

        Obtiene los datos del cliente desde los widgets, los valida y los guarda en la base de datos.
        """
        try:
            if var.ui.rbtEmpresario.isChecked():
                nombre = var.ui.leNombre.text().strip()
                direccion = var.ui.leNombre.text().strip()
                fecha = var.ui.leNombre.text().strip()
                telefono = var.ui.leNombre.text().strip()
                email = var.ui.leNombre.text().strip()
                if not nombre or direccion or fecha or telefono or email:
                    print("faltan datos")
                else:
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
                    categoria = "Empresario"

                    newCliente.append(categoria)
                    conexion.conexion.guardarCliente(newCliente)
                    conexion.conexion.mostrarCliente()
            elif var.ui.rbtParticular.isChecked():
                nombre = var.ui.leNombre.text().strip()
                apellidos = var.ui.leNombre.text().strip()
                direccion = var.ui.leNombre.text().strip()
                fecha = var.ui.leNombre.text().strip()
                telefono = var.ui.leNombre.text().strip()
                email = var.ui.leNombre.text().strip()
                if not nombre or apellidos or direccion or fecha or telefono or email:
                    print("faltan datos")
                else:
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
                    categoria = "Particular"

                    newCliente.append(categoria)
                    conexion.conexion.guardarCliente(newCliente)
                    conexion.conexion.mostrarCliente()

        except Exception as error:
            print(error, " alta cliente")

    def cargarTablaClientes(registros):
        """
        Carga los registros en la tabla de Clientes.

        :param registros: Lista de registros de Clientes.
        :type registros: list
        """
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
        """
        Carga un conductor seleccionado en el panel de Clientes.

        Obtiene los datos del Clientes seleccionado en la tabla y los carga en los widgets del panel.
        """
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
        """
        Da de baja a un cliente de la base de datos.

        Obtiene la fecha seleccionada en el widget, el ID del cliente y realiza la eliminación en la base de datos.
        """
        try:
            codigo = var.ui.leCodigo.text()
            if conexion.conexion.clienteEstaDadoDeBaja(codigo):
                print("El cliente ya está dado de baja.")
                return
            else:
                conexion.conexion.bajaCliente(codigo)
            conexion.conexion.mostrarCliente()
        except Exception as error:
            print("Error en baja cliente cliente ",error)
    def modifCliente(self):
        """
        Modifica los datos de un cliente en la base de datos.

        Obtiene los datos del panel, los valida y los guarda en la base de datos.
        """
        try:
            cliente = [
                var.ui.leCodigo,
                var.ui.leNombre,
                var.ui.leApellidos,
                var.ui.leDireccion,
                var.ui.leFecha,
                var.ui.leTelefono,
                var.ui.leEmail
            ]
            modifCliente = []
            for i in cliente:
                modifCliente.append(i.text().title())
            if var.ui.rbtEmpresario.isChecked():
                categoria = "Empresario"
            elif var.ui.rbtParticular.isChecked():
                categoria = "Particular"
            modifCliente.append(categoria)
            conexion.conexion.modifCliente(modifCliente)
            conexion.conexion.mostrarCliente()
        except Exception as error:
            print(error," modifCliente")