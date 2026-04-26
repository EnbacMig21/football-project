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
