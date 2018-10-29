import pandas as pd

#custom models
from data_management.models import CountryModel, Migration

def read_csv_source(file_path, cols=[], filters={}, null_values={}):
    df = pd.read_csv(file_path, na_values=null_values)
    # apply column single value based filters
    if(filters):
        for key, value in filters.items():
            df = df[df[key] == value]

    # extract specific columns
    if(cols):
        df = df[cols]

    return df


def get_country(short_name):
    return CountryModel.query.filter_by(short_name=short_name).first()


if __name__ == "__main__":
    base_file = './sources/general_migration0016.csv'
    
    # general input migration
    filters = {}
    filters['Variable'] = 'Inflows of foreign population by nationality'
    cols = [
        'CO2',
        'Country of birth/nationality',
        'COU',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_input_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_input_df['Value'] = general_input_df['Value'].fillna(0.0).astype(int)

    # text cleaning
    text_cols = [
        'CO2',
        'Country of birth/nationality',
        'COU',
        'Country'
    ]
    for name in text_cols:
        general_input_df[name] = general_input_df[name].str.strip().lower()


    # iterate and save in db
    for i, row in general_input_df.iterrows():
        # first check if the countries already exists

        # source
        source_country = get_country(row['Country of birth/nationality'])
        if(not source_country):
            source_country = CountryModel(row['CO2'], row['Country of birth/nationality'])

        # destination
        dest_country = get_country(row['Country of birth/nationality'])
        if(not dest_country):
            dest_country = CountryModel(row['COU'], row['Country'])
   
    '''
    # general output migration
    filters = {}
    filters['Variable'] = 'Inflows of foreign population by nationality'
    cols = [
        'Country of birth/nationality',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_outut_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_outut_df['Value'] = general_outut_df['Value'].fillna(0.0).astype(int)

    '''