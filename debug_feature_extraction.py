# debug_feature_extraction.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.feature_extractor import LightCurveProcessor

# Initialize processor
processor = LightCurveProcessor()

print("=== DEBUGGING FEATURE EXTRACTION ===")

# 1. First, let's check what's in our sample data
print("\n1. Checking sample data...")
df = pd.read_csv('data/sample_light_curve.csv')
print(f"Data shape: {df.shape}")
print(f"Time range: {df['time'].min():.2f} to {df['time'].max():.2f}")
print(f"Flux stats: min={df['flux'].min():.6f}, max={df['flux'].max():.6f}, mean={df['flux'].mean():.6f}")

# 2. Let's manually check if there's a visible transit
print("\n2. Looking for transits manually...")
time = df['time'].values
flux = df['flux'].values

# Check if we can see any dips in flux
flux_diff = np.diff(flux)
significant_dips = np.where(flux_diff < -0.001)[0]  # Look for drops > 0.1%
print(f"Significant flux drops found: {len(significant_dips)}")

if len(significant_dips) > 0:
    print("Transit-like signals detected!")
else:
    print("No obvious transit signals found.")

# 3. Test the preprocessing
print("\n3. Testing preprocessing...")
try:
    time_clean, flux_clean = processor.preprocess_light_curve(time, flux)
    print(f"✓ Preprocessing successful")
    print(f"Clean data - Time: {len(time_clean)} points, Flux range: {flux_clean.min():.6f} to {flux_clean.max():.6f}")
except Exception as e:
    print(f"✗ Preprocessing failed: {e}")

# 4. Let's create a simple plot to visualize the data
print("\n4. Creating visualization...")
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(time, flux, 'b.-', markersize=1)
plt.title('Original Light Curve')
plt.xlabel('Time')
plt.ylabel('Flux')

plt.subplot(1, 2, 2)
# Zoom in on a small section to see details
if len(time) > 100:
    plt.plot(time[:100], flux[:100], 'r.-', markersize=2)
    plt.title('First 100 points (zoomed)')
    plt.xlabel('Time')
    plt.ylabel('Flux')

plt.tight_layout()
plt.savefig('data/light_curve_debug.png', dpi=150, bbox_inches='tight')
print("✓ Visualization saved as 'data/light_curve_debug.png'")

print("\n=== DEBUG COMPLETE ===")