# Implementazione Blockchain Google Cloud Platform

## Introduzione
La PoC che è stata creata per testare la Blockchain in Google Cloud Platform, 
consiste in una transazione tra un Ente A ed un Ente B.
Tale transazione va a creare un blocco e successivamente viene inserito all'interno 
della Blockchain in maniera sequenziale, andando a creare una vera e propria catena.

## Spiegazione codice
### Avvio dell'applicazione
L'applicazione inizia controllando se esiste già un file contenente una blockchain salvata. 
Se il file è presente, viene eliminato per avviare una nuova sessione. 
Successivamente, viene effettuato il download della blockchain da un Gcloud Bucket, e se esiste 
una blockchain salvata, viene caricata.
Se non è presente una blockchain salvata, viene creata una blockchain iniziale (genesis block) 
contenente una transazione di avvio. Questa nuova blockchain viene poi salvata e successivamente 
caricata.

### Interazione con l'utente
L'utente viene presentato con un menu di opzioni. Può scegliere tra visualizzare la blockchain 
esistente o inserire una nuova transazione. Se sceglie di visualizzare la blockchain, 
vengono mostrate tutte le transazioni contenute nei blocchi.

### Inserimento di Nuove Transazioni
Se l'utente sceglie di inserire una nuova transazione, entra in un ciclo che consente di inserire 
mittente, destinatario e importo per una nuova transazione. Ogni transazione viene aggiunta 
alla blockchain.

### Conclusioni e Salvataggio
Dopo l'inserimento delle transazioni, l'utente può scegliere se inserirne altre o uscire 
dall'applicazione. Nel caso in cui si scelga di uscire, il file contenente la blockchain 
viene caricato nuovamente e successivamente eliminato. Questo processo garantisce che la 
blockchain rimanga salvata tra le esecuzioni dell'applicazione.

### Note sulla Blockchain e Hash dei Blocchi
L'hash di un blocco rappresenta criptograficamente il contenuto del blocco, garantendo l'integrità 
e l'immutabilità dei dati. 
Un hash di blocco è composto dai seguenti elementi:
- Indice del blocco (index): un numero intero che rappresenta la posizione del blocco nella blockchain.
- Hash del blocco precedente (prev_hash): l'hash del blocco precedente nella blockchain, che crea un legame tra i blocchi e garantisce l'integrità della catena.
- Timestamp (timestamp): il timestamp di quando è stato creato il blocco.
- Dati del blocco (data): il contenuto del blocco, che può includere transazioni, informazioni del contratto o qualsiasi altro dato.
- Nonce (nonce): un numero intero arbitrario che viene utilizzato nell'algoritmo di 
- Proof of Work (PoW) per trovare un hash che soddisfi un determinato requisito di difficoltà.

L'hash di un blocco è una stringa alfanumerica di lunghezza fissa (64 caratteri per l'hash SHA-256) 
che sembra casuale. Tuttavia, ogni modifica, anche minima, ai dati del blocco genera un hash 
completamente diverso.
