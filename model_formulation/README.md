# I. Ký hiệu và biến quyết định 
## 1. Tập hợp và chỉ số :
- I: tập hợp tất cả các cầu thủ , i ∈ I
- J: tập hợp tất cả các vị trí trên sân, j ∈ J
- Q: tập hợp tất cả các kỹ năng , q ∈ Q
## 2. Tham số 
-
$$
PS_{ij}*x_{ij}, \text{Điểm đánh giá của cầu thủ i khi chơi tại vị trí j}
$$

$$
 \text{s.t.}\sum_{i \in I} x_{ij} = 1, \quad \forall j \in J \quad  (1)
$$
Trong đó:

(1): Tối đa hóa tổng điểm phù hợp vị trí

(2): Mỗi vị trí có đúng một cầu thủ

(3): Mỗi cầu thủ chỉ đá tối đa một vị trí


$$
\sum_{i \in I} S_{iq_{n}} *x_{ij_{n}} \ge grade_{j_{n}}*y_{n}, \text{           n=1,...,N}
$$

$$
\sum_{i \in I} y_{n} = 1, \text{ với }y_{n} \in \{0, 1\},\text{           n=1,...,N}
$$

