# Smart Fish Feeder (ESP8266)

## Deskripsi
Smart Fish Feeder adalah sistem pemberian pakan ikan otomatis menggunakan NodeMCU ESP8266 dan servo motor. Sistem ini akan memberikan pakan ikan secara otomatis berdasarkan interval waktu tertentu.

## Komponen
- NodeMCU ESP8266
- Servo Motor
- Wadah pakan ikan
- Power supply

## Cara Kerja Sistem
1. NodeMCU menjalankan program Python (MicroPython).
2. Servo motor akan membuka wadah pakan ikan.
3. Pakan akan jatuh ke dalam aquarium.
4. Servo menutup kembali wadah.
5. Proses diulang setiap 12 jam.

## Struktur Project
smart-fish-feeder
│
├── main.py
├── feeder.py
├── config.py
│
├── docs
│   ├── wiring_diagram.png
│   └── flowchart.png
│
└── README.md