# Orbital Telemetry & Sensor Fusion Pipeline: Modeling Conflict-Driven Infrastructure Decay and Demographic Displacement in Sudan

This project uses VIIRS nighttime satellite radiance data, paired with ACLED conflict event data, to test whether armed conflict in Sudan produces measurable, predictable signatures in infrastructure decay and population displacement.

---

## 🔬 Core Methodology & Hypotheses

This test uses satellite observation grids to assess structural disruptions across critical administrative zones within Sudan:

### 📑 Research Question
*To what extent do satellite-derived nighttime patterns serve as an indicator of structural infrastructure decline and population displacement during active conflict in Sudan?*

### 🧪 Hypothesis Status Matrix
1. **Hypothesis 1: The "Blackout Vector" of Territorial Capture — 🟢 SUPPORTED**
   * **The Concept:** Territorial capture events produce an abrupt, statistically distinct drop in nighttime radiance, followed by a prolonged recovery period lasting more than 12 months.
   * **The Reality:** Highly supported. Time-series extraction demonstrates an abrupt dive in radiance matching the April 2023 outbreak line. Furthermore, radiance remains deeply suppressed below the pre-war baseline for nearly three years, confirming a prolonged grid failure extending well past a 12-month period.
2. **Hypothesis 2: Safe-Haven "Hyper-Urbanization" and Saturation — 🟡 PARTIALLY SUPPORTED**
   * **The Concept:** Displacement is associated with an increase in nighttime radiance in non-conflict hubs (Port Sudan), inversely mirroring the decline in the conflict zone, with growth decelerating over time as resource limitations emerge.
   * **The Reality:** Partially supported. The data clearly validates the inverse relationship: Port Sudan's light footprint escalates dramatically as Khartoum falls into darkness. However, current data does not show an asymptotic curve; rather, it reflects heavy volatility and oscillation. The resource saturation claim remains an **open question**.

### 3. Ground-Truth Sensor Fusion Validation
Looking at localized kinetic combat metrics from the **ACLED (Armed Conflict Location & Event Data)** data logs provides an objective validation framework for the satellite telemetry:
* **Pre-War Baseline (2021 – Early 2023):** Nominal or baseline kinetic events match a highly stable, bright urban radiance signal.
* **Tactical Disruption Outbreak (April 2023):** The highest historical spike in combat intensity perfectly intersects the exact month the satellite signal experiences its sharpest cliff-dive, proving artificial light decline is directly combat-driven.
* **Sustained Attrition Envelope (2023 – 2025):** Continuous, dense conflict metrics explain why the capital's grid remained suppressed, demonstrating an active operational state that systematically blocked civilian infrastructure reconstruction.
