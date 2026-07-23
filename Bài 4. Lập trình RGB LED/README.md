# 📘 Bài 4: ESP32 RGB LED

Dự án này hướng dẫn cách điều khiển đèn LED RGB bằng vi điều khiển ESP32 sử dụng MicroPython. Thông qua việc phát các tín hiệu PWM với chu kỳ nhiệm vụ (Duty Cycle) khác nhau đến 3 chân màu Đỏ (Red), Xanh lá (Green), Xanh dương (Blue), chúng ta có thể phối hợp và tạo ra hàng triệu màu sắc sống động.

---

## ⚡ 1. Nguyên Lý Hoạt Động Của LED RGB

LED RGB là sự kết hợp của 3 đèn LED độc lập (Đỏ - Red, Xanh lá - Green, Xanh dương - Blue) đóng gói trong cùng một vỏ linh kiện. 

Hầu hết màn hình hiển thị và hệ thống chiếu sáng màu đều áp dụng chuẩn phối màu RGB. Bằng cách điều chỉnh tỷ lệ độ sáng tương đối giữa 3 màu cơ bản này, mắt người sẽ ghi nhận được màu sắc tổng hợp.

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/5991a0af-a1aa-411e-95b6-a1ffa0daec95" />
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/af44382b-d657-4e54-aad5-c1f003e63afc" />

Tín hiệu PWM được sử dụng để điều tiết độ sáng của từng LED thành phần:
* **Tần số (Frequency):** Thiết lập ở mức `5000Hz` để độ sáng phát ra ổn định và không bị nhấp nháy.
* **Chu kỳ nhiệm vụ (Duty Cycle):** Với thang đo 10-bit trong MicroPython (`0` đến `1023`), chúng ta có thể điều khiển chính xác cấp độ sáng của từng màu.

---

## ❓ 2. Phân Biệt LED RGB Cathode Chung Và Anode Chung

Trong thực tế, LED RGB có 2 loại cấu trúc chân:

1. **Cathode Chung (Common Cathode - CC):** * Chân chung nối về cực Âm (**GND**).
   * Xuất mức điện áp cao (HIGH/PWM) vào chân màu nào thì màu đó sẽ sáng.
2. **Anode Chung (Common Anode - CA):** * Chân chung nối về cực Dương (**3.3V/5V**).
   * Xuất mức điện áp thấp (LOW/0V) thì màu đó mới sáng (Active-Low).

 
<img width="300" height="156" alt="image" src="https://github.com/user-attachments/assets/0b5ff490-b004-4890-adb1-a83060fa967b" />
---

## 🛠️ 3. Các Ứng Dụng Thực Tế Của LED RGB

* **Đèn trang trí & Chiếu sáng không gian:** Tạo hiệu ứng chuyển màu cho hệ thống đèn LED dây, đèn thông minh trong gia đình.
* **Đèn báo trạng thái thiết bị:** Dùng các màu sắc khác nhau để biểu thị trạng thái hệ thống (VD: Đỏ = Lỗi/Cảnh báo, Xanh lá = Hoạt động bình thường, Xanh dương = Đang kết nối Wifi).
* **Màn hình hiển thị & Bảng quảng cáo:** Tạo nên các điểm ảnh (Pixel) màu trên màn hình LED lớn.

---

## 💡 4. Giới Thiệu Dự Án: Trộn Màu LED RGB Tự Động

Dự án này lập trình cho ESP32 tự động phát sinh các bộ giá trị màu ngẫu nhiên (hoặc chuyển màu mượt mà - Color Fading) bằng cách xuất 3 luồng tín hiệu PWM đồng thời ra các chân điều khiển R, G, B.

### 📦 Thành Phần Linh Kiện (Parts Required)
* 1 x Mạch ESP32 DEVKIT V1 Board.
* 1 x Đèn LED RGB 5mm.
* 3 x Điện trở hạn dòng 220Ω.
* 1 x Bo cắm mạch (Breadboard).
* Dây bus cắm mạch (Jumper wires).


---

## 🔌 5. Sơ Đồ Đấu Nối (Schematic)

Tiến hành kết nối LED RGB với board ESP32 theo cấu hình:
* **Chân 2 (Chân dài nhất - Cathode chung):** Nối về hàng **GND** của ESP32.
* **Chân 1 (Red):** Nối qua điện trở **220Ω** vào chân **GPIO 13**.
* **Chân 3 (Green):** Nối qua điện trở **220Ω** vào chân **GPIO 12**.
* **Chân 4 (Blue):** Nối qua điện trở **220Ω** vào chân **GPIO 14**.

<img width="493" height="488" alt="image" src="https://github.com/user-attachments/assets/9de67121-2302-403b-aad3-3f266a80e2b8" />

---

## 💻 6. Mã Nguồn Lập Trình

Toàn bộ mã nguồn MicroPython điều khiển đổi màu LED RGB được lưu trữ trong tệp [`main.py`](./main.py).

Các điểm trọng tâm xử lý trong mã nguồn:
* Khởi tạo 3 đối tượng `PWM` tại các chân `GPIO 13`, `GPIO 12`, và `GPIO 14` với tần số `5000Hz`.
* Xây dựng hàm `set_color(r, g, b)` để quy đổi dải màu chuẩn 8-bit (`0 - 255`) sang thang PWM 10-bit (`0 - 1023`).
* Sử dụng thư viện `urandom` để đổi màu ngẫu nhiên.

---

## 🚀 7. Kiểm Thử Dự Án (Testing the Example)

1. **Chuẩn bị môi trường:** Mở Thonny IDE và kết nối mạch ESP32 với máy tính.
2. **Tải mã nguồn:** Mở tệp `main.py` và nạp chương trình lên board ESP32.
3. **Quan sát hiện tượng:**
   * Quan sát đèn LED RGB: Đèn sẽ liên tục chuyển đổi sang các màu sắc ngẫu nhiên khác nhau sau mỗi 0.5 giây.
   * Màn hình Shell hiển thị thông số mã màu RGB (dải 0-255) tương ứng theo thời gian thực.
