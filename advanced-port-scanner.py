import socket
import threading

target = input("Enter target IP: ")
print(f"Scanning {target}...\n")

def scan(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"

        print(f"[OPEN] Port {port} | {banner}")
        s.close()
    except:
        pass

threads = []

for port in range(20, 200):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()