import dask.dataframe as dd
import time

t = time.time()
df = dd.read_csv('../CSV/data/dataset.txt', sep=';', usecols=['store'])
df = df.compute()


def create_search_items_list():
    june = [6361, 3458, 6340, 6470, 6481, 3768, 5128, 4886, 4887, 3065, 4889, 6466, 3482]
    july = [6326, 3110, 4745, 3634, 6392, 4656, 5382, 3608]
    return june + july


def find_one(store_id):
    df_found = df[df['store'] == store_id]
    print(df_found.head(5))
    index = df_found.index
    number_of_rows = len(index)
    print(number_of_rows)
    print("Find one took: ", time.time() - t)


# find_one(6529)

search_items_list = create_search_items_list()

mask = df.store.apply(lambda x: any(item for item in search_items_list if item == x))
df1 = df[mask]

in_the_list = df1.store.unique()

print("Found : ", in_the_list)
print("Missing : ", list(set(search_items_list) - set(in_the_list)))

print("Whole process took: ", time.time() - t)
