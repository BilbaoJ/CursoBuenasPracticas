from CreadorServicio import CreadorServicio

#creando servicio TS
creador = CreadorServicio()
servicio = creador.crearServicioTS()

#habilita logs
creador.habilitarLogs(servicio)

servicio.enviarCorreo("correo de prueba")
correos = servicio.listarCorreos(1,3)
print(correos)
correo = servicio.dercargarCorreo("correo...")
print(correo)

#habilita cache
creador.habilitarCache(servicio)
servicio.enviarCorreo("correo de prueba 2")
correos = servicio.listarCorreos(1,3)
print(correos)
correo = servicio.dercargarCorreo("correo...")
print(correo)