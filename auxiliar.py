import cliente
from calendarWindow import *
from datetime import datetime
import sys,var
class Calendar(QtWidgets.QDialog):
    def __init__(self):
        bool= None
        super(Calendar,self).__init__()
        var.calendar=Ui_calendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        if var.ui.btnCalendar.clicked:
            var.calendar.calendari.setSelectedDate(QtCore.QDate(ano,mes,dia))
            var.calendar.calendari.clicked.connect(cliente.cliente.cargarFecha)