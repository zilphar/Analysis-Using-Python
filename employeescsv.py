import pandas as pd 

#read the csv
customers = pd.read_csv("customers.csv")
print(customers)

#print the first 5 rows of the data to her a glimpse of what it entails 
print(customers.head())

#interpretation of each column data type 
print(customers.dtypes)  # data types include integers (int64)  floats (float64), and strings (object). 

# a quick overview of the numerical data 
print(customers.describe()) #numerical data is contained in columns Age, AnnualSalary, Bonus, and Id. (deriving an overview of the column Id is then not needed. let's change that)

print(customers[["Age", "AnnualSalary", "Bonus"]].describe()) # gives only results of data in the selected columns 

#a quick technical summary of the dataframe
print(customers.info()) # shows there are no null values in the DF 

print(customers.shape)

print(customers[["FullName", "Gender", "Age"]])

#I only want to work with customer names. and Gender of customers with Age greater than 35
desired_columns = ["FullName", "Gender", "Age"] 
older_customers = customers[customers["Age"] > 35] 
print(older_customers[desired_columns])
