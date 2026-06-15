# Whale Tracker

A machine-learning project for **detecting whales in aerial imagery** and **predicting where whale sightings occur** from environmental conditions. It combines computer vision (YOLOv8), geospatial mapping, and a location-regression model trained on real whale-watching data.

## Components

The project has three independent pieces:

### 1. Aerial whale detection (YOLOv8)
[`src/AerialWhaleDetectionImpl.py`](src/AerialWhaleDetectionImpl.py)

Detects whales in aerial/satellite images using a YOLOv8 model fine-tuned on ~500 labeled aerial whale images

### 2. Whale sighting map
[`src/WhaleLocationPredImpl.py`](src/WhaleLocationPredImpl.py)

Plots historical whale sightings on an interactive map, filtered to the Stellwagen Bank region off Massachusetts. Data comes from the [OBIS-SEAMAP](https://seamap.env.duke.edu/) dataset (`obis_seamap_dataset_1764`). Output is written to `src/whale_map.html`.

### 3. Whale location prediction model
[`predictionModel/model.ipynb`](predictionModel/model.ipynb)

A RandomForestRegressor that predicts the (latitude, longitude) of a whale sighting from:

- **Month** of the year
- **sea conditions** — Beaufort wind force, visibility
- **Species** (one-hot encoded)
- **Archive weather** — temperature, pressure, dew point, wind speed, humidity (from the [Open-Meteo archive API](https://open-meteo.com/))

Data is the **Futurismo Azores** whale-watching dataset (GBIF Darwin Core Archive, 2008–2018, off São Miguel Island). The notebook merges occurrence.txt, event.txt, and extendedmeasurementorfact.txt, engineers features, trains the model, and evaluates it.

## Project structure

```
whaleTracker/
├── src/
│   ├── AerialWhaleDetectionImpl.py   # YOLOv8 detection / inference
│   ├── WhaleLocationPredImpl.py      # OBIS-SEAMAP sighting map
│   └── whale_map.html                # generated map output
├── predictionModel/
│   ├── model.ipynb                   # location regression notebook
│   ├── README.md                     # dataset documentation
│   └── dataset2/gbif/                # GBIF Darwin Core Archive (event/occurrence/emof)
├── runs/detect/train/                # YOLO training run + weights & plots
├── train/images/                     # labeled aerial whale training images
├── data.yaml                         # YOLO dataset config (1 class: whale)
└── yolov8n.pt                        # base pretrained YOLOv8 nano model
```

## Setup

```bash
# Clone the repo
git clone <repo-url>
cd whaleTracker

# Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate     # Windows (Git Bash) / use venv\Scripts\activate on cmd
# source venv/bin/activate       # macOS / Linux

# Install dependencies
pip install ultralytics pandas folium scikit-learn matplotlib requests
```

## Usage

**Run whale detection on an image:**
```bash
python src/AerialWhaleDetectionImpl.py
```
This loads the trained weights (`runs/detect/train/weights/best.pt`) and runs inference on `aerialwhaleimg.jpg`. To re-train, uncomment the `model.train(...)` block at the top of the file.

**Generate the sighting map:**
```bash
python src/WhaleLocationPredImpl.py
```
Open the resulting `whale_map.html` in a browser.

**Run the location prediction model:**
```bash
jupyter notebook predictionModel/model.ipynb
```
Run the cells top to bottom to load data, fetch weather, train, and visualize results.

## Notes

- Large files (raw CSVs, `.pt`/`.tif` imagery, the `venv/`) are git-ignored — see [`.gitignore`](.gitignore).

## Data sources

- **Aerial detection** — Roboflow "Aerial Right Whale Detection" (YOLOv8 export)
- **Sighting map** — OBIS-SEAMAP dataset 1764 (Duke University)
- **Prediction model** — González García L, Barata C, Idárraga Garcés V (2025). *Whale-Watching cetacean occurrences by Futurismo Azores Adventures from 2008 to 2018 off São Miguel (Azores)*. GBIF / Futurismo Azores Adventures.
