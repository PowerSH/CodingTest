import re
import pandas as pd

# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

tbl = list()
tbl_row = list()

for file in files:
    NUMBER = re.findall('\d+', file)
    HEAD = file.split(str(NUMBER[0]))[0]
    TAIL = file.split(str(NUMBER[0]))[1]

    tbl_row.append(HEAD)
    tbl_row.append(NUMBER)
    tbl_row.append(TAIL)
    tbl.append(tbl_row)

df_tbl = pd.DataFrame(tbl)
df_tbl = df_tbl.transpose()

print(df_tbl)