#Importing Pandas library
import pandas as pd
#Importing Json Library
import json

#Reading JSON file using pandas
js =pd.read_json("data.json",lines=True)

#Connvering JSON to dataframe
df=pd.DataFrame.from_dict(js)
json_struct = json.loads(df.to_json(orient="records"))

#Flattening JSON Dataframe
df = pd.json_normalize(json_struct)

#Adding new column Names
df.columns=["address","linkedin_id","profile_url","name","mob_num","email"]
#Droping Duplicate values
df=df.loc[df.astype(str).drop_duplicates().index]

#Main_Data
df_main=df.drop(['mob_num', 'email'],axis=1)
print(df_main.columns)

#Email_Data with linkedin_ID
df_email=df.drop(["address","profile_url","name","mob_num"],axis=1)
print(df_email.columns)

#Phone_number with linkedin_ID
df_number=df.drop(["address","profile_url","name","email"],axis=1)
print(df_number.columns)

#Exporting the DataFrame to CSV
df_main.to_csv("data_main.csv",index=False)
df_email.to_csv("data_email.csv",index=False)
df_number.to_csv("data_number.csv",index=False)