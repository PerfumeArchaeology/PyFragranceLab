# PyFragranceLab

The method developed by db.s on Basenotes is indeed an intriguing approach to formulating fragrances using GC/MS data and automated tools. This method offers a systematic way to analyze and replicate the aromatic profile of a target fragrance by leveraging the percentage compositions of aroma chemicals (AC) obtained from GC/MS results.

The process begins with three primary inputs:

A list of AC percentages from a target GC/MS.
A comprehensive table of AC percentages of all the materials owned by the perfumer.
The desired length of the formula.
Using this information, the program generates a formula that closely matches the target GC/MS profile. Additionally, it allows for the inclusion of weights on ACs, enabling the prioritization of certain materials based on their importance in the final fragrance blend.

The program employs a weighted squared error approach to measure the closeness of the match, ensuring an accurate representation of the target fragrance. It utilizes techniques from machine learning and statistics, such as simplex-constrained Lasso with weighted least squares, to identify the included materials and optimize the final formula.

To provide context and demonstrate the effectiveness of the method, examples are provided using popular fragrances like Sauvage by fragrance.drama. The "Percentage Match" metric is used to evaluate the similarity between the outputted formula and the target GC/MS, providing insights into the accuracy of the formulation process.

Overall, this method showcases the fusion of fragrance formulation with advanced computational techniques, offering perfumers a powerful tool to streamline the creation process and achieve precise scent profiles.


This Python code snippet is an example of using numerical optimization techniques to find the optimal weights of materials in fragrance formulation. Here's a breakdown of what each part of the code does:

Importing Libraries:

import numpy as np: Imports the NumPy library, which provides support for numerical operations and array manipulation in Python.
from scipy.optimize import minimize: Imports the minimize function from the scipy.optimize module, which is used for numerical optimization.
Sample Data:

target_percentages: Represents the target percentages of aroma chemicals in a fragrance.
owned_materials: Contains the percentages of aroma chemicals in the materials owned or available for use in fragrance formulation.
Objective Function:

objective(weights): Defines the objective function to minimize. It calculates the difference between the predicted percentages of aroma chemicals (based on the weights assigned to materials) and the target percentages, squared.
Initial Guess for Weights:

initial_weights: Provides an initial guess for the weights of materials. In this example, all materials are initialized with a weight of 0.5.
Optimization:

result = minimize(objective, x0=[initial_weights[material] for material in owned_materials.values()]): Uses the minimize function to find the weights that minimize the objective function. The initial guess for weights is provided as x0.
Extracting Optimized Weights:

optimized_weights: Extracts the optimized weights from the optimization result.
Output:

Prints the optimized weights for each material.
Overall, this code demonstrates a simplified approach to optimizing fragrance formulations based on target percentages of aroma chemicals and the composition of available materials. The optimization process aims to find the best combination of material weights that closely matches the target fragrance composition.
