# Whale location regression — summary stats

## Setup

- **Dataset:** Futurismo Azores whale-watching observations, GBIF DwC-A
- **Date range covered:** 2009-09-18 → 2018-12-27
- **Geographic centerpoint:** 37.659° N, −25.606° E (off São Miguel, Azores)
- **Rows after cleaning & weather merge:** 13,153 (from 20,413 raw occurrences)
- **Split:** 80% train / 20% test, `random_state=42`
- **Model:** `RandomForestRegressor`, 300 trees, predicting `(decimalLatitude, decimalLongitude)` jointly
- **Features (15 total):** month, beaufort, visibility_km, 6 Open-Meteo hourly variables, one-hot species

## Headline numbers

| metric | value | interpretation |
|---|---|---|
| MAE latitude | 0.0238° | ≈ **2.6 km** average miss N–S |
| MAE longitude | 0.0595° | ≈ **5.2 km** average miss E–W (1° lon at 37.7° N ≈ 88 km) |
| R² latitude | **0.717** | model explains ~72% of variance in latitude |
| R² longitude | **0.725** | model explains ~73% of variance in longitude |
| mean haversine error | **6.33 km** | average distance between predicted and actual point |
| median haversine error | **4.18 km** | half of predictions land within 4.2 km |
| baseline (predict mean lat/lon) | 14.99 km | what "no model, just guess the centerpoint" gets |

**Improvement over baseline:** mean error drops by **58%** (14.99 → 6.33 km). The model is meaningfully better than dumb prediction.

That `mean > median` gap (6.33 vs 4.18) means the error distribution is right-skewed: most predictions are decent, but a tail of bad ones drags the mean up.

## Feature importances (top 15)

```
wind_speed_10m               0.184
dew_point_2m                 0.143
temperature_2m               0.137
relative_humidity_2m         0.111
surface_pressure             0.103
pressure_msl                 0.103
month                        0.080
beaufort                     0.055
sp_Physeter macrocephalus    0.023
sp_Globicephala              0.007
sp_Delphinus delphis         0.005
sp_Balaenoptera physalus     0.005
sp_Balaenoptera borealis     0.005
sp_Tursiops truncatus        0.005
sp_Grampus griseus           0.005
```

**Takeaways:**
- The six Open-Meteo weather variables account for ~78% of total importance. Weather is doing most of the work.
- `wind_speed_10m` is the single strongest predictor — wind drives sea state, which drives where the operator can safely take the boat.
- `month` (8%) is a distant second tier — there's some seasonal signal, but it's smaller than weather.
- `beaufort` (in-situ wind from the boat) only gets 5.5% — largely redundant with `wind_speed_10m` from the API.
- Species columns are all tiny (<2.5% each). Sperm whale stands out slightly because that species is found in deeper offshore water and the others aren't.
- `visibility_km` didn't even make top 15 — drop it next iteration.

 Random Forest importance is split across correlated features. `temperature_2m` and `dew_point_2m` are highly correlated; `surface_pressure` and `pressure_msl` are nearly identical. The true "weather signal" is even more concentrated than the table makes it look.

## NOTE!!

- All data comes from one whale-watching operator's boat trips from one harbor on São Miguel.
- The boat's route on a given day is itself a function of weather (operators avoid bad sea states, run different patterns by season).
- So the model is partly learning "**where the boat goes given the weather**," not just "where whales are given the weather."

Useful if in São Miguel harbor planning a trip; training data covers a ~50 km box.

## Working on...

1. Drop `visibility_km` and one of each correlated pair (`pressure_msl`, `dew_point_2m`) — shouldn't affect accuracy and clarifies importance.
2. Try `GradientBoostingRegressor` or `XGBoost` — often btter than rf
3. Add lagged weather (24h, 48h prior) — whales may respond to weather *changes*, not just instantaneous conditions.
4. Hold out by **time** (train on 2009–2016, test on 2017–2018) instead of random split, to check if the model generalizes to unseen seasons.
