import pandas as pd


data = {
    'Date': ['2023-01', '2023-01', '2023-02', '2023-02', '2023-01'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [250, 150, 300, 200, 100]
}


df = pd.DataFrame(data)
print(df)


pivot_table_df = df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc='sum', fill_value=0)
print("Pivot Table Result:")
print(pivot_table_df)


