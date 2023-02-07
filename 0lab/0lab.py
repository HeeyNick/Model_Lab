import random
from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np

N = 10000

def generate_list_of_vlues(count_of_elements: int) -> list[float]:
    "Generate subsequence to list"
    list_of_values: list = [round(random.random(), 8) \
                            for i in range(count_of_elements)]
    return list_of_values
    
def make_collection_of_values(list_of_values: list[float]) -> Counter[float]:
    "Discrete distribution function (frequency polygon)"
    return Counter(list_of_values)

# def make_unique_values(list_of_values: list[float]):
#     unique, counts = np.unique (list_of_values, return_counts= True )
#     return(np.asarray ((unique, counts)). T )

def beautiful_print_of_discrate_population(collections_of_values: dict) -> None:
    "Print Discrete distribution function (frequency polygon)"
    print('{:<13} {}'.format('Value', 'Count'))
    [print(values, " ", collections_of_values[values]) \
     for values in collections_of_values]




def write_to_json(collections_of_values: dict) -> None:
    "Write to json file frequency polygon"
    with open('data.json', 'w') as outfile:
        json.dump(collections_of_values, outfile)


def convert_dict_to_numpy(collections_of_values: dict):
    result = collections_of_values.items()
    data = list(result)
    numpy_array = np.array(data)
    return numpy_array

def plotting_discrate_population(collections_of_values: dict) -> None:
    # fig, ax = plt.subplots()
    plt.plot(collections_of_values.keys(), collections_of_values.values())
    # ax.scatter(data=collections_of_values)
    plt.show()

def make_interval_frequencies() -> None:
    ...



list_of_values = generate_list_of_vlues(N)
# print(make_unique_values(list_of_values))
# # print(make_collection_of_values(list_of_values))
collections_of_values = make_collection_of_values(list_of_values)
# beautiful_print_of_discrate_population(dict(collections_of_values))
# print(collections_of_values)
print(collections_of_values.most_common(3))
# # print(dict.items(collections_of_values))
# # write_to_json(dict(collections_of_values))

plotting_discrate_population(dict(collections_of_values))
# numpy_array = (convert_dict_to_numpy(dict(collections_of_values)))
# print(numpy_array[::10])
# a = (numpy_array[0][::10])
# b = (int(numpy_array[0][1::]))
# print(a)
# print(b)
# plt.plot(a, b)
# plt.show()