# Last updated: 16.06.2025, 19:57:16
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products[mask][['product_id']]
