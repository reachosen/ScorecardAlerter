The script outputs sane, borderline, and insane ranges for each healthcare metric based on simulated historical data. These ranges help healthcare administrators understand performance variability and set improvement targets.

Implementation Details
Historical Data Simulation: Simulates 12 months of data for each metric using a normal distribution centered around defined mean values with specified standard deviations.
Range Suggestion: Calculates mean and standard deviation from the historical data to suggest sane (±1 SD), borderline (±2 SD), and insane (outside ±2 SD) ranges.
Practical Numbers: Uses realistic averages and standard deviations to reflect achievable performance targets and expected variability in healthcare settings.
Metric Parameters
30-day Readmission:
Mean: 15%
Standard Deviation: 3%
HTN: Controlling High BP:
Mean: 70%
Standard Deviation: 5%
These parameters are based on the goal of minimizing negative outcomes (e.g., readmissions) and maximizing positive outcomes (e.g., effective BP control).
