# Trading di Opzioni con Interactive Brokers
Questo progetto presenta un bot di trading di opzioni progettato per eseguire operazioni automatizzate sulla piattaforma Interactive Brokers (IB). L'obiettivo principale del bot è il trading di opzioni legate all'ETF SPY (S&P 500).

## Definizione di Opzioni
Le opzioni sono strumenti finanziari il cui valore non è autonomo ma deriva dal prezzo di una attività sottostante di varia natura (reale come nel caso di materie prime quali grano, oro, petrolio, ecc. , oppure finanziaria come nel caso di azioni, obbligazioni, tassi di cambio, indici, ecc.). Il termine “derivato” indica questa dipendenza.

Possiamo quindi definire le opzioni come dei contratti finanziari che danno il diritto, ma non l’obbligo, all’acquirente dietro il pagamento di un prezzo (Premio), di esercitare o meno la facoltà di acquistare (CALL) o vendere (PUT) una data quantità di una determinata attività finanziaria, detta sottostante, a una determinata data di scadenza o entro tale data e a un determinato prezzo di esercizio (Strike Price).

## Tipologia di Opzioni: Call e Put
Un'**opzione call** è uno strumento derivato che garantisce all'acquirente il diritto, ma non l'obbligo, di acquistare un titolo (detto sottostante) a scadenza (o entro la scadenza) a un dato prezzo (strike).

Nel caso di esercizio di opzioni su indici non è possibile ricevere il sottostante bensì solo il corrispettivo in denaro.

Ovviamente l’esercizio avrà senso (escludendo il costo pagato per acquistare l’opzione, il cosiddetto “premio”) solo se il prezzo del sottostante sarà superiore allo strike ed il profitto realizzato sarà pari alla differenza tra il prezzo di mercato e lo strike.

Un'**opzione put** è uno strumento derivato che garantisce al possessore il diritto di vendere a scadenza il sottostante ad un prezzo prefissato. In questo caso l’esercizio avrà senso (sempre escludendo il costo pagato per acquistare l’opzione, il cosiddetto “premio”) solo se il prezzo del sottostante sarà inferiore allo strike; il profitto realizzato ammonterà alla differenza tra lo strike e il prezzo di mercato.

Il bot si concentra su opzioni legate all'ETF SPY.

## Funzionalità Principali
- **Connessione a Interactive Brokers:** Il bot si connette a Interactive Brokers per l'esecuzione delle operazioni di trading.
- **Backfilling dei Dati:** Inizialmente, il bot recupera i dati storici necessari per l'analisi.
- **Aggiornamento Catene di Opzioni:** Le catene di opzioni vengono aggiornate regolarmente per mantenere informazioni aggiornate sulle opzioni disponibili.
- **Strategia di Trading:** Il bot implementa una strategia basata su 3 chiusure consecutive più alte in un intervallo di 5 minuti, decidendo di acquistare contratti CALL fuori dal denaro con uno strike price più alto di $5.
- **Gestione del Trade:** Una volta iniziato un trade, il bot monitora le chiusure successive per decidere se vendere per ottenere un profitto.
