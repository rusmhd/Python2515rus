#Rushil Mohamed 1258033
#Financial Modelling
import pandas as pd, numpy as np, numpy_financial as npf
from google.colab import files

u = files.upload()
f = list(u.keys())[0]

d = pd.read_excel(f, header=None)

def find(k):
    for i, v in d[0].items():
        if isinstance(v, str) and k.lower() in v.lower():
            return i
rv = find("sales")
ex = find("expense")
yr = rv - 1
print(yr, rv, ex)

YH = d.loc[yr, 1:].dropna().values
R = pd.to_numeric(d.loc[rv, 1:len(YH)], errors='coerce').fillna(0).values
C = pd.to_numeric(d.loc[ex, 1:len(YH)], errors='coerce').fillna(0).values

inv = float(input("Initial Investment (Cr): ")) * 1e7
yrs = int(input("Project Years: "))
disc = float(input("Discount Rate (%): ")) / 100

gR = (R[-1] - R[-2]) / R[-2] if len(R) >= 2 and R[-2] != 0 else 0
gC = (C[-1] - C[-2]) / C[-2] if len(C) >= 2 and C[-2] != 0 else 0

Y = np.arange(1, yrs + 1)

S1, C1 = R[-1] * (1 + gR), C[-1] * (1 + gC)
SF, CFv = S1 * (1 + gR) ** (Y - 1), C1 * (1 + gC) ** (Y - 1)

PF = SF - CFv
CFm = PF * 1e7

DF = 1 / (1 + disc) ** Y
PV = CFm * DF

if disc > gR:
    TV = (CFm[-1] * (1 + gR)) / (disc - gR)
    TV_PV = TV / (1 + disc) ** yrs
else:
    TV = TV_PV = 0

NPV = -inv + PV.sum() + TV_PV

try:
    IRR = npf.irr(np.concatenate(([-inv], CFm, [TV]))) * 100
except:
    IRR = np.nan

cum = np.cumsum(CFm)

PB = next(
    (
        i if i == 0 else (i - 1) + (-cum[i - 1] / CFm[i])
        for i, v in enumerate(cum) if v >= 0
    ),
    None
)

ROI = (CFm.sum() - inv) / inv * 100

proj = []
n0 = len(YH)

for i in range(d.shape[0]):
    if i == yr:
        proj.append(
            [d.loc[i, 0]] +
            list(d.loc[i, 1:n0]) +
            [f"Proj{t}" for t in range(1, yrs + 1)]
        )
    else:
        vals = d.loc[i, 1:n0]
        num = pd.to_numeric(vals, errors='coerce').dropna()

        if len(num) >= 2 and num.iloc[-2] != 0:
            g = (num.iloc[-1] - num.iloc[-2]) / num.iloc[-2]
            proj.append(
                [d.loc[i, 0]] +
                list(vals) +
                [num.iloc[-1] * (1 + g) ** t for t in range(1, yrs + 1)]
            )
        else:
            proj.append(
                [d.loc[i, 0]] +
                list(vals) +
                [np.nan] * yrs
            )

proj = pd.DataFrame(proj)

DCF = [
    [""],
    ["DCF Calculations"],
    ["Year", *Y, "TV"],
    ["Sales", *SF, ""],
    ["Cost", *CFv, ""],
    ["Profit", *PF, ""],
    ["CF (Cr)", *(CFm / 1e7), TV / 1e7],
    ["DF", *DF, 1 / (1 + disc) ** yrs],
    ["PV (Cr)", *(PV / 1e7), TV_PV / 1e7],
    [""],
    ["RESULT", ""],
    ["ROI %", ROI],
    ["NPV (Cr)", NPV / 1e7],
    ["IRR %", IRR],
    ["Payback", PB]
]

E = pd.concat([proj, pd.DataFrame(DCF)], ignore_index=True)

E.to_excel("output.xlsx", header=False, index=False)

files.download("output.xlsx")
