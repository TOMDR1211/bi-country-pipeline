from app.api_connector import get_data_from_api
import pandas as pd

pd.set_option('display.max_columns', None)

try:
    data = get_data_from_api()
except:
    with open('data/raw/restcountries.json', encoding='utf-8') as f:
        data = json.load(f)

if data:
    # print('Done! We Got: ',len(data),'Countries')
    fdata = pd.json_normalize(data, sep='_')

    # creating dim_lang
    cols = [col for col in fdata.columns if col.startswith('languages_')]
    # print(fdata[cols].head())
    df_langages = pd.melt(fdata, id_vars='cca2', value_vars=cols, var_name='language_code', value_name='language')
    df_langages = df_langages.dropna()
    df_langages['language_code'] = df_langages['language_code'].str.split('_').str[1]
    # print(df_langages.head())

    # captial is tricky and can be list or str so we fix it
    fdata['capital'] = fdata['capital'].apply(
        lambda x: x[0] if isinstance(x, list) and x else x if isinstance(x, str) else None

    )
    # print(fdata['capital'].head())

    # create dim_country
    df_country = fdata[['cca2', 'name_common', 'capital']]

    # creating dim for urls
    dim_country_media = fdata[['cca2', 'flag', 'flags_png', 'maps_googleMaps', 'coatOfArms_png']]
    # print(dim_country_media.head())

    # creating fact_country_profile
    fdata['lat'] = fdata['latlng'].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) == 2 else None

    )

    fdata['lng'] = fdata['latlng'].apply(
        lambda x: x[1] if isinstance(x, list) and len(x) == 2 else None

    )

    fdata['borders_count']= fdata['borders'].apply(
        lambda x: len(x) if isinstance(x,list) and x else None

    )
    fdata['timezones_count'] = fdata['timezones'].apply(
        lambda x: len(x) if isinstance(x,list) and x else None
    )

    fdata['density'] =fdata[['population','area']].apply(
        lambda row: row['population']/row['area'] if row['area']>0 and pd.notna(row['population']) else None,
        axis = 1
    )


    fact_country_profile = fdata[['cca2', 'area', 'population', 'lat','lng','borders_count','timezones_count','density']].head()
    #print(fact_country_profile)

    #creating fact_country_gini

    #check we have 'gini' column
    #print([col for col in fdata.columns if 'gini' in col])

    #melt gini_ columns to one column with gini values by key cca2

    cols_gini = [col for col in fdata.columns if col.startswith('gini_')]

    fact_country_gini = pd.melt (fdata,id_vars='cca2', value_vars=cols_gini,var_name='year',value_name='gini')
    fact_country_gini = fact_country_gini.dropna()
    fact_country_gini['year'] =  fact_country_gini['year'].str.split('_').str[1].astype(int)

    #print(fact_country_gini.head())
    #print(fact_country_gini['year'].dtype)

    #print(dim_country_media.head(), df_langages.head(), df_country.head(), fact_country_profile.head(), fact_country_gini.head())

else:
    print('Problem To Get API Data')
