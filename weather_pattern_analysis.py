import xarray as xr
import matplotlib.pyplot as plt

# Load NetCDF weather dataset
ds = xr.open_dataset("weather_data.nc")

# Select temperature variable
temp = ds['temperature']

# Plot average temperature over time
temp.mean(dim='time').plot()
plt.title("Average Temperature Pattern")
plt.show()