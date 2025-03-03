# Fordypningsprosjekt datasett: Best Books Ever
## Bakgrunn for arbeidet
Jeg er over gjennomsnittet glad i å lese bøker, og synes også det er ganske gøy å se på hvordan statistikken ser ut for de bøkene jeg leser. Derfor har jeg valgt å bruke et datasett basert på goodreads-listen [**Best Books Ever**](https://www.goodreads.com/list/show/1.Best_Books_Ever). Kort fortalt er Goodreads et slags sosialt medium for bøker, hvor lesere blant annet kan dokumentere hva de leser, det de vil lese, diskutere bøker og skrive anmeldelser. Best Books Ever er den største listen av bøker på nettstedet, og er laget av at brukere på Goodreads har stemt på hvilke bøker de mener hører til i listen. Per 21. februar 2025 inneholder listen over 75 000 bøker. 

## Datasettet
Datasettet ble laget i 2020 for et universitetsprosjekt av Lorena Casanova Lozano og Sergio Costa Planells. På den tiden inneholdt listen ca. 52 000 bøker. I 2020 [stengte Goodreads API-et sitt](https://debugger.medium.com/goodreads-is-retiring-its-current-api-and-book-loving-developers-arent-happy-11ed764dd95), derfor har jeg ikke tilgang til data for bøker lagt til etter november 2020.

**Lenker:**
- [Datasett på GitHub](https://github.com/scostap/goodreads_bbe_dataset/blob/main/Best_Books_Ever_dataset/books_1.Best_Books_Ever.csv)
- [Datasett på Zenodo (en nettside for å dele forskning)](https://zenodo.org/records/4265096 )

Hvis du vil bruke datasettet anbefaler jeg å installere extensionen "Rainbow CSV" av mechatroner i VSCode for å lettere kunne få oversikt over hvilken kategori man ser på hvis man vil åpne filen. 

**Merk:** Enkelte verdier i datasettet inneholder linjeskift, som Rainbow CSV ikke helt forstår. De ser derfor ut som nye bøker i datasettet. Det er bare å ignorere dette, da det fungerer slik det skal når dataen leses inn med både pandas- og csv-modulene. 


## Hva jeg vil finne ut av
Det er for mye interessant til å finne ut av alt, derfor har jeg valgt ut noen idéer:

**Implementerte idéer:**

|   Idé	|   Python	|   Pandas	|
|---	|---	|---	|
|   Gjennomsnittlig sidetall	|   X	|   X	|
|   Stolpediagram sidetall	|   X	|   X	|
|   Forhold numratings + rating	|   X	|   X	|
|   Forekomst av sjangre	|   X	|   X	|
|   Største språk (uten engelsk)	|   X	|   X	|
|   	|   	|   	|


## For å kjøre koden:
**.py fil:**
- Krav: 
  - matplotlib-biblioteket
  - terminalen *må* ha utf-8 encoding, da det er enkelte navn på språk og bøker som ikke støttes ellers (planen er å legge dette inn i koden senere)

- Anbefalinger: -

**.ipynb fil:**
- Krav: 
  - matplotlib- og pandas-bibliotekene

- Anbefalinger: - 

# Tanker og ting:
## "Manuell" vs Pandas
For arbeid med datasett er Pandas den soleklare vinneren. Tankegangen og fremgangsmåten er stort sett det samme, men Pandas har allerede innebygd funksjonene jeg ellers ville skrevet manuelt. 

**Noen tanker:**

Jeg synes også Pandas sine "bins" gjorde ting mye lettere, samme med funksjonen for å ta gjennomsnitt av en kolonne. 

For kakediagrammet med språk brukte jeg med manuell løsning 25 linjer, mens Pandas bare trengte 9. Dessuten var det mye enklere å telle og sortere med Pandas. 

Ekstrapoeng til Pandas: Jeg måtte ikke gå inn for å fjerne "tomme" språk selv, da dette skjer av seg selv

## Videre utvikling
Jeg synes det var mye interessant data i datasettet, og jeg måtte begrense meg litt for å velge ut hva jeg ville vise fram. Hvis jeg jobber med datasettet videre, er dette blant tingene jeg tenker kunne vært gøy å se på:

- Boktitler - er det noen ord eller strukturer som går igjen?
- Forhold mellom språk og rating - er noen språk mer tilgivende?
- Hvordan har ting utviklet seg over tid? (utgivelsesår, ratings, sidetall)
- Bokomslag - det er linket til bokomslag i datasettet, med 99% completeness i følge [kilderepoet](https://github.com/scostap/goodreads_bbe_dataset/blob/main/README.md). Det kunne vært interessant å analysere disse; man kan se på farger eller lage en AI modell som kan forutsi sjanger basert på omslaget