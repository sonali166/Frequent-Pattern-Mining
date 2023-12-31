#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install pandas')
get_ipython().run_line_magic('pip', 'install numpy')
get_ipython().run_line_magic('pip', 'install plotly')
get_ipython().run_line_magic('pip', 'install mlxtend')


# In[2]:


import pandas as pd
dataset = pd.read_csv("Market_basket_data.csv")
dataset.shape


# In[3]:


dataset.head()


# In[4]:


import numpy as np
transaction =[]
for i in range(0, dataset.shape[0]):
    for j in range(0, dataset.shape[1]):
        transaction.append(dataset.values[i,j])
# 
transaction = np.array(transaction)
print(transaction)


# In[5]:


df = pd.DataFrame(transaction, columns=["items"]) 

df["incident_count"] = 1 

indexNames = df[df['items'] == "nan" ].index
df.drop(indexNames , inplace=True)

df_table = df.groupby("items").sum().sort_values("incident_count", ascending=False).reset_index()

df_table.head(5).style.background_gradient(cmap='Blues')


# In[59]:


import plotly.express as px
df_table["all"] = "Top 50 items" 

fig = px.treemap(df_table.head(50), path=['all', "items"], values='incident_count',
                  color=df_table["incident_count"].head(50), hover_data=['items'],
                  color_continuous_scale='Blues',
                )

fig.show()


# In[51]:


transaction = []
for i in range(dataset.shape[0]):
    transaction.append([str(dataset.values[i,j]) for j in range(dataset.shape[1])])
transaction = np.array(transaction)
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(transaction).transform(transaction)
dataset = pd.DataFrame(te_ary, columns=te.columns_)

dataset.head()


# In[52]:


first30 = df_table["items"].head(30).values 
dataset = dataset.loc[:,first30] 
dataset.shape


# In[53]:


from mlxtend.frequent_patterns import fpgrowth
res=fpgrowth(dataset,min_support=0.05, use_colnames=True)
res.head(10)


# In[56]:


from mlxtend.frequent_patterns import association_rules

res=association_rules(res, metric="lift", min_threshold=1)
res


# In[57]:


res.sort_values("confidence",ascending=False)


# In[ ]:




