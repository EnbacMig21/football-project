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
