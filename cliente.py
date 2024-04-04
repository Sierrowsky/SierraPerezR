import var
class cliente:
    def cargarFecha(qDate):
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(error + " en clientes")
    def limpiar(self=None):
        try:
            limpiar = [var.ui.leCodigo,var.ui.leApellidos,var.ui.leNombre,var.ui.leDireccion,
                       var.ui.leFecha,var.ui.leTelefono,var.ui.leEmail]
            for i in limpiar:
                i.setText(None)
        except Exception as error:
            print (error , " Clientes")
