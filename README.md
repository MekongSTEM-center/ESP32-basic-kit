# ⚡ KHO TÀI LIỆU KIT HỌC TẬP ESP32 BASIC KIT ⚡

Đây là kho tài nguyên mở, lưu trữ toàn bộ tài liệu hướng dẫn, sơ đồ mạch và mã nguồn mẫu sử dụng ngôn ngữ **MicroPython** cho bộ **ESP32 Basic Kit** từ **Mekong STEM** giúp bạn dễ dàng làm chủ công nghệ IoT và lập trình nhúng.

---

## 📌 1. GIỚI THIỆU BỘ KIT

**ESP32 Basic Kit** là bộ kit học tập lập trình phần cứng và IoT từ Mekong STEM được thiết kế tối ưu cho học sinh, sinh viên và người mới bắt đầu. Trung tâm của bộ kit là vi điều khiển **ESP32-WROOM-32** mạnh mẽ, tích hợp sẵn Wi-Fi và Bluetooth. 

Bộ kit này loại bỏ các rào cản phức tạp về hàn mạch, giúp người học tập trung hoàn toàn vào việc phát triển tư duy thuật toán, hiểu nguyên lý hoạt động của các linh kiện điện tử và tự tay xây dựng các ứng dụng tự động hóa thông minh trong đời sống.

---

## 📦 2. CÁC THÀNH PHẦN CƠ BẢN CỦA BỘ KIT

Gói sản phẩm bao gồm đầy đủ các module cảm biến, linh kiện ngoại vi và phụ kiện kết nối sau:

* **Khối xử lý & Hiển thị trung tâm:**
    * 1 x Board vi điều khiển ESP32
    * 1 x Màn hình hiển thị OLED 0.96 inch (Giao tiếp I2C trực quan)
* **Khối cảm biến & Dữ liệu đầu vào (Inputs):**
    * 1 x Module cảm biến nhiệt độ và độ ẩm DHT11
    * 1 x Module cảm biến ánh sáng (Quang trở)
    * 1 x Module cảm biến chuyển động PIR HC-SR501
    * 1 x Module cảm biến tránh chướng ngại vật LM393
    * 1 x Biến trở xoay 10K
    * 6 x Nút nhấn giữ/nhả (Kích thước 12x12)
* **Khối cơ cấu chấp hành & Cảnh báo (Outputs):**
    * 1 x Module Relay 2 kênh 5V (Hỗ trợ đóng cắt độc lập 2 thiết bị điện)
    * 1 x Buzzer thụ động (Phát âm thanh/nốt nhạc)
    * 1 x Buzzer hoạt động (Phát tiếng bíp cảnh báo cố định)
    * 15 x Đèn LED đơn (5 Đỏ, 5 Vàng, 5 Xanh lục) phục vụ dự án đèn giao thông
    * 1 x Đèn LED RGB (Lập trình phối màu sắc bất kỳ)
* **Khối phụ kiện kết nối & Lưu trữ:**
    * 1 x Breadboard MB102 (Bo cắm mạch cỡ lớn)
    * 1 x Cáp truyền dữ liệu (Cáp nạp code Micro-USB)
    * 30 x Dây cắm testboard (10 Đực - Cái, 10 Cái - Cái, 10 Đực - Đực)
    * 30 x Điện trở vạch chống cháy LED (10 cái 220R, 10 cái 1K, 10 cái 10K)
    * 1 x Hộp nhựa đựng toàn bộ Module gọn gàng
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
