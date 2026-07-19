# ==============================================================================
# Mekong STEM - Giáo trình lập trình vi điều khiển ESP32 với MicroPython
# Dự án: Analog Input (Đọc giá trị Biến trở xoay)
# ==============================================================================

from machine import Pin, ADC  # Nhập lớp Pin và ADC để cấu hình chân đọc tín hiệu tương tự
from utime import sleep       # Nhập hàm sleep để tạo chu kỳ lấy mẫu dữ liệu

print("Hệ thống khởi động... Đang đọc dữ liệu từ biến trở xoay.")

# 1. Cấu hình chân GPIO 4 đọc tín hiệu Analog (ADC Input)
pot = ADC(Pin(4))

try:
    # Vòng lặp giám sát và lấy mẫu dữ liệu liên tục
    while True:
        
        # Đọc giá trị số nguyên 12-bit sau khi chuyển đổi từ điện áp
        # Dải giá trị trả về sẽ nằm trong khoảng từ 0 (0V) đến 4095 (3.3V)
        pot_value = pot.read()
        
        # Xuất giá trị thô đọc được ra màn hình Terminal / Shell
        print("Giá trị Analog hiện tại:", pot_value)
        
        # Chu kỳ lấy mẫu dữ liệu sau mỗi 0.5 giây (500ms). 
        sleep(0.5)        

except KeyboardInterrupt:
    # Khối lệnh ngừng chương trình khi người dùng bấm tổ hợp Ctrl+C
    print("Dừng chương trình thành công.")
