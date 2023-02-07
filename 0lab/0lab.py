import random
from collections import Counter
from pprint import pprint 
import json
import matplotlib.pyplot as plt

N = 1000

def generate_list_of_vlues(count_of_elements: int) -> list[float]:
    "Generate subsequence to list"
    list_of_values: list = [round(random.random(), 8) \
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

def plotting_discrate_population():
    fig = plt.figure()
    # Добавление на рисунок прямоугольной (по умолчанию) области рисования
    scatter1 = plt.scatter(0.0, 1.0)
    print('Scatter: ', type(scatter1))

    graph1 = plt.plot([-1.0, 1.0], [0.0, 1.0])
    print('Plot: ', len(graph1), graph1)

    text1 = plt.text(0.5, 0.5, 'Text on figure')
    print('Text: ', type(text1))

    grid1 = plt.grid(True)   # линии вспомогательной сетки
    plt.show()

def make_interval_frequencies() -> None:
    ...



# list_of_values = generate_list_of_vlues(N)
# # print(make_collection_of_values(list_of_values))
# collections_of_values = make_collection_of_values(list_of_values)
# beautiful_print_of_discrate_population(dict(collections_of_values))
# print(collections_of_values.most_common(3))
# # print(dict.items(collections_of_values))
# # write_to_json(dict(collections_of_values))

plotting_discrate_population()
