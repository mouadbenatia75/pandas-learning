import pandas as pd
import numpy as np
# df = pd.DataFrame({"Yes":[50,21] , "No":[131,2]})


# df2 = pd.DataFrame({
#     "A":1.0,
#     "B" : pd.Timestamp("20260213"),
#     "C" :pd.Series(1,index=list(range(4)),dtype ="float32"),
#     "D":np.array([3]*4,dtype="int32"),
#     "E":pd.Categorical(["test","train","test","train"]),
#     "F":"foo"

# })

# df3 = pd.DataFrame({
#     "A":[1,2],
#     "B":[1,5]
# })
# print(df)
# print(df2)
# print(df3.to_numpy())
# print(df3.describe())

df = pd.read_csv("data.csv",index_col="Name")
print(df.to_string())

# -------------------Selection by column------------------
# print(df["Name"])
# print(df["Height"])
# print(df[["Name","Height" , "Weight"]])

# -------------Selection by Row/s ------------------------
# print(df.loc["Pikachu", ["Height","Weight"]]) # select column of height and weight of the row of Pikachu
# print(df.loc["Pikachu":"Dragonair", ["Height","Weight"]]) # select the rows between Pikachu and Dragonair with the columns of height and weight
# print(df.iloc[0:11]) # Select by index location between 0 and 11
# print(df.iloc[0:11:2 ,0:3]) # Select the first 11 rows with the step of two and the first three columns

# Pokemon = input("Enter a Pokemon name :")
# try :
#     print(df.loc[Pokemon])
# except KeyError:
#     print(f"{Pokemon} not found")

# ---------Filtering data-----------------

# tall_pokemon = df[df["Height"] >=2]
# heavy_pokemon = df[df["Weight"]> 100]
# water_pokemon = df[(df["Type1"] == "Water") |(df["Type2"] == "Water")]
# print(tall_pokemon)
# print(heavy_pokemon)
# print(water_pokemon)

# -----------Aggregate functions -------------

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())
# --------Group by ------------
# group = df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].max())
# print(group["Height"].min())
# -----------------Data cleanning -----------
# Drop irrevelent columns
# df =  df.drop(columns=["Legendary"])
# Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2":"None"})  replace missing values
# Fix inconsistant values
# df["Type1"] = df["Type1"].replace({"Grass" : "GRASS","Water":"WATER"})

# Standarize values
# df["Name"] = df["Name"].str.lower()
# Change data type
df["Legendary"] = df["Legendary"].astype(bool)
# Remove duplicates
# df = df.drop_duplicates()
print(df.to_string())


