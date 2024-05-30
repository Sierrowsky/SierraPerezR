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
                if i == 3 or i==5:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con tabCli", error)
    @staticmethod
    def resiceTabProd():
        try:
            header = var.ui.tabProd.horizontalHeader()
            for i in range(var.ui.tabProd.columnCount()):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con tabProd",error)