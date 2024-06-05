from datetime import datetime
import os
from PIL import Image

from PyQt6 import QtSql
from reportlab.pdfgen import canvas
import var

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
            var.report.drawString(165, 675, str(items[2]))
            var.report.drawString(250, 675, str(items[3]))
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
                        var.report.drawString(450, 90, 'Pagina Siguiente')
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
                    var.report.drawString(i + 195, j, str(query.value(3)))
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
                var.report.line(50, 800, 525, 800)
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
                var.report.line(50, 800, 525, 800)
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
            informes.topInforme(titulo)
            informes.footInforme(titulo)
            items = ['idProducto', 'Nombre', 'Precio', 'Stock']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(150, 675, str(items[1]))
            var.report.drawString(275, 675, str(items[2]))
            var.report.drawString(325, 675, str(items[3]))
            var.report.line(50, 670, 570, 670)
            # query
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * from producto order by id_producto')
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 90, 'Pagina Siguiente')
                        var.report.showPage()  # Crear una pagina nueva
                        informes.topInformeProducto(titulo)
                        informes.footInformeProducto(titulo)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(150, 675, str(items[1]))
                        var.report.drawString(275, 675, str(items[2]))
                        var.report.drawString(325, 675, str(items[3]))
                        var.report.line(50, 625, 570, 670)
                        i = 55
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 100, j, str(query.value(1)))
                    var.report.drawString(i + 220, j, str(query.value(2)))
                    var.report.drawString(i + 270, j, str(query.value(3)))
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