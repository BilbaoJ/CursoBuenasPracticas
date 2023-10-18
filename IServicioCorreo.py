from abc import ABC, abstractmethod


class IServicioCorreo(ABC):

    @abstractmethod
    def enviarCorreo(self, correo):
        pass

    @abstractmethod
    def listarCorreos(self, inicio, fin):
        pass

    @abstractmethod
    def dercargarCorreo(self, infoCorreo):
        pass

    @abstractmethod
    def notificarEvento(self, evento):
        pass

    @abstractmethod
    def setRegistroEventos(self, registroEventos):
        pass