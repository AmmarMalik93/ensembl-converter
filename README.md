# **Ensembl_converter**

The **`Ensembl_converter`** package is a Python library that allows you to convert Ensembl IDs to gene symbols. It provides a simple and convenient way to retrieve gene symbols for a given list of Ensembl IDs using the Ensembl REST API.

## **Installation**

You can install **`Ensembl_converter`** using pip:

```shell
pip install Ensembl_converter
```

## **Usage**
To convert Ensembl IDs to gene symbols, follow these steps:

1. Import the **`EnsemblConverter`** class from the Ensembl_converter package.
2. Create an instance of **`EnsemblConverter`**
3. Call the **`convert_ids`** method with a list of Ensembl IDs as input.

Here's an example:

```python
from Ensembl_converter import EnsemblConverter

# Create an instance of EnsemblConverter
converter = EnsemblConverter()

# Provide a list of Ensembl IDs
ensembl_ids = ['ENSG00000000457', 'ENSG00000273486', 'ENSG00000273493']

# Convert Ensembl IDs to gene symbols
result = converter.convert_ids(ensembl_ids)

# Print the resulting DataFrame
print(result)
```

This will output a DataFrame with two columns: ENSG (Ensembl IDs) and Symbol (gene symbols).

## **Options**
The **`EnsemblConverter`** class supports the following options:

* **`use_progressbar`** (default=False): Set this to **`True`** to display a progress bar during the conversion process. This can be useful for larger gene lists.

## **Dependencies**
The Ensembl_converter package depends on the following libraries:

* requests
* pandas
* tqdm

These dependencies will be automatically installed when you install the **`Ensembl_converter`** package (If you don't already have these installed).

## **Contributing**
Contributions to **`Ensembl_converter`** are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## **License**
This project is licensed under the MIT License. See the [**LICENSE**](/LICENSE) file for details.

