#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pip', 'install pyECLAT')
get_ipython().run_line_magic('pip', 'install numpy')
get_ipython().run_line_magic('pip', 'install pandas')
get_ipython().run_line_magic('pip', 'install plotly')


# In[5]:


from pyECLAT import Example2
dataset = Example2().get()
dataset.head()


# In[6]:


dataset.info()


# In[7]:



from pyECLAT import ECLAT

eclat = ECLAT(data=dataset)
eclat.df_bin


# In[8]:


items_total = eclat.df_bin.astype(int).sum(axis=0)
items_total


# In[9]:



items_per_transaction = eclat.df_bin.astype(int).sum(axis=1)
items_per_transaction


# In[10]:


import pandas as pd
df = pd.DataFrame({'items': items_total.index, 'transactions': items_total.values}) 
df_table = df.sort_values("transactions", ascending=False)
df_table.head(5).style.background_gradient(cmap='Blues')


# In[11]:


import plotly.express as px
df_table["all"] = "Tree Map" 
fig = px.treemap(df_table.head(50), path=['all', "items"], values='transactions',
                  color=df_table["transactions"].head(50), hover_data=['items'],
                  color_continuous_scale='Blues',
                )
fig.show()


# In[12]:



min_support = 5/100

min_combination = 2

max_combination = max(items_per_transaction)
rule_indices, rule_supports = eclat.fit(min_support=min_support,
                                                 min_combination=min_combination,
                                                 max_combination=max_combination,
                                                 separator=' & ',
                                                 verbose=True)


# In[13]:


import pandas as pd
result = pd.DataFrame(rule_supports.items(),columns=['Item', 'Support'])
result.sort_values(by=['Support'], ascending=True)


# In[ ]:




