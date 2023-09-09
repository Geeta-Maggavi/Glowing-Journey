#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[9]:


df = pd.read_csv("E:\\Diwali-Sale-Data.csv", encoding = 'unicode_escape')


# In[11]:


df.shape


# In[14]:


df.head(10)


# In[15]:


df.info()


# In[18]:


df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[20]:


pd.isnull(df).sum()


# In[21]:


df.dropna(inplace = True)


# In[23]:


pd.isnull(df).sum()


# In[24]:


df.shape


# In[27]:


#change datatype
df['Amount'] = df['Amount'].astype('int')


# In[28]:


df.info()


# In[29]:


df.columns


# In[31]:


df.describe()


# In[35]:


df[['Age', 'Orders', 'Amount']].describe()


# ### EXPLORATORY DATA ANALYSIS
# 

# ###### Gender

# In[37]:


ax = sns.countplot(x='Gender', data=df)
for i in ax.containers:
    ax.bar_label(i)


# In[42]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by=['Amount'], ascending=False)
ax = sns.barplot(x='Gender', y='Amount', data=sales_gen)



# From above graph we can see that most af the buyer are females and even the purchasing power of females is greather than males

# ##### Age

# In[55]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
for i in ax.containers:
    ax.bar_label(i)


# In[59]:


# Total ampunt Vs Age group 
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)


# by above graph we can see that the most of the buyers are from the age group of 26-35 years females

# ##### State

# In[77]:


# Total no. of orders from top 10 states
sales_state=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by=['Orders'], ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Orders', data=sales_state, width=0.9)

plt.xticks(rotation='vertical')
plt.show()


# In[79]:


# Total amount/sales from top 10 states
sales_state=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Amount', data=sales_state)
plt.xticks(rotation='vertical')
plt.show()


# Here we can see that most of the orders and total sales/amount are from UP, Maharashtra, Karnataka

# ###### MARITAL STATUS

# In[81]:


df.columns


# In[89]:


ax = sns.countplot(x = 'Marital_Status', data = df, width=0.3)
sns.set(rc={'figure.figsize':(4,4)})
for i in ax.containers:
    ax.bar_label(i)


# In[91]:


ms_amount=df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Marital_Status', y='Amount', data=ms_amount, hue='Gender')


# From above graph we can understand that most of the buyers are married woman and spends more money

# ###### Occupation

# In[97]:


sns.set(rc={'figure.figsize':(15,5)})
ax = sns.countplot(x='Occupation', data=df)
for i in ax.containers:
    ax.bar_label(i)
plt.xticks(rotation='vertical')
plt.show()


# In[98]:


#occ_amount is occupation wise amount
occ_amount=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Occupation', y='Amount', data=occ_amount)


# From above graph we can see that the most of the buyer are from IT, healthcare and aviation sector

# ###### PRODUCT CATEGORY

# In[102]:


ax = sns.countplot(x='Product_Category', data = df)
for i in ax.containers:
    ax.bar_label(i)
plt.xticks(rotation='vertical')
plt.show()


# In[104]:


# pc_amount is product wise amount
pc_amount=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Product_Category', y='Amount', data=pc_amount)
plt.xticks(rotation='vertical')
plt.show()


# From above graph we can see that most of the sold product are from food, clothing, electronics & gadjets

# In[111]:


# top 10 most sold products 
#pi_orders is product id wise orders
pi_orders = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(x='Product_ID', y='Orders', data=pi_orders)


# ###### Conclusion :

# Married women age group 26-35 years from UP, MH, KA working in IT, healthcare and aviation sector are more likely
# to buy products from food, clothing and electroninc gadjets category

# 
# End of the project 
# 

# Thank You

# In[ ]:




