# 📘 Bài 2: Khảo Sát Mạch Điện Cơ Bản Và Lập Trình GPIO

Hướng dẫn từng bước từ việc nhận biết linh kiện phần cứng, lắp ráp mạch điện độc lập, đến việc hiểu về cơ chế điện trở kéo (Pull-up/Pull-down) để kiểm soát chân GPIO trên ESP32.

---

## ⚡ 1. Giới Thiệu Các Loại Linh Kiện Trong Bài

Mỗi linh kiện trong bộ kit đóng một vai trò vật lý riêng biệt trong mạch điện:

* **Bo cắm mạch (Breadboard MB102):** Đế cắm kết nối linh kiện không cần hàn. Hàng dọc biên (ký hiệu `+` và `-`) thông suốt theo chiều dọc dùng để cấp nguồn. Các hàng ngang khối trong (đánh số 1, 2, 3...) thông suốt theo cụm 5 lỗ (A-B-C-D-E) để cắm tín hiệu.<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9bc7f51a-5864-4642-819c-a9e9bb91b0db" />

* **Đèn LED đơn:** Linh kiện bán dẫn phát sáng 1 chiều. Chân dài là cực Dương (Anode), chân ngắn là cực Âm (Cathode).<img width="660" height="357" alt="image" src="https://github.com/user-attachments/assets/d4eea833-9243-435b-bda4-766b2b147bb9" />

* **Điện trở (Resistor):** Sử dụng loại **220Ω** mắc nối tiếp với LED để giảm dòng điện, tránh làm cháy LED. <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0228d370-5104-4571-9771-53d765ed347f" />

* **Nguồn điện:** Cung cấp điện áp cho mạch, gồm cực dương (VCC 3.3V/5V) và cực âm/đất (GND).<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/405959dc-7ca3-461f-bc6d-532bc34e0e5e" />

* **Nút nhấn (Push button):** Nút nhấn dùng để đóng hoặc ngắt mạch điện dựa trên lực tác động từ ngón tay.<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/ba5fb541-3a86-4a5c-a9fc-ad9a26cdde3c" /><img width="539" height="350" alt="image" src="https://github.com/user-attachments/assets/3231e238-df7b-47a7-962d-fb200cb65e6f" />



---

## 🔌 2. Hướng Dẫn Tạo Mạch Điện Bật/Tắt Đèn Bằng Nút Nhấn (Chưa có ESP32)

Bước này giúp người học hiểu về nguyên lý mạch điện kín. Mạch ESP32 chỉ đóng vai trò là nguồn cấp điện từ hai chân `3V3` và `GND` ra hai hàng dọc biên của Breadboard.

### Các bước cắm mạch nối tiếp:
1. Nối chân **3V3** của ESP32 vào hàng dọc nguồn màu đỏ `+` của Breadboard.
2. Nối chân **GND** của ESP32 vào hàng dọc nguồn màu xanh `-` của Breadboard.
3. Cắm nút nhấn bắc qua rãnh giữa của Breadboard. Nối một dây từ hàng nguồn đỏ `+` vào một chân của nút nhấn.
4. Từ chân đối diện của nút nhấn, cắm một **Điện trở hạn dòng 220Ω** sang một hàng ngang trống.
5. Cắm **chân dài (Anode)** của LED chung hàng ngang với đầu còn lại của điện trở.
6. Cắm **chân ngắn (Cathode)** của LED vào hàng dọc nguồn màu xanh `-` (GND) để khép kín mạch.

<img width="808" height="482" alt="image" src="https://github.com/user-attachments/assets/d0239f37-400b-44a6-a22f-4225f6f7d995" />
<img width="1024" height="611" alt="image" src="https://github.com/user-attachments/assets/acc76ef2-a374-4bd3-8261-c6e40a1b0522" />


**💡 Nguyên lý hoạt động:** Khi nhấn phím, mạch kín, dòng điện chạy từ 3.3V qua nút nhấn -> điện trở hạn dòng -> LED -> GND làm LED sáng. Khi buông tay, mạch hở, dòng điện bị ngắt làm LED tắt.

---

## 📡 3. Liên Kết Kiến Thức Mạch Điện Với GPIO Của ESP32

Khi lập trình vi điều khiển, các chân GPIO sẽ thay thế các liên kết vật lý cơ học để chạy tự động thông qua lập trình. 

### A. Cổng ra (Digital Output) điều khiển LED
ESP32 thay thế nguồn cấp điện trực tiếp. Khi cấu hình chân GPIO làm cổng ra (`Pin.OUT`) và xuất mức logic `1` (HIGH), chân đó sẽ phát ra điện áp 3.3V cấp dòng cho LED sáng. Khi xuất mức logic `0` (LOW), điện áp về 0V làm LED tắt.

### B. Cổng vào (Digital Input) đọc Nút nhấn & Cơ chế Điện trở kéo
Khi một chân GPIO cấu hình làm cổng vào (`Pin.IN`) để đọc nút nhấn, nếu nút chưa bấm, chân đó sẽ ở trạng thái cô lập ("lơ lửng" - floating). Điện tích nhiễu từ môi trường sẽ khiến chân đọc sai lệch liên tục giữa mức 0 và 1. Để xử lý, ta bắt buộc phải sử dụng điện trở kéo:

* **Điện trở kéo lên (Pull-up Resistor):** Nối chân GPIO lên nguồn 3.3V. Giữ trạng thái mặc định của chân luôn là mức `1`. Khi bấm nút (nối xuống GND), chân sụt về mức `0` (Mạch Active-Low).
* **Điện trở kéo xuống (Pull-down Resistor):** Nối chân GPIO xuống Đất (GND). Giữ trạng thái mặc định của chân luôn là mức `0`. Khi bấm nút (nối lên nguồn 3.3V), chân được cấp điện áp lên mức `1` (Mạch Active-High).

*Lưu ý:* ESP32 tích hợp sẵn các điện trở kéo này bên trong chip, cho phép kích hoạt bằng lập trình mà không cần cắm thêm điện trở 10kΩ bên ngoài.

Tiếp theo, ta sẽ kết hợp giữa mạch điện và lập trình tạo ra một dự án đơn giản, kết hợp giữa Digital Input và Digital Output.

Bước 1: Chuẩn bị linh kiện
* ESP32
* LED
* Điện trở 220 ohm
* Nút nhấn
Bước 2: Sơ đồ kết nối


---

## 💻 4. Lập Trình 
- Phần lập trình sẽ được trình bày chi tiết trong file 'main.py'
