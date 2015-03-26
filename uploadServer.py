import ftplib
import os

class uploadServer:
	raiz = '/public_html'

	def main(self):
		servidor = raw_input("Ingrese el servidor FTP: ")
        	usuario = raw_input("User: ")
        	clave = raw_input("Password: ")
        	print "Conectando a ", servidor ,"... "
      	  	if(p.conectar(servidor, usuario, clave)):
        		ruta_origen = raw_input("Path del archivo a subir: ")
    	            	nombre_archivo = raw_input("Ingrese un nombre para el archivo")
        	        subir_archivo()
	        else:
	                print "No Se Pudo Conectar al Servidor", servidor


	def conectar(self, servidor, usuario, clave):
		try:
   	        	conexion_servidor = ftplib.FTP(self.servidor, self.usuario, self.clave)
        	        return True
        	except:
        		return False

	def subir_archivo(self):
        	try:
                	fichero = open(ruta_origen_archivo, 'rb')
        	        conexion_servidor.cwd(raiz)
                	conexion_servidor.storbinary('STOR' + ruta_destino_archivo, fichero)
                	fichero.close()
                	conexion_servidor.quit()
        	except: print "Verifique si la ruta del archivo es valida"

p = uploadServer()
p.main()
