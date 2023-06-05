import pandas as pd
from Ensembl_converter import EnsemblConverter

# Create an instance of the EnsemblConverter
converter = EnsemblConverter()

# Example gene list
genes = ['ENSG00000000457', 'ENSG00000273486', 'ENSG00000273493']

# Convert gene IDs to gene symbols
df = converter.convert_ids(genes)

# Print the resulting DataFrame
print(df)
