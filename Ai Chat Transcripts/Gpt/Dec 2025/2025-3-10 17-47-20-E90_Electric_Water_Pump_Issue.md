# E90 Electric Water Pump Issue

https://chat.openai.com/c/67cf5de7-6360-8011-bded-480e15471ade

## USER
so what woul cause the electric water pump to turn on at random when the key is on but engine not runnint e90 335xi

## ASSISTANT
The electric water pump on an E90 335xi can turn on at random with the key on but the engine off due to several potential reasons:

1. **Normal Operation & Self-Test**  
   - The water pump in the N54 engine operates on an electric control system and can run briefly as a self-test when the ignition is on.
   - It may also activate to cool down the turbochargers if they were recently used.

2. **Faulty Water Pump or Thermostat**  
   - A failing electric water pump can turn on and off unpredictably.
   - A malfunctioning thermostat can send incorrect signals to the pump, causing it to turn on unexpectedly.

3. **Residual Heat Mode (REST Feature)**  
   - If the REST function is active, it may trigger the water pump to circulate coolant.

4. **Faulty Temperature Sensor**  
   - If the coolant temperature sensor is sending incorrect readings, the DME (engine computer) may activate the pump unnecessarily.

5. **Wiring or Electrical Issues**  
   - Damaged wiring or a short circuit in the power supply to the pump could cause intermittent activation.
   - Corrosion in the connectors can also cause erratic behavior.

6. **Stored Fault Codes in the DME**  
   - Checking for stored fault codes using ISTA+ or INPA could reveal issues with the cooling system.

7. **Software or Coding Anomalies**  
   - If the car has been coded or reprogrammed recently, check if any cooling-related parameters have been modified.

### Recommended Diagnostic Steps:
- **Check for fault codes** with ISTA+, INPA, or a BMW-compatible scanner.
- **Monitor live data** to see if the pump is receiving abnormal activation signals.
- **Inspect wiring and connectors** for damage or corrosion.
- **Test the coolant temperature sensor** for proper function.
- **Consider replacing the pump** if it is showing signs of failure (e.g., running when it shouldn’t or not running when it should).

Let me know if you need help with specific diagnostic procedures!

## USER
with is REST

## ASSISTANT
REST (Residual Heat Function) is a feature in BMW vehicles, including the E90 3 Series, that allows the climate control system to utilize residual engine heat to warm the cabin when the engine is off. This function operates by circulating coolant through the heater core using the electric water pump and activating the blower fan at a low speed. The system remains active for a limited time (usually around 15 minutes) or until the battery voltage drops below a certain threshold.

### How REST Works:
1. **Activation:**  
   - The REST function can be activated by pressing the "REST" button on the climate control panel (available on models equipped with this feature).  
   - It functions only when the engine is off but the ignition is on (or in accessory mode).  

2. **Cooling System Involvement:**  
   - The electric water pump circulates warm coolant through the heater core.  
   - The blower fan distributes heat into the cabin.  
   - The system shuts off automatically after a preset time or when battery voltage is low.  

### Potential Connection to Random Water Pump Activation:
- If the water pump is turning on unexpectedly with the ignition on but the engine off, the REST function could be unintentionally active.
- Faulty climate control module settings or a malfunctioning temperature sensor could mistakenly trigger the pump.
- Checking the activation status of the REST function and verifying coding settings in the climate control module could help diagnose the issue.

Would you like guidance on checking and disabling REST if needed?

## USER
hmm not sure i have that Rest, i think mine says all.

## ASSISTANT
If your E90 climate control panel displays **"ALL"** instead of **"REST"**, your vehicle likely does not have the Residual Heat Function (REST). Instead, the **"ALL"** button is a feature that synchronizes the climate control settings between the driver and passenger sides. When activated, adjustments made to the temperature or airflow on the driver's side will be mirrored on the passenger side.  

### Confirming REST vs. ALL:  
1. **Check the Climate Control Panel:**  
   - If your vehicle has **"REST"**, pressing the button should activate the residual heat function when the engine is off.  
   - If your vehicle has **"ALL"**, pressing the button should synchronize climate settings between both zones.  

2. **Vehicle Model & Options:**  
   - The REST function was more common on earlier E90 models with specific climate control configurations.  
   - Vehicles with automatic dual-zone climate control often feature the **"ALL"** function instead.  

### Impact on Electric Water Pump:  
Since **REST is responsible for running the water pump when the engine is off**, not having this function means your issue is likely unrelated to residual heat operation. Instead, the random activation of the electric water pump when the ignition is on but the engine is off could be caused by:  
- **A failing water pump** that is intermittently turning on due to internal faults.  
- **A faulty coolant temperature sensor** providing incorrect signals to the DME (engine control unit).  
- **A software or coding issue** affecting the cooling system logic.  
- **An electrical short or faulty relay** sending unintended power to the pump.  

Would you like guidance on diagnosing this further using INPA or ISTA+?

## USER
hmm mayne temp sensor; the car was cold when this happen

## ASSISTANT
If the electric water pump is turning on while the engine is off and the car is cold, a **faulty coolant temperature sensor** is a strong possibility. The engine control unit (DME) uses data from the coolant temperature sensor to determine when the pump should activate. If the sensor is providing incorrect readings (such as falsely detecting high temperatures), the DME may engage the pump unnecessarily.  

### **Steps to Diagnose a Faulty Coolant Temperature Sensor:**  

1. **Check for Fault Codes**  
   - Use **INPA, ISTA+, or a BMW-compatible OBD-II scanner** to read stored fault codes in the **DME (ECU)** and **EKP (electric coolant pump module)**.  
   - Look for any codes related to **coolant temperature sensor faults**, such as:  
     - **2E81 / 2E82 / 2E83 / 2E84** (Water pump communication or speed issues)  
     - **2E85** (Water pump power issue)  
     - **2E8B** (Coolant temperature sensor error)  

2. **Monitor Live Data (Real-Time Coolant Temperature Readings)**  
   - Using **INPA or ISTA+**, check the **coolant temperature sensor values** when the engine is cold.  
   - The temperature should match **ambient air temperature** (e.g., if the outside temperature is 10°C, the coolant temperature should also be around 10°C).  
   - If the sensor reports an unusually high temperature (e.g., 70°C when the engine is cold), it is likely malfunctioning.  

3. **Physical Inspection of the Sensor & Wiring**  
   - The coolant temperature sensor is located near the **thermostat housing** on the **N54 engine**.  
   - Check for:  
     - **Loose or corroded connectors**  
     - **Damaged wiring**  
     - **Coolant leaks around the sensor**  

4. **Test the Sensor with a Multimeter (If Needed)**  
   - Unplug the sensor and measure resistance using a multimeter.  
   - Compare the resistance to BMW specifications for different temperatures (cold readings should be high resistance, while hot readings should be lower resistance).  

### **Possible Solutions:**  
- **If the sensor is faulty**, replace it with a new **OEM or high-quality aftermarket coolant temperature sensor**.  
- **If the wiring is damaged**, repair or replace the affected section.  
- **If fault codes indicate water pump issues**, further testing on the pump may be required.  

Would you like instructions on replacing the coolant temperature sensor if needed?

## USER
can having odb connected cuase that?

## ASSISTANT
Yes, having an **OBD-II scanner or diagnostic tool connected** can sometimes cause unexpected behaviors, including the electric water pump turning on. This happens due to the way BMW’s diagnostic and communication systems interact with the vehicle’s **CAN bus and DME (engine control unit)**.  

### **How an OBD-II Scanner Might Trigger the Water Pump:**  
1. **Wake-Up Signal to the CAN Bus:**  
   - Some OBD-II tools can send a **wake-up signal** to the vehicle’s electronic modules when connected, even if the ignition is off.  
   - This can cause the **DME to activate certain components**, including the **electric water pump**, for diagnostic purposes.  

2. **Polling or Interrogation of Modules:**  
   - If the OBD scanner continuously **queries data** from the DME, the system may assume the engine is in a pre-start state and activate the water pump momentarily.  
   - This is more common with **advanced BMW diagnostic tools** like **ISTA+, INPA, or Carly**, especially if real-time data logging is enabled.  

3. **Coding or Adaptation Changes:**  
   - If the OBD tool is used for **coding, adaptation resets, or live testing**, it can temporarily activate the water pump as part of the system check.  

4. **Faulty or Low-Quality OBD Adapter:**  
   - Some **cheap Bluetooth or Wi-Fi OBD adapters** do not properly go into sleep mode, keeping some modules awake and potentially triggering unintended behavior.  

### **How to Check If OBD Is the Cause:**  
- **Disconnect the OBD scanner**, turn the ignition off, and wait a few minutes.  
- **Reconnect the scanner** with the ignition **off** and observe if the pump starts again.  
- **Try a different OBD adapter** to rule out issues with a faulty device.  

### **Conclusion:**  
If the water pump turns on **only when an OBD tool is plugged in**, it is likely related to **OBD polling or wake-up signals** rather than a faulty sensor or pump. However, if the issue happens **without an OBD scanner connected**, then further diagnostics (such as checking the coolant temperature sensor or fault codes) would be necessary.  

Would you like recommendations on safe OBD adapters for BMW diagnostics?

