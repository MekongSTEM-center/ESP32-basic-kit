# ==============================================================================
# Mekong STEM - Giáo trình lập trình vi điều khiển ESP32 với MicroPython
# Dự án: Điều khiển LED RGB
# ==============================================================================

from machine import Pin, PWM  # Nhập lớp Pin và PWM để cấu hình xuất xung
from utime import sleep_ms   # Nhập hàm sleep_ms để tạo độ trễ giữa các lần đổi màu
import urandom               # Nhập thư viện sinh số ngẫu nhiên

print("Hệ thống khởi động... Đang phát tín hiệu PWM điều khiển LED RGB.")
print("Bấm tổ hợp phím `Ctrl+C` tại cửa sổ Shell để dừng chương trình an toàn.")

# 1. Cấu hình các chân xuất PWM cho 3 màu R, G, B, tần số 5000hz
red_pwm   = PWM(Pin(13), freq=5000)  # Chân điều khiển màu Đỏ (Red)
green_pwm = PWM(Pin(12), freq=5000)  # Chân điều khiển màu Xanh lá (Green)
blue_pwm  = PWM(Pin(14), freq=5000)  # Chân điều khiển màu Xanh dương (Blue)

def set_color(r, g, b):
    """
    Hàm thiết lập màu sắc cho LED RGB (Loại Cathode chung)
    :param r: Mức độ màu Đỏ (0 - 255)
    :param g: Mức độ màu Xanh lá (0 - 255)
    :param b: Mức độ màu Xanh dương (0 - 255)
    """
    # Quy đổi giá trị RGB 8-bit (0-255) sang thang PWM 10-bit của MicroPython (0-1023)
    duty_r = int((r / 255) * 1023)
    duty_g = int((g / 255) * 1023)
    duty_b = int((b / 255) * 1023)
    
    # Gán giá trị Duty Cycle cho từng kênh PWM
    red_pwm.duty(duty_r)
    green_pwm.duty(duty_g)
    blue_pwm.duty(duty_b)

try:
    # Vòng lặp liên tục tạo màu ngẫu nhiên
    while True:
        # Sinh giá trị ngẫu nhiên trong dải từ 0 đến 255 cho từng màu
        r = urandom.randint(0, 255)
        g = urandom.randint(0, 255)
        b = urandom.randint(0, 255)
        
        # Cập nhật màu sắc lên đèn LED RGB
        set_color(r, g, b)
        
        # Xuất giá trị màu hiện tại ra màn hình Terminal
        print(f"Màu hiện tại -> R: {r} | G: {g} | B: {b}")
        
        # Chờ 500ms trước khi đổi sang màu tiếp theo
        sleep_ms(500)

except KeyboardInterrupt:
    # Khối lệnh dọn dẹp và giải phóng tài nguyên PWM khi nhấn Ctrl+C
    print("\n[HỆ THỐNG DỪNG] Đang tắt toàn bộ các kênh màu LED RGB...")
    set_color(0, 0, 0)      # Tắt cả 3 màu (Duty = 0)
    
    # Hủy khởi tạo PWM trên các chân GPIO
    red_pwm.deinit()
    green_pwm.deinit()
    blue_pwm.deinit()
    print("Đã ngắt hệ thống an toàn.")
