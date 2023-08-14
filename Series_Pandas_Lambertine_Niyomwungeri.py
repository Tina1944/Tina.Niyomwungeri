#!/usr/bin/env python
# coding: utf-8

# # Qn1.

# In[1]:


# Import pandas library
import pandas as pd

# Lets create series 
Fruit = pd.Series(["apple","mango","orange","apple"])
#check for unique values
Fruit.unique # this attribute retursn the unique names and shows "apple" as duplicate


# In[2]:


# use attribute that returns Boolean output for unique values
Fruit.is_unique # this answers if series have unique value or not, therefore the output is True or False


# # Qn2.

# In[143]:


# read titanic series
titanic_names_series= pd.read_csv("/Users/lniyomwungeri2/Downloads/Titanic.csv",usecols =["Survived","Name"],index_col="Name",squeeze = True)
titanic_names_series.head(3)
#type(titanic_names_series)


# In[17]:


# Let's use index lable that does not exixt to pull the names 
titanic_names_series["Lambertine"] # We get the error that the index used is not in the index 


# In[20]:


# Let's try to use try statement to get "does not exixt" output message
try:
    print(titanic_names_series["Lambertine"])
except:
    print("does not exist")


# In[22]:


# extract two values
titanic_names_series[["Braund, Mr. Owen Harris","Heikkinen, Miss. Laina"]] # we get two values 0 and 1


# In[23]:


# extract values with  one index lable that doesn't exixt
titanic_names_series[["Braund, Mr. Owen Harris","Lambertine"]] # Gives the error that Lambertine is not in the index


# # ****Qn3.****

# In[43]:


# Import nobel.csv file
nobel = pd.read_csv("/Users/lniyomwungeri2/Downloads/nobel.csv")
#nobel.info()
selected_columns=["Year", "Category", "Prize", "Motivation", "Laureate Type","Full Name", "Birth Date", "Birth Country", "Birth City","Sex","Death Date"]
new_nobel = nobel[selected_columns]
                                                                              


# In[44]:


# ceate nobel series
nobel_Laureate_type= new_nobel["Laureate Type"]
type(nobel_Laureate_type)


# In[42]:


# count values
nobel_Laureate_type.value_counts() # there are 939 individuals and 30 organizations


# In[46]:


# add a new column "Age"
nobel["Age"]=50
nobel.head(3)


# In[171]:


# replace nan wiht zero
nobel["Year"].replace("NaN",0)
nobel["Birth Date"].replace("NaN",0)
#extract the year “Birth Date”
#Birth_year = nobel["Birth Date"].str[:4]
#nobel["Birth Date"] 
#convert the column of type string to a numeric column
nobel["Birth Date"] =nobel["Birth Date"] .apply(pd.to_numeric)
nobel.Year
# create Real age colunm
nobel["Real Age"] = nobel["Year"] - nobel["Birth Date"]
nobel["Real Age"]
nobel= nobel.drop("Age",axis=1)
nobel.head(3)


# In[172]:


#Review the data
nobel.describe().transpose()# Average real Age is 59


# # Qn 4.

# In[144]:


nba = pd.read_csv("/Users/lniyomwungeri2/Downloads/nba.csv")
nba_series = pd.read_csv("/Users/lniyomwungeri2/Downloads/nba.csv",usecols = ["Salary","Name"], index_col = "Name",squeeze = True)
nba.head()


# In[133]:





# In[134]:


#Getting salary for John Holland
nba_series[["John Holland"]]


# In[135]:


#Is the salary value of any person 5000000.0
nba_series.sort_values( ascending = False).head() # Yes ! Kobe Bryant's salary is $25,000,000


# In[138]:


Avg_Salary =nba_series.mean()


# In[ ]:


#Write a function that returns “No Salary Reported”, “Average salary”, “below
#Average”, or “Above Average” where salary is NaN, equal to average value, below
#the average or above the average, respectively. Then apply the function to nba_series.


# In[154]:


def salary_level(n):
    if n =="NaN":
        return Avg_salary
    elif n> Avg_Salary:
        return "Above Average"
    elif n< Avg_Salary:
        return "below Average"
    elif n == Avg_Salary:
        return "Average salary"
    else:
        return "No Salary Reported"
Salary_Levels = nba_series.apply(salary_level)
print(Salary_Levels)


# In[ ]:




