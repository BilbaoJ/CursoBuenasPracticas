from ServicioCorreoCache import ServicioCorreoCache
from ServicioCorreoThreadSafe import ServicioCorreoThreadSafe
from ServicioCorreoNonThreadSafe import ServicioCorreoNonThreadSafe
from Logger import Logger


class CreadorServicio():

    def crearServicioTS(self):
        return ServicioCorreoThreadSafe()

    def crearServicioNTS(self):
        return ServicioCorreoNonThreadSafe()

    def habilitarLogs(self, servicio):
        logger = Logger()
        servicio.setRegistroEventos(logger)

    def habilitarCache(self, servicio):
        h = ServicioCorreoCache()
        servicioCache = ServicioCorreoCache(servicio)
        return servicioCache
