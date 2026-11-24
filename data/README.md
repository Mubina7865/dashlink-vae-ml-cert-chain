# Data Registry

## Raw dataset: DASHlink Curated 4-Class Anomaly Detection Data Set (Matthews, 2022)
Obtained prior to project start; identity + integrity verified 2026-11-23.

| File | Size (bytes) | SHA-256 |
|---|---|---|
| DASHlink_full_fourclass_raw_comp.npz | 1,759,319,547 | c5807fe88e34b838e669d385e50e967c14032c0843c8b3cf915642480393d6a2 |
| DASHlink_full_fourclass_raw_meta.csv | 4,101,030 | aa464d2badc19553cea0cda419cb2c31277f9520728ace13a6278714b37bdc2e |

Provenance: NASA DASHlink resource 1018 - https://c3.ndc.nasa.gov/dashlink/resources/1018/
Documentation: DASHlink_full_data_documentation.pdf (435,573 bytes)

## Excluded from registry (recorded decision, 2026-11-23)
Tail_682_1.zip .. Tail_687_1.zip (~5 GB): raw FOQA tail data underlying the curated
set. Out of scope for the SuC data environment (doc section 7.1). Location recorded in
docs/data-infrastructure.md. Possible future use: out-of-envelope/OOD inputs for REQ-06
robustness tests; decision deferred to P3.
