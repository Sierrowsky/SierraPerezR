from PyQt6 import QtWidgets, QtSql

import cliente
import var

class conexion:
    def conexion(self=None):
        var.bbdd='bbdd.sqlite'
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error conexion')
            return False
        else:
            print('base datos encontrada')
            return True
    def guardarCliente(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'INSERT INTO Cliente(nombre, apellido, direccion, fecha_nacimiento, telefono, email, categoria) '
                'VALUES(:nombre, :apellido, :direccion, :fecha_nacimiento, :telefono, :email, :categoria)')
            query.bindValue(':nombre', str(cliente[0]))
            query.bindValue(':apellido', str(cliente[1]))
            query.bindValue(':direccion', str(cliente[2]))
            query.bindValue(':fecha_nacimiento', str(cliente[3]))
            query.bindValue(':telefono', str(cliente[4]))
            query.bindValue(':email', str(cliente[5]))
            query.bindValue(':categoria', str(cliente[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Cliente dado de alta")
                mbox.exec()
            else:
                print(query.lastError().text())
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al guardar el cliente")
                mbox.exec()
        except Exception as error:
            print(error, "guardarCliente")