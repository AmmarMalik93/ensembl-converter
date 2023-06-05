import argparse
from ensembl_converter import EnsemblConverter

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Ensembl ID Converter')
parser.add_argument('genes', metavar='gene', nargs='+',
                    help='Ensembl gene IDs')
parser.add_argument('--output', metavar='output_file',
                    help='Output file path')
parser.add_argument('--progress', action='store_true',
                    help='Display progress bar')
args = parser.parse_args()

# Initialize Ensembl Converter
converter = EnsemblConverter(use_progress_bar=args.progress)

# Convert Ensembl IDs to gene symbols
df = converter.convert_ids(args.genes)

# Print or save the result
if args.output:
    df.to_csv(args.output, index=False)
    print(f"Result saved to {args.output}")
else:
    print(df)
