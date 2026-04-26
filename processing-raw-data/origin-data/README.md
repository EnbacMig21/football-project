# Thu thập dữ liệu các chỉ số của cầu thủ 
Để minh họa mô hình chúng tôi sử dụng một bộ dữ liệu thực tế.
## Hồ sơ chi tiết của tất cả 29 cầu thủ của câu lạc bộ Ajax trong mùa giải 2010-2011:[player_skill.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/origin-data/player_skill.csv)
| Tên cột      	| Ý nghĩa|
|--------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Player        	| Tên của các cầu thủ |
| Short pass back     	| Chuyền ngắn về phía sau  |
| Short pass forward   	| Chuyền ngắn lên phía trước    |
| Short pass wide	| Chuyền ngắn ra biên   |
| Long pass back	| Chuyền dài về phía sau |
| Long pass forward	| Chuyền dài lên phía trước  |
| Long pass wide	| Chuyền dài ra biên  | 
| Cross	 | Tạt bóng  |
| Heading	 | Đánh đầu  |
| Finishing	 | Dứt điểm   | 
| Long shot	 | Sút xa |
| Dribbles	 | Rê dắt bóng, qua người  | 
|  Reception	| Khống chế bóng bước một  |
| Interceptions	 | Cắt bóng |
| Goalkeeping	 | Cản phá bóng(GK)  |
| Goal kick	 | Phát bóng dài (GK)  |
| Set pieces	| Tình huống cố định   |
| Short pass	 | Chuyền ngắn (Tổng quát)  |
| Long Passes	 | Chuyền dài(Tổng quát)  |
| Pressing	    | Áp sát, gây áp lực |
## Bảng hệ số của các kỹ năng tại từng vị trí trên sân: [pos_weights_criteria.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/origin-data/pos_weights_criteria.csv)
| Tên hàng | Ý nghĩa |
|--------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| GK	|Thủ môn  |
| DR	| Hậu vệ cánh phải |
| DCR	 |Trung vệ lệch phải  |
| DCL	| Trung vệ lệch trái  |
| DL	 | Hậu vệ cánh trái  |
| MCR	 | Tiền vệ trung tâm lệch phải |
| MC	| Tiền vệ trung tâm |
| MCL	 | Tiền vệ trung tâm lệch trái  |
| FR	| Tiền đạo cánh phải  |
| FC	| Tiền đạo cắm  |
| FL	| Tiền đạo cánh trái|
