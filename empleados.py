from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QLineEdit, QComboBox
from PyQt6 import QtWidgets

import conexion
import eventos
import var


class Empleado:
    @staticmethod
    def limpiarEmpleado():
        try:
            empleado = [var.ui.leTelefonoEmp, var.ui.leNombreEmp,var.ui.leCodigoEmp]
            var.ui.cbDepartamento.setCurrentIndex(0)
            for i in empleado:
                i.setText("")

        except Exception as error:
            print(error)
    def altaempleado(self):
        try:
            empleado=[var.ui.leNombreEmp.text().title(),var.ui.cbDepartamento.currentText().strip(),var.ui.leTelefonoEmp.text().title()]

            if var.ui.rbtTarde.isChecked():
                turno="Tarde"
                empleado.append(turno)
            elif var.ui.rbtManhana.isChecked():
                turno = "Mañana"
                empleado.append(turno)
            conexion.conexion.altaEmpleado(empleado)
        except Exception as error:
            print("Fallo en alta empleado", error)
    def cargarTablaEmpleados(registros):
        try:
            print(registros)
            var.ui.tblEmpleado.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tblEmpleado.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla clientes:", error)

    @staticmethod
    def cargarEmpleado():
        try:
            Empleado.limpiarEmpleado()
            selected_row = var.ui.tblEmpleado.currentRow()
            if selected_row != -1:
                idEmpleado = var.ui.tblEmpleado.item(selected_row, 0).text()
                registro = conexion.conexion.oneEmpleado(idEmpleado)
                if registro:
                    datos = [var.ui.leCodigoEmp, var.ui.leNombreEmp, var.ui.cbDepartamento, var.ui.leTelefonoEmp]
                    categoria = registro[4]
                    if categoria == "Tarde":
                        var.ui.rbtTarde.setChecked(True)
                    elif categoria == "Mañana":
                        var.ui.rbtManhana.setChecked(True)
                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))
                        elif isinstance(dato, QComboBox):
                            dato.setCurrentText(str(value))


                else:
                    print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)
    def bajaEmpleado(self):
        try:
            codigo = var.ui.leCodigoEmp.text()
            if conexion.conexion.empleadoEstaDadoDeBaja(codigo):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("empleado ya estaba dado de baja")
                mbox.exec()
                return
            else:
                conexion.conexion.bajaEmpleado(codigo)
            conexion.conexion.cargarEmpleado()
        except Exception as error:
            print("Error en baja empleado cliente ",error)

    def modifEmpleado(self):
        try:
            empleado=[var.ui.leCodigoEmp.text().title(),var.ui.leNombreEmp.text().title(),var.ui.cbDepartamento.currentText().strip(),var.ui.leTelefonoEmp.text().title()]

            if var.ui.rbtTarde.isChecked():
                turno="Tarde"
                empleado.append(turno)
            elif var.ui.rbtManhana.isChecked():
                turno = "Mañana"
                empleado.append(turno)
            conexion.conexion.modifEmpleado(empleado)
        except Exception as error:
            print("Fallo en modif empleado", error)

