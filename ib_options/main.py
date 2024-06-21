## Trading di Optioni | Interactive Brokers

""""
Opzioni - Contratti finanziari derivati che di danno il diritto, ma non l'obbligo, di acquistare (CALL) o di vendere (PUT) 
un sottostante (azione, indice, valuta, ecc) ad un prezzo specifico per un determinato periodo di tempo

Il bot è progettato per eseguire operazioni di trading automatizzate utilizzando la piattaforma Interactive Brokers (IB) 
e si concentra sul trading di opzioni legate all'ETF SPY (S&P 500)
"""

# Librerie
import pandas as pd
import numpy as np
from datetime import datetime
from ib_insync import *
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

"""
Lo strike di un'opzione, detto anche prezzo di esercizio, può essere uguale, maggiore o inferiore al prezzo del sottostante, 
a cui fa riferimento.

La scadenza indica la durata dell’opzione, quindi il suo periodo di validità, e può essere settimanale o mensile. 

Il premio è il valore dell’opzione, e può essere pagato, se si acquista un'opzione, o incassato, se si vende un'opzione.
"""

# Classe
class RiskyOptionsBot:
    """
    Risky Options Bot (Python, Interactive Brokers)

    Buy SPY Contracts on 3 consecutive 5-min higher closes and profit target on next bar
    """

    # Variabili Inizializzate
    def __init__(self, *args, **kwargs):
        print("Options Bor Running, connectin to IB ...")

        # Connessione a IB
        try:
            self.ib = IB()
            self.ib.connect('127.0.0.1',7496,clientId=1)
        except Exception as e:
            print(str(e))

        # Crea contratto SPY
        self.underlying = Stock('SPY','SMART','USD') #sottostante
        self.ib.qualifyContracts(self.underlying)

        print("Backfilling data to catchup ...")

        # Richiesta barre di streaming
        self.data = self.ib.reqHistoricalData(self.underlying,endDateTime='',durationStr='2 D',
                                              barSizeSetting='5 mins',whatToShow='TRADES',useRTH=True,keepUpToDate=True)
        # Variabili Locali
        self.in_trade = False
        
        # Ottieni le catene di opzioni correnti
        self.chains = self.bi.reqSecDefOptParams(self.underlying.symbol,'',self.underlying.secType,self.underlying.conId)

        # Update Chains every hour
        update_chain_scheduler = BackgroundScheduler(job_defaults={'max_istances': 2})
        update_chain_scheduler.add_job(func=self.update_options_chains,trigger='cron',hour='*')
        update_chain_scheduler.start()

        print("Running Live")

        # Imposta la funzione di callback per le barre in streaming
        self.data.updateEvent += self.on_bar_update
        self.bi.execDetailsEvent += self.exec_status

        # Run
        self.ib.run()

    # Aggiorna le catene di opzioni
        def update_options_chains(self):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                print("Updating options chains")
                self.chains = self.bi.reqSecDefOptParams(self.underlying.symbol,'',self.underlying.secType,self.underlying.conId)
            except Exception as e:
                print(str(e))

    # All'aggiornamento della barra,
    def on_bar_update(self, bars: BarDataList, has_new_bar: bool):
        try:
            if has_new_bar:
                # Converte BarDataList in dataframe pandas
                df = util.df(bars)
                # Verifica se siamo in un trade
                if not self.in_trade:
                    print("Last Close: " + str(df.close.iloc[-1]))
                    # Verifica per 3 chiusure consecutive più alte
                    if df.close.iloc[-1] > df.close.iloc[-2] and df.close.iloc[-2] > df.close.iloc[-3]:
                        # Trovate 3 chiusure consecutive più alte, acquista contratti call fuori dal denaro con uno strike 
                        # price più alto di 5 dollari
                        for optionschain in self.chains:
                            for strike in optionschain.strikes:
                                if strike > df.close.iloc[-1] + 5:
                                    print("Found 3 consecutive higher closers, entering trade.")
                                    self.optionscontract = Option(self.underlying.symbol,optionschain.expirations[1], strike, 'C','SMART',tradingClass=self.underlying.symbol)
                                    # Entriamo in trade, inviamo l'ordine
                                    options_order = MarketOrder('BUY',1,account=self.ib.wrapper.accounts[-1])
                                    trade = self.ib.placeOrder(self.options_contract, options_order)
                                    self.lastEstimatedFillPrice = df.close.iloc[-1]
                                    self.in_trade = not self.in_trade
                                    return # Importante per evitare un loop continuo
            else: # Siamo in un trade  
                if df.close.iloc[-1] > self.lastEstimatedFillPrice:
                    # Vendiamo per un profitto
                    options_order = MarketOrder('SELL',1,account=self.ib.wrapper.accounts[-1])
                    trade = self.ib.placeOrder(self.options_contract, options_order)   
        except Exception as e:
            print(str(e))
        
    # Stato di esecuzione
    def exec_statu(self, trade: True, fill: Fill):
        print("Filled")

# Istanziare la classe per far partire il tutto
RiskyOptionsBot()