def monitor_matrix(func):
    def wrapper(*args, **kwargs):
        matrix = func(*args, **kwargs)
        anomaly_detected = detect_anomaly(matrix)
        if anomaly_detected is not None:
            print(f"Anomaly found: {anomaly_detected}")
        return matrix

    def detect_anomaly(matrix):
        for row_index, row in enumerate(matrix):
            for item in row:
                if item != 0 and item != 1:
                    return item  # Anomaly detected, return the anomaly value
        return None

    return wrapper
