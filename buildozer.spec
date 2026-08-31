# Write the buildozer.spec content to the file
%%writefile buildozer.spec
[app]
title = RF CCTV GPS Detector
package.name = rfcctvgpsdetector
package.domain = com.detector.rfcctv

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 2.0
version.regex = __version__ = ['"]([^"]*)['"]
version.filename = %(source.dir)s/main.py

[buildozer]
log_level = 2
warn_on_root = 1

# Kivy + Plyer + Android permissions untuk akurasi tinggi
requirements = python3,kivy,plyer,pyjnius,android

orientation = portrait

# Izin penting untuk deteksi GPS, Bluetooth, WiFi, Kamera - AKURASI TINGGI
android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, CAMERA, VIBRATE, ACCESS_BACKGROUND_LOCATION
android.api = 33
android.minapi = 21
android.ndk = 25
android.accept_sdk_license_agreement = True

# Untuk Magnetometer & BLE akurasi tinggi
android.features = android.hardware.sensor.compass, android.hardware.bluetooth_le, android.hardware.camera

# Icon (opsional)
#icon.filename = %(source.dir)s/icon.png

[app:android]
# Tambahan untuk BLE scan
android.gradle_dependencies =

p4a.bootstrap = sdl2
p4a.port = android

# Antivirus: jangan pakai webview yang mencurigakan
