#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Reading dataset
df = pd.read_csv('MOVIES.csv', encoding='latin1') #df is named as movies data
print(df.head()) #data is showed


# In[3]:


df #dataset is showed


# In[4]:


df.shape #data shape is brought


# In[5]:


df.columns #data columns are showed


# In[7]:


df.isnull().sum() #Empty spots are detected


# In[8]:


#Nan spots are in Name columns are deleted by entire lines .
df = df.dropna(subset=['NAME'])


# In[9]:


df


# In[10]:


df.isnull().sum() #Empty spots are checkhed


# In[11]:


# Group by the "YEAR" column
grouped_by_year = df.groupby('YEAR')

# Display groups
for year, group in grouped_by_year:
    print(f"Movies from {year}:")
    print(group[['NAME']])
    print("\n")


# In[14]:


#Calculating how many movies are named according to published year
movies_per_year = df['YEAR'].value_counts().sort_index()

#Showing results
print(movies_per_year)


# In[19]:


import matplotlib.pyplot as plt

movies_per_year.plot(kind='bar', figsize=(10,5), color='purple')
plt.xlabel("Year")
plt.ylabel("Movies Quantity")
plt.title("Movies Quantity According to Years")
plt.show()


# In[20]:


#Filtred min 10 times frequency
filtered_years = movies_per_year[movies_per_year >= 10]

#Showing results
print(filtered_years)


# In[21]:


import matplotlib.pyplot as plt

filtered_years.plot(kind='bar', figsize=(10,6), color='red')
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by Year")
plt.show()


# In[23]:


#Filtred min 10 times frequency
filtered_years15 = movies_per_year[movies_per_year >= 15]

#Showing results
print(filtered_years15)


# In[27]:


import matplotlib.pyplot as plt

# Sort the data by the number of movies in descending order
filtered_years15 = filtered_years15.sort_values(ascending=False)

# Plot the bar chart
filtered_years15.plot(kind='bar', figsize=(10,6), color='black')

plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by Year")

plt.show()


# In[29]:


df.info


# In[30]:


unique_df = df['YEAR'].unique()
print(unique_df)


# In[31]:


unique_famous_one = df['FAMOUS ONE'].dropna().unique()
unique_famous_two = df['FAMOUS TWO'].dropna().unique()
unique_famous_three = df['FAMOUS THREE'].dropna().unique()

# Print or use these unique values
print("Unique Famous One:", unique_famous_one)
print("Unique Famous Two:", unique_famous_two)
print("Unique Famous Three:", unique_famous_three)


# In[33]:


# FAMOUS ONE, FAMOUS TWO and FAMOUS THREE columns frequency
famous_one_counts = df['FAMOUS ONE'].dropna().value_counts()
famous_two_counts = df['FAMOUS TWO'].dropna().value_counts()
famous_three_counts = df['FAMOUS THREE'].dropna().value_counts()

# Sonuçları yazdır
print("FAMOUS ONE counts:")
print(famous_one_counts)

print("\nFAMOUS TWO counts:")
print(famous_two_counts)

print("\nFAMOUS THREE counts:")
print(famous_three_counts)


# In[34]:


famous_one_counts


# In[43]:


#famous_one_counts is showed
for name, count in famous_one_counts.items():
    print(f"{name}: {count}")


# In[45]:


import pandas as pd

# FAMOUS ONE, FAMOUS TWO and FAMOUS THREE columns frequency index
famous_one_counts = df['FAMOUS ONE'].dropna().value_counts().reset_index()
famous_two_counts = df['FAMOUS TWO'].dropna().value_counts().reset_index()
famous_three_counts = df['FAMOUS THREE'].dropna().value_counts().reset_index()

#Making columns's names
famous_one_counts.columns = ['Name', 'FAMOUS ONE Count']
famous_two_counts.columns = ['Name', 'FAMOUS TWO Count']
famous_three_counts.columns = ['Name', 'FAMOUS THREE Count']

#Merging results
result12 = pd.merge(famous_one_counts, famous_two_counts, on='Name', how='outer')
result = pd.merge(result12, famous_three_counts, on='Name', how='outer')

#Showing results
print(result)


# In[46]:


result


# In[47]:


import pandas as pd

# "FAMOUS ONE", "FAMOUS TWO" ve "FAMOUS THREE" columns merging
combined_names = pd.concat([df['FAMOUS ONE'], df['FAMOUS TWO'], df['FAMOUS THREE']]).dropna()

# Name frequency is computed 
frequency_counts = combined_names.value_counts().reset_index()

# Naming results
frequency_counts.columns = ['Name', 'Frequency']

# Showing results
print(frequency_counts)


# In[48]:


frequency_counts


# In[49]:


# Frequency > 1 filtred
filtered_df = frequency_counts[frequency_counts["Frequency"] > 1]

# Result
print(filtered_df)


# In[53]:


# Frequency > 10 filtred
filtered8_df = frequency_counts[frequency_counts["Frequency"] > 8]

# Sonuç
print(filtered8_df)


# In[58]:


import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(filtered8_df["Name"], filtered8_df["Frequency"], color='orange')
plt.title("Frequency of Names Greater Than 8", fontsize=14)
plt.xlabel("Name", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()


# In[59]:


# Pie chart
plt.figure(figsize=(5, 4))
plt.pie(filtered8_df["Frequency"], labels=filtered8_df["Name"], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Frequency Distribution for Names Greater Than 8 Times Seen", fontsize=14)
plt.show()


# In[60]:


pip install gender-guesser


# In[61]:


pip show gender-guesser


# In[62]:


import gender_guesser.detector as gender  # gender-guesser module is imported

# Gender-Guesser detector created
d = gender.Detector()

# Gender guess is created
def get_gender(name):
    first_name = str(name).split()[0]  # Take first name
    gender_prediction = d.get_gender(first_name)
    
    if gender_prediction in ['male', 'mostly_male']:
        return 'man'
    elif gender_prediction in ['female', 'mostly_female']:
        return 'woman'
    else:
        return 'unknown'

# Finding actors or actresses genders
df["FAMOUS ONE GENDER"] = df["FAMOUS ONE"].apply(get_gender)
df["FAMOUS TWO GENDER"] = df["FAMOUS TWO"].apply(get_gender)
df["FAMOUS THREE GENDER"] = df["FAMOUS THREE"].apply(get_gender)

# DataFrame showed
print(df[["NAME", "FAMOUS ONE", "FAMOUS ONE GENDER", "FAMOUS TWO", "FAMOUS TWO GENDER", "FAMOUS THREE", "FAMOUS THREE GENDER"]])


# In[63]:


df


# In[64]:


df_unknown = df[
    (df["FAMOUS ONE GENDER"] == "unknown") |
    (df["FAMOUS TWO GENDER"] == "unknown") |
    (df["FAMOUS THREE GENDER"] == "unknown")
]

# "Unknown" olan satırları göster
print(df_unknown[["NAME", "FAMOUS ONE", "FAMOUS ONE GENDER", "FAMOUS TWO", "FAMOUS TWO GENDER", "FAMOUS THREE", "FAMOUS THREE GENDER"]])


# In[71]:


df_unknown


# In[79]:


# Öncelikle sütun isimlerini kontrol edelim
print(df.columns)

# Boş değerleri "unknown" ile dolduralım (Eğer boş hücreler varsa)
df[["FAMOUS ONE GENDER", "FAMOUS TWO GENDER", "FAMOUS THREE GENDER"]] = \
df[["FAMOUS ONE GENDER", "FAMOUS TWO GENDER", "FAMOUS THREE GENDER"]].fillna("unknown")

# "unknown" değerlerini temizleyerek filtreleme yapalım
df_known = df[
    (df["FAMOUS ONE GENDER"].str.strip().str.lower() != "unknown") &
    (df["FAMOUS TWO GENDER"].str.strip().str.lower() != "unknown") &
    (df["FAMOUS THREE GENDER"].str.strip().str.lower() != "unknown")
]

# Sonucu göster
print(df_known[["NAME", "FAMOUS ONE", "FAMOUS ONE GENDER", "FAMOUS TWO", "FAMOUS TWO GENDER", "FAMOUS THREE", "FAMOUS THREE GENDER"]])


# In[80]:


df_unknown


# In[81]:


df_unknown.shape


# In[86]:


df_known.shape


# In[87]:


# Count occurrences of "unknown" in each gender column
unknown_one = (df["FAMOUS ONE GENDER"] == "unknown").sum()
unknown_two = (df["FAMOUS TWO GENDER"] == "unknown").sum()
unknown_three = (df["FAMOUS THREE GENDER"] == "unknown").sum()

# Total unknown count across all columns
total_unknown = unknown_one + unknown_two + unknown_three

# Print results
print(f"FAMOUS ONE GENDER 'unknown' count: {unknown_one}")
print(f"FAMOUS TWO GENDER 'unknown' count: {unknown_two}")
print(f"FAMOUS THREE GENDER 'unknown' count: {unknown_three}")
print(f"Total 'unknown' count across all columns: {total_unknown}")


# In[88]:


# **Toplamları hesaplarken "unknown" olanları dahil etme**
total_men = ((df["FAMOUS ONE GENDER"] == "man") | 
             (df["FAMOUS TWO GENDER"] == "man") | 
             (df["FAMOUS THREE GENDER"] == "man")).sum()

total_women = ((df["FAMOUS ONE GENDER"] == "woman") | 
               (df["FAMOUS TWO GENDER"] == "woman") | 
               (df["FAMOUS THREE GENDER"] == "woman")).sum()

# Sonuçları yazdır
print(f"Toplam Erkek Sayısı: {total_men}")
print(f"Toplam Kadın Sayısı: {total_women}")

# DataFrame'i göster (TÜM VERİLERİ İÇERİR, "unknown" olanları silmez)
print(df[["NAME", "FAMOUS ONE", "FAMOUS ONE GENDER", "FAMOUS TWO", "FAMOUS TWO GENDER", "FAMOUS THREE", "FAMOUS THREE GENDER"]])


# In[89]:


# "unknown" olanları göz ardı ederek sadece benzersiz isimleri al
unique_names = pd.concat([df["FAMOUS ONE"], df["FAMOUS TWO"], df["FAMOUS THREE"]]).drop_duplicates()

# Erkek ve kadın sayısını hesapla
total_men = unique_names[unique_names.apply(lambda x: get_gender(x) == 'man')].count()
total_women = unique_names[unique_names.apply(lambda x: get_gender(x) == 'woman')].count()

# Sonuçları yazdır
print(f"Toplam Erkek Sayısı (Tekrar Etmeyen): {total_men}")
print(f"Toplam Kadın Sayısı (Tekrar Etmeyen): {total_women}")

# DataFrame'i göster (TÜM VERİLERİ İÇERİR, "unknown" olanları silmez)
print(df[["NAME", "FAMOUS ONE", "FAMOUS ONE GENDER", "FAMOUS TWO", "FAMOUS TWO GENDER", "FAMOUS THREE", "FAMOUS THREE GENDER"]])


# In[90]:


df


# In[ ]:




