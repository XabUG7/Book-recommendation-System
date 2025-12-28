import random
import dexplot
import matplotlib.pyplot as plt


def rows_number(df):
    """
    Show number of rows in DataFrame.
    :param df: Pandas DataFrame.
    """
    print(f'Number of rows is {len(df)}')


def unique_values(df):
    """
    Show number of unique values for each column in DataFrame.
    :param df: Pandas DataFrame.
    """
    for col in df.columns:
        print(f'Number of unique values in {col} column is {len(df[col].unique())}')


def grouping(df, col_name):
    """
    :param df:        Pandas DataFrame.
    :param col_name:  Name of column.
    :return DataFrame grouped by given column with count aggregation function
    """
    return df.groupby(col_name)['rating'].count()


def show_df_info(df):
    """
    Show basic information about DataFrame : header,
    number of rows, number of NaNs and unique values in each column.
    :param df: Pandas DataFrame.
    """
    print('Header : ')
    display(df.head())
    rows_number(df)
    print('Number of NaN values in each column : ')
    display(df.isna().sum())
    unique_values(df)


def show_duplicates(df):
    """
    Show number of duplicated rows in given DataFrame.
    :param df: Pandas DataFrame.
    """
    print('Number of duplicated rows : ')
    display(df.duplicated().sum())


def filter_random_values(n, df, col_name):
    """
    Filter randomly chosen part of DataFrame.
    :param n: Sample size
    :param df: Pandas DataFrame.
    :param col_name: DataFrame column name
    :return filtered DataFrame
    """
    # check if sample size is lower than 1
    assert n < 1
    # list of unique values in column col_name
    val_list = list(df[col_name].unique())
    # randomly choose part of DataFrame
    chosen_val = random.sample(val_list, int(n * len(val_list)))
    return df[df[col_name].isin(chosen_val)]


def generate_hist(df, col_name, title):
    """
    Generate a histogram for DataFrame grouped by col_name
    and show basic statistics.
    :param df:       Pandas DataFrame.
    :param col_name: DataFrame column name.
    :param title:    Title to be used in histogram
    """
    data_grouped = grouping(df, col_name)
    display(dexplot.hist(val='rating', data=data_grouped, title=title, cmap='plasma',
                         xlabel='Number of ratings'))
    print('Statistics for dataframe grouped by ' + str(col_name) + ':')
    print(data_grouped.describe())
