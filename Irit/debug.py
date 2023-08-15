import pandas as pd
from Irit.psychodiagnostic_computations import compute_swan_scores, compute_sdq_scores, compute_cbcl_scores
from Irit.utils_Irit import calc_t_scores
from Variables import rename_align, Irit_columns_to_drop
import os

df = pd.read_excel(r"data/ADHD.xlsx")

df = df.drop(Irit_columns_to_drop, axis=1)

rename_align_r = {j: i for i, j in rename_align.items()}
df = df.rename(rename_align_r, axis=1)

df, params_swan = compute_swan_scores(df)
# df, params_sdq = compute_sdq_scores(df)

df, params_cbcl = compute_cbcl_scores(df)

df, param_t_score = calc_t_scores(df)
print(909090909)


df['suicidal_ideation'] = df['t1_p_rawscore_cbcl_91'] > 0
df['suicidal_behavior'] = df['t1_p_rawscore_cbcl_18'] > 0

directory = "data/tests"
if not os.path.exists(directory):
    os.makedirs(directory)

filepath = os.path.join(directory, "processed_ADHD.csv")
df.to_csv(filepath, index=False)