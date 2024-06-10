import var
import sys
from PyQt6 import QtWidgets

class Eventos():
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print(error, " Events")
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print(error, " Events")
    def abrirCalendarVentas(self):
        try:
            var.calendarVentas.show()
        except Exception as error:
            print(error, " eventos calendarVentas")
    @staticmethod
    def resiceTabCli():
        try:
            header = var.ui.tabCli.horizontalHeader()
            for i in range(var.ui.tabCli.columnCount()):
                if i==2 or i == 3 or i==5:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        except Exception as error:
            print("error con tabCli", error)
    @staticmethod
    def resicetabFactura():
        try:
            header = var.ui.tblFactura.horizontalHeader()
            for i in range(var.ui.tblFactura.columnCount()):
                if i ==2:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        except Exception as error:
            print ("Error resice tabFactura",error)
    @staticmethod
    def resicetblLineaFactura():
        try:
            header = var.ui.tblLineaFactura.horizontalHeader()
            for i in range(var.ui.tblLineaFactura.columnCount()):
                if i == 2:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        except Exception as error :
            print("error con tblLieneaVenta", error)
    @staticmethod
    def resiceTabProd():
        try:
            header = var.ui.tabProd.horizontalHeader()
            for i in range(var.ui.tabProd.columnCount()):
                if i == 1:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as error:
            print("error con tabProd",error)