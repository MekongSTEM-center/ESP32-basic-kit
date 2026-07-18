# Nhập (import) lớp Pin từ thư viện machine để cấu hình và điều khiển các chân phần cứng
from machine import Pin  
# Nhập (import) hàm sleep từ thư viện utime để tạo thời gian trễ/chờ tính bằng giây
from utime import sleep  

# Khởi tạo và cấu hình chân GPIO số 15 ở chế độ xuất tín hiệu (Digital Output)
# Chân này sẽ đóng vai trò cấp điện hoặc ngắt điện để điều khiển đèn LED
led = Pin(15, Pin.OUT)

# Khởi chạy một vòng lặp vô hạn (chạy liên tục không bao giờ dừng)
while True:
    led.on()      # Xuất điện áp mức cao (3.3V) ra chân GPIO15 -> Đèn LED bật sáng, có thể thay thế thành led.value(1)
    sleep(0.5)    # Duy trì trạng thái sáng này và tạm dừng chương trình trong 0.5 giây
    
    led.off()     # Hạ điện áp xuống mức thấp (0V/GND) tại chân GPIO15 -> Đèn LED tắt,có thể thay thế thành led.value(0)
    sleep(0.5)    # Duy trì trạng thái tắt này và tạm dừng chương trình trong 0.5 giây
