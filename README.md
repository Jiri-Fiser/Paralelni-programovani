# Paralelní programování

## Paralelní hardware
Flynnova taxonomie (a další členění)
* SIMD (CPU SIMD extensions, GPU)
* MIMD
  * volně vázané systémy (bez sdílené paměti)
  * těsně vázané systémy (se sdílenou pamětí a sběrnicí)
    * SMTP systémy
    
## význam mezipaměti pro paralelní systémy

## účinnost paralelního programování
* Amdahlovo pravidlo
* Gustafsonovo pravidlo

##  úlohově orientované programování
* souběžné programování
* úlohy a jejich mapování na hardwarová vlákna
* STMD versus MTMD (úlohově vers. datově orientovaný paralelismus)

stručné shrnutí v presentaci
detailnější informace v opoře

## paralelní programování v Pythonu a C
### knihovna multiprocessing
* vysokoúrovňové rozhraní (pool.map apod.)
* využití komunikačních front
* distribuované zpracování v adhoc clusteru

### knihovna MPI
* odbočka: knihovna Numba
* MPI nad pythonskými objekty
* MPI nad numpy poli
* MPI v jazyce C

### paralelní for
* v Numbě
* v Cythonu
* v C (OpenMP)

### vektorizace
* v C (knihovna VLC)

viz opora a projekt PAR2023

### vysokoúrovňová paralelizace
???
