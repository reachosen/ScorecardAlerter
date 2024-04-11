# -*- coding: utf-8 -*-
"""Scorecard Alerter.ipynb

Updated script for practical and clear data analysis in healthcare metrics with test cases.

Original file location:
    https://colab.research.google.com/drive/1vMHHxAvBvYJazwbr9rC_Jw9QvEY_43jC
"""

import numpy as np

def check_data_point(value, mean, std_dev):
    """
    Classify a data point as sane, borderline, or insane, providing clear explanations.
    This function uses hardcoded thresholds to determine classifications.
    """
    sane_lower, sane_upper = mean - std_dev, mean + std_dev
    borderline_lower, borderline_upper = mean - 2*std_dev, mean + 2*std_dev

    if value < borderline_lower or value > borderline_upper:
        return "Insane"
    elif value < sane_lower or value > sane_upper:
        return "Borderline"
    else:
        return "Sane"

# Example metrics with realistic means and variability
metrics = {
    "30-day Readmission": {"mean": 15, "std_dev": 3},
    "HTN: Controlling High BP": {"mean": 70, "std_dev": 5}
}

# Hardcoded examples for each metric showing different classifications based on standard deviations from the mean.
# this will be replaced from either an AutoSuggester Value or manual file.
hardcoded_values = {
    "30-day Readmission": {
        # 'Sane' value: 14% readmission rate, which means 14 out of every 100 patients discharged from the hospital 
        # are readmitted within 30 days. This rate is considered 'sane' because it falls within one standard deviation (SD) 
        # from the mean (average) of 15%, indicating it is a common and expected outcome within the current operational performance.
        "sane": 14,  # Within 1 SD from mean
        
        # 'Borderline' value: 20% readmission rate. This indicates a higher-than-average scenario where 20 out of every 100 
        # patients are readmitted. Being exactly 2 SDs from the mean, this rate is borderline—it’s unusual but not extreme enough 
        # to be alarming. It serves as a warning signal that some factors might be adversely affecting patient outcomes.
        "borderline": 20,  # Exactly 2 SD from mean
        
        # 'Insane' value: 25% readmission rate, which is significantly higher than the mean. This rate suggests that 25 out of 
        # every 100 patients are being readmitted within 30 days. Since it’s more than 2 SDs from the mean, it is considered 
        # 'insane'—a rare and critical indicator that potentially serious issues need immediate attention.
        "insane": 25  # More than 2 SD from mean, very unusual
    },
    "HTN: Controlling High BP": {
        # 'Sane' value: 68% control rate means that 68 out of 100 patients with high blood pressure are successfully managing 
        # their condition under current health interventions. This rate is within one standard deviation from the mean of 70%, 
        # showing that it's a typical and effective rate of control, aligning with expected healthcare management outcomes.
        "sane": 68,  # Within 1 SD from mean
        
        # 'Borderline' value: 80% control rate is higher than usual—80 out of 100 patients have their high blood pressure under 
        # control. This rate is at the boundary of 2 SDs from the mean, categorizing it as borderline. It indicates very good 
        # performance but needs to be monitored for consistency or potential data inaccuracies.
        "borderline": 80,  # Exactly 2 SD from mean
        
        # 'Insane' value: 85% control rate is exceptionally high and far exceeds the average. It means 85 out of every 100 
        # patients are controlling their high blood pressure effectively. Being more than 2 SDs from the mean, this rate is 
        # considered 'insane'—it’s an extraordinary and uncommon outcome that could suggest exceptionally effective treatment 
        # strategies or possibly data errors or anomalies.
        "insane": 85  # More than 2 SD from mean, very unusual
    }
}


# Test cases to confirm the classification logic
def test_metric_classification():
    print("Testing Metric Classifications:")
    for metric, values in hardcoded_values.items():
        mean = metrics[metric]["mean"]
        std_dev = metrics[metric]["std_dev"]
        sane_range = (mean - std_dev, mean + std_dev)
        borderline_range = (mean - 2*std_dev, mean + 2*std_dev)
        insane_range = f"<{borderline_range[0]:.2f}% or >{borderline_range[1]:.2f}%"
        print(f"\nMetric: {metric}")
        print(f"  Sane Range: {sane_range[0]:.2f}% to {sane_range[1]:.2f}%")
        print(f"  Borderline Range: {borderline_range[0]:.2f}% to {borderline_range[1]:.2f}%")
        print(f"  Insane Range: {insane_range}")
        for category, value in values.items():
            expected = category.capitalize()
            actual = check_data_point(value, mean, std_dev)
            result = "Pass" if actual == expected else "Fail"
            print(f"  Test {category.capitalize()} ({value}%): Expected = {expected}, Actual = {actual} -> {result}")

# Run the test cases
test_metric_classification()
