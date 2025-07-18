# Simulate predator-prey interactions using the Kulik Formula framework

# Generate test data for predator-prey interactions
predator_prey_data = pd.DataFrame({
    "Scenario": [f"Predator-Prey Interaction {i+1}" for i in range(30)],  # 30 test scenarios
    "Prey Population (N)": np.random.uniform(50, 1000, 30),  # Number of prey
    "Predator Population (P)": np.random.uniform(5, 50, 30),  # Number of predators
    "Interaction Rate (R)": np.random.uniform(0.01, 0.2, 30),  # Rate of interaction between prey and predators
    "Environmental Stability (S)": np.random.uniform(0.5, 1.0, 30),  # Stability factor of the environment
})

# Define a predator-prey interaction model using the Kulik Formula framework
def predator_prey_model(prey_population, predator_population, interaction_rate, environmental_stability):
    """
    Simulate predator-prey interactions.
    :param prey_population: Number of prey
    :param predator_population: Number of predators
    :param interaction_rate: Rate of interaction between prey and predators
    :param environmental_stability: Environmental stability factor
    :return: Interaction health score
    """
    # Base interaction health score
    interaction_health = (prey_population * predator_population * interaction_rate) * environmental_stability

    # Apply consistency scaling using Kulik Formula principles
    consistency_factor = 1 / (1 + np.exp(-10 * (environmental_stability - 0.5)))
    adjusted_health = interaction_health * consistency_factor

    return adjusted_health

# Apply the model to each scenario
predator_prey_data["Predicted Health Score"] = predator_prey_data.apply(
    lambda row: predator_prey_model(
        row["Prey Population (N)"], row["Predator Population (P)"], row["Interaction Rate (R)"], row["Environmental Stability (S)"]
    ),
    axis=1
)

# Calculate a baseline health score for comparison
predator_prey_data["Baseline Health Score"] = predator_prey_data.apply(
    lambda row: (row["Prey Population (N)"] * row["Predator Population (P)"] * row["Interaction Rate (R)"] * row["Environmental Stability (S)"]),
    axis=1
)

# Calculate deviations
predator_prey_data["Deviation (%)"] = (
    (predator_prey_data["Predicted Health Score"] - predator_prey_data["Baseline Health Score"]) / 
    predator_prey_data["Baseline Health Score"] * 100
)

# Display results for predator-prey interaction testing
import ace_tools as tools; tools.display_dataframe_to_user(name="Predator-Prey Interaction Testing with Kulik Formula", dataframe=predator_prey_data)

# Visualize deviations over scenarios
plt.figure(figsize=(14, 8))
plt.plot(predator_prey_data["Scenario"], predator_prey_data["Deviation (%)"], marker='o', linestyle='-', color="orange")
plt.axhline(0, color="green", linestyle="--", label="Perfect Consistency")
plt.axhline(5, color="red", linestyle="--", label="Positive Threshold")
plt.axhline(-5, color="blue", linestyle="--", label="Negative Threshold")
plt.xlabel("Predator-Prey Interaction Scenarios")
plt.ylabel("Deviation (%)")
plt.title("Predator-Prey Interaction Consistency Analysis using Kulik Formula")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
