# Data Details
### data collected from GBIF site off São Miguel Island (Azores, Portugal) from whale-watching vessels between 2008 and 2018
---
## event data:
- event level info on whale watching trips. location date, weather, country, depth
- best usage: timestamps, locations, extra environmental context

## occurrence.txt 
- records the actual animal sightings — each row is one observed organism (or group), noting the species (scientific name, taxonomy), how many individuals were seen, their sex/life stage if recorded, and whether they were present. It links each sighting to an encounter event via the eventID and uses a unique occurrenceID per record.
## event.txt 
- is the spatial and temporal backbone — it records when and where each cruise and encounter took place. It has two levels: parent cruise events (the full boat trip, with a date range and a bounding multipoint geometry) and child encounter events (specific sightings within a cruise, with a point location and narrower time window). It also stores depth, country, water body, and coordinate uncertainty.

## extendedmeasurementorfact.txt 
- holds quantitative and categorical measurements; It links back to either an event or a specific occurrence via occurrenceID. In this dataset it captures things like Beaufort wind force, visibility percentage, the sampling instrument used (observers), and the minimum/maximum individual count estimates, essentially the environmental conditions and refined count data for each encounter.

## Measurment data:
- Contains detailed observations tied to specific encounters
- Includes Beaufort wind force, visibility, sampling instruments, observer info
- Linked to occurrences via occurrenceID
- best usage: Environmental conditions, methodology, detailed measurements

---


- citation: González García L, Barata C, Idárraga Garcés V (2025). Whale-Watching cetacean occurrences by Futurismo Azores Adventures from 2008 to 2018 off São Miguel (Azores). Version 1.0. Futurismo Azores Adventures. http://ipt.gbif.pt/ipt/resource?r=futurismo_sm_0818

