# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###
* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

*In questo progetto estrarremo dei dati testuali da due fonti diverse: In primo luogo estrarremo degli articoli 
di giornale attraverso il web scraping sul sito 'The economist'; in secondo luogo estrarremo dei tweet delle 3 
persone più influenti nel panorama economico europeo attraverso una libreria già implementata in python chiamata 'Twint'.

*Procederemo con una sentiment analysis per quanto riguarda i tweet. L'output sarà un modello addestrato ad individuare 
la positività o la negatività di ogni nuovo tweet.

*Con gli articoli estratti elaboreremo un topic model: Il modello prenderà in input i nostri articoli e sarà capace 
di restituire in output in output non solo i topic (ossia di cosa gli articoli stanno parlando), ma anche per ogni nuovo 
articolo ci darà la probabilità che questo appartenga o meno ad uno dei topic individuati.
 
*L'output di questi due modelli sarà utilizzato come input per la creazione di un modello di regressione lineare: 
I due modelli saranno i predittori del modello e la variabile di risposta sarà il 'tasso overnight' della BCE.
 
*In conclusione, ci aspettiamo che l'analisi dei tweet e degli articoli vada realmente ad influenzare il tasso overnight
e predirne gli andamenti futuri con un'accuratezza dell'80% minimo.

*Questa è una linea giuda del nostro lavoro, ma potrebbe essere soggetta a cambiamenti durante il precorso.


### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact