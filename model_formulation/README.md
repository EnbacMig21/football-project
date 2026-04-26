# I. Ký hiệu và biến quyết định 
## 1. Tập hợp và chỉ số :
- I: tập hợp tất cả các cầu thủ , i ∈ I
- J: tập hợp tất cả các vị trí trên sân, j ∈ J
- Q: tập hợp tất cả các kỹ năng , q ∈ Q
- K: tập hợp các kịch bản chiến thuật, k ∈ K
## 2. Tham số 
$$
PS_{ij}*x_{ij}, \text{: Điểm đánh giá của cầu thủ i khi chơi tại vị trí j}
$$
$$
ge grade_{j} \text{:  Ngưỡi yêu cầu tối thiểu cho vị trí j}
$$
$$
S_{iq} \text{:  Điểm kỹ năng q của cầu thủ i}
$$
## 3. Biến quyết định 
$$
x_{ij} \text{= 1 nếu cầu thủ i được phân công vào vị trí j}
$$
$$
x_{ij} \text{= 0 nếu ngược lại}
$$
$$
y_{k} \text{: Biến nhị phân cho kịch bản chiến thuật k ∈ K}
$$
# II. Mô hình tối ưu hóa cơ bản 
Mô hình cơ bản không xét đến yêu cầu chiến thuật:


$$
\text{Max } \sum_{i \in I} \sum_{j \in J} PS_{ij}*x_{ij} 
$$

$$
 \text{s.t.}\sum_{i \in I} x_{ij} = 1, \quad \forall j \in J \quad  (1)
$$

$$
\sum_{j \in J} x_{ij} \le 1, \quad \forall i \in I \quad (2)
$$

$$
x_{ij} \in \{0, 1\}, \quad \forall i \in I, j \in J \quad (3)
$$

Trong đó:

-(1): Tối đa hóa tổng điểm phù hợp vị trí

-(2): Mỗi vị trí có đúng một cầu thủ

-(3): Mỗi cầu thủ chỉ đá tối đa một vị trí


# III. Chạy mô hình 

## [footballv6.py](https://github.com/EnbacMig21/football-project/blob/main/model_formulation/footballv6.py): Là mô hình tối ưu hóa được viết bằng ngôn ngữ Python.

## [team_profile (2).csv](https://github.com/EnbacMig21/football-project/blob/main/model_formulation/team_profile%20(2).csv): Là các kịch bản chiến thuật nhưng do đang xét mô hình cơ bản nên sẽ không có kịch bản nào trong file này. 

## [player_position_scores.csv](https://github.com/EnbacMig21/football-project/blob/main/processing-raw-data/processed/player_position_scores.csv): Đây là dữ liệu của tất cả các cầu thủ, khi đá tại tất cả các vị trí trên sân .
## Kết quả sau khi chạy mô hình.
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
