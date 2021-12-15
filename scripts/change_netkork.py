import os

def cambiar(IP, MASK):
    comando = "sudo ifconfig eth0 " + IP + " netmask " + MASK
    os.system(comando)
    print("Se logro cambiar con exito la IP del Eth0")


if __name__ == '__main__':
    cambiar("192.168.0.1", "255.255.255.0")