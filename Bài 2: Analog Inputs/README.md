# 📘 Bài 3: ESP32 Analog Inputs

Dự án này hướng dẫn cách đọc tín hiệu đầu vào Analog với ESP32 sử dụng MicroPython. Việc đọc giá trị Analog rất hữu ích để lấy dữ liệu từ các biến trở hoặc các cảm biến analog.

---

## ⚡ 1. Tín Hiệu Đầu Vào Analog (ADC)

Đọc một giá trị analog với ESP32 có nghĩa là bạn có thể đo lường các mức điện áp biến thiên trong khoảng giữa 0V và 3.3V. 

Điện áp đo được sau đó sẽ được chuyển đổi thành một giá trị số nguyên nằm trong khoảng từ 0 đến 4095 (12-bit):
* Mức điện áp 0V tương ứng với giá trị số 0.
* Mức điện áp 3.3V tương ứng với giá trị số 4095.
* Bất kỳ mức điện áp nào nằm giữa 0V và 3.3V sẽ được quy đổi thành giá trị tương ứng nằm trong khoảng giữa.
  
<img width="573" height="209" alt="image" src="https://github.com/user-attachments/assets/fc86b392-2ef1-4fa3-baad-884d0671089b" />

---

## ⚠️ 2. Đặc Tính Phi Tuyến Của ADC (ADC is Non-linear)

Về mặt lý thuyết, bộ chuyển đổi ADC của ESP32 sẽ hoạt động theo đường tuyến tính thẳng. Tuy nhiên, trên thực tế điều đó không xảy ra. Đặc tính phi tuyến này dẫn đến các giới hạn sau:
* ESP32 không thể phân biệt được mức điện áp 3.2V và 3.3V. Cả hai mức điện áp này đều trả về cùng một giá trị là 4095.
* Hiện tượng tương tự xảy ra ở vùng điện áp cực thấp: mức điện áp từ 0V đến 0.1V đều sẽ trả về cùng một giá trị là 0.

 Bạn cần lưu ý đặc tính này khi sử dụng các chân ADC của ESP32.
<img width="790" height="489" alt="image" src="https://github.com/user-attachments/assets/a965a9d9-b4d3-46f3-b3a4-efdaa0bd738f" />

---

## 📌 3. Quy Hoạch Chân Chức Năng (Pinout)

* Chỉ có 15 chân ADC có sẵn trên board mạch DEVKIT V1 (phiên bản 30 chân GPIO).
* **Lưu ý quan trọng:** Các chân thuộc nhóm ADC2 không thể sử dụng khi chức năng Wi-Fi được kích hoạt. Nếu bạn đang sử dụng Wi-Fi và gặp lỗi không lấy được giá trị từ một chân ADC2,
hãy cân nhắc chuyển sang sử dụng một chân thuộc nhóm ADC1 để giải quyết vấn đề (Sơ đồ các chân của ESP32
đã được đề cập ở những phần trước). 

---

## 📦 4. Thành Phần Linh Kiện (Parts Required)

* 1 x Mạch ESP32 DEVKIT V1 Board.
* 1 x Biến trở xoay (Potentiometer).
* 1 x Bo cắm mạch (Breadboard).
* Dây bus cắm mạch (Jumper wires).

---

## 🔌 5. Sơ Đồ Đấu Nối (Schematic)

Tiến hành kết nối biến trở với board mạch ESP32 theo sơ đồ phối chân:
* Hai chân biên của biến trở nối lần lượt vào hàng nguồn **3V3** và **GND** của ESP32.
* Chân ở giữa (chân tín hiệu) của biến trở được kết nối trực tiếp vào chân **GPIO 4** (tương ứng với kênh ADC2_CH0).

<img width="790" height="553" alt="image" src="https://github.com/user-attachments/assets/3d5b636a-0c37-4187-a509-902f55106d79" />

---

## 💻 6. Lập Trình

Phần lập trình chi tiết được trình bày trong file '**main.py**'

## 🚀 7. Kiểm Thử Dự Án (Testing the Example)
* Nạp tệp code trên vào mạch ESP32 thông qua phần mềm Thonny IDE.

* Mở cửa sổ Terminal / Shell giám sát lệnh.

* Tiến hành xoay trục của biến trở và quan sát các giá trị số thay đổi trực thời trên màn hình.

* Giá trị tối đa thu được khi xoay kịch khung về hướng 3.3V là 4095, và giá trị tối thiểu khi xoay về hướng 0V là 0.
