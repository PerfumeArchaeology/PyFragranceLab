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

This code is an example of numerical optimization using Python, specifically the minimize function from the scipy.optimize module. It finds the optimal weights for a given set of materials to match a target composition, minimizing the difference between predicted and target percentages.

Here's a brief breakdown of what the code does:

It defines a target composition (target_percentages) and the percentages of aroma chemicals in owned materials (owned_materials).
An objective function (objective) is defined, which calculates the squared difference between predicted and target percentages.
Initial weights for the materials are set (initial_weights).
The optimization algorithm (minimize) is used to find the weights that minimize the objective function.
The optimized weights are extracted and printed.
As for the title for a text file containing this code, you could choose something like "fragrance_optimization.py" to reflect the content of the code. This title indicates that the file contains Python code related to optimizing fragrance formulations.


