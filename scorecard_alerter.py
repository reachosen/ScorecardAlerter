import pandas as pd
import numpy as np

def load_metric_data(filepath):
    data = pd.read_csv(filepath)
    data['SNP_MONTH_YR'] = pd.to_datetime(data['SNP_MONTH_YR'], format='%b-%Y')
    return data

def calculate_statistics(data, metric, pavilion):
    historical_data = data[(data['MEAS'] == metric) & (data['PAV_NAME'] == pavilion)]
    historical_data = historical_data[historical_data['SNP_MONTH_YR'] < historical_data['SNP_MONTH_YR'].max()]
    if not historical_data.empty:
        mean = historical_data['FYTD_P'].mean()
        std_dev = historical_data['FYTD_P'].std()
        return mean, std_dev
    return None, None

def validate_latest_month(data, mean, std_dev):
    latest_month_data = data[data['SNP_MONTH_YR'] == data['SNP_MONTH_YR'].max()]
    results = {}
    for index, row in latest_month_data.iterrows():
        metric_value = row['FYTD_P']
        metric_abbr = row['METRIC_ABBR']
        if pd.isnull(metric_value):
            results[metric_abbr] = {'Classification': 'Data Missing'}
            continue
        # Define non-overlapping ranges
        sane_range = (mean - std_dev, mean + std_dev)
        borderline_lower_range = (mean - 2 * std_dev, mean - std_dev)
        borderline_upper_range = (mean + std_dev, mean + 2 * std_dev)
        # Classify metric values
        if borderline_lower_range[0] <= metric_value < borderline_lower_range[1]:
            classification = 'Borderline'
        elif borderline_upper_range[0] <= metric_value < borderline_upper_range[1]:
            classification = 'Borderline'
        elif sane_range[0] <= metric_value < sane_range[1]:
            classification = 'Sane'
        elif metric_value < borderline_lower_range[0]:
            classification = 'Insane'
        elif metric_value >= borderline_upper_range[1]:
            classification = 'Insane'
        else:
            classification = 'Unclassified'  # Catch-all for unexpected cases

        results[metric_abbr] = {
            'Classification': classification,
            'Value': metric_value,
            'Mean': mean,
            'Standard Deviation': std_dev,
            'Sane Range': sane_range,
            'Borderline Range': (borderline_lower_range, borderline_upper_range)
        }
    return results

def analyze_metrics(filepath):
    data = load_metric_data(filepath)
    metrics = data['MEAS'].unique()
    pavilions = data['PAV_NAME'].unique()
    for pavilion in pavilions:
        for metric in metrics:
            mean, std_dev = calculate_statistics(data, metric, pavilion)
            if mean is not None and std_dev is not None:
                validation_results = validate_latest_month(data[(data['MEAS'] == metric) & (data['PAV_NAME'] == pavilion)], mean, std_dev)
                latest_date = data['SNP_MONTH_YR'].max().strftime('%b-%Y')
                print(f"Validation Results for {metric} in {pavilion} as of {latest_date}: {validation_results}")

analyze_metrics('metric_data.csv')
