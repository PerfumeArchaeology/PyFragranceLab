import numpy as np
from scipy.optimize import minimize

# Sample data
target_percentages = np.array([10, 20, 30, 40])  
owned_materials = {'Material1': np.array([5, 15, 25, 35]), 'Material2': np.array([8, 18, 28, 38])}

# Objective function
def objective(weights):
    predicted_percentages = sum(weights[material] * material_percentages for material, material_percentages in owned_materials.items())
    return np.sum((predicted_percentages - target_percentages) ** 2)

# Initial guess for weights
initial_weights = {material: 0.5 for material in owned_materials}

# Optimization
result = minimize(objective, x0=[initial_weights[material] for material in owned_materials.values()])

# Extract optimized weights
optimized_weights = {material: result.x[i] for i, material in enumerate(owned_materials)}

# Output optimized weights
print("Optimized Weights:")
for material, weight in optimized_weights.items():
    print(f"{material}: {weight}")
