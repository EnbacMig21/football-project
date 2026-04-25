# Xây dựng mô hình tối ưu hóa đội hình bóng đá 

Ở đây chúng tôi xây dựng mô hình tối ưu cho một đội bóng dựa trên dữ liệu thu thập được từ thực tế. Quá trình xây dựng mô hình sẽ bao gồm các quy trình bên dưới, mong bạn dành chút thời gian đọc nó.
1. [Đặt vấn đề](https://github.com/EnbacMig21/football-project/blob/main/README.md#1-%C4%91%E1%BA%B7t-v%E1%BA%A5n-%C4%91%E1%BB%81)
2. Thu thập dữ liệu
3. Xử lý dữ liệu các cầu thủ
4. Mô hình hóa bài toán và các ràng buộc
5. Mở rộng mô hình với hồ sơ đội bóng
6. Ví dụ cụ thể
## 1. Đặt vấn đề 
### Giới thiệu chung 
Bóng đá (soccer hay football) là những tên gọi phổ biến nhất cho môn bóng đá liên đoàn. Để phân biệt trò chơi với một số môn thể thao khác chơi bằng chân vào thế kỷ 18, tên gọi bóng đá liên đoàn đã được đặt ra. Các quy tắc hiện đại mà chúng ta quen thuộc ngày nay có nguồn gốc từ giữa thế kỷ 19. 
### Vấn đề 
Trong bối cảnh bóng đá hiện đại, việc xây dựng đội hình tối ưu không chỉ dựa trên kinh nghiệm và cảm nhận của huấn luyện viên, mà ngày càng được hỗ trợ bởi các phương pháp phân tích dữ liệu và mô hình toán học. Việc tận dụng nguồn dữ liệu phong phú từ các trận đấu thực tế để đưa ra quyết định khách quan và khoa học đang trở thành một hướng nghiên cứu đầy tiềm năng. Từ đó giúp các đội bóng có những lựa chọn đúng đắn khi tham gia vào thị trường chuyển nhượng để tránh dư thừa hoặc thiếu hụt tại các vị trí.
