import socket
import argparse
import ipaddress
from colorama import Fore, Style, init

init(autoreset=True)

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def scan_ip_ports(ip, ports):
    open_ports = []
    print(f"\n{Fore.CYAN}Escaneando {ip}:")
    for port in ports:
        if scan_port(ip, port):
            print(f"{Fore.GREEN}[+] Puerto abierto: {port}")
            open_ports.append(port)
        else:
            print(f"{Fore.RED}[-] Puerto cerrado: {port}")
    return open_ports

def parse_ports(port_str):
    if not port_str:
        # Puertos comunes
        return [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    ports = []
    for part in port_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.extend(range(start, end+1))
        else:
            ports.append(int(part))
    return ports

def get_targets(target):
    try:
        # Si es un rango CIDR
        if '/' in target:
            return [str(ip) for ip in ipaddress.IPv4Network(target, strict=False)]
        else:
            return [target]
    except Exception as e:
        print(f"{Fore.YELLOW}Error al analizar el objetivo: {e}")
        return []

def save_results(results, filename):
    with open(filename, 'w') as f:
        for ip, ports in results.items():
            f.write(f"{ip}:\n")
            for port in ports:
                f.write(f"  - Puerto abierto: {port}\n")
    print(f"{Fore.MAGENTA}Resultados guardados en {filename}")

def main():
    parser = argparse.ArgumentParser(description="Escáner de IPs y puertos")
    parser.add_argument('-t', '--target', required=True, help="IP o rango CIDR a escanear")
    parser.add_argument('-p', '--ports', help="Puertos (ej: 22,80,443 o 1-1024)")
    parser.add_argument('-o', '--output', help="Archivo de salida")
    args = parser.parse_args()

    targets = get_targets(args.target)
    ports = parse_ports(args.ports)

    results = {}
    for ip in targets:
        open_ports = scan_ip_ports(ip, ports)
        results[ip] = open_ports

    if args.output:
        save_results(results, args.output)

if __name__ == '__main__':
    main()
