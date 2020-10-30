Creare una coppia di applicativi Python in cui, attraverso un protocollo predefinito, il `client` possa inviare una serie di comandi al `server` e il `server`, dopo aver eseguito questi comandi restituisca al `client` il risultato di questi comandi.
I comandi che possono essere eseguiti dal `server` sono comandi standard POSIX (i.e. `ls`, `cat`, etc.), l'esecuzione deve avvenire direttamente mediante l'esecuzione di questi comandi utilzzando il modulo `subprocess`.
Il `client` dovrà inviare i comandi e tutti gli argomenti che servono per eseguire il comando, attraverso un socket TCP. Il `client` riceverà i comandi in una shell interattiva, ogni comando è una sequenza di comandi terminati da `\n`.
Mappa dei comandi: 
  - `list` -> `ls` (per questo comando è possibile indicare una specifica directory)
  - `concat` -> `cat` (per questo comando è possibile indicare tutti i file che si vogliono concatenare)
  - `print` -> `echo`
  - `help` -> il `sever` risponde al `client` con la lista dei comandi possibili
In caso di comando errato o di errore nell'esecuzione il server deve notificare il client del problema.
Passi:
 1. Creare un `echo server` che risponda a un messaggio del `client` con il messaggio stesso
 1. Modificare il `server` per eseguire il comando inviato dal `client` direttamente (il `client` invia `ls` -> il `server` esegue `ls`)
 1. Modificare il `server` per introdurre i comandi che possono essere gestiti, in caso di comando non presente il `server` deve inviare il comando di `help`, i comandi dovranno essere parsati dal `server` per capire qual è il comando giusto da eseguire, se nell'esecuzione del comando ci sono degli errori il `server` deve inviare al `client` il messaggio di errore.

