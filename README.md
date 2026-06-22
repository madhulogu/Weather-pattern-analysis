# Weather-pattern-analysis
Here’s a **simple, concrete example** you can include in your README to show how weather pattern analysis works in practice:

---

## 📌 Example: Temperature Trend Analysis

### 🧾 Sample Dataset

| Date       | Temperature (°C) | Rainfall (mm) |
| ---------- | ---------------- | ------------- |
| 2024-01-01 | 28               | 0             |
| 2024-01-02 | 29               | 2             |
| 2024-01-03 | 31               | 0             |
| 2024-01-04 | 30               | 5             |
| 2024-01-05 | 32               | 0             |

---

### 🧠 Analysis Goal

Identify:

* Temperature trend over time
* Relationship between rainfall and temperature

---

### 💻 Example Code (Python)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Temperature": [28, 29, 31, 30, 32],
    "Rainfall": [0, 2, 0, 5, 0]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Plot temperature trend
plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend")
plt.show()
```

---

### 📈 Output Insight

* Temperature shows a **gradual increasing trend**
* Rainfall spikes correspond to **slight drops in temperature**
* Helps understand **short-term weather fluctuations**

---

### 🔍 Interpretation

* Warmer days tend to follow dry conditions
* Rainfall may temporarily reduce temperature
* This pattern can be useful for:

  * Agriculture planning 🌾
  * Energy consumption forecasting ⚡
  * Climate monitoring
