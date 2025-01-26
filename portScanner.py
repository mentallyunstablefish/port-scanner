import socket

def con_scan(target_host, target_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_socket:
            conn_socket.settimeout(1)
            conn_socket.connect((target_host, target_port))
            print(f"[+] {target_port}/tcp open")
    except socket.error:
        print(f"[-] {target_port}/tcp closed")

def port_scan(target_host, target_ports):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[-] Cannot resolve {target_host}")
        return

    try:
        target_name = socket.gethostbyaddr(target_ip)[0]
        print(f"\n[+] Scan result for: {target_name} ({target_ip})")
    except socket.herror:
        print(f"\n[+] Scan result for: {target_ip}")

    for target_port in target_ports:
        print(f"Scanning Port: {target_port}")
        con_scan(target_host, target_port)

if __name__ == "__main__":
    port_scan("microsoft.com", [80, 22])