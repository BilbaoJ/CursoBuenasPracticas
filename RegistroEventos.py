from abc import ABC, abstractmethod


class RegistroEventos(ABC):

    @abstractmethod
    def registrarEvento(self, evento):
        pass