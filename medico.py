import os
import sys
import subprocess

# Elenco dei file critici di Linux da controllare e i loro permessi ottali massimi consentiti
FILE_CRITICI = {
    "/etc/shadow": 0o600,   # Contiene le password criptate (solo root)
    "/etc/passwd": 0o644,   # Informazioni utenti (scrivibile solo da root)
    "/etc/gshadow": 0o600,  # Informazioni sicure sui gruppi
    "/etc/crontab": 0o644   # Task pianificati di sistema
}

def controlla_permessi_file():
    print("\n[*] Controllo integrità e permessi dei file critici...")
    falle_trovate = 0
    
    for percorso, permesso_sicuro in FILE_CRITICI.items():
        if os.path.exists(percorso):
            try:
                # Ottiene i permessi attuali del file
                info = os.stat(percorso)
                permessi_attuali = info.st_mode & 0o777
                
                # Se i permessi attuali sono più permissivi di quelli sicuri
                if permessi_attuali > permesso_sicuro:
                    print(f"[!] PERICOLO: {percorso} ha permessi troppo alti: {oct(permessi_attuali)} (Sicuro: {oct(permesso_sicuro)})")
                    print(f"    └─> Consigliato: sudo chmod {oct(permesso_sicuro)[2:]} {percorso}")
                    falle_trovate += 1
                else:
                    print(f"[+] {percorso}: Permessi Sicuri ({oct(permessi_attuali)})")
            except PermissionError:
                print(f"[-] Errore: Permessi insufficienti per analizzare {percorso}.")
                falle_trovate += 1
            except Exception as e:
                print(f"[-] Errore imprevisto su {percorso}: {e}")
                falle_trovate += 1
        else:
            print(f"[-] {percorso} non trovato su questo sistema.")
            
    return falle_trovate

def controlla_porte_aperte():
    print("\n[*] Controllo servizi in ascolto sulle porte di rete...")
    
    try:
        # Rimosso shell=True e aggiunto timeout per massima sicurezza
        risultato = subprocess.run(["ss", "-tuln"], shell=False, text=True, capture_output=True, timeout=5)
        
        if risultato.returncode == 0:
            output = risultato.stdout
            print(output)
            
            # Ricerca precisa con i due punti per evitare falsi positivi (es. porta 5021 o 121)
            if ":21 " in output or ":21\n" in output:
                print("[!] ATTENZIONE: Rilevato protocollo obsoleto FTP (:21) in ascolto!")
            if ":23 " in output or ":23\n" in output:
                print("[!] ATTENZIONE: Rilevato protocollo obsoleto Telnet (:23) in ascolto!")
        else:
            print(f"[-] Impossibile recuperare lo stato delle porte: {risultato.stderr}")
    except FileNotFoundError:
        print("[-] Errore: Il comando 'ss' non è installato o non è stato trovato nel sistema.")
    except subprocess.TimeoutExpired:
        print("[-] Errore: Il controllo delle porte ha impiegato troppo tempo (Timeout).")
    except Exception as e:
        print(f"[-] Errore durante il controllo delle porte: {e}")

def esegui_diagnosi():
    # Controllo amministratore (root) obbligatorio prima di toccare i file di sistema
    if os.geteuid() != 0:
        print("[-] ERRORE: Questo script richiede privilegi di ROOT. Esegui con: sudo python3 medico.py")
        sys.exit(1)

    print("==================================================")
    print("    CYBERSCAFFOLDING - DIAGNOSTIC MEDICAL TOOL    ")
    print("==================================================")
    
    falle = controlla_permessi_file()
    controlla_porte_aperte()
    
    print("\n=== DIAGNOSI COMPLETATA ===")
    if falle == 0:
        print("[+] Ottimo! Nessuna vulnerabilità macroscopica trovata sui file.")
    else:
        print(f"[!] Attenzione: Rilevate {falle} anomalie di configurazione.")

if __name__ == "__main__":
    esegui_diagnosi()
