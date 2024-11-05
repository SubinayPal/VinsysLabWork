# Purpose: Store and manipulate the sequence of human preproinsulin

# Store the human preproinsulin sequence in a variable called preproInsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"  # Leader sequence of insulin
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  # B chain of insulin
aInsulin = "giveqcctsicslyqlenycn"  # A chain of insulin
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # C-peptide of insulin

# Combine the B and A chains to get the final insulin sequence
insulin = bInsulin + aInsulin


# Printing the sequences of human insulin to the console
print("The sequence of human preproinsulin:")
print(preproInsulin)
# print("The sequence of human insulin, chain a: " + aInsulin)
print("The sequence of human insulin, chain a:", aInsulin)
print("Combined sequence of insulin (B chain + A chain):", insulin)


# Calculating the molecular weight of insulin
# Creating a dictionary of amino acid weights
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Counting the number of each amino acid in the insulin sequence
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

# Calculating the molecular weight of insulin
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights)

# Calculating the molecular weight of insulin
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights)

print("The rough molecular weight of insulin:", molecularWeightInsulin)


molecularWeightInsulinActual = 5807.63
# Calculating the error percentage
errorPercentage = abs(molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual * 100
print("Error percentage:", errorPercentage)
