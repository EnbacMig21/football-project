import gurobipy as gp
from gurobipy import GRB
import pandas as pd

# 1. Load dữ liệu
skills_df = pd.read_csv(r"C:\toi_uu_hoa\player_skills.csv")
ps_df = pd.read_csv(r"C:\toi_uu_hoa\player_position_scores.csv")
team_df = pd.read_csv(r"C:\toi_uu_hoa\team_profile (1).csv")

for df in [skills_df, ps_df, team_df]:
    df.columns = df.columns.str.strip()

skills_df["Player"] = skills_df["Player"].str.strip()
ps_df["player"] = ps_df["player"].str.strip()
team_df["Scenario"] = team_df["Scenario"].str.strip()
team_df["RequiredSkill"] = team_df["RequiredSkill"].str.strip()

players = skills_df["Player"].tolist()
positions = ps_df.columns[1:].tolist()   # GK, DR, DCR, ...

# 2. Dictionary tham số
# Position Score
PS = {
    (row["player"], pos): row[pos]
    for _, row in ps_df.iterrows()
    for pos in positions
}

# Player Skill
skill_names = skills_df.columns[1:].tolist()
S = {
    (row["Player"], skill): row[skill]
    for _, row in skills_df.iterrows()
    for skill in skill_names
}

# 3. Khởi tạo model

model = gp.Model("Soccer_Lineup_Optimization")

# 4. Biến
x = model.addVars(players, positions, vtype=GRB.BINARY, name="x")

# 5. Hàm mục tiêu (Position Score)
model.setObjective(
    gp.quicksum(PS[i, j] * x[i, j] for i in players for j in positions),
    GRB.MAXIMIZE
)

# 6. Ràng buộc đội hình
# Mỗi vị trí đúng 1 cầu thủ
for j in positions:
    model.addConstr(gp.quicksum(x[i, j] for i in players) == 1)

# Mỗi cầu thủ tối đa 1 vị trí
for i in players:
    model.addConstr(gp.quicksum(x[i, j] for j in positions) <= 1)

# 7. Ràng buộc Team Profile

important_positions = {
    "Shots": ["FR", "FC", "FL"],
    "Crosses": ["DR", "DL"],
    "Interceptions": ["DCR", "DR", "DCL", "DL"],
    "Passes": ["MCR", "MC", "MCL"]
}

for _, row in team_df.iterrows():
    scenario = row["Scenario"]
    skill = row["RequiredSkill"]
    grade = float(row["Grade"])

    if scenario not in important_positions:
        continue

    model.addConstr(
        gp.quicksum(
            S[i, skill] * x[i, pos]
            for pos in important_positions[scenario]
            for i in players
        ) >= grade
    )

# 8. Tối ưu
model.optimize()

# 9. In kết quả
if model.status == GRB.OPTIMAL or model.status == GRB.SUBOPTIMAL:
    print("\n=== OPTIMAL LINE-UP ===")
    for j in positions:
        for i in players:
            if x[i, j].x > 0.5:
                print(f"{j}: {i}: {PS[i,j]}")
    print("Total Score:", model.objVal)
else:
    print("Can't optimize")
