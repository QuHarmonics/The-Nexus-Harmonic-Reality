# Simulate energy flow in food chains using the Kulik Formula framework

# Generate test data for energy flow in food chains
food_chain_data = pd.DataFrame({
    "Scenario": [f"Food Chain Energy Flow {i+1}" for i in range(30)],  # 30 test scenarios
    "Producer Energy (J)": np.random.uniform(1000, 5000, 30),  # Energy produced by plants (producers)
    "Transfer Efficiency (%)": np.random.uniform(5, 20, 30),  # Energy transfer efficiency between trophic levels
    "Trophic Levels": np.random.randint(2, 5, 30),  # Number of trophic levels in the food chain
    "Environmental Stability (S)": np.random.uniform(0.5, 1.0, 30),  # Environmental stability factor
})

# Define a food chain energy flow model using the Kulik Formula framework
def food_chain_energy_model(producer_energy, transfer_efficiency, trophic_levels, environmental_stability):
    """
    Simulate energy flow in food chains.
    :param producer_energy: Energy produced by the primary producers (Joules)
    :param transfer_efficiency: Energy transfer efficiency between trophic levels (%)
    :param trophic_levels: Number of trophic levels in the food chain
    :param environmental_stability: Environmental stability factor
    :return: Energy available at the top trophic level
    """
    # Calculate the energy flow through trophic levels
    energy_flow = producer_energy * (transfer_efficiency / 100)**trophic_levels

    # Apply environmental stability as a scaling factor
    scaled_energy = energy_flow * environmental_stability

    # Apply consistency scaling using Kulik Formula principles
    consistency_factor = 1 / (1 + np.exp(-10 * (environmental_stability - 0.5)))
    adjusted_energy = scaled_energy * consistency_factor

    return adjusted_energy

# Apply the model to each scenario
food_chain_data["Predicted Top-Level Energy (J)"] = food_chain_data.apply(
    lambda row: food_chain_energy_model(
        row["Producer Energy (J)"], row["Transfer Efficiency (%)"], row["Trophic Levels"], row["Environmental Stability (S)"]
    ),
    axis=1
)

# Calculate a baseline energy flow for comparison
food_chain_data["Baseline Top-Level Energy (J)"] = food_chain_data.apply(
    lambda row: row["Producer Energy (J)"] * (row["Transfer Efficiency (%)"] / 100)**row["Trophic Levels"] * row["Environmental Stability (S)"],
    axis=1
)

# Calculate deviations
food_chain_data["Deviation (%)"] = (
    (food_chain_data["Predicted Top-Level Energy (J)"] - food_chain_data["Baseline Top-Level Energy (J)"]) / 
    food_chain_data["Baseline Top-Level Energy (J)"] * 100
)

# Display results for food chain energy flow testing
import ace_tools as tools; tools.display_dataframe_to_user(name="Food Chain Energy Flow Testing with Kulik Formula", dataframe=food_chain_data)

# Visualize deviations over scenarios
plt.figure(figsize=(14, 8))
plt.plot(food_chain_data["Scenario"], food_chain_data["Deviation (%)"], marker='o', linestyle='-', color="green")
plt.axhline(0, color="blue", linestyle="--", label="Perfect Consistency")
plt.axhline(5, color="red", linestyle="--", label="Positive Threshold")
plt.axhline(-5, color="orange", linestyle="--", label="Negative Threshold")
plt.xlabel("Food Chain Energy Flow Scenarios")
plt.ylabel("Deviation (%)")
plt.title("Food Chain Energy Flow Consistency Analysis using Kulik Formula")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
