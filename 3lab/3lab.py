import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
from io import TextIOWrapper
import sys


def read_graph(f: TextIOWrapper) -> nx.Graph:
    g = nx.Graph()

    s = f.readline()
    l = s.split(' ')
    n = int(l[0])
    g.add_nodes_from(range(n))

    for s in f.readlines():
        l = s.split(' ')
        g.add_edge(int(l[0]), int(l[1]))
        g.add_edge(int(l[1]), int(l[0]))

    return g

def display_graph():
    g = nx.Graph()
    with open('a.gph', 'r') as f:
        g = read_graph(f)
    nx.draw_spring(g, with_labels=True)
    plt.show()

def create_graph(height: int, width: int):
    with open('a.gph', 'w') as f:
        print("Create graph") 
        f.write(f'{1} {1}')
        m = 1
        if(width > 1):
            r = random.randint(1, height-m)
            rp = random.randint(1, width-m)

        cnt = height + 1
        for i in range(height):
            if (i == r):
                if width == 1:
                    print(i,'--',i + 1)
                    f.write(f'{i} {i + 1}')
                else:
                    for j in range(width):
                        if j == rp:
                            print(i,'--',i + 1)
                            f.write(f'\n{i} {i + 1}')
                        else:
                            print(i,'--',cnt)
                            f.write(f'\n{i} {cnt}')
                            cnt += 1
            else:
                if width > 1:
                    rr = random.randint(1, width-m+1)
                if rr == 1:
                    print(i,'--',i + 1)
                    f.write(f'\n{i} {i + 1}')
                else:
                    if rr > 1:
                        rrp = random.randint(1, rr-m)
                    for k in range(rr):
                        if (k == rrp):
                            print(i,'--',i + 1)
                            f.write(f'\n{i} {i + 1}')
                        else:
                            print(i,'--',cnt)
                            f.write(f'\n{i} {cnt}')
                            cnt += 1

if __name__ == '__main__':
    print('Input Height: ')
    height = int(input())
    if height < 2:
        print("Height < 2")
        sys.exit()
    print('Input Width: ')
    width = int(input())
    if width < 1:
        print("Width < 1")
        sys.exit()

    create_graph(height, width)
    display_graph()

    
