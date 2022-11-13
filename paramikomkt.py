#Connection to mikrotik router via paramiko
#Import paramiko (module must be installed: sudo pip install paramiko)
import paramiko

#Connection to mkt:
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Specify router connection:
client.connect(str(input('Ingrese IP de router:')), username=str(input('ingrese Usuario: ')), password=str(input('Ingrese clave: ')))
opc = 0
while(opc==0):
        stdin, stdout, stderr = client.exec_command(str(input('Ingrese comando a ejecutar en la consola de MKT: ')))

        for line in stdout:
                print(line.strip('\n'))
client.close()
