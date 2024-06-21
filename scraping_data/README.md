# Scraping Dati da Wikipedia

## Descrizione
Questo script Python è progettato per effettuare lo scraping dei dati delle più grandi aziende degli Stati Uniti in base al loro fatturato da una pagina Wikipedia. Il codice utilizza BeautifulSoup per analizzare la struttura HTML della pagina web e pandas per organizzare i dati raccolti in un DataFrame.

## Utilizzo

### Librerie Necessarie
- pandas
- datetime
- bs4 (BeautifulSoup)
- requests

### Parametri
- `data_odierna`: La data odierna nel formato 'ddmmyyyy'.
- `url`: L'URL della pagina Wikipedia contenente i dati delle aziende.
- `output_folder_path`: La directory di output in cui verrà salvato il file CSV risultante.

### Esecuzione
1. Assicurarsi di avere tutte le librerie necessarie installate tramite `pip install -r requirements.txt`.
2. Eseguire lo script `scraping_data.py`.

### Output
Il risultato dello scraping verrà salvato come file CSV nella directory specificata con il nome seguente: `companies_{data_odierna}.csv`.

## Attenzione
Lo scraping di dati da pagine web può essere soggetto a limitazioni imposte dal sito web e alle sue politiche. È responsabilità dell'utente utilizzare questo script in conformità con le regole e i regolamenti del sito web target.
