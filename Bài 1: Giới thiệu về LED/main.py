# ==============================================================================
# Mekong STEM - Giáo trình lập trình vi điều khiển ESP32 với MicroPython
# Dự án: Digital Input (Nút nhấn) và Digital OutPut (LED)
# ==============================================================================

from machine import Pin  # Nhập lớp Pin để cấu hình các chân phần cứng
from utime import sleep  # Nhập hàm sleep để tạo độ trễ 

# 1. Cấu hình chân xuất lệnh điều khiển LED (Digital Output)
led = Pin(4, Pin.OUT)

# 2. Cấu hình chân đọc tín hiệu nút nhấn (Digital Input) với điện trở kéo lên (PULL_UP)
# Mặc định khi CHƯA BẤM, chân GPIO5 sẽ đọc được mức 1 (HIGH) nhờ trở kéo lên nguồn 3.3V. 
button = Pin(5, Pin.IN, Pin.PULL_UP)

try:
    # Vòng lặp giám sát và xử lý liên tục
    while True:
        
        # Kiểm tra nếu nút được bấm (Khi bấm nút Active-Low, chân GPIO5 nối thẳng xuống GND -> trả về 0)
        if button.value() == 0:
            led.on()       # Cấp điện thế mức cao (3.3V) ra chân GPIO4 -> LED sáng
        else:
            led.off()      # Hạ điện thế về mức thấp (0V) tại chân GPIO4 -> LED tắt
            
        # Độ trễ ngắn 10ms (0.01 giây) để chống nhiễu cơ học (Debounce) khi bấm nút
        sleep(0.01)        

except KeyboardInterrupt:
    # Khối lệnh dừng toàn bộ chương trình khi người dùng bấm Ctrl+C
    print("\n[HỆ THỐNG DỪNG] Đang ngắt nguồn toàn bộ chân Output...")
    led.off()            
    print("Đã tắt nguồn chân GPIO4 thành công.")
