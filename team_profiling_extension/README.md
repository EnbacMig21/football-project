# Mở rộng mô hình đội bóng 
Để tối ưu hóa đội hình một cách toàn diện hơn, mô hình quy hoạch số nguyên cơ bản cần được mở rộng. để tích hợp các yếu tố phức tạp liên quan đến sự tương tác giữa các cầu thủ và chiến thuật của đội bóng. Hồ sơ đội bóng bao gồm nhiều kịch bản chiến thuật thuộc 4 nhóm:Để tối ưu hóa đội hình một cách toàn diện hơn, mô hình quy hoạch số nguyên cơ bản cần được mở rộng. để tích hợp các yếu tố phức tạp liên quan đến sự tương tác giữa các cầu thủ và chiến thuật của đội bóng. Hồ sơ đội bóng bao gồm nhiều kịch bản chiến thuật thuộc 4 nhóm:
| Kịch bản chiến thuật | Mô tả | 
|----------------------| -------------|
|Dứt điểm (Shots) | Bao gồm 9 kịch bản . Trong đó các kịch bản với yêu cầu như: ít nhất 1 Tiền vệ hoặc Tiền đạo với kỹ năng dứt điểm hoặc sút xa,….Bao gồm 9 kịch bản . Trong đó các kịch bản với yêu cầu như: ít nhất 1 Tiền vệ hoặc Tiền đạo với kỹ năng dứt điểm hoặc sút xa,…. |
| Tạt bóng (Crosses) | Bao gồm 13 kịch bản ví dụ như:  ít nhất 1 cầu thủ có khả năng tạt bóng chính xác có thể là tiền vệ hoặc hậu vệ cánh,…. |
| Cắt bóng (Interceptions) | Bao gồm 12 kịch bản: có ít nhất 1 tiền vệ trung tâm có kỹ năng cắt bóng chính xác,… |
| Chuyền bóng (Passes) | Bao gồm 18 kịch bản VD: có ít nhất 1 hậu vệ có kỹ năng chuyền bóng,… |

Lưu ý :Mỗi kịch bản k yêu cầu: ít nhất một cầu thủ ở một trong các vị trí được chỉ định có kỹ năng đạt ngưỡng yêu cầu.
# Cấu trúc ràng buộc theo số điều kiện 
Trong mô hình mở rộng, chúng ta cần xem xét các ràng buộc dựa trên số lượng điều kiện mà một kịch bản chiến thuật yêu cầu. Chúng ta gọi N là tổng số điều kiện ( kỹ năng x vị trí) phải được thỏa mãn trong một kịch bản chiến thuật cụ thể.
## Trường hợp N = 1: Kịch bản chỉ có một điều kiện duy nhất


$$
\sum_{i \in I} S_{iq}* x_{ij} \ge grade_{j}
$$

## Trường hợp N = 2: Kịch bản có hai khả năng thỏa mãn, cần ít nhất một điều kiện đạt:

$$
\sum_{i \in I} S_{iq_{1}} *x_{ij_{1}} \ge grade_{j_{1}}*y
$$


$$
\sum_{i \in I} S_{iq_{2}} \cdot x_{ij_{1}} \ge grade_{j_{1}} \cdot (1-y)
$$


$$
\text{với }y \in \{0, 1\}
$$

## Trường hợp N > 2: Với N điều kiện, cần N biến nhị phân:

$$
\sum_{i \in I} S_{iq_{n}} *x_{ij_{n}} \ge grade_{j_{n}}*y_{n}, \text{           n=1,...,N}
$$

$$
\sum_{i \in I} y_{n} = 1, \text{ với }y_{n} \in \{0, 1\},\text{           n=1,...,N}
$$

## Ví dụ minh họa 
- # Ví dụ một vị trí nhiều kịch bản
Xét kỹ năng tạt bóng của vị trí MC với 3 kịch bản :
Tham số: q = Crossing, N = 3.
Ràng buộc: 

$$
\sum_{i \in I_k} S_{i,Crossing}*x_{i,MC} \ge 7*y_{1}
$$

$$
\sum_{i \in I_k} S_{i,Crossing}*x_{i,MC} \ge 8*y_{2}
$$

$$
\sum_{i \in I_k} S_{i,Crossing}*x_{i,MC} \ge 6*y_{3}
$$

$$
y_{1} + y_{2}+y_{3}=1,y_{1} ,y_{2},y_{3} \in \{0,1\}
$$

