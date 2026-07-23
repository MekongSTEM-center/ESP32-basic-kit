# ==============================================================================
# Mekong STEM - Giáo trình lập trình vi điều khiển ESP32 với MicroPython
# Dự án: Điều khiển độ sáng LED bằng Biến trở (Kết hợp Analog Input & Analog Output)
# ==============================================================================

from machine import Pin, ADC, PWM  # Nhập các lớp phần cứng cần thiết
from utime import sleep_ms        # Nhập hàm sleep_ms để tạo độ trễ lấy mẫu

print("Hệ thống khởi động... Xoay biến trở để điều khiển độ sáng LED.")
print("Bấm tổ hợp phím `Ctrl+C` tại cửa sổ Shell để dừng chương trình an toàn.")

# 1. Cấu hình chân đọc Analog Input (Biến trở tại GPIO 4)
pot = ADC(Pin(4))
pot.atten(ADC.ATTN_11DB)  # Đọc dải điện áp đầy đủ 0V - 3.3V (Trả về: 0 - 4095)

# 2. Cấu hình chân xuất PWM Output (Đèn LED tại GPIO 5)
led_pwm = PWM(Pin(5), freq=5000)  # Tần số từ 1000 - 5000Hz giúp sáng mượt không nhấp nháy

try:
    # Vòng lặp liên tục đọc biến trở và cập nhật độ sáng LED
    while True:
        # Đọc giá trị thô 12-bit từ biến trở (Dải giá trị: 0 đến 4095)
        pot_value = pot.read()
        
        # Quy đổi từ thang 12-bit (0-4095) sang thang 10-bit PWM (0-1023)
        pwm_duty = pot_value // 4
        
        # Cập nhật chu kỳ nhiệm vụ (Duty Cycle) cho chân xuất LED PWM
        led_pwm.duty(pwm_duty)
        
        # In thông số giám sát ra cửa sổ Terminal / Shell
        print(f"ADC Value: {pot_value} | PWM Duty: {pwm_duty}")
        
        # Độ trễ ngắn 20ms giúp tín hiệu đáp ứng nhanh và mượt mà khi xoay biến trở
        sleep_ms(20)

except KeyboardInterrupt:
    # Khối lệnh giải phóng tài nguyên phần cứng khi dừng chương trình
    print("\n[HỆ THỐNG DỪNG] Đang ngắt nguồn chân PWM và dừng đọc ADC...")
    led_pwm.duty(0)      # Tắt hẳn LED
    led_pwm.deinit()    # Hủy khởi tạo PWM
    print("Đã dọn dẹp hệ thống an toàn.")
