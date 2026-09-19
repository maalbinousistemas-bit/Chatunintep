class servidor:
    def __init__(self,):
      #lista donde se almacenan los usuarios  y las conexiones
      self.usuarios = []
      self.conexiones = []

    def iniciar(self):
        print("Servidor iniciado")
        print("esperando conexxiones...")

    def conectarusuario(self, usuario, conexion):
        # comprobar si el usuario ya esta conectado al servidor
        if usuario not in self.usuarios:

            #agregar el usuario y la conexion a las listas
            self.usuarios.append(usuario)
            self.conexiones.append(conexion)

            print(f"usuario {usuario.nombre} se ha conectado al servidor")

        else:
            print(f"usuario {usuario.nombre} ya esta conectado al servidor")

    def desconectarusuario(self, usuario):
       # comprobar si el usuario esta conectado al servidor
       if usuario in self.usuarios:
          #obtener la posicion del usuario
          posicion = self.usuarios.index(usuario)

          #eliminar el usuario y la conexion de las listas
          self.usuarios.pop(posicion)
          self.conexiones.pop(posicion)

          print(f"usuario {usuario.nombre} se ha desconectado del servidor")

       else:
          print(f"usuario {usuario.nombre} no esta conectado al servidor")


    def recibir_mensaje(self, usuario, mensaje):

        #mostrar informacion del mensaje recibido
        print("mensaje recibido")
        print(f"mensaje recibido de {usuario.nombre}: {mensaje}")
        print(f"mensaje: {mensaje.contenido}")

        #despues de recibirlo el mensaje, enviarlo al destinatario
        self.enviar_mensaje(usuario, mensaje)

    def enviar_mensaje(self, usuario, mensaje,):
        #comprobar si el destinatario del mensaje esta conectado al servidor
        if mensaje.destinatario in self.usuarios:

          #obtener la posicion del destinatario en la lista de usuarios y enviar el mensaje a su conexion
          posicion = self.usuarios.index(mensaje.destinatario)

          #obtenemos la conexion del destinatario y enviamos el mensaje
          self.conexiones[posicion].enviar(mensaje.contenido)

          
          print(f"mensaje enviado a {mensaje.destinatario.nombre}: {mensaje.contenido}")
        else:
          print(f"usuario {mensaje.destinatario.nombre} no esta conectado al servidor")

class testservidor:
    def ejecutar(self):
       #crear servidor 
       servidor_chat = servidor()

       #iniciar servidor
       servidor_chat.iniciar()

       #crear usuarios
       miguel = usuario("miguel")
       juan = usuario("juan")

       #crear conexiones
       conexion_miguel = conexion(miguel)
       conexion_juan = conexion(juan)

       #conectar usuarios al servidor
       servidor_chat.conectarusuario(miguel, conexion_miguel)
       servidor_chat.conectarusuario(juan, conexion_juan)

       #crear mensaje de miguel a juan
       mensaje1 = mensaje("hola juan")
       mensaje1.destinatario = juan

       #enviar mensaje 
       servidor_chat.recibir_mensaje(miguel, mensaje)

       #desconectar a juan
       servidor_chat.desconectarusuario(juan)

       #intentar enviar otro mensaje a juan
       mensaje2 = mensaje("hola juan, ¿como estas?")
       mensaje2.destinatario = juan

       servidor_chat.recibir_mensaje(miguel, mensaje2)

test = testservidor()
test.ejecutar()
        