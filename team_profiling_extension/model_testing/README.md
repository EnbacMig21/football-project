# Chạy mô hình với bộ dữ liệu và các kịch bản cụ thể 
[footballv6.py](https://github.com/EnbacMig21/football-project/blob/main/team_profiling_extension/model_testing/footballv6.py): Nơi chạy chương trình được code bằng Python

[team_profile (1).csv](https://github.com/EnbacMig21/football-project/blob/main/team_profiling_extension/model_testing/team_profile%20(1).csv) : Ghi các kịch bản yêu cầu thêm

| Tên cột | Ý nghĩa  |
| --------------| -------------|
| Scenario | Một trong 4 kịch bản, bao gồm Shots, Crosses, Interceptions, Passes | 
| RequiredSkill | Kĩ năng yêu cầu |
| Grade | Ngưỡng điểm tối thiểu của kĩ năng |

Với các kịch bản: 
- Shots: Ta xét các vị trí tấn công như FR, FC, FL.
- Crosses: Ta xét các vị trí DC và DR
- Interceptions: Ta xét DCR, DR, DCL, DL
- Passes: MCR, MC, MCL
## Sau khi ta vận hành mô hình với bộ dữ liệu thực tế 
Ta giả sử yêu cầu về [kịch bản chiến thuật](https://github.com/EnbacMig21/football-project/blob/main/team_profiling_extension/model_testing/team_profile%20(1).csv)
- Với Shots: yêu cầu điểm kĩ năng Finishing tổi thiểu là 10
- Với Crosses: yêu cầu điểm kĩ năng Cross tổi thiểu là 10
- Với Interceptions: yêu cầu điểm kĩ năng Interceptions tổi thiểu là 10
- Với Passes: yêu cầu điểm kĩ năng Short pass tổi thiểu là 10
### [player_position_scores.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/processed/player_position_scores.csv): bảng chứa điểm đánh giá từng cầu thủ Ajax khi chơi ở tất cả các vị trí trên sân của mùa giải 2010-2011.
| Vị trí     	| Tên cầu thủ | Số điểm |
|--------------	|----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------|
| GK | Steekelenburg | 103.21 |
| DR | Sulejmani | 80.74 |
| DCR | Alderweireld | 102.48 |
| DCL | Vertonghen | 103.08 |
| DL | Anita | 62.41 |
| MCR | Zeeuw | 68.76 |
| MC | de Jong | 58.75 |
| MCL | Wiel | 49.46 |
| FR | Eriksen | 76.85 |
| FC | Ebecilio|  60.36 |
| FL |  Suarez | 55.42 |


Total Score: 821.52
