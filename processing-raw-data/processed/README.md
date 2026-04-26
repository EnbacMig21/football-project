# [Xử lý dữ liệu](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/processed/tienxulydulieu.py)
Chúng ta có bảng [player_skill.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/origin-data/player_skill.csv) là bảng chứa điểm đánh giá các kỹ năng của từng cầu thủ Ajax của mùa giải 2010-2011. Và bảng [pos_weights_criteria.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/origin-data/pos_weights_criteria.csv) là bảng hệ số của các kỹ năng tại từng vị trí. Khi đó , ta lấy bảng player_skill.csv nhân với bảng pos_weights_criteria.cs để ra được bảng [player_position_scores.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/processed/player_position_scores.csv). Bảng player_position_scores.csv thể hiện điểm đánh giá của từng cầu thủ khi chơi ở tất cả các vị trí trên sân. Hỗ trợ các quy trình xây dựng mô hình tiếp theo.
# Bảng player_position_scores.csv
| Tên cột      	| Ý nghĩa|
|--------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Player        	| Tên của các cầu thủ |
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
