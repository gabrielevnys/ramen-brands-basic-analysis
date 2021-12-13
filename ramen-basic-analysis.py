import pandas as pd

print("Basic Exploratory Analysis on Ramen Brands\n\n")


#read the CSV file
df = pd.read_csv("ramen-ratings.csv")


#the number of entries and columns
print("There are", df.shape[0], "entries and", df.shape[1], "columns in this dataframe.\n")


#first five entries
print("These are the first five entries:\n", df.head(), "\n")


#last five entries
print("These are the last five entries:\n", df.tail(), "\n")


#checking the data types of each column
print("These are the data types of each column:", df.dtypes, sep="\n", end ="\n\n")


#set Review # as index
df.set_index("Review #", inplace = True)
df.index.names = ["Review No."]
print("After changing the index:\n", df, sep="", end="\n\n")


#sort index
df.sort_index(ascending = True, inplace = True)
print("After sorting the index:\n", df, sep="", end="\n\n")


#changing the data type for "Stars" from object to float
df["Stars"] = pd.to_numeric(df["Stars"], errors="coerce") #to coerce non-numeric junk to NaNs

print("There are the data types after changing the Stars column:\n", df.dtypes, sep="", end="\n\n") 


#finding outliers
#data < Q1 - 1.5 * IQR or data > Q3 + 1.5 * IQR
Q1 = df.loc[:,"Stars"].quantile(0.25)
Q3 = df.loc[:,"Stars"].quantile(0.75)
IQR = Q3 - Q1

df["Outliers"] = (df["Stars"] < Q1 - 1.5 * IQR) | (df["Stars"] > Q3 + 1.5 * IQR)

outliers_df = df[df["Outliers"] == True]
print("The outliers data:\n", outliers_df, sep="")


#describe numerical data
print("This is a brief description of the dataframe:\n", df.describe(include="all"),"\n")


#describe outliers data
print("This is a brief description of the outliers:\n", outliers_df.describe(include="all"),"\n")


#analysis
print("From the above description, we can conclude that:")
print("1) The most reviewed ramen brand is \"Nissin\"")
print("2) The most reviewed ramen variant is beef")
print("3) Almost 60% of the packaging style are packs")
print("4) Japan's ramens are mostly reviewed")
print("5) The average rating given is 3.6")
print("6) According to the data, there are 129 outliers")
print("7) The smallest ratings are mostly the ramens from the USA")
print("8) Nissin is the most favourite ramen brand and Baijia is the least favourite one")
