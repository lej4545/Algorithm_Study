import numpy as np
import pandas as pd

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
info_np = []
for i in info:
    i_list = list(i.split())
    info_np.append(i_list)

df = pd.DataFrame(info_np,colums=['lan','b_or_f','j_or_s','food'])
print(df)