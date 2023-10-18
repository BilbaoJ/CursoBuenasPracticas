from IServicioCorreo import IServicioCorreo


class ServicioCorreoNonThreadSafe(IServicioCorreo):

    def __int__(self):
        self.registroEventos = None

    def enviarCorreo(self, correo):
        print("Enviando correo no seguro para hilos...")
        if self.registroEventos is not None:
            self.notificarEvento("Se envio un correo con servicio no seguro para hilos")

    def listarCorreos(self, inicio, fin):
        print("Listando correos no seguro para hilos...")
        listaCorreos = ["correo1", "correo2", "correo3"]
        if self.registroEventos is not None:
            self.notificarEvento("Se listaron correos con servicio no seguro para hilos")
        return listaCorreos

    def dercargarCorreo(self, infoCorreo):
        print("Descargando correo...")
        correo = "Correo"
        if self.registroEventos is not None:
            self.notificarEvento("Se dercargo correo con servicio no seguro para hilos")
        return correo

    def notificarEvento(self, evento):
        self.registroEventos.registrarEvento(evento)

    def setRegistroEventos(self, registroEventos):
        self.registroEventos = registroEventos