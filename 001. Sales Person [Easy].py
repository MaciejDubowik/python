import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    orders_company = pd.merge(company[['com_id', 'name']], orders[['com_id', 'sales_id']], on=['com_id'], how='inner')
    persons_orders = pd.merge(sales_person[['sales_id', 'name']], orders_company, on=['sales_id'], how='left')
    persons_red = persons_orders.where(persons_orders['name_y'] == 'RED').dropna()
    persons_red = persons_red['name_x'].drop_duplicates().to_frame()

    result = pd.merge(sales_person, persons_red, left_on='name', right_on='name_x', how='outer', indicator=True).query('_merge=="left_only"')

    return result['name'].to_frame()