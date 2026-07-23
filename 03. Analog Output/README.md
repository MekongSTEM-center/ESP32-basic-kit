# 📘 Project 4: ESP32 PWM (Analog Output)

Dự án này hướng dẫn cách tạo tín hiệu Điều chế độ rộng xung (PWM) với vi điều khiển ESP32 sử dụng MicroPython. Ví dụ thực hành tập trung vào việc tạo hiệu ứng điều chỉnh độ sáng đèn LED (Dimmer LED) thông qua bộ điều khiển LED PWM phần cứng của ESP32.

---

## ⚡ 1. Khái Niệm Về PWM (Pulse Width Modulation)

**PWM (Điều chế độ rộng xung)** là phương pháp giả lập tín hiệu Analog bằng cách bật/tắt điện áp ở mức Kỹ thuật số (Digital Output - 0V và 3.3V/5V) ở tần số rất cao.



Tín hiệu PWM được đặc trưng bởi 2 thông số cốt lõi:
* **Tần số (Frequency):** Số chu kỳ bật/tắt diễn ra trong 1 giây, đơn vị Hertz (Hz).
* **Chu kỳ nhiệm vụ (Duty Cycle):** Tỷ lệ phần trăm (%) thời gian tín hiệu ở mức cao (HIGH) so với tổng thời gian của một chu kỳ.

Điện áp trung bình đầu ra ($V_{out}$) phụ thuộc trực tiếp vào **Duty Cycle**:
$$V_{out} = V_{max} \times \text{Duty Cycle}$$

* *Ví dụ:* Nguồn cấp $V_{max} = 3.3V$. Nếu Duty Cycle = $50\%$, điện áp trung bình cấp ra tải tương đương $3.3V \times 0.5 = 1.65V$.
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/bb8d2045-1c23-497e-bb50-49c4f13611e9" />

---

## ❓ 2. Tại Sao Dùng PWM Thay Vì Xuất Analog Trực Tiếp (DAC)?

Mặc dù việc xuất điện áp Analog thực tế bằng bộ chuyển đổi DAC (Digital-to-Analog Converter) giúp điện áp ra liên tục, PWM vẫn là lựa chọn ưu việt nhờ các ưu điểm:

* **Tiết kiệm tài nguyên phần cứng:** Vi điều khiển tích hợp rất ít bộ DAC phần cứng do mạch phức tạp (ESP32 chỉ có 2 kênh DAC 8-bit, trong khi hỗ trợ tới 16 kênh PWM phần cứng).
* **Giữ nguyên đặc tính tải:** Đối với các thiết bị như Động cơ DC, dùng PWM giữ điện áp đỉnh luôn ở mức tối đa ($V_{max}$), giúp động cơ duy trì mô-men xoắn (lực kéo) ngay cả khi quay ở tốc độ chậm.

---

## 🛠️ 3. Các Ứng Dụng Thực Tế Của PWM

* **Điều khiển độ sáng (Dimming):** Bật/tắt LED ở tần số cao ($>100\text{Hz}$) để mắt người không nhận ra hiện tượng nhấp nháy, giúp điều chỉnh độ sáng mượt mà.
* **Điều khiển tốc độ động cơ DC:** Thay đổi điện áp trung bình cấp cho động cơ để tăng/giảm tốc độ quạt, xe robot.
* **Tạo âm thanh (Buzzer / Loa):** Thay đổi tần số xung PWM để phát ra các nốt nhạc hoặc âm thanh cảnh báo.
<img width="576" height="311" alt="image" src="https://github.com/user-attachments/assets/9d1b60e7-073f-4c8b-ad6c-18b5969b106d" />

---

## 🎛️ 4. Bộ Điều Khiển LED PWM Trên ESP32

ESP32 tích hợp bộ điều khiển LED PWM với **16 kênh độc lập** (từ kênh `0` đến `15`) có thể cấu hình để phát tín hiệu PWM với các thuộc tính riêng biệt:

* **Tần số (Frequency):** Thiết lập tần số phát xung. Đối với LED, tần số **5000 Hz** là phù hợp.
* **Độ phân giải (Resolution):** Trong MicroPython, thang đo Duty Cycle chuẩn cho PWM sử dụng dải 10-bit (giá trị từ `0` đến `1023`). 
---

## 💡 5. Giới Thiệu Dự Án: Điều Khiển Độ Sáng LED Bằng Biến Trở

Dự án này kết hợp giữa tín hiệu đầu vào **Analog Input (ADC)** và tín hiệu đầu ra **PWM Output**. Hệ thống liên tục đọc giá trị từ biến trở (0 - 4095), sau đó quy đổi trực tiếp giá trị này thành chu kỳ nhiệm vụ (Duty Cycle) để điều chỉnh độ sáng của đèn LED.

### 📦 Thành Phần Linh Kiện (Parts Required)
* 1 x Mạch ESP32 DEVKIT V1 Board.
* 1 x Biến trở xoay (Potentiometer).
* 1 x Đèn LED 5mm.
* 1 x Điện trở hạn dòng 220Ω.
* 1 x Bo cắm mạch (Breadboard).
* Dây bus cắm mạch (Jumper wires).

---

## 🔌 6. Sơ Đồ Đấu Nối (Schematic)

Tiến hành cắm mạch theo các kết nối sau:
* **Mạch Biến trở (Analog Input):**
  * Hai chân biên nối vào hàng nguồn **3V3** và **GND** của ESP32.
  * Chân tín hiệu ở giữa nối vào chân **GPIO 4**.
* **Mạch LED (PWM Output):**
  * Chân **Anode (chân dài)** của LED nối qua điện trở **220Ω** vào chân **GPIO 5**.
  * Chân **Cathode (chân ngắn)** của LED nối về hàng **GND**.

---

## 💻 7. Mã Nguồn Lập Trình

Toàn bộ mã nguồn MicroPython được lưu trữ độc lập trong tệp [`main.py`](./main.py).

Các điểm trọng tâm xử lý trong mã nguồn:
* Đọc tín hiệu thô 12-bit từ biến trở qua lớp `ADC` tại `GPIO 4`.
* Quy đổi dải dữ liệu từ 12-bit (`0 - 4095`) về dải 10-bit (`0 - 1023`) bằng phép chia `pot_value // 4`.
* Gán giá trị sau quy đổi làm `duty` cho chân `PWM` tại `GPIO 5`.

---

## 🚀 8. Kiểm Thử Dự Án (Testing the Example)

1. **Chuẩn bị môi trường:** Mở Thonny IDE, kết nối mạch ESP32 với máy tính.
2. **Tải mã nguồn:** Nạp tệp `main.py` lên board mạch ESP32.
3. **Quan sát hiện tượng:**
   * Xoay trục biến trở về phía 0V: Đèn LED mờ dần cho đến khi tắt hoàn toàn.
   * Xoay trục biến trở về phía 3.3V: Đèn LED tăng dần độ sáng cho đến khi đạt mức tối đa.
   * Màn hình Shell hiển thị đồng thời giá trị ADC thô và giá trị PWM Duty Cycle tương ứng.
