import numpy as np
import pandas as pd
import requests
from tqdm import tqdm

class EnsemblConverter:
    def __init__(self, use_progress_bar=False):
        self.endpoint = 'https://rest.ensembl.org/lookup/id'
        self.headers = {"Content-Type": "application/json"}
        self.use_progress_bar = use_progress_bar

    def convert_ids(self, genes):
        gene_symbols = []

        if self.use_progress_bar:
            genes = tqdm(genes)

        for ensembl_id in genes:
            url = f"{self.endpoint}/{ensembl_id}"
            response = requests.get(url, headers=self.headers)
            if response.ok:
                data = response.json()
                gene_symbol = data.get('display_name', ensembl_id)
                gene_symbols.append(gene_symbol)
            else:
                gene_symbols.append(ensembl_id)

        df = pd.DataFrame({'ENSG': genes, 'Symbol': gene_symbols})
        return df
