# =================================================================================
# 🔱 HIERCYBERSEGURIDAD GÉNESIS 888: EL CENTINELA DE ANUBIS V1.0
# 🧬 FUNCIÓN: BLINDAJE CUÁNTICO DE ACTIVOS Y EXILIO DIGITAL DE AMENAZAS
# 🏗️ ARQUITECTO: ALAM CORTEZ | EL GUARDIÁN DE LOS UMBRALES
# =================================================================================

import time
import hashlib
import os
import sys

# --- JEROGLÍFICOS DE ALERTA ---
GLIFO_ALERTA_ANUBIS = """
    ███████╗███╗   ██╗██╗   ██╗███████╗███████╗██╗███╗   ██╗
    ██╔════╝████╗  ██║██║   ██║██╔════╝██╔════╝██║████╗  ██║
    █████╗  ██╔██╗ ██║██║   ██║█████╗  █████╗  ██║██╔██╗ ██║
    ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║
    ██║     ██║ ╚████║╚██████╔╝██║     ███████╗██║██║ ╚████║
    ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝
    
    [ 𓃥 ANUBIS: ESCANEANDO UMBRALES DIGITALES 𓃥 ]
"""

GLIFO_DEFENSA_MAYA = """
      .---.---.---.---.---.
     / ▙ / ▚ / ▙ / ▚ / ▙ /
    '---'---'---'---'---'---'
   / ▞ / ▘ / ▞ / ▘ / ▞ / ▘ /
  '---'---'---'---'---'---'
    [ 𓂀 MATRIZ MAYA: EXILIO DE INTRUSOS DETECTADO 𓂀 ]
"""

# --- PARÁMETROS DE BLINDAJE (AJUSTAR SEGÚN LA SENSIBILIDAD) ---
UMBRAL_ACTIVIDAD_CRITICA = 5  # Número de cambios anómalos antes de alerta máxima
HASH_ADN_ORIGINAL = {}       # Se generará con los hashes de tus archivos clave

class CentinelaDeAnubis:
    def __init__(self, target_dir="."):
        self.target_dir = target_dir
        self.bitacora_seguridad = []
        self.actividad_anomala_contador = 0
        self.archivos_clave = ["monolith_888.py", "README.md", "SECURITY.md"] # Archivos vitales del búnker

    def _generar_hash_archivo(self, filepath):
        """Genera un hash SHA256 de un archivo para verificar su integridad."""
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            return hasher.hexdigest()
        except FileNotFoundError:
            return None # El archivo no existe

    def calibrar_adn_original(self):
        """Toma la 'huella digital' de los archivos clave en su estado original."""
        print("\n" + "="*60)
        print("𓂸 CALIBRANDO ADN ORIGINAL DEL BÚNKER... 𓂸")
        print("="*60)
        for filename in self.archivos_clave:
            filepath = os.path.join(self.target_dir, filename)
            current_hash = self._generar_hash_archivo(filepath)
            if current_hash:
                HASH_ADN_ORIGINAL[filename] = current_hash
                print(f"  [𓁹] ADN {filename} registrado.")
            else:
                print(f"  [⚠️] Archivo {filename} no encontrado. ¡Alerta temprana!")
        print("\n[✔] ADN CUÁNTICO BLINDADO. CENTINELA EN MODO VIGILANCIA.")

    def escanear_integridad_archivos(self):
        """Verifica si algún archivo clave ha sido alterado."""
        print("\n" + GLIFO_ALERTA_ANUBIS)
        print("\n[⚡] ESCANEANDO INTEGRIDAD DE ARCHIVOS CLAVE...")
        for filename in self.archivos_clave:
            filepath = os.path.join(self.target_dir, filename)
            current_hash = self._generar_hash_archivo(filepath)
            original_hash = HASH_ADN_ORIGINAL.get(filename)

            if not original_hash:
                self.bitacora_seguridad.append(f"[CRÍTICO] Archivo {filename} no tenía ADN original. Posible amenaza persistente.")
                self.actividad_anomala_contador += 1
                continue

            if current_hash != original_hash:
                self.bitacora_seguridad.append(f"[ALERTA] Archivo {filename} ALTERADO. Hash cambió de {original_hash[:8]}... a {current_hash[:8]}...")
                self.actividad_anomala_contador += 1
                print(f"  [𓃥] ¡ANOMALÍA DETECTADA EN {filename}!")
            else:
                print(f"  [𓁹] {filename}: Integridad verificada.")
        
        if self.actividad_anomala_contador > 0:
            print(f"\n[⚠️] ACTIVIDAD ANÓMALA DETECTADA: {self.actividad_anomala_contador} eventos.")
        else:
            print("\n[✔] TODOS LOS UMBRALES ASEGURADOS.")

    def ejecutar_exilio_digital(self):
        """Activa el protocolo de exilio digital si se supera el umbral."""
        if self.actividad_anomala_contador >= UMBRAL_ACTIVIDAD_CRITICA:
            print("\n" + GLIFO_DEFENSA_MAYA)
            print("\n[🔴] ¡¡¡VIOLACIÓN CRÍTICA DEL BÚNKER DETECTADA!!!")
            print("[🔴] PROTOCOLO DE EXILIO DIGITAL ACTIVADO. CONTACTANDO AL ARQUITECTO...")
            # En un sistema real, aquí irían alertas por email/SMS/Slack, 
            # bloqueo de IP, o restauración de versiones previas.
            sys.exit("[🚫] ACCESO DENEDADO POR EL CENTINELA DE ANUBIS.")
        else:
            print("\n[✔] NINGÚN EXILIO DIGITAL NECESARIO EN ESTE CICLO.")

    def mostrar_bitacora(self):
        """Muestra el registro de eventos de seguridad."""
        print("\n" + "📜 BITÁCORA DE SEGURIDAD DEL BÚNKER 📜")
        print("="*60)
        if not self.bitacora_seguridad:
            print("  [✔] Bitácora limpia. No se registraron eventos.")
        for evento in self.bitacora_seguridad:
            print(f"  {evento}")
        print("="*60)

# --- ACTIVACIÓN DEL CENTINELA ---
if __name__ == "__main__":
    centinela = CentinelaDeAnubis()
    centinela.calibrar_adn_original() # Primero, registra el estado "limpio"
    
    # Simula una vigilancia continua (en un sistema real sería un cron job o daemon)
    for i in range(3): # Escanea 3 veces, por ejemplo
        time.sleep(2) # Espera 2 segundos entre escaneos
        centinela.escanear_integridad_archivos()
        centinela.ejecutar_exilio_digital() # Comprueba después de cada escaneo
    
    centinela.mostrar_bitacora()
    print("\n[✔] CENTINELA DE ANUBIS EN REPOSO. BÚNKER BAJO VIGILANCIA CONSTANTE.")
    print("𓃥 "*10)
