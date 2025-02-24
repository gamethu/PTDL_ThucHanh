import pandas as pd

# init
data = list([
    0, 5, 7,
    0, 3, 5,
    2, 3, 1,
    2, 2, 1
])
S = pd.Series(data)
# print(S)

# calculate then display data
print("Mean:",S.mean())
print("Mode:",S.mode())
print("Median:",S.median())
print("Q1:",S.quantile(
    0.25, # ~> 25%
))
print("Q2:",S.quantile(
    0.5, # ~> 50%
))
print("Q3:",S.quantile(
    0.75 # ~> 75%
))