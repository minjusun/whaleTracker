import pandas as pd
import folium

df = pd.read_csv(r"C:\Users\minju\Desktop\CSProjects\whaleTracker\obis_seamap_dataset_1764_csv_v1.4.0_96891\obis_seamap_dataset_1764_points.csv")

df = df[['decimal_latitude', 'decimal_longitude', 'event_date', 'organism_name']].dropna()

stellwagen = df[
    (df['decimal_latitude'].between(41, 45)) &
    (df['decimal_longitude'].between(-71, -66))
]

# Create map centered on Stellwagen Bank
m = folium.Map(location=[42.5, -70.0], zoom_start=8)

# Add a dot for each sighting
for _, row in stellwagen.iterrows():
    folium.CircleMarker(
        location=[row['decimal_latitude'], row['decimal_longitude']],
        radius=3,
        color='blue',
        fill=True,
        popup=f"{row['organism_name']} - {row['event_date']}"
    ).add_to(m)

# Save as HTML file you can open in browser
m.save("whale_map.html")
print("Map saved- type start whale_map.html")