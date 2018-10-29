import pandas as pd

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


if __name__ == "__main__":
    base_file = './data/general_migration0016.csv'
    
    # general input migration
    filters = {}
    filters['Variable'] = 'Inflows of foreign population by nationality'
    cols = [
        'Country of birth/nationality',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_input_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_input_df['Value'] = general_input_df['Value'] = general_input_df['Value'].fillna(0.0).astype(int)
    

    # general input migration
    filters = {}
    filters['Variable'] = 'Inflows of foreign population by nationality'
    cols = [
        'Country of birth/nationality',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_input_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_input_df['Value'] = general_input_df['Value'] = general_input_df['Value'].fillna(0.0).astype(int)

    # general input migration
    filters = {}
    filters['Variable'] = 'Inflows of foreign population by nationality'
    cols = [
        'Country of birth/nationality',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_input_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_input_df['Value'] = general_input_df['Value'] = general_input_df['Value'].fillna(0.0).astype(int)
    

    # general input migration
    filters = {}
    filters['Variable'] = 'Outflows of foreign population by nationality'
    cols = [
        'Country of birth/nationality',
        'Country',
        'Year',
        'Value'
    ]
    null_values = {'Value': 0}
    general_output_df = read_csv_source(base_file, cols, filters, null_values)

    # type casting
    general_output_df['Value'] = general_input_df['Value'] = general_input_df['Value'].fillna(0.0).astype(int)