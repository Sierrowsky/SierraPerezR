from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

import conexion
import var


class producto:
    @staticmethod
    def limpiarProductos():
        try:
            limpiar = [var.ui.leCodigoPrd,var.ui.leNombreProd,var.ui.lePrecio,var.ui.leStock]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print("Error al limpiar productos," ,error)
    def crearProducto(self):
        try:
            producto = [var.ui.leNombreProd,var.ui.lePrecio,var.ui.leStock]
            newproducto = []
            for i in producto:
                newproducto.append(i.text().title())
            conexion.conexion.crearProducto(newproducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print("error al crear productos, ",error)
    def cargarTablaProductos(registros):
        try:
            print(registros)
            var.ui.tabProd.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabProd.setItem(index, col_index, item)
        except Exception as error:
            print("error en cargar tabla clientes:", error)
    @staticmethod
    def cargarProducto():
        try:
            producto.limpiarProductos()
            selected_row = var.ui.tabProd.currentRow()
            if selected_row != -1:
                id_producto = var.ui.tabProd.item(selected_row, 0).text()
                registro = conexion.conexion.oneproducto(id_producto)
                if registro:
                    datos = [var.ui.leCodigoPrd,var.ui.leNombreProd,var.ui.lePrecio,var.ui.leStock]
                    for dato, value in zip(datos, registro):
                        dato.setText(str(value))

            else:
                print("No row selected")
        except Exception as error:
            print("Error cargar Clientes: ", error)
    def modifProducto(self):
        try:
            producto = [
                var.ui.leCodigoPrd,
                var.ui.leNombreProd,
                var.ui.lePrecio,
                var.ui.leStock
            ]
            modifProducto = []
            for i in producto:
                modifProducto.append(i.text().title())
            conexion.conexion.modficarProducto(modifProducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print(error," modif Producto")
    def eliminarProducto(self):
        try:
            idProducto = var.ui.leCodigoPrd.text().title()
            conexion.conexion.borrarProducto(idProducto)
            conexion.conexion.mostrarProducto()
        except Exception as error:
            print(error, " eliminar Producto")