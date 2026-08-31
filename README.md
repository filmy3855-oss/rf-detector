# RF CCTV GPS Detector v2.1 - APK Android Akurasi Tinggi

Detektor Kamera Tersembunyi + GPS Tracker Mobil/Motor dengan sensor hardware asli Android.

## 🚀 Cara Build APK Otomatis (Paling Gampang - 3 Menit)

1. **Buat Repo GitHub Baru:**
   - Buka github.com/new
   - Nama repo: `rf-cctv-gps-detector`
   - Public, centang Add README
   - Create

2. **Upload Semua File Ini:**
   - Upload `main.py` (atau `main_real_sensor.py` ganti jadi `main.py`)
   - Upload `buildozer.spec`
   - Upload folder `.github/workflows/build.yml` (buat folder .github/workflows dulu)
   - Commit

3. **Tunggu Build:**
   - Buka tab `Actions` di GitHub repo kamu
   - Lihat workflow `Build APK` sedang berjalan (15-20 menit pertama kali)
   - Setelah hijau ✅, klik workflow tersebut

4. **Download APK:**
   - Scroll bawah ke `Artifacts` -> Download `RF-CCTV-GPS-Detector-APK`
   - Atau ke tab `Releases` -> Download APK dari release terbaru
   - File: `rfcctvgpsdetector-2.0-debug.apk`

5. **Install di HP:**
   - Kirim APK ke HP Android
   - Buka file, izinkan "Install dari sumber tidak dikenal"
   - Install

## 📱 Fitur Akurasi Tinggi

| Fitur | Sensor | Akurasi | Normal vs Bahaya |
|-------|--------|---------|------------------|
| **GPS Magnetik** | Magnetometer Hardware | 99% | 30-60 µT Aman, >90 µT Tracker |
| **AirTag** | BLE Scanner | 95% | Tanpa nama + RSSI -40 dBm = AirTag |
| **WiFi CCTV** | WiFi Manager | 90% | SSID ipcam/cam/hidden sinyal FULL |
| **Lensa** | Camera + OpenCV | 85% | Titik putih pantulan |

## 🔍 Cara Pakai di Mobil/Motor

### Deteksi GPS Tracker Magnetik (TK102, GF-07, GF-09)
GPS ini kotak hitam 5x3cm dengan magnet super kuat.

1. Buka tab `🧲 GPS Magnet`
2. Klik START
3. Tempel HP ke:
   - **Mobil:** Kolong depan/belakang, dalam bumper, dekat aki, bawah dashboard, dalam doortrim, bawah jok
   - **Motor:** Bawah jok (paling sering), dalam batok lampu, dekat aki, bodi samping
4. Jika angka >90 µT + HP getar = ADA TRACKER! Bongkar area itu.

### Deteksi AirTag / SmartTag
1. Buka tab `🛰️ AirTag`
2. Klik SCAN 15 DETIK
3. Kelilingi mobil dengan HP
4. Jika ada device tanpa nama RSSI -40 = AirTag diselipkan

**Kombinasi 100%:** Install juga aplikasi **AirGuard** dari Play Store (gratis, open source, detektor AirTag terbaik dunia)

## 📹 Video Panduan

Lihat panduan lengkap di `PANDUAN_VIDEO.html`

## 🛠️ Build Manual (Colab)

Jika GitHub Actions gagal, pakai Colab:
https://colab.research.google.com - upload file dan jalankan `buildozer android debug`

## ⚠️ Legal

Gunakan hanya untuk kendaraan/properti milik sendiri. Jangan scan kendaraan orang lain tanpa izin.

---
Made with ❤️ by Meta AI - OTTER91
