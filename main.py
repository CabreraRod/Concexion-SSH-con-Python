import paramiko
import time
from getpass import getpass

from paramiko import ssh_exception

HOST = '161.35.56.145'
USER = 'root'

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient() #Objeto SSH cliente
        client.set_missing_host_key_policy( paramiko.AutoAddPolicy() ) #Le indicamos que nos vamos a autenticar con nuestras propias credenciales
    
        password = getpass('Ingrese su contraseña: ')
        client.connect(HOST, username=USER, password=password) #Autenticacion
    
        stdin, stdout, stderr = client.exec_command('ls') #Ejecucion de comando
        time.sleep(1)
    
        result = stdout.read().decode() #Convertimos el retorno a un string
    
        print(result)
        client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print('Autenticacion fallida.')