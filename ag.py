import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# CSV dosyasından verileri oku
df = pd.read_csv("ag.csv", delimiter=";")

# Graf oluştur
G = nx.Graph()
for index, row in df.iterrows():
    G.add_node(row['Name'], country=row['Country'], pos=(row['Longitude'], row['Latitude']))

# Ülkesi aynı olan limanları bağla
for node1, attr1 in G.nodes(data=True):
    for node2, attr2 in G.nodes(data=True):
        if attr1["country"] == attr2["country"] and node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)

# Liman adı ve ülke etiketlerini güncelle
node_labels = {node: f"{node}\n({attr['country']})" for node, attr in G.nodes(data=True)}

# Grafı oluştur
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

# Ülkeleri ve eyaletleri çiz
ax.add_feature(cfeature.COASTLINE, linewidth=1.5)
ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=1)

# Düğümleri çiz
for node, (lon, lat) in nx.get_node_attributes(G, 'pos').items():
    ax.plot(lon, lat, 'o', markersize=10, color='skyblue', transform=ccrs.PlateCarree())
    ax.text(lon, lat, node, fontsize=10, ha='center', va='center', transform=ccrs.PlateCarree())

# Kenarları çiz
for u, v in G.edges():
    lon1, lat1 = G.nodes[u]['pos']
    lon2, lat2 = G.nodes[v]['pos']
    ax.plot([lon1, lon2], [lat1, lat2], transform=ccrs.PlateCarree(), color='darkblue', linewidth=1)

# Düğüm etiketlerini ekle
for node, (lon, lat) in nx.get_node_attributes(G, 'pos').items():
    ax.text(lon, lat, node, fontsize=10, ha='center', va='center', transform=ccrs.PlateCarree())

# Harita boyutunu ayarla
ax.set_extent([-180, 180, -90, 90])

plt.title('Dünya Haritası Üzerinde Limanlar', fontsize=14)
plt.legend(loc='upper right', fontsize=10, markerscale=1.5)
plt.show()
