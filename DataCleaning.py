import pandas as pd
import csv

# Importing raw data.
df1 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset1.csv")
df2 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset2.csv")
df3 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset3.csv")
df4 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset4.csv")
df5 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset5.csv")
df6 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset6.csv")
df7 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset7.csv")
df8 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset8.csv")
df9 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset9.csv")

df = [df1, df2, df3, df3, df4, df5, df6, df7, df8, df9]

df = pd.concat(df)

df.head(100)

df.shape
# Output suggest 201 shops and 16 features. 