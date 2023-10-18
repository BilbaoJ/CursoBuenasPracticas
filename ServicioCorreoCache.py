from IServicioCorreo import IServicioCorreo


class ServicioCorreoCache(IServicioCorreo):

    def __int__(self, servicioCorreo):
        self.servicio = servicioCorreo
        self.registroEventos = None
        self.listaCorreosCache = ["correo4", "correo5"]
        self.infoCorreoCache = "correo guardado en cache"

    def enviarCorreo(self, correo):
        self.servicio.enviarCorreo(correo)

    def listarCorreos(self, inicio, fin):
        if self.listaCorreosCache is None:
            self.servicio.listarCorreos(inicio, fin)
        if self.registroEventos is not None:
            self.notificarEvento("Se listaron correos con servicio cache")
        return self.listaCorreosCache

    def dercargarCorreo(self, infoCorreo):
        if (self.infoCorreoCache is None):
            self.servicio.descargarCorreo(infoCorreo)
        if self.registroEventos is not None:
            self.notificarEvento("Se descrgo correo con servicio cache")
        return self.infoCorreoCache

    def notificarEvento(self, evento):
        self.registroEventos.registrarEvento(evento)

    def setRegistroEventos(self, registroEventos):
        self.registroEventos = registroEventos