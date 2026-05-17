import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate timestamps for 5000 minutes (approx. 3.47 days)
start_time = datetime(2026, 5, 17, 0, 0)
timestamps = [start_time + timedelta(minutes=i) for i in range(5000)]

# Initialize normal data with baseline Gaussian noise
# 1. Cooling Water Flow Rate: Stable around 12.0 LPM
cooling_flow = np.random.normal(12.0, 0.15, 5000)

# 2. Chamber Vacuum Pressure: Normal around 1.1 x 10^-6 Torr
chamber_pressure = np.random.normal(1.10, 0.03, 5000)

# 3. QCM Deposition Rate: Stable target at 2.0 A/s
qcm_rate = np.random.normal(2.00, 0.05, 5000)

# 4. Crucible Temperature: Stable around 320.0 C
crucible_temp = np.random.normal(320.0, 0.8, 5000)

# inject Anomaly: Slow vacuum micro-leak and thermal instability starting at index 4200 (minute 4200)
anomaly_start = 4200
for idx in range(anomaly_start, 5000):
    factor = (idx - anomaly_start) / (5000 - anomaly_start) # Scales from 0 to 1
    
    # Pressure drifts upwards linearly from ~1.1 to ~1.95 Torr
    chamber_pressure[idx] += 0.85 * factor + np.random.normal(0, 0.02)
    
    # Deposition rate becomes unstable and fluctuates wider
    qcm_rate[idx] += np.sin(idx * 0.1) * 0.25 * factor - 0.1 * factor + np.random.normal(0, 0.05)
    
    # Crucible temperature drifts upwards to 328 C trying to maintain rate
    crucible_temp[idx] += 8.0 * factor + np.random.normal(0, 1.2)

# Create DataFrame
df = pd.DataFrame({
    '일시 (Timestamp)': [t.strftime('%Y-%m-%d %H:%M') for t in timestamps],
    '냉각수 유량 (Cooling_Water_Flow_LPM)': np.round(cooling_flow, 2),
    '챔버 압력 (Chamber_Pressure_10n6_Torr)': np.round(chamber_pressure, 3),
    'QCM 증착속도 (QCM_Rate_A_s)': np.round(qcm_rate, 2),
    '도가니 온도 (Crucible_Temp_C)': np.round(crucible_temp, 1)
})

# Save to CSV
output_path = 'oled_deposition_sensor_dataset.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"Dataset generated successfully with {len(df)} rows and saved to '{output_path}'.")
