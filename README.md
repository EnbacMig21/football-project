# Xây dựng mô hình tối ưu hóa đội hình bóng đá 

Ở đây chúng tôi xây dựng mô hình tối ưu cho một đội bóng dựa trên dữ liệu thu thập được từ thực tế. Quá trình xây dựng mô hình sẽ bao gồm các quy trình bên dưới, mong bạn dành chút thời gian đọc nó.
1. [Hiểu bài toán](https://github.com/EnbacMig21/football-project/blob/main/README.md#1-%C4%91%E1%BA%B7t-v%E1%BA%A5n-%C4%91%E1%BB%81)
2. Thu thập dữ liệu
3. Xử lý dữ liệu các cầu thủ
4. Mô hình hóa bài toán và các ràng buộc
5. Mở rộng mô hình với hồ sơ đội bóng
6. Ví dụ cụ thể
# Danh mục nội dung 
- [Đặt vấn đề](https://github.com/EnbacMig21/football-project/blob/main/README.md#1-%C4%91%E1%BA%B7t-v%E1%BA%A5n-%C4%91%E1%BB%81)
- [Mục tiêu phân tích](https://github.com/EnbacMig21/football-project/blob/main/README.md#m%E1%BB%A5c-ti%C3%AAu)
## 1. Đặt vấn đề 
### Giới thiệu chung 
Bóng đá (soccer hay football) là những tên gọi phổ biến nhất cho môn bóng đá liên đoàn. Để phân biệt trò chơi với một số môn thể thao khác chơi bằng chân vào thế kỷ 18, tên gọi bóng đá liên đoàn đã được đặt ra. Các quy tắc hiện đại mà chúng ta quen thuộc ngày nay có nguồn gốc từ giữa thế kỷ 19. 
### Tại sao cần xây dựng mô hình tối ưu hóa 
Trong bóng đá truyền thống, việc lựa chọn đội hình thường dựa vào trực giác và kinh nghiệm cá nhân của Huấn luyện viên. Tuy nhiên, khi bóng đá trở thành một ngành công nghiệp trị giá hàng tỷ đô la, sai lầm trong việc dùng người hoặc chuyển nhượng có thể gây ra thiệt hại khổng lồ. Việc xây dựng mô hình tối ưu hóa là cấp thiết vì những lý do sau:
- #### Loại bỏ định kiến cá nhân (Bias)
  Mọi HLV đều có những thiên kiến nhất định về lối chơi hoặc sự yêu thích dành cho một vài cầu thủ. Mô hình toán học đóng vai trò như một "trọng tài khách quan", đánh giá cầu thủ dựa trên các con số cụ thể (bàn thắng kỳ vọng xG, tỷ lệ chuyền bóng, khả năng đánh chặn...), từ đó tìm ra những "viên ngọc thô" bị đánh giá thấp nhưng có đóng góp cực lớn vào lối chơi chung.
- #### Giải quyết bài toán ràng buộc (Constraints Mapping)
  Việc chọn đội hình không đơn giản là đưa 11 người giỏi nhất vào sân. Nó là một bài toán tối ưu với hàng loạt ràng buộc thực tế:
Ngân sách: Tổng lương hoặc giá trị chuyển nhượng không được vượt quá quỹ của CLB.

Sự tương thích: Các cầu thủ phải có bộ kỹ năng bổ trợ cho nhau (ví dụ: một tiền vệ kiến thiết cần đi đôi với một tiền đạo chạy chỗ thông minh).

Chiến thuật: Phải đảm bảo đủ vị trí (GK, DF, MF, FW) theo sơ đồ đề ra.
## Mục tiêu 
Trong bối cảnh bóng đá hiện đại, việc xây dựng đội hình tối ưu không chỉ dựa trên kinh nghiệm và cảm nhận của huấn luyện viên, mà ngày càng được hỗ trợ bởi các phương pháp phân tích dữ liệu và mô hình toán học. Việc tận dụng nguồn dữ liệu phong phú từ các trận đấu thực tế để đưa ra quyết định khách quan và khoa học đang trở thành một hướng nghiên cứu đầy tiềm năng. Từ đó giúp các đội bóng có những lựa chọn đúng đắn khi tham gia vào thị trường chuyển nhượng, tránh dư thừa hoặc thiếu hụt tại các vị trí.

Tóm lại, mô hình sẽ giúp các đội bóng đánh giá được cầu thủ chơi tốt nhất tại từng vị trí. Qua đó có thể nhìn thấy sự chênh lệch trình độ, vị trí mà cầu thủ đó chơi tốt nhất. Giúp các đội bóng đánh giá vị trí cần thay đổi và bổ sung để phân bổ ngân sách chuyển nhượng cho hợp lý. Các CLB sẽ có sự chuẩn bị tốt nhất cho các mùa giải tiếp theo. Giúp đội bóng từng bước phát triển và thành công hơn mùa giải trước.Đồng thời cũng có thể đánh giá đội hình của các đội bóng khác, phục vụ cho việc phân tích đối thủ hay mục tiêu chuyển nhượng phù hợp. 
