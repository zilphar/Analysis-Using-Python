import pandas as pd 

employees = pd.read_csv("Employee.csv")
employees.head()

#working with employees  whose Age is 35 years and above 

age_35 = employees[["FullName", "Gender", "Age"]]
age_35.head()
age_35.shape

desired_columns = ["FullName", "Gender", "Age"] 
older_employees = employees[employees["Age"] > 35] 
older_employees[desired_columns].shape # returns 737 rows and 3 columns 

#employees in the United states 

US_employees = employees[employees["Country"].isin(["United States"])]
US_employees # 643 employees live in the United States 

#of the employees in the United states which of them are above 35 years old 

US_employees= employees[employees["Country"].isin(["United States"])] 

US_employees_above35 = US_employees[US_employees["Age"] > 35 ]

US_employees_above35 # 465 employees who live in the US are above 35 years of age 

# I want to get the department of employees who are above 35 years and live in Beijing 

above_35years_inBeijing = employees[(employees["Age"] > 35) & (employees["City"] == "Beijing")]

above_35years_inBeijing[["FullName", "Department", "Gender"]]   # 46 employees live in Beijing and are above 35 years

above_35years_inBeijing[["FullName", "Department", "Gender"]].shape


#countries where highest employees come from 
no_of_employees_percountry= employees["Country"].value_counts()

no_of_employees_percountry


#number of males and females employed 

no_of_employees_pergender = employees["Gender"].value_counts()

no_of_employees_pergender  # 518 females and 482 males 

#statistics on age, annual salary, and Bonus 

numerical_statistics = employees[["Age", "AnnualSalary", "Bonus"]].describe()

numerical_statistics

  # mode and median of Age, AnnualSalary, and  Bonus 
  
mode_statistics = employees[["Age", "AnnualSalary", "Bonus"]].mode().iloc[0] #mode() returns a DF and iloc[0] selects the 1st row of the resulting DF which contains the modes for each column 

mode_statistics
             #median()
median_statistics = employees[["Age", "AnnualSalary", "Bonus"]].median()

median_statistics 

#creating a new year column from the existing HireDate column 

    # convert the date to datetime 
employees["HireDate"] = pd.to_datetime(employees["HireDate"])

employees["HireDate"]

employees["Year"]= employees["HireDate"].dt.year

employees["Year"]

employees

# what is the max and min Hiredate for the employees 

print(employees["HireDate"].min(), employees["HireDate"].max())  # max hiredate is 2021-12-26 and min is 1992-01-09 




