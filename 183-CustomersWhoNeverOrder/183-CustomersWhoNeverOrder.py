# Last updated: 16.06.2025, 19:57:00
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    all_data = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')
    
    no_orders = all_data[all_data['customerId'].isna()]
    return no_orders[['name']].rename(columns={'name': 'Customers'})
