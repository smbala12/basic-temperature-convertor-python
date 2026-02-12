# 🌡️ Temperature Converter (Python)

A simple Python program that converts temperatures between:

- Celsius (°C)
- Fahrenheit (°F)
- Kelvin (°K)

> ⚠️ Note: All conversion values are approximate.

---

## 📌 Features

The program allows the user to convert between:

- C to F
- C to K
- F to C
- F to K
- K to C
- K to F

It also:

- Prevents same-unit conversions (e.g., C to C)
- Handles empty input
- Displays an error message for invalid conversions
- Rounds results to 2 decimal places
- Displays the correct temperature symbol (°C, °F, °K)

---

## 🔁 Conversion Formulas Used

- **C to F** → (C × 9/5) + 32  
- **C to K** → C + 273.15  
- **F to C** → (F − 32) × 5/9  
- **F to K** → (F − 32) × 5/9 + 273.15  
- **K to C** → K − 273.15  
- **K to F** → (K − 273.15) × 9/5 + 32  

---

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Save the file as `temperature_converter.py`
3. Open a terminal or command prompt.
4. Run:

```bash
python temperature_converter.py
