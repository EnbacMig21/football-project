# Xây dựng mô hình tối ưu hóa đội hình bóng đá 

Ở đây chúng tôi xây dựng mô hình tối ưu cho một đội bóng dựa trên dữ liệu thu thập được từ thực tế. Quá trình xây dựng mô hình sẽ bao gồm các quy trình bên dưới, mong bạn dành chút thời gian đọc nó.
1. [Hiểu bài toán](https://github.com/EnbacMig21/football-project/blob/main/README.md#1-%C4%91%E1%BA%B7t-v%E1%BA%A5n-%C4%91%E1%BB%81)
2. [Thu thập dữ liệu](https://github.com/EnbacMig21/football-project/tree/main/processing-raw-data/origin-data)
3. [Xử lý dữ liệu các cầu thủ](https://github.com/EnbacMig21/football-project/tree/main/processing-raw-data/processed)
4. [Mô hình hóa bài toán và các ràng buộc](https://github.com/EnbacMig21/football-project/tree/main/model_formulation)
5. [Mở rộng mô hình với hồ sơ đội bóng](https://github.com/EnbacMig21/football-project/tree/main/team_profiling_extension)

Trong file README.md này sẽ là giải thích thứ tự file nên đọc theo và giải thích tổng quan về mỗi file sẽ bao gồm những gì. File cũng sẽ có một danh mục nội dung phía dưới đây để phục vụ cho việc tra cứu.
# Danh mục nội dung 
- [Đặt vấn đề](https://github.com/EnbacMig21/football-project/blob/main/README.md#1-%C4%91%E1%BA%B7t-v%E1%BA%A5n-%C4%91%E1%BB%81)
- [Mục tiêu phân tích](https://github.com/EnbacMig21/football-project/blob/main/README.md#m%E1%BB%A5c-ti%C3%AAu)
- [Giải thích](https://github.com/EnbacMig21/football-project/blob/main/README.md#gi%E1%BA%A3i-th%C3%ADch)
- [Lời kết](https://github.com/EnbacMig21/football-project/blob/main/README.md#gi%E1%BA%A3i-th%C3%ADch)
## 1. Đặt vấn đề 
### Giới thiệu chung 
Bóng đá (soccer hay football) là những tên gọi phổ biến nhất cho môn bóng đá liên đoàn. Để phân biệt trò chơi với một số môn thể thao khác chơi bằng chân vào thế kỷ 18, tên gọi bóng đá liên đoàn đã được đặt ra. Các quy tắc hiện đại mà chúng ta quen thuộc ngày nay có nguồn gốc từ giữa thế kỷ 19. 
### Tại sao cần xây dựng mô hình tối ưu hóa 
Trong bóng đá truyền thống, việc lựa chọn đội hình thường dựa vào trực giác và kinh nghiệm cá nhân của Huấn luyện viên. Tuy nhiên, khi bóng đá trở thành một ngành công nghiệp trị giá hàng tỷ đô la, sai lầm trong việc dùng người hoặc chuyển nhượng có thể gây ra thiệt hại khổng lồ. Việc xây dựng mô hình tối ưu hóa là cấp thiết vì những lý do sau:
- #### Loại bỏ định kiến cá nhân (Bias)
  Mọi HLV đều có những ý kiến nhất định về lối chơi hoặc sự yêu thích dành cho một vài cầu thủ. Mô hình toán học đóng vai trò như một "trọng tài khách quan", đánh giá cầu thủ dựa trên các con số cụ thể (bàn thắng kỳ vọng xG, tỷ lệ chuyền bóng, khả năng đánh chặn...), từ đó tìm ra những "viên ngọc thô" bị đánh giá thấp nhưng có đóng góp cực lớn vào lối chơi chung.
- #### Giải quyết bài toán ràng buộc (Constraints Mapping)
  Việc chọn đội hình không đơn giản là đưa 11 người giỏi nhất vào sân. Nó là một bài toán tối ưu với hàng loạt ràng buộc thực tế:
Ngân sách: Tổng lương hoặc giá trị chuyển nhượng không được vượt quá quỹ của CLB.

Sự tương thích: Các cầu thủ phải có bộ kỹ năng bổ trợ cho nhau (ví dụ: một tiền vệ kiến thiết cần đi đôi với một tiền đạo chạy chỗ thông minh).

Chiến thuật: Phải đảm bảo đủ vị trí (GK, DF, MF, FW) theo sơ đồ đề ra.
- #### Quản trị rủi ro và Hiệu quả kinh tế
Trên thị trường chuyển nhượng, các CLB lớn thường phải đối mặt với tình trạng "thổi giá". Mô hình tối ưu giúp xác định giá trị thực của cầu thủ dựa trên hiệu suất (Performance-to-Price ratio). Điều này giúp các đội bóng có ngân sách hạn hẹp vẫn có thể cạnh tranh sòng phẳng với các "ông lớn" bằng cách tối ưu hóa từng đồng vốn bỏ ra.
- #### Liên hệ ứng dụng trong thực tế
Trường hợp của Brentford và Brighton (Ngoại hạng Anh): Đây là những ví dụ điển hình nhất. Họ sử dụng các mô hình tối ưu hóa để tìm ra các cầu thủ từ các giải đấu cấp thấp với giá rẻ, nhưng có chỉ số tương đương với các ngôi sao lớn. Sau đó, họ bán lại với giá cao gấp 10-20 lần sau khi tối ưu hóa vị trí thi đấu của họ.

Liverpool dưới thời Jürgen Klopp: Sự thành công của Liverpool gắn liền với bộ phận phân tích dữ liệu của Ian Graham. Mô hình của họ không chỉ tìm cầu thủ giỏi, mà tìm cầu thủ "tối ưu nhất" cho hệ thống Gegenpressing, giúp họ giành Champions League và Premier League với mức chi tiêu thông minh.

Phân tích đối thủ: Các đội bóng sử dụng mô hình để giả lập các đội hình khác nhau của đối thủ trong trận đấu tới, từ đó tìm ra phương án tối ưu để khắc chế dựa trên điểm yếu về chỉ số của hàng phòng ngự đối phương.
## Mục tiêu 
Trong bối cảnh bóng đá hiện đại, việc xây dựng đội hình tối ưu không chỉ dựa trên kinh nghiệm và cảm nhận của huấn luyện viên, mà ngày càng được hỗ trợ bởi các phương pháp phân tích dữ liệu và mô hình toán học. Việc tận dụng nguồn dữ liệu phong phú từ các trận đấu thực tế để đưa ra quyết định khách quan và khoa học đang trở thành một hướng nghiên cứu đầy tiềm năng. Từ đó giúp các đội bóng có những lựa chọn đúng đắn khi tham gia vào thị trường chuyển nhượng, tránh dư thừa hoặc thiếu hụt tại các vị trí.

Tóm lại, mô hình sẽ giúp các đội bóng đánh giá được cầu thủ chơi tốt nhất tại từng vị trí. Qua đó có thể nhìn thấy sự chênh lệch trình độ, vị trí mà cầu thủ đó chơi tốt nhất. Giúp các đội bóng đánh giá vị trí cần thay đổi và bổ sung để phân bổ ngân sách chuyển nhượng cho hợp lý. Các CLB sẽ có sự chuẩn bị tốt nhất cho các mùa giải tiếp theo. Giúp đội bóng từng bước phát triển và thành công hơn mùa giải trước.Đồng thời cũng có thể đánh giá đội hình của các đội bóng khác, phục vụ cho việc phân tích đối thủ hay mục tiêu chuyển nhượng phù hợp. 
## Giải thích 
Các giải thích về cách đọc repo có thể được tìm thấy trong phần này.

File đầu tiên cần đọc là phần tiền xử lý dữ liệu, hay processing raw data. Tại đây, có hai tệp chính: dữ liệu gốc – dùng để kiểm tra dữ liệu ban đầu, và dữ liệu đã qua xử lý – giúp theo dõi cách dữ liệu được biến đổi thông qua tệp .py. Tiếp theo là model_formulation mô tả mô hình kèm các ràng buộc cho mô hình tối ưu hóa đơn giản. Đồng thời, file này cũng thể hiện kết quả của mô hình đơn giản khi vận hành mô hình. Cuối cùng là team_profiling_extension, nơi mở rộng mô hình và phát triển thêm các kịch bản chiến thuật . Tại đây, có thể tìm thấy dữ liệu đã qua xử lý và kết quả khi thực hiện mô hình với các kịch bản, yêu cầu mới.
Mỗi file đều có kèm một file README nên được đọc trước khi nghiên cứu các nội dung bên trong file đó.

Các công nghệ được sử dụng trong bài bao gồm:

- Excel (.csv): chứa tệp dữ liệu chung.
- Python: công nghệ chính được xây dựng và vận hành mô hình.
## Lời kết 
Dự án này là kết quả của quá trình tự nghiên cứu và niềm đam mê ứng dụng các mô hình toán học vào các bài toán thực tế của em. Với tư cách là một sinh viên chuyên ngành Toán - Tin tại trường Đại học Khoa học Tự nhiên, em tin rằng mọi vấn đề phức tạp trong vận hành hay kinh doanh đều có thể được tối ưu hóa thông qua dữ liệu và các thuật toán phù hợp.

Dù đây mới chỉ là những bước đi đầu tiên trong việc xây dựng mô hình, dự án đã giúp em rèn luyện tư duy logic, kỹ năng xử lý dữ liệu và khả năng lập trình Python một cách bài bản. Em rất mong nhận được những ý kiến đóng góp từ các anh chị và các bạn độc giả để mô hình này ngày càng hoàn thiện và thực tế hơn.

Em xin chân thành cảm ơn mọi người đã dành thời gian theo dõi dự án này. Hy vọng những chia sẻ này có thể mang lại một góc nhìn mới mẻ về việc kết hợp giữa toán học và bóng đá.

Thông tin liên hệ:

- Tác giả: Nguyễn Văn Bình

- Email: binhnguyenvan422@gmail.com

- GitHub: https://github.com/EnbacMig21
