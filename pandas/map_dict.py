import pandas as pd

player_profile = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/player_profile.csv")
player_profile["bmi"] = player_profile["weightKilograms"] / player_profile["heightMeters"]**2
print(player_profile[["temporaryDisplayName", "bmi"]].head())

#類別對應類別
'''
透過 Series 的 .map() 方法來實踐，傳入 dict 作為對應的準則，
字典的鍵（Key）為對應前的原始類別，字典的值（Value）為對應後的類別，
例如將本來分類較細膩的鋒衛對應為較粗略的前場、後場
'''

print(player_profile['pos'].value_counts())

pos_dict = {
    "G": "Backcourt",
    "F": "Frontcourt",
    "C": "Frontcourt",
    "G-F": "Backcourt",
    "F-C": "Frontcourt",
    "F-G": "Frontcourt",
    "C-F": "Frontcourt"
}

print("Pos before mapping:")
print(player_profile["pos"].value_counts())


print("Pos after mapping:")
player_profile["pos_recoded"] = player_profile["pos"].map(pos_dict)
print(player_profile["pos_recoded"].value_counts())
