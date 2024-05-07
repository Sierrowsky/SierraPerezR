import datetime

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
    @staticmethod
    def mostrarCliente():
        try:
            if var.ui.cbHistorico.isChecked():
                consulta= 'select id_cliente, categoria, nombre, direccion, telefono, email, fecha_baja from cliente WHERE fecha_baja is not null'
            else :
                consulta = 'select id_cliente, categoria, nombre, direccion, telefono, email, fecha_baja from cliente'
            registros=[]
            query=QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row=[query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            else:
                print(query.lastError())
            cliente.cliente.cargarTablaClientes(registros)
        except Exception as error:
            print("Fallos en mostrar cliente ", error)
    @staticmethod
    def onecli(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM cliente WHERE id_cliente = :id')
            query.bindValue(':id',int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print ("Error fichero cliente", err)
    def bajaCliente(codigo):
        try:
            fecha = datetime.date.today()
            print(fecha)
            fecha = fecha.strftime('%d/%m/%Y')
            query=QtSql.QSqlQuery()
            query.prepare("UPDATE cliente set fecha_baja = :fechabaja where id_cliente = :codigo")
            query.bindValue(':fechabaja', str(fecha))
            query.bindValue(':codigo', str(codigo))
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Cliente dado de baja")
                mbox.exec()
            else:
                print(query.lastError().text())
        except Exception as error:
            print("Error bajaCliente,", error)
    def crearProducto(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'INSERT INTO cliente(nombre, precio, stock) '
                'VALUES(:nombre, :precio, :stock)')
            query.bindValue(':nombre', str(producto[0]))
            query.bindValue(':precio', str(producto[1]))
            query.bindValue(':stock', str(producto[2]))
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print("Error CrearProducto",error)
    def mostrarProducto(self):
        try:
            registro=[]
        except Exception as error:
            print("Error mostrarProducto",error)