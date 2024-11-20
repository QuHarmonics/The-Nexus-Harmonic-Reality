### **Validation Metrics for the Dual State Prediction Model (DSPM)**

To rigorously validate the DSPM, we need to establish robust metrics for assessing its performance. These metrics should evaluate both short-term precision (Mark 1-based) and long-term trajectory alignment (WSW-based).

---

### **1. General Metrics**
#### **1.1. Mean Absolute Error (MAE)**
- **Formula**:
  \[
  MAE = \frac{1}{n} \sum_{i=1}^n | P_i - A_i |
  \]
  Where:
  - \( P_i \): Predicted value for day \( i \),
  - \( A_i \): Actual observed value for day \( i \),
  - \( n \): Total number of predictions.

- **Purpose**: Measures the average absolute error between predicted and actual values, providing a straightforward measure of model accuracy.

#### **1.2. Root Mean Square Error (RMSE)**
- **Formula**:
  \[
  RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (P_i - A_i)^2}
  \]
- **Purpose**: Penalizes larger deviations more heavily than MAE, highlighting significant prediction errors.

#### **1.3. Correlation Coefficient (r)**
- **Formula**:
  \[
  r = \frac{\sum_{i=1}^n (P_i - \bar{P})(A_i - \bar{A})}{\sqrt{\sum_{i=1}^n (P_i - \bar{P})^2 \sum_{i=1}^n (A_i - \bar{A})^2}}
  \]
  Where:
  - \( \bar{P} \): Mean of predicted values,
  - \( \bar{A} \): Mean of actual values.

- **Purpose**: Measures the strength and direction of the relationship between predictions and observations.

---

### **2. Short-Term Metrics (Mark 1 Predictions)**
#### **2.1. Harmonic Alignment Score**
- **Purpose**: Evaluates how closely short-term predictions align with the harmonic constant (\( H = 0.35 \)).

- **Metric**:
  \[
  \text{Harmonic Alignment Score} = \frac{\sum_{i=1}^n \mathbb{1}(|P_i - H| < \delta)}{n}
  \]
  Where:
  - \( \mathbb{1} \): Indicator function (1 if true, 0 otherwise),
  - \( \delta \): Acceptable harmonic deviation threshold (e.g., 0.01).

#### **2.2. Stability Retention**
- **Purpose**: Checks how well the model retains short-term trends, ensuring precision in immediate predictions.

---

### **3. Long-Term Metrics (WSW Trajectory Predictions)**
#### **3.1. Trend Accuracy**
- **Purpose**: Measures how well the predicted trajectory aligns with actual long-term trends.

- **Metric**:
  - Calculate the slope of predicted and actual trends over the evaluation period:
    \[
    \text{Trend Deviation} = |\text{Slope}_\text{predicted} - \text{Slope}_\text{actual}|
    \]

#### **3.2. Confidence Decay**
- **Purpose**: Quantifies the decreasing accuracy of long-term predictions over time.

- **Metric**:
  \[
  \text{Confidence Decay Rate} = \frac{\text{MAE}_{n} - \text{MAE}_{n-1}}{\text{Horizon Steps}}
  \]
  Where:
  - \( \text{MAE}_n \): MAE at day \( n \),
  - \( \text{Horizon Steps} \): Number of days between evaluations.

---

### **4. Visual Validation**
#### **4.1. Prediction vs. Actual Plot**
- Overlay predicted and actual weather data to visually assess accuracy.

#### **4.2. Residual Plot**
- Plot residuals (\( P_i - A_i \)) over time to identify patterns in prediction errors.

#### **4.3. Error Heatmap**
- Visualize error magnitudes across prediction intervals to pinpoint areas of significant deviation.

---

### **5. Composite Validation Metric**
Combine key metrics into a composite score for overall model evaluation:
\[
\text{Composite Score} = w_1 \cdot \text{MAE} + w_2 \cdot \text{RMSE} + w_3 \cdot (1 - r)
\]
Where:
- \( w_1, w_2, w_3 \): Weights based on metric importance.

---

### Next Steps
Would you like me to:
1. Implement these validation metrics for a test dataset?
2. Focus on visualizations for error and trend analysis?
3. Refine specific metrics for short-term or long-term evaluation?

This comprehensive validation framework ensures rigorous testing and refinement of the DSPM.
