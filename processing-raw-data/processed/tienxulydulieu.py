import pandas as pd

# 1. Đọc dữ liệu và thiết lập cột đầu tiên làm chỉ mục (Index)
# Giả sử cột đầu tiên của player_skills là Tên cầu thủ
df_skills = pd.read_csv(r"C:\toi_uu_hoa\player_skills.csv")

# Giả sử cột đầu tiên của pos_weights_criteria là Tên vị trí
df_weights = pd.read_csv(r"C:\toi_uu_hoa\pos_weights_criteria.csv")

# 2. Chuẩn hóa tên cột (Viển hoa/thường và khoảng trắng)
# Việc này giúp khớp "Long passes" với "Long Passes"
df_skills.columns = [c.strip().lower() for c in df_skills.columns]
df_weights.columns = [c.strip().lower() for c in df_weights.columns]

# 3. Thiết lập chỉ mục (Index)
# Trong file skills, cột đầu tiên là tên cầu thủ (player)
# Trong file weights, cột đầu tiên là tên vị trí (player/position)
df_skills = df_skills.set_index('player')
df_weights = df_weights.set_index('player')

# 4. Chuyển vị ma trận trọng số: (Vị trí x Kỹ năng) -> (Kỹ năng x Vị trí)
df_weights_T = df_weights.T

# 5. Lấy các kỹ năng chung của cả 2 bảng để đảm bảo phép nhân ma trận hợp lệ
common_skills = df_skills.columns.intersection(df_weights_T.index)
df_skills_filtered = df_skills[common_skills]
df_weights_T_filtered = df_weights_T.loc[common_skills]

# 6. Thực hiện nhân ma trận (Chỉ số cầu thủ = Điểm kỹ năng x Trọng số vị trí)
# Kết quả sẽ là một bảng với: Hàng = Tên cầu thủ, Cột = Vị trí
result = df_skills_filtered.dot(df_weights_T_filtered)
result = result.round(2)

# 7. Xuất kết quả ra file CSV
result.to_csv(r"C:\toi_uu_hoa\player_position_scores.csv")

print("Đã xử lý thành công! File 'player_position_scores.csv' đã được tạo.")
print(result.head())
