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
    * 1 x Module cảm biến vật cản LM393
    * 1 x Biến trở xoay 10K
    * 6 x Nút nhấn giữ/nhả (Kích thước 12x12)
* **Khối cơ cấu chấp hành & Cảnh báo (Outputs):**
    * 1 x Module Relay 2 kênh 5V (Hỗ trợ đóng cắt độc lập 2 thiết bị điện)
    * 1 x Buzzer thụ động (Phát âm thanh/nốt nhạc)
    * 1 x Buzzer hoạt động (Phát tiếng bíp cảnh báo cố định)
    * 15 x Đèn LED đơn (5 Đỏ, 5 Vàng, 5 Xanh lục)
    * 1 x Đèn LED RGB (Lập trình phối màu sắc bất kỳ)
* **Khối phụ kiện kết nối & Lưu trữ:**
    * 1 x Breadboard MB102 (Bo cắm mạch cỡ lớn)
    * 1 x Cáp truyền dữ liệu (Cáp nạp code Micro-USB)
    * 30 x Dây cắm testboard (10 Đực - Cái, 10 Cái - Cái, 10 Đực - Đực)
    * 30 x Điện trở vạch chống cháy LED (10 cái 220R, 10 cái 1K, 10 cái 10K)
    * 1 x Hộp nhựa đựng toàn bộ Module
---

## 🛠️ 3. HƯỚNG DẪN SỬ DỤNG TRANG GITHUB NÀY

Để người học tra cứu và thực hành, toàn bộ các bài học trong kho lưu trữ này được chia thành các **Thư mục dự án** 
Khi bạn bấm truy cập vào bất kỳ một thư mục dự án nào, cấu trúc bên trong gồm **3 phần** sau:

### 📑 Phần 1: Hướng dẫn lý thuyết & Nhiệm vụ 

* Mục tiêu của bài học (Ví dụ: Đọc cảm biến ánh sáng, khi tối thì bật đèn).
* Nguyên lý hoạt động của linh kiện mới xuất hiện trong bài.
* Giải thích chi tiết các câu lệnh MicroPython quan trọng được sử dụng.
* Sơ đồ kết nối trực quan mô tả cách đi dây từ board ESP32 sang các linh kiện trên breadboard.
* Sơ đồ được vẽ ở dạng **hình ảnh thực tế** giúp học sinh nhìn rõ từng màu dây, từng chân cắm (GPIO nào nối với chân nào của cảm biến) để thao tác theo một cách chính xác nhất, tránh nguy cơ cắm ngược chân gây hỏng mạch.

### 💻 Phần 2: Mã nguồn lập trình mẫu (`main.py`)
* File code mẫu MicroPython hoàn chỉnh.
* Trong code được **chú thích bằng tiếng Việt** rõ ràng ở các dòng lệnh quan trọng, giúp người học hiểu rõ bản chất của thuật toán.


---
*💡 Trong quá trình thực hành, nếu phát hiện lỗi code mẫu hoặc thư viện bị xung đột, xin vui lòng tạo một **GitHub Issue** để đội ngũ kỹ thuật của Mekong STEM kịp thời cập nhật và hỗ trợ.*
