from machine import Pin, PWM
import time

# KONFIGURASI

SERVO_PIN = 2          # GPIO2 = D4
OPEN_ANGLE = 90        # sudut buka wadah
CLOSE_ANGLE = 0        # sudut tutup wadah
FEED_INTERVAL = 43200  # 12 jam (dalam detik)

# SETUP SERVO

servo = PWM(Pin(SERVO_PIN), freq=50)

def set_angle(angle):
    """
    Mengatur sudut servo
    """
    duty = int((angle / 180) * 75 + 40)
    servo.duty(duty)

# FUNGSI MEMBERI PAKAN

def feed_fish():
    print("Memberi makan ikan...")

    # Buka wadah pakan
    set_angle(OPEN_ANGLE)
    time.sleep(2)

    # Tutup kembali
    set_angle(CLOSE_ANGLE)
    time.sleep(1)

    print("Pakan selesai diberikan")

# PROGRAM UTAMA

print("Smart Fish Feeder Aktif")

# Pastikan wadah tertutup saat mulai
set_angle(CLOSE_ANGLE)

while True:
    feed_fish()

    print("Menunggu jadwal berikutnya...")
    time.sleep(FEED_INTERVAL)