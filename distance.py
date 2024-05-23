import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
import tkinter as tk
from tkinter import messagebox

def haversine_distance(lat1, lon1, lat2, lon2):
    # dünyanın yarıçapı km cinsinden
    R = 6371.0
    
    # dereceleri radyanlara dönüştürür
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    # formül için koordinatlar arasındaki farkları alır
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # haversine formülü
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    
    return distance

def plot_3d_distance(lat1, lon1, lat2, lon2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. nokta
    x1, y1, z1 = lon1, lat1, 0
    ax.scatter(x1, y1, z1, color='r', marker='o')
    ax.text(x1, y1, z1, '1', color='black')
    
    # 2. nokta
    x2, y2, z2 = lon2, lat2, 0
    ax.scatter(x2, y2, z2, color='b', marker='o')
    ax.text(x2, y2, z2, '2', color='black')
    
    # noktalar arası çizgi
    ax.plot([x1, x2], [y1, y2], [z1, z2], color='g')
    
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    ax.text((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2, f'{distance:.2f} km', color='black')
    
    ax.set_xlabel('Boylam')
    ax.set_ylabel('Enlem')
    ax.set_zlabel('Yükseklik')
    
    plt.show()

def calculate_distance():
    try:
        lat1 = float(entry_lat1.get())
        lon1 = float(entry_lon1.get())   
        lat2 = float(entry_lat2.get())
        lon2 = float(entry_lon2.get())
        
        plot_3d_distance(lat1, lon1, lat2, lon2)
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz giriş! Lütfen sayısal değerler girin.")

# tkinter penceresini oluşturur
root = tk.Tk()
root.title("Koordinat Mesafe Hesaplayıcı")

# kullanıcı arayüzü öğelerini oluşturur
label_lat1 = tk.Label(root, text="Birinci noktanın enlemi:")
label_lon1 = tk.Label(root, text="Birinci noktanın boylamı:")
label_lat2 = tk.Label(root, text="İkinci noktanın enlemi:")
label_lon2 = tk.Label(root, text="İkinci noktanın boylamı:")
entry_lat1 = tk.Entry(root)
entry_lon1 = tk.Entry(root)
entry_lat2 = tk.Entry(root)
entry_lon2 = tk.Entry(root)
calculate_button = tk.Button(root, text="Mesafeyi Hesapla", command=calculate_distance)

# kullanıcı arayüzü öğelerini düzenler
label_lat1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_lon1.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_lat2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_lon2.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_lat1.grid(row=0, column=1, padx=5, pady=5)
entry_lon1.grid(row=1, column=1, padx=5, pady=5)
entry_lat2.grid(row=2, column=1, padx=5, pady=5)
entry_lon2.grid(row=3, column=1, padx=5, pady=5)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
