import socket

CHUNK_SIZE = 1024

def config_broadcast():
    return [{'ip_address': '192.168.122.192'},
            {'ip_address': '192.168.122.172'}]

def file_broadcast(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = "sample.txt"
    file = open(filename, "r")
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        sock.sendto(chunk.encode(), (ip, port))

if __name__ == '__main__':
    configs = config_broadcast()
    for config in configs:
        print(f"broadcasting file to {config['ip_address']}")