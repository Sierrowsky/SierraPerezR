from PyQt6 import QtWidgets, QtSql

import cliente
import var

class conexion:
    def conexion(self=None):
        var.bbdd='bbddR.db'
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error conexion')
            return False
        else:
            print('base datos encontrada')
            return True
    @staticmethod
    def guardarCliente(newCliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'INSERT INTO cliente(nombre, apellido, direccion, fecha_nacimiento, telefono, email, categoria) '
                'VALUES(:nombre, :apellido, :direccion, :fecha_nacimiento, :telefono, :email, :categoria)')
            query.bindValue(':nombre', str(newCliente[0]))
            query.bindValue(':apellido', str(newCliente[1]))
            query.bindValue(':direccion', str(newCliente[2]))
            query.bindValue(':fecha_nacimiento', str(newCliente[3]))
            query.bindValue(':telefono', str(newCliente[4]))
            query.bindValue(':email', str(newCliente[5]))
            query.bindValue(':categoria', str(newCliente[6]))
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print(error, " en guardarCliente")
    def mostrarCliente(self=None):
        try:
            registros=[]
            query=QtSql.QSqlQuery()
            query.prepare('select categoria, nombre, direccion, telefono, email from cliente')
            if query.exec():
                while query.next():
                    row=[query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            if registros:

