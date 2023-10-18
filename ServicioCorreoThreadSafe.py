from IServicioCorreo import IServicioCorreo


class ServicioCorreoThreadSafe(IServicioCorreo):

    def __int__(self):
        self.registroEventos = None
        self.limiteIntentos = 3

    def enviarCorreo(self, correo):
        print("Enviando correo seguro para hilos...")
        if self.registroEventos is not None:
            self.notificarEvento("Se envio un correo con servicio seguro para hilos")

    def listarCorreos(self, inicio, fin):
        print("Listando correos seguro para hilos...")
        listaCorreos = ["correo1", "correo2", "correo3"]
        if self.registroEventos is not None:
            self.notificarEvento("Se listaron correos con servicio seguro para hilos")
        return listaCorreos

    def dercargarCorreo(self, infoCorreo):
        print("Descargando correo...")
        correo = "Correo"
        return correo

    def notificarEvento(self, evento):
        self.registroEventos.registrarEvento(evento)

    def setRegistroEventos(self, registroEventos):
        self.registroEventos = registroEventos


