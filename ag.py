import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Excel dosyasını okuyun
df = pd.read_excel("C:/Users/Monster/Desktop/ag.xlsx")

# Graf oluşturun
G = nx.Graph()
for index, row in df.iterrows():
    G.add_node(row['Name'], country=row['Country'], longitude=row['Longitude'], latitude=row['Latitude'])

# Aynı ülkedeki limanları birbirine bağlayın
for node1, attr1 in G.nodes(data=True):
    for node2, attr2 in G.nodes(data=True):
        if attr1["country"] == attr2["country"] and node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)

# Düğümlerin etiketlerini güncelleyin (liman adı ve ülke)
node_labels = {node: f"{node}\n({attr['country']})" for node, attr in G.nodes(data=True)}

# Liman renkleri (her liman için ülke renklerinden farklı tonlar kullanarak)
# Düğüm isimlerine göre renk ataması yapın


# Daha fazla renk elde etmek için bir renk haritası kullanın
cmap = plt.get_cmap("Set3")  # Renk haritasını değiştirin

# 3 boyutlu düzen için düğüm pozisyonlarını önceden belirleyin
pos = nx.kamada_kawai_layout(G, dim=3, scale=3)  # Kamada-Kawai düzeni kullanın ve scale parametresini artırın

# 3D çizim alanı oluşturun ve boyutunu ayarlayın
fig = plt.figure(figsize=(12, 10))  # Genişlik: 12, Yükseklik: 10
ax = fig.add_subplot(111, projection="3d")

# Düğümleri 3D alana yerleştirin, düğüm boyutlarını artırın ve kenarlarını kalınlaştırın
x, y, z = zip(*pos.values())
ax.scatter(x, y, z, s=150, edgecolors="k", linewidths=1.5, cmap=cmap)  # Düğüm renklerini renk haritasından alın

# Kenarları 3D alana çizin
for u, v in G.edges():
    x1, y1, z1 = pos[u]
    x2, y2, z2 = pos[v]
    ax.plot([x1, x2], [y1, y2], [z1, z2], color="red", alpha=0.5, linewidth=0.5)  # Kenarların kalınlığını ve opaklığını artırın

# Etiketleri ekleyin
for node, (x, y, z) in pos.items():
    ax.text(x, y, z, node_labels[node], fontsize=8, ha='center', va='center')  # Düğüm etiketlerini büyütün

# Görünümü ayarlayın
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

