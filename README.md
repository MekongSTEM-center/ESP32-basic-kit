# ⚡ KHO TÀI LIỆU KIT HỌC TẬP ESP32 BASIC KIT ⚡

Chào mừng bạn đã sở hữu bộ **ESP32 Basic Kit** từ **Mekong STEM**. Đây là kho tài nguyên mở, lưu trữ toàn bộ tài liệu hướng dẫn, sơ đồ mạch và mã nguồn mẫu sử dụng ngôn ngữ **MicroPython** giúp bạn dễ dàng làm chủ công nghệ IoT và lập trình nhúng.

---

## 📌 1. GIỚI THIỆU BỘ KIT

**ESP32 Basic Kit** là bộ kit học tập lập trình phần cứng và IoT được Mekong STEM thiết kế tối ưu cho học sinh, sinh viên và người mới bắt đầu. Trung tâm của bộ kit là vi điều khiển **ESP32-WROOM-32** mạnh mẽ, tích hợp sẵn Wi-Fi và Bluetooth. 

Bộ kit này loại bỏ các rào cản phức tạp về hàn mạch, giúp người học tập trung hoàn toàn vào việc phát triển tư duy thuật toán, hiểu nguyên lý hoạt động của các linh kiện điện tử và tự tay xây dựng các ứng dụng tự động hóa thông minh trong đời sống.

---

## 📦 2. CÁC THÀNH PHẦN CƠ BẢN CỦA BỘ KIT

Bộ kit bao gồm các linh kiện điện tử và cảm biến thông dụng được chuẩn hóa để thực hành chuỗi bài học từ cơ bản đến nâng cao:

* **Khối xử lý trung tâm:** Board mạch ESP32 NodeMCU (Phiên bản 38 chân) kèm cáp nạp dữ liệu Micro-USB.
* **Khối hiển thị:** Màn hình LCD 16x2 tích hợp mạch chuyển đổi giao tiếp I2C (giúp tiết kiệm chân cắm).
* **Khối cảm biến (Sensors):**
    * Cảm biến nhiệt độ & độ ẩm không khí (DHT11 / DHT20).
    * Cảm biến ánh sáng (Quang trở - LDR).
    * Cảm biến vật cản hồng ngoại hoặc cảm biến chuyển động.
* **Khối cơ cấu chấp hành (Outputs):**
    * Hệ thống đèn LED nhiều màu (Đỏ, Vàng, Xanh) phục vụ mô phỏng đèn giao thông.
    * Còi chip (Buzzer) phát âm thanh cảnh báo.
    * Mạch Relay 5V cách ly an toàn dùng để đóng/ngắt các thiết bị điện lớn (như quạt, máy bơm nhỏ).
* **Phụ kiện kết nối:** Breadboard (Testboard cắm mạch), dây cắm testboard (Dây đực - đực, đực - cái, cái - cái).

---

## 🛠️ 3. HƯỚNG DẪN SỬ DỤNG TRANG GITHUB NÀY

Để người học dễ dàng tra cứu và thực hành mà không bị rối, toàn bộ các bài học trong kho lưu trữ này được chia thành các **Thư mục dự án riêng biệt** (được đánh số thứ tự từ `01_` đến `05_`... bên trên). 

Khi bạn bấm truy cập vào bất kỳ một thư mục dự án nào, cấu trúc bên trong luôn đảm bảo có đầy đủ **3 phần cốt lõi** sau:

### 📑 Phần 1: Hướng dẫn lý thuyết & Nhiệm vụ (`README.md` con)
File này sẽ giải thích rõ ràng:
* Mục tiêu của bài học (Ví dụ: Đọc cảm biến ánh sáng, khi tối thì bật đèn).
* Nguyên lý hoạt động của linh kiện mới xuất hiện trong bài.
* Giải thích chi tiết các câu lệnh MicroPython quan trọng được sử dụng.

### 🔌 Phần 2: Sơ đồ kết nối chân (`schematics.png`)
* Đây là hình ảnh trực quan mô tả cách đi dây từ board ESP32 sang các linh kiện trên breadboard.
* Sơ đồ được vẽ ở dạng **hình ảnh thực tế** giúp học sinh nhìn rõ từng màu dây, từng chân cắm (GPIO nào nối với chân nào của cảm biến) để thao tác theo một cách chính xác nhất, tránh nguy cơ cắm ngược chân gây hỏng mạch.

### 💻 Phần 3: Mã nguồn lập trình mẫu (`main.py`)
* File code mẫu MicroPython hoàn chỉnh, đã được test chạy ổn định 100%.
* Trong code được **chú thích bằng tiếng Việt** rõ ràng ở từng dòng lệnh quan trọng, giúp người học hiểu rõ bản chất của thuật toán chứ không chỉ copy-paste một cách thụ động.

---

## 📚 DANH SÁCH CÁC BÀI HỌC THỰC HÀNH (MỤC LỤC)

*Bạn có thể bấm trực tiếp vào tên bài học dưới đây để dẫn thẳng tới thư mục chứa tài liệu, sơ đồ cắm dây và code mẫu tương ứng:*

| Thứ tự | Tên Bài Học / Dự Án | Nội Dung Thực Hành | Đường Dẫn Hệ Thống |
| :---: | :--- | :--- | :--- |
| **01** | Nháy LED Onboard (Blink) | Làm quen Thonny IDE, cấu hình chân Output cơ bản. | [Truy cập bài 1](./01_Blink_LED) |
| **02** | Đọc cảm biến Analog (ADC) | Thu thập dữ liệu từ quang trở, xử lý điều kiện `if/else`. | [Truy cập bài 2](./02_Read_Sensor_ADC) |
| **03** | Điều khiển Relay an toàn | Ứng dụng đóng cắt thiết bị tự động dựa trên cảm biến. | [Truy cập bài 3](./03_Control_Relay) |
| **04** | Hiển thị màn hình LCD I2C | Xuất dữ liệu chữ và số lên màn hình trực quan. | [Truy cập bài 4](./04_LCD_I2C) |
| **05** | Kết nối không dây ESP-NOW | Giao tiếp không dây tốc độ cao giữa 2 mạch ESP32. | [Truy cập bài 5](./05_ESP_NOW_Basic) |

---
*💡 Trong quá trình thực hành, nếu phát hiện lỗi code mẫu hoặc thư viện bị xung đột, xin vui lòng tạo một **GitHub Issue** để đội ngũ kỹ thuật của Mekong STEM kịp thời cập nhật và hỗ trợ.*
