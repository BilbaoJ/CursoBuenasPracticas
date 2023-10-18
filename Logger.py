from RegistroEventos import RegistroEventos


class Logger(RegistroEventos):

    def registrarEvento(self, evento):
        print("log: " + evento)