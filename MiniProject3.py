"""
Created on Mon Nov 17 15:40:43 2025

@author: gdlamb, epjohns4
"""

from itertools import combinations
import pandas as pd

# change path to that of desired dataset
df = pd.read_csv(r"C:\Users\gdl12\OneDrive - North Carolina State University\North Carolina State University\2025 Term 2 (Autumn)\ISE 135\Mini-Project 3\coverage1.txt", header=None)
df.columns = ["Center", "cost $M", "Agadez", "Dosso", "Maradi", "Tahoua", "Tillabery", "Zinder", "Diffa", "Niamey", "Faso", "Mali"]

# iterate through every possible combination of rows and remember any that cover every county
validCombos = []
for i in range(1, len(df) + 1):
    combos = combinations(df.index, i)
    for c in combos:
        # create temporary dataframe with each subset of rows in the dataframe
        dftemp = df.loc[list(c)]
        # check if every county column in the temporary dataframe contains at least one 1
        if (dftemp[["Agadez", "Dosso", "Maradi", "Tahoua", "Tillabery", "Zinder", "Diffa", "Niamey", "Faso", "Mali"]] == 1).any().all():
            validCombos.append(c)

# of the valid combinations found before, calculate the cost of each and remember the cheapest one
minimumCost = float('inf')
minimumCostCombo = None
for c in validCombos:
    dftemp = df.loc[list(c)]
    # find the cost of each combination of centers
    cost = sum(dftemp["cost $M"])
    # if it's cheaper than the cheapest on record so far, update the record
    if cost < minimumCost:
        minimumCost = cost
        minimumCostCombo = c

# print the cheapest combination that covers every county with its expected cost
print("Open these centers: ", end="")
for i in range(0, len(minimumCostCombo)):
    print(df.loc[minimumCostCombo[i], "Center"], end="")
    if i < len(minimumCostCombo) - 1:
        print(", ", end="")
print("")
print("The total cost is ${0:,d}".format(int(minimumCost * 1000000)))