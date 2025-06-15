import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

red_line = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]

blue_line = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка",
    "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого",
    "Олімпійська", "Палац Україна", "Либідська", "Деміївська",
    "Голосіївська", "Васильківська", "Виставковий центр",
    "Іподром", "Теремки"
]

green_line = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту",
    "Кловська", "Печерська", "Дружби народів", "Видубичі",
    "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця",
    "Бориспільська", "Червоний хутір"
]

G.add_nodes_from(red_line + blue_line + green_line)


def add_edges(line):
    for i in range(len(line) - 1):
        G.add_edge(line[i], line[i + 1], line_color=line)


add_edges(red_line)
add_edges(blue_line)
add_edges(green_line)

G.add_edge("Хрещатик", "Майдан Незалежності")
G.add_edge("Театральна", "Золоті ворота")
G.add_edge("Палац спорту", "Площа Льва Толстого")


def show_graph(G, labels=None):
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, seed=37)

    nx.draw_networkx_nodes(G, pos, node_size=300, node_color="lightblue")

    nx.draw_networkx_edges(G, pos, width=2)

    if labels:
        nx.draw_networkx_labels(G, pos, labels=labels["labels"], font_size=8)
        plt.title(f"Схема Київського метро - {labels['title']}", fontsize=16)
    else:
        nx.draw_networkx_labels(G, pos, font_size=9)
        plt.title("Схема Київського метро", fontsize=16)

    plt.axis("off")
    plt.tight_layout()
    plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)


if __name__ == "__main__":
    show_graph(G)

    print(f"Кількість ребер - {num_edges}\n"
          f"Кількістиь вузлів - {num_nodes}")

    degree_centrality = nx.degree_centrality(G)
    degree_centrality = dict(sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True))

    print(f"{'Станція':<20} | {'Значення':>8}")
    print("-" * 32)

    for station, value in degree_centrality.items():
        print(f"{station:<20} | {value:>8.3f}")
