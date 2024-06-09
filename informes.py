from datetime import datetime
import os
from PIL import Image

from PyQt6 import QtSql
from reportlab.pdfgen import canvas
import var
import conexion

"""
if rbtEmpresario.isChecked():
    select ....
elif rbtParticular.isChecked():
    select....
elif (rbtEmpresario.isChecked() && cbHistorico.isChecked() || rbtParticular.isChecked() && cbHistorico.isChecked())
    select *    
"""


class informes:
    @staticmethod
    def reportCLientes():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoClientes.pdf'
            var.report = canvas.Canvas('informesClientes/' + nombre)
            titulo = 'Listado Clientes'
            informes.topInforme(titulo)
            informes.footInforme(titulo)
            items = ['Codigo', 'Categoria', 'Nombre', 'Telefono', 'Direccion', 'Email']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))
            var.report.drawString(205, 675, str(items[2]))
            var.report.drawString(300, 675, str(items[3]))
            var.report.drawString(370, 675, str(items[4]))
            var.report.drawString(470, 675, str(items[5]))
            var.report.line(50, 670, 570, 670)
            # query
            query = QtSql.QSqlQuery()
            if var.ui.cbHistorico.isChecked():
                if var.ui.rbtEmpresario.isChecked():
                    query.prepare(
                        'SELECT id_cliente,categoria,nombre,telefono,direccion,email from cliente order by id_cliente')
                elif var.ui.rbtParticular.isChecked():
                    query.prepare(
                        'SELECT id_cliente,categoria,nombre,telefono,direccion,email from cliente order by id_cliente')
            else:  # cbHistorico is not checked
                if var.ui.rbtEmpresario.isChecked():
                    query.prepare(
                        "SELECT id_cliente,categoria,nombre,telefono,direccion,email from cliente WHERE categoria like 'Empresario' order by id_cliente")
                elif var.ui.rbtParticular.isChecked():
                    query.prepare(
                        "SELECT id_cliente,categoria,nombre,telefono,direccion,email from cliente WHERE categoria like 'Particular' order by id_cliente")

            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 70, 'Pagina Siguiente')
                        var.report.showPage()  # Crear una pagina nueva
                        informes.topInforme(titulo)
                        informes.footInforme(titulo)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(100, 675, str(items[1]))
                        var.report.drawString(165, 675, str(items[2]))
                        var.report.drawString(280, 675, str(items[3]))
                        var.report.drawString(380, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 625, 570, 670)
                        i = 55
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 245, j, str(query.value(3)))
                    var.report.drawString(i + 320, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j=j-25
            else:
                print(query.lastError())
            var.report.save()
            rootPath='.\\informesClientes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath,file))
        except Exception as error:
            print("Error listado clientes: " , error)

    def topInforme(titulo):
        try:
            ruta_logo = 'images/logo.png'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 570, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'GamesTeis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 570, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: GamesTeis@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)
    def footInforme(titulo):
        try:
            var.report.line(50,50,570,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

###################################################Report Productos######################################################

    def topInformeProducto(titulo):
        try:
            ruta_logo = 'images/logo.png'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 570, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'GamesTeis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 570, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: GamesTeis@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)
    def footInformeProducto(titulo):
        try:
            var.report.line(50,50,570,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    @staticmethod
    def reportProductos():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoProductos.pdf'
            var.report = canvas.Canvas('informesProductos/' + nombre)
            titulo = 'Listado Productos'
            informes.topInformeProducto(titulo)
            informes.footInformeProducto(titulo)
            items = ['idProducto', 'Nombre', 'Precio', 'Stock']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(250, 675, str(items[1]))
            var.report.drawString(400, 675, str(items[2]))
            var.report.drawString(500, 675, str(items[3]))
            var.report.line(50, 670, 570, 670)
            # query
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * from producto order by id_producto')
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 70, 'Pagina Siguiente')
                        var.report.showPage()  # Crear una pagina nueva
                        informes.topInformeProducto(titulo)
                        informes.footInformeProducto(titulo)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(250, 675, str(items[1]))
                        var.report.drawString(400, 675, str(items[2]))
                        var.report.drawString(500, 675, str(items[3]))
                        var.report.line(50, 625, 570, 670)
                        i = 55
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 100, j, str(query.value(1)))
                    var.report.drawString(i + 355, j, str(query.value(2)))
                    var.report.drawString(i + 455, j, str(query.value(3)))
                    j=j-25
            else:
                print(query.lastError())
            var.report.save()
            rootPath='.\\informesProductos'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath,file))
        except Exception as error:
            print("Error listado Producto: " , error)

#############################################REPORT FACTURAS #####################################################
    @staticmethod
    def reportFacturas():
        try:
            if var.ui.leCodigoFactura2.text() is str(""):
                print("Seleccione una factura")
            else:
                # Generate file name
                fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
                nombre = f"{fecha}_listadoFactura.pdf"
                var.report = canvas.Canvas(f'informesFacturas/{nombre}')
                titulo = 'Listado Productos'

                # Report headers and footers
                informes.topInformeFactura(titulo)
                informes.footInformeFactura(titulo)

                # Column titles
                items = ['IdVenta', 'IdFactura', 'NombreProducto', 'Cantidad', 'Precio','Total']
                var.report.setFont('Helvetica-Bold', size=10)
                var.report.drawString(50, 635, str(items[0]))
                var.report.drawString(100, 635, str(items[1]))
                var.report.drawString(275, 635, str(items[2]))
                var.report.drawString(400, 635, str(items[3]))
                var.report.drawString(470, 635, str(items[4]))
                var.report.drawString(520, 635, str(items[5]))
                var.report.line(50, 630, 570, 630)
                print(252)
                # Database query
                query = QtSql.QSqlQuery()

                query.prepare(
                    "SELECT venta.idVenta, venta.idFactura, producto.nombre, venta.cantidad, venta.precio, "
                    "(venta.cantidad * venta.precio) AS precio_total FROM venta "
                    "INNER JOIN producto ON venta.idProducto = producto.id_producto WHERE idFactura = :dato"
                )
                query.bindValue(":dato", var.ui.leCodigoFactura.text())  # You need to provide the value for :dato

                if query.exec():

                    i = 55
                    j = 615
                    while query.next():
                        if j <= 80:
                            var.report.drawString(450, 70, 'Pagina Siguiente')
                            var.report.showPage()  # Crear una pagina nueva
                            informes.topInformeFactura(titulo)
                            informes.footInformeFactura(titulo)
                            var.report.drawString(50, 615, str(items[0]))
                            var.report.drawString(100, 615, str(items[1]))
                            var.report.drawString(275, 615, str(items[2]))
                            var.report.drawString(400, 615, str(items[3]))
                            var.report.drawString(470, 615, str(items[4]))
                            var.report.drawString(520, 615, str(items[5]))
                            var.report.line(50, 625, 570, 670)
                            i = 55
                            j = 615
                        var.report.setFont('Helvetica', size=9)
                        var.report.drawString(i + 15, j, str(query.value(0)))
                        var.report.drawString(i + 50, j, str(query.value(1)))
                        var.report.drawString(i + 115, j, str(query.value(2)))
                        var.report.drawString(i + 355, j, str(query.value(3)))
                        var.report.drawString(i + 420, j, str(query.value(4)))
                        var.report.drawString(i + 465, j, str(query.value(5)))
                        j = j - 25
                else:
                    print(query.lastError().text())

                var.report.save()
                rootPath = './informesFacturas'
                for file in os.listdir(rootPath):
                    if file.endswith(nombre):
                        os.startfile(os.path.join(rootPath, file))
        except Exception as error:
            print("Error informesFacturas: ", error)

    @staticmethod
    def topInformeFactura(titulo):
        try:
            cliente = var.ui.cbCliente.currentText().strip()
            codCli = cliente.split(". ")[0]
            registro = conexion.conexion.onecli(codCli)
            ruta_logo = './images/logo.png'
            logo = Image.open(ruta_logo)
            fecha = datetime.today().strftime('%d/%m/%Y')

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 570, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'GamesTeis')
                var.report.drawString(240, 665, titulo)
                var.report.line(50, 660, 570, 660)

                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: GamesTeis@mail.com')

                var.report.setFont('Helvetica', size=8)
                var.report.drawString(290, 755, f'ID: {registro[0]}')
                var.report.drawString(290, 740, f'Nombre: {registro[1]}')
                var.report.drawString(290, 725, f'Categoria: {registro[7]}')
                var.report.drawString(290, 710, f'Email: {registro[6]}')
                var.report.drawString(290, 695, f'Teléfono: {registro[5]}')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe Factura:', error)

    @staticmethod
    def footInformeFactura(titulo):
        try:
            var.report.line(50, 100, 570, 100)
            var.report.setFont('Helvetica', size=11)
            var.report.drawString(430, 85, f'Subtotal:')
            var.report.drawString(430, 70, f'IVA:')
            var.report.drawString(430, 55, f'Total:')
            var.report.drawString(490, 85, var.ui.txtSubtotal.text())
            var.report.drawString(490, 70, var.ui.txtIVA.text())
            var.report.drawString(490, 55, var.ui.txtTotal.text())

            fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.line(50, 50, 570, 50)
            var.report.drawString(50, 40, fecha)
            var.report.drawString(250, 40, titulo)
            var.report.drawString(490, 40, f'Página {var.report.getPageNumber()}')
        except Exception as error:
            print('Error en pie informe Factura: ', error)