import datetime

from PyQt6 import QtWidgets, QtSql

import cliente
import empleados
import producto
import var
import ventas


class conexion:
    """
    Clase para realizar las operaciones relacionadas con la base de datos
    """
    def conexion(self=None):
        """
        Metodo para conectarse a la base de datos
        :return:
        """
        var.bbdd = 'bbddR.db'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error conexion')
            return False
        else:
            print('base datos encontrada')
            return True

    @staticmethod
    def guardarCliente(newCliente):
        """
        MEtodo para guardar el cliente
        :param newCliente: datos del cliente
        :type newCliente: list
        :return:
        """
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
    def clienteEstaDadoDeBaja(codigo):
        """
        MEtodo par revisar si un cliente esta dado de baja
        :param codigo: id del cliente
        :return:
        """
        try:
            consulta = "SELECT COUNT(*) FROM cliente WHERE id_cliente = ? AND fecha_baja IS NOT NULL"
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.addBindValue(codigo)
            if query.exec() and query.next():
                return query.value(0) > 0
            else:
                return False
        except Exception as error:
            print("Error en clienteEstaDadoDeBaja:", error)
            return False

    @staticmethod
    def mostrarCliente():
        """
        Metodo para mostrar los clientes en la tabla de clientes
        :return:
        """
        try:
            if var.ui.cbHistorico.isChecked():
                consulta = 'select id_cliente, categoria, nombre, direccion, telefono, email, fecha_baja from cliente WHERE fecha_baja is not null'
            else:
                consulta = 'select id_cliente, categoria, nombre, direccion, telefono, email, fecha_baja from cliente'
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            else:
                print(query.lastError())
            cliente.cliente.cargarTablaClientes(registros)
        except Exception as error:
            print("Fallos en mostrar cliente ", error)

    @staticmethod
    def onecli(id):
        """
        Recupera los detalles de un cliente según el código proporcionado
        :param id: id del cliente
        :return:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM cliente WHERE id_cliente = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print("Error fichero cliente", err)

    def bajaCliente(codigo):
        """
        Metodo para dar de baja a un cliente
        :param codigo: id del cliente
        :return:
        """
        try:
            fecha = datetime.date.today()
            print(fecha)
            fecha = fecha.strftime('%d/%m/%Y')
            query = QtSql.QSqlQuery()
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

    def modifCliente(modifCliente):
        """
        MEtodo para modificar el cliente
        :param modifCliente: datos del cliente
        :type modifCliente: list
        :return:
        """
        try:
            consulta = ('update cliente set nombre=:nombre, apellido=:apellido, direccion=:direccion, '
                        'fecha_nacimiento=:fecha_nacimiento, telefono=:telefono, '
                        'email=:email, categoria=:categoria where id_cliente=:id_cliente')
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':id_cliente', int(modifCliente[0]))
            query.bindValue(':nombre', str(modifCliente[1]))
            query.bindValue(':apellido', str(modifCliente[2]))
            query.bindValue(':direccion', str(modifCliente[3]))
            query.bindValue(':fecha_nacimiento', str(modifCliente[4]))
            query.bindValue(':telefono', str(modifCliente[5]))
            query.bindValue(':email', str(modifCliente[6]))
            query.bindValue(':categoria', str(modifCliente[7]))
            print(modifCliente)
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print(error, " en modifCliente")

    def crearProducto(newproducto):
        """
        Metodo para insertar un nuevo porducto
        :param newproducto: datos del producto
        :type newproducto:list
        :return:
        """
        try:
            print(newproducto)
            query = QtSql.QSqlQuery()
            query.prepare(
                'INSERT INTO producto (nombre, precio, stock) '
                'VALUES(:nombre, :precio, :stock)')
            query.bindValue(':nombre', str(newproducto[0]))
            query.bindValue(':precio', str(newproducto[1]))
            query.bindValue(':stock', str(newproducto[2]))
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print("Error CrearProducto", error)

    @staticmethod
    def mostrarProducto():
        """
        Metodo para mostrar los datos del producto en la tabla producto
        :return: NONE
        """
        try:
            consulta = 'SELECT id_producto,nombre,precio,stock FROM producto '
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            registros = []
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            else:
                print(query.lastError())
            producto.producto.cargarTablaProductos(registros)
        except Exception as error:
            print("Error mostrarProducto", error)

    @staticmethod
    def oneproducto(id):
        """
        Recupera los detalles de un producto según el código proporcionado
        :param id: id del producto
        :return:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM producto WHERE id_producto = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print("Error fichero cliente", err)

    def modficarProducto(modicarProducto):
        """
        Metodo para modificar el producto
        :param modicarProducto: Datos del producto a modificar
        :type modicarProducto: list
        :return:
        """
        try:
            consulta = ('update producto set nombre=:nombre, precio=:precio, stock=:stock '
                        'where id_producto=:id_producto')  # Removed the comma before 'where'
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':id_producto', int(modicarProducto[0]))
            query.bindValue(':nombre', str(modicarProducto[1]))
            query.bindValue(':precio', str(modicarProducto[2]))
            query.bindValue(':stock', int(modicarProducto[3]))
            print(modicarProducto)
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print(error, " en modifCliente")

    def borrarProducto(idProducto):
        """
        Metodo para borrar un producto
        :param idProducto: id del producto
        :return:
        """
        try:
            consulta = 'DELETE FROM producto WHERE id_producto = :id_producto'
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':id_producto', int(idProducto))
            print(idProducto)
            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print(error, " en borrarProducto")

    def cargarCliente(self=None):
        """
        metodo para cargar el id del cliente y su nombre en la combobox de ventas
        :return:
        """
        try:
            var.ui.cbCliente.clear()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_cliente, nombre FROM cliente ORDER BY id_cliente')
            if query.exec():
                var.ui.cbCliente.addItem('')
                while query.next():
                    var.ui.cbCliente.addItem(f"{query.value(0)}. {query.value(1)}")
            else:
                raise Exception("Query execution failed")
        except Exception as error:
            print(f"Error loading clients: {error}")

    def cargarProducto(self=None):
        """
        metodo para cargar el id del producto y su nombre en la combobox de ventas
        :return:
        """
        try:
            var.ui.cbProducto.clear()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_producto, nombre FROM producto ORDER BY id_producto')
            if query.exec():
                var.ui.cbProducto.addItem('')
                while query.next():
                    var.ui.cbProducto.addItem(f"{query.value(0)}. {query.value(1)}")
            else:
                raise Exception("Query execution failed")
        except Exception as error:
            print(f"Error loading products: {error}")

    def altaFactura(registro):
        """
        metodo para dar de alta una factura de un cliente
        :param registro: datos (id del cliente y fecha de alta de la facura)
        :type registro: list
        :return:
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO facturas (idCliente, fecha) VALUES (:idCliente, :fecha)')
            query.bindValue(":idCliente", str(registro[0]))
            query.bindValue(":fecha", str(registro[1]))
            if query.exec():
                print("Factura guardada")
            else:
                raise Exception(query.lastError().text())
            conexion.cargarFactura()
        except Exception as error:
            print("Error al guardar factura:", error)

    @staticmethod
    def cargarFactura():
        """
        metodo para cargar los datos de todas las facturas de los clientes
        :return:
        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT idFactura, idCliente, fecha FROM facturas")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            ventas.ventas.cargarTablaFacturas(registros)
        except Exception as error:
            print("Error cargando tabla facturas:", error)

    @staticmethod
    def oneFactura(id):
        """
        Recupera los detalles de una factura según el código proporcionado
        :param id:  id del cliente
        :return:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM facturas WHERE idFactura = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(3):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print("Error fichero cliente", err)

    #############################################Ventas######################################

    def altaVenta(registro):
        """
        metodo para agregar una linea de venta a una factura
        :param registro: datos de la linea de venta
        :type registro: list
        :return:
        """
        try:
            idProducto = registro[1]
            print(idProducto)
            precio = conexion.getPrecio(idProducto)
            newReg = []
            for i in registro:
                newReg.append(i)
            newReg.append(precio)
            print(newReg)
            query = QtSql.QSqlQuery()
            query.prepare(
                'INSERT INTO venta (idFactura, idProducto,cantidad,precio) VALUES (:idFactura, :idProducto,:cantidad,:precio)')
            query.bindValue(":idFactura", int(newReg[0]))
            query.bindValue(":idProducto", int(newReg[1]))
            query.bindValue(":cantidad", int(newReg[2]))
            query.bindValue(":precio", str(newReg[3]))

            if query.exec():
                print("Venta guardada")
            else:
                raise Exception(query.lastError().text())
            conexion.cargarVenta(newReg[0])
        except Exception as error:
            print("Error al guardar factura:", error)

    def getPrecio(idProducto):
        """
        metodo para obtener el precio de un producto
        :param idProducto: id del producto
        :return:
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT precio FROM producto where id_producto = :id')
            query.bindValue(":id", str(idProducto))
            if query.exec():
                while query.next():
                    precio = query.value(0)
                    print(precio)
                    return precio
            print(query.lastError().text())
        except Exception as error:
            print("Error con el precio", error)

    @staticmethod
    def cargarVenta(dato):
        """
        metodo para cargar la venta en la tabla de lineas de venta
        :param dato: id de le factura
        :return:
        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT venta.idVenta, venta.idFactura, producto.nombre, venta.cantidad, venta.precio,(venta.cantidad * venta.precio) AS precio_total FROM venta INNER JOIN producto ON venta.idProducto = producto.id_producto Where idFactura = :dato")
            query.bindValue(':dato',dato)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            ventas.ventas.cargarTablaVentas(registros)
        except Exception as error:
            print("Error cargando tabla facturas:", error)

    @staticmethod
    def oneVenta(id):
        """
        Recupera los detalles de una linea de venta según el código proporcionado
        :param id:
        :return:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('''
                        SELECT idVenta, idFactura, idProducto, cantidad FROM venta WHERE idVenta = :id
                    ''')
            query.bindValue(':id', int(id))
            if query.exec():
                if query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print("Error oneFactura", err)

    def borrarLinea(id):
        """
        Metodo para borrar la linea de venta
        :param id: id de la linea de venta
        :return:
        """
        try:
            print(id)
            query = QtSql.QSqlQuery()
            query.prepare("delete from venta where idVenta = :id")
            query.bindValue(":id", int(id))
            if query.exec():
               print('Aviso', "producto eliminado correctamente")
            else:
                print('Aviso', "Error al borrar el producto")

        except Exception as error:
            print(error)

    def modifLinea(producto):
        """
        Metodo para modificar la linea de venta
        :param producto: datos del producto
        :type producto: list
        :return:
        """
        try:
            consulta = ('UPDATE venta '
                        'SET idProducto = :idProducto, cantidad = :cantidad '
                        'WHERE idVenta = :idVenta')

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':idVenta', int(producto[0]))
            query.bindValue(':idProducto', str(producto[1]))
            query.bindValue(':cantidad', int(producto[2]))
            print(producto)

            if query.exec():
                return True

            else:
                print(query.lastError().text())
                return False
        except Exception as error:
            print(error, " en modifLinea")
##############################################################Empleado##################################################
    def altaEmpleado(empleado):
        print(empleado)
        query = QtSql.QSqlQuery()
        query.prepare(
                'INSERT INTO empleado (nombre, departamento,telefono,turno) VALUES (:nombre, :departamento,:telefono,:turno)')
        query.bindValue(":nombre", str(empleado[0]))
        query.bindValue(":departamento", str(empleado[1]))
        query.bindValue(":telefono", int(empleado[2]))
        query.bindValue(":turno", str(empleado[3]))
        if query.exec():
            print("Empleado guardado")
            conexion.cargarEmpleado()
        else:
            raise Exception(query.lastError().text())

    @staticmethod
    def cargarEmpleado():
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare(
                "SELECT * FROM empleado")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            empleados.Empleado.cargarTablaEmpleados(registros)
        except Exception as error:
            print("Error cargando tabla facturas:", error)
    @staticmethod
    def oneEmpleado(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('''
                        SELECT id_empleado, nombre, departamento, telefono,turno FROM empleado WHERE id_empleado = :id
                    ''')
            query.bindValue(':id', int(id))
            if query.exec():
                if query.next():
                    for i in range(5):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as err:
            print("Error oneFactura", err)

    @staticmethod
    def empleadoEstaDadoDeBaja(codigo):

        try:
            consulta = "SELECT COUNT(*) FROM empleado WHERE id_empleado = ? AND fecha_baja IS NOT NULL"
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.addBindValue(codigo)
            if query.exec() and query.next():
                return query.value(0) > 0
            else:
                return False
        except Exception as error:
            print("Error en clienteEstaDadoDeBaja:", error)
            return False
    @staticmethod
    def bajaEmpleado(codigo):
        try:
            fecha = datetime.date.today()
            print(fecha)
            fecha = fecha.strftime('%d/%m/%Y')
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE empleado set fecha_baja = :fechabaja where id_empleado = :codigo")
            query.bindValue(':fechabaja', str(fecha))
            query.bindValue(':codigo', str(codigo))
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("empleado dado de baja")
                mbox.exec()
            else:
                print(query.lastError().text())
        except Exception as error:
            print("Error bajaCliente,", error)
    def modifEmpleado(empleado):
        print(empleado)
        query = QtSql.QSqlQuery()
        query.prepare(
                'UPDATE empleado set nombre = :nombre,departamento = :departamento,telefono = :telefono,turno=:turno WHERE id_empleado = :id_empleado')
        query.bindValue(":id_empleado",str(empleado[0]))
        query.bindValue(":nombre", str(empleado[1]))
        query.bindValue(":departamento", str(empleado[2]))
        query.bindValue(":telefono", int(empleado[3]))
        query.bindValue(":turno", str(empleado[4]))
        if query.exec():
            print("Empleado modificado")
            conexion.cargarEmpleado()
        else:
            raise Exception(query.lastError().text())