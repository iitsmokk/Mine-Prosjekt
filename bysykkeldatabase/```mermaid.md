```mermaid
erDiagram
```
    Entiteter:
        sykler
        kunder
        sykkel_stasjoner
        utleie
```
    Attributer:
        sykkel_id(INTEGER)
        stasjon_id(INTEGER)
        låst(BOOLEAN)
        utlevert(BOOLEAN)
        stasjon_posisjon(TEXT)
        antall_sykler(INTEGER)
        tlf_nr(INTEGER)
        e-post(TEXT)
        fornavn(CHAR)
        etternavn(CHAR)
        leiebeløp(INTEGER)
        ordre_nr(INTEGER)
```
    sykler:
        sykkel_id(PK)
        stasjon_id(FK)
        låst
        utlevert
```
    kunder:
        tlf_nr(PK)
        e-post(PK)
        fornavn
        etternavn
```
    sykkel_stasjoner:
        stasjon_id(PK)
        sykkel_id(FK)
        antall_sykler
        posisjon
```
    

    


