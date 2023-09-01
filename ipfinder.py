import subprocess

print("=============================================")
print("        Deteksi Alamat IP Berdasarkan ESSID")
print("=============================================")

essid = input("Masukkan ESSID: ")

# Menggunakan perintah 'iwconfig' untuk mendapatkan informasi tentang antarmuka WiFi
result = subprocess.run(['iwconfig', 'wlan0'], capture_output=True, text=True)

# Mencari baris yang mengandung informasi ESSID
lines = result.stdout.split('\n')
found = False
for line in lines:
    if essid in line:
        parts = line.split()
        for part in parts:
            if 'inet' in part:
                ip_address = part.split(':')[1]
                print("---------------------------------------------")
                print(f"Alamat IP untuk ESSID '{essid}': {ip_address}")
                print("---------------------------------------------")
                found = True
                break

if not found:
    print(f"ESSID '{essid}' tidak ditemukan.")

print("Terima kasih telah menggunakan script ini.")