from pandas_gbq import to_gbq
import pandas as pd
import os
from app.main import dim_country_media
from app.main import df_country
from app.main import df_langages
from app.main import fact_country_profile
from app.main import fact_country_gini

#project_id = "bi-country-data-pipeline"
#load env vars

from dotenv import load_dotenv

load_dotenv()

project_id=os.getenv("GCP_PROJECT_ID")
project_dataset=os.getenv("GCP_DATASET")
dataset_id=os.getenv("BQ_DATASET_ID")

#check env vars
#print(project_dataset,";",project_id,';',dataset_id)

table_dest_urls = f"{dataset_id}.df_country_media"
table_dest_countries=f"{dataset_id}.df_countries"
tbl_dst_lagn=f"{dataset_id}.df_languages"
tbl_dst_fct_c_profile=f"{dataset_id}.df_fct_state_profile"
tbl_dst_fct_c_gini=f"{dataset_id}.df_fct_state_gini"

to_gbq(dim_country_media,destination_table=table_dest_urls,project_id=project_id,if_exists="replace")
to_gbq(df_country,destination_table=table_dest_countries,project_id=project_id,if_exists="replace")
to_gbq(df_langages,destination_table=tbl_dst_lagn,project_id=project_id,if_exists="replace")
to_gbq(fact_country_profile,destination_table=tbl_dst_fct_c_profile,project_id=project_id,if_exists="replace")
to_gbq(fact_country_gini,destination_table=tbl_dst_fct_c_gini,project_id=project_id,if_exists="replace")