# Simulate energy flow in marine ecosystems using the Kulik Formula framework

# Generate test data for marine ecosystems
marine_ecosystem_data = pd.DataFrame({
    "Scenario": [f"Marine Ecosystem Energy Flow {i+1}" for i in range(30)],  # 30 test scenarios
    "Phytoplankton Energy (J)": np.random.uniform(1000, 10000, 30),  # Energy produced by phytoplankton
    "Transfer Efficiency (%)": np.random.uniform(5, 25, 30),  # Energy transfer efficiency in marine food chains
    "Trophic Levels": np.random.randint(3, 6, 30),  # Number of trophic levels
    "Environmental Stability (S)": np.random.uniform(0.4, 1.0, 30),  # Stability of marine environment
})

# Define the marine ecosystem energy flow model
def marine_ecosystem_energy_model(phytoplankton_energy, transfer_efficiency, trophic_levels, environmental_stability):
    """
    Simulate energy flow in marine ecosystems.
    :param phytoplankton_energy: Energy produced by phytoplankton (Joules)
    :param transfer_efficiency: Energy transfer efficiency between trophic levels (%)
    :param trophic_levels: Number of trophic levels
    :param environmental_stability: Environmental stability factor
    :return: Energy available at the top trophic level
    """
    # Base energy flow through the marine ecosystem
    energy_flow = phytoplankton_energy * (transfer_efficiency / 100)**trophic_levels

    # Apply environmental stability scaling
    scaled_energy = energy_flow * environmental_stability

    # Apply consistency scaling using Kulik Formula principles
    consistency_factor = 1 / (1 + np.exp(-10 * (environmental_stability - 0.5)))
    adjusted_energy = scaled_energy * consistency_factor

    return adjusted_energy

# Apply the model to each scenario
marine_ecosystem_data["Predicted Top-Level Energy (J)"] = marine_ecosystem_data.apply(
    lambda row: marine_ecosystem_energy_model(
        row["Phytoplankton Energy (J)"], row["Transfer Efficiency (%)"], row["Trophic Levels"], row["Environmental Stability (S)"]
    ),
    axis=1
)

# Calculate a baseline energy flow for comparison
marine_ecosystem_data["Baseline Top-Level Energy (J)"] = marine_ecosystem_data.apply(
    lambda row: row["Phytoplankton Energy (J)"] * (row["Transfer Efficiency (%)"] / 100)**row["Trophic Levels"] * row["Environmental Stability (S)"],
    axis=1
)

# Calculate deviations
marine_ecosystem_data["Deviation (%)"] = (
    (marine_ecosystem_data["Predicted Top-Level Energy (J)"] - marine_ecosystem_data["Baseline Top-Level Energy (J)"]) / 
    marine_ecosystem_data["Baseline Top-Level Energy (J)"] * 100
)

# Display results for marine ecosystem energy flow testing
import ace_tools as tools; tools.display_dataframe_to_user(name="Marine Ecosystem Energy Flow Testing with Kulik Formula", dataframe=marine_ecosystem_data)

# Visualize deviations over scenarios
plt.figure(figsize=(14, 8))
plt.plot(marine_ecosystem_data["Scenario"], marine_ecosystem_data["Deviation (%)"], marker='o', linestyle='-', color="blue")
plt.axhline(0, color="green", linestyle="--", label="Perfect Consistency")
plt.axhline(5, color="red", linestyle="--", label="Positive Threshold")
plt.axhline(-5, color="orange", linestyle="--", label="Negative Threshold")
plt.xlabel("Marine Ecosystem Energy Flow Scenarios")
plt.ylabel("Deviation (%)")
plt.title("Marine Ecosystem Energy Flow Consistency Analysis using Kulik Formula")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
