# Simulate energy flow in rainforest ecosystems using the Kulik Formula framework

# Generate test data for rainforest ecosystems
rainforest_ecosystem_data = pd.DataFrame({
    "Scenario": [f"Rainforest Ecosystem Energy Flow {i+1}" for i in range(30)],  # 30 test scenarios
    "Primary Producer Energy (J)": np.random.uniform(2000, 10000, 30),  # Energy produced by rainforest producers (plants)
    "Transfer Efficiency (%)": np.random.uniform(5, 15, 30),  # Energy transfer efficiency in rainforest food chains
    "Trophic Levels": np.random.randint(3, 6, 30),  # Number of trophic levels
    "Environmental Stability (S)": np.random.uniform(0.6, 1.0, 30),  # Stability of rainforest environment
})

# Define the rainforest ecosystem energy flow model
def rainforest_ecosystem_energy_model(producer_energy, transfer_efficiency, trophic_levels, environmental_stability):
    """
    Simulate energy flow in rainforest ecosystems.
    :param producer_energy: Energy produced by primary producers (Joules)
    :param transfer_efficiency: Energy transfer efficiency between trophic levels (%)
    :param trophic_levels: Number of trophic levels
    :param environmental_stability: Environmental stability factor
    :return: Energy available at the top trophic level
    """
    # Base energy flow through the rainforest ecosystem
    energy_flow = producer_energy * (transfer_efficiency / 100)**trophic_levels

    # Apply environmental stability scaling
    scaled_energy = energy_flow * environmental_stability

    # Apply consistency scaling using Kulik Formula principles
    consistency_factor = 1 / (1 + np.exp(-10 * (environmental_stability - 0.5)))
    adjusted_energy = scaled_energy * consistency_factor

    return adjusted_energy

# Apply the model to each scenario
rainforest_ecosystem_data["Predicted Top-Level Energy (J)"] = rainforest_ecosystem_data.apply(
    lambda row: rainforest_ecosystem_energy_model(
        row["Primary Producer Energy (J)"], row["Transfer Efficiency (%)"], row["Trophic Levels"], row["Environmental Stability (S)"]
    ),
    axis=1
)

# Calculate a baseline energy flow for comparison
rainforest_ecosystem_data["Baseline Top-Level Energy (J)"] = rainforest_ecosystem_data.apply(
    lambda row: row["Primary Producer Energy (J)"] * (row["Transfer Efficiency (%)"] / 100)**row["Trophic Levels"] * row["Environmental Stability (S)"],
    axis=1
)

# Calculate deviations
rainforest_ecosystem_data["Deviation (%)"] = (
    (rainforest_ecosystem_data["Predicted Top-Level Energy (J)"] - rainforest_ecosystem_data["Baseline Top-Level Energy (J)"]) / 
    rainforest_ecosystem_data["Baseline Top-Level Energy (J)"] * 100
)

# Display results for rainforest ecosystem energy flow testing
import ace_tools as tools; tools.display_dataframe_to_user(name="Rainforest Ecosystem Energy Flow Testing with Kulik Formula", dataframe=rainforest_ecosystem_data)

# Visualize deviations over scenarios
plt.figure(figsize=(14, 8))
plt.plot(rainforest_ecosystem_data["Scenario"], rainforest_ecosystem_data["Deviation (%)"], marker='o', linestyle='-', color="forestgreen")
plt.axhline(0, color="blue", linestyle="--", label="Perfect Consistency")
plt.axhline(5, color="red", linestyle="--", label="Positive Threshold")
plt.axhline(-5, color="orange", linestyle="--", label="Negative Threshold")
plt.xlabel("Rainforest Ecosystem Energy Flow Scenarios")
plt.ylabel("Deviation (%)")
plt.title("Rainforest Ecosystem Energy Flow Consistency Analysis using Kulik Formula")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
