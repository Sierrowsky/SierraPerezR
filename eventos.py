import sys

import var


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