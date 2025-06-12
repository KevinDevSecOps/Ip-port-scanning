# ip-port-scanner

Escáner de IPs y puertos en Python 3  
Herramienta simple y flexible para descubrir hosts activos y puertos abiertos en una red.

## 🚀 Características

- Escanea una IP o un rango de IPs (formato CIDR o lista manual).
- Escaneo de puertos comunes o personalizados.
- Resultados por consola y en archivo.
- Fácil de usar y ampliar.

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/KevinDevSecOps/ip-port-scanner.git
   ```
2. Ingresa al directorio:
   ```bash
   cd ip-port-scanner
   ```
3. (Opcional) Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## ⚡ Uso

Escanear una IP:
```bash
python3 scanner.py -t 192.168.1.1
```

Escanear un rango de IPs:
```bash
python3 scanner.py -t 192.168.1.0/24
```

Escanear puertos personalizados:
```bash
python3 scanner.py -t 192.168.1.1 -p 22,80,443
```

Guardar resultados:
```bash
python3 scanner.py -t 192.168.1.1 -o resultado.txt
```

## 📦 Dependencias

- colorama

## 📝 Licencia

MIT

---

Hecho con ❤️ por [KevinDevSecOps](https://github.com/KevinDevSecOps)
