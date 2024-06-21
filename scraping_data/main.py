## Scraping Data

# Librerie
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# Parametri
data_odierna = datetime.now().strftime('%d%m%Y')

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
#print(soup)

soup.find('table')
soup.find_all('table')[1]
soup.find('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1]
#print(table)

world_titles = table.find_all('th')
#world_titles

world_table_titles = [title.text.strip() for title in world_titles]
#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

print(df)

# Salvataggio output
output_folder_path = './output/'

file_name = f'companies_{data_odierna}.csv'
output_file_path = output_folder_path + file_name

df.to_csv(output_file_path, index=False)
