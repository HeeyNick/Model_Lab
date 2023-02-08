import random
from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objs as go

import pandas as pd

N = 1000

def generate_list_of_vlues(count_of_elements: int) -> list[float]:
    "Generate subsequence to list"
    list_of_values: list = [round(random.random(), 6) \
                            for i in range(count_of_elements)]
    return list_of_values
    
def make_collection_of_values(list_of_values: list[float]) -> Counter[float]:
    "Discrete distribution function (frequency polygon)"
    return Counter(list_of_values)

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

    plt.bar(list(collections_of_values.keys()), \
            collections_of_values.values(), width=0.005, color='g')
    plt.show()

    # fig = px.scatter(x=collections_of_values.keys(), y=collections_of_values.values())
    # fig.show()


def make_interval_population() -> None:
    ...



list_of_values = generate_list_of_vlues(N)
collections_of_values = make_collection_of_values(list_of_values)

beautiful_print_of_discrate_population(dict(collections_of_values))
print(collections_of_values.most_common(3))

plotting_discrate_population(dict(collections_of_values))
