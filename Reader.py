import dask.dataframe as dd
import time

# global dataframe will be used in main script and the methods
df = None
search_column = 'store'


def load_csv_to_dataframe():
    global df
    df = dd.read_csv('./data/dataset.txt', sep=';', usecols=[search_column])
    df = df.compute()


def create_search_items_list():
    june = [6361, 3458, 6340, 6470, 6481, 3768, 5128, 4886, 4887, 3065, 4889, 6466, 3482]
    july = [6326, 3110, 4745, 3634, 6392, 4656, 5382, 3608]
    return june + july


def find_one(store_id):
    df_found = df[df[search_column] == store_id]
    # quick glance of the dataframe
    print(df_found.head(5))
    # place of the item (which row)
    index = df_found.index
    number_of_rows = len(index)
    print(number_of_rows)
    print("Find one took: ", time.time() - t)


# get the time to check time consumed
t = time.time()

# load csv file
load_csv_to_dataframe()

# create search items
search_items_list = create_search_items_list()

# filter the dataframe columnt with the search items
mask = df[search_column].apply(lambda x: any(item for item in search_items_list if item == x))
df1 = df[mask]

# get the unique ones
in_the_list = df1[search_column].unique()

# print the results
print("Found : ", in_the_list)
print("Missing : ", list(set(search_items_list) - set(in_the_list)))

# print the time consumed
print("Whole process took: ", time.time() - t)
