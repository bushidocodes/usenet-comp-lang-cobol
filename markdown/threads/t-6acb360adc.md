[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problemen met indexed bestand en lezen ervan.

_1 message · 1 participant · 2004-02_

---

### Problemen met indexed bestand en lezen ervan.

- **From:** peeters.charly@skynet.be (Charly)
- **Date:** 2004-02-03T08:33:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1495a4e4.0402030833.7e68d391@posting.google.com>`

```
Ik ben een programma aan het schrijven die een vragen spel is, de
eerste vraag heeft een index 0001 ik geef deze in, de vraag wordt
gesteld bij een goed antw zal de tweede vraag moeten gestled worden,
maar ik zie dat zelf als ik manueel de nieuwe index dus 0002 ingeef
nog steeds vraag 0001 wordt gesteld.

Ik heb de fout al gezocht maar vind deze niet, een automatisch systeem
dat ik hed ingesteld verhoogde een teller met een en zette dit met
move in de index. Dit werkte maar hetzelfde probleem met dat manueel
invoeren.

Ik post hier dan bij mijn code, mischien vindt er een van julie de weg
om zo naar vraag twee te gaan enz.

ps: Kennen julie geen versie van cobol dat op windows draait? Fujitsu
cobol doet vervend en ik werk daar niet graag mee. Nu gebruik ik CB
een compiler maar ik em daar geen info van alleen dat dat snel vast
looopt.

Bedankt, Charly

000005 IDENTIFICATION DIVISION.
000010  PROGRAM-ID. VRAAG-SPEL.
000011
000012  AUTHOR. Charly, Peeters.
000013  DATE-WRITTEN. 02-02-2004.
000015 ENVIRONMENT DIVISION.
000016* CONFIGURATION SECTION.
000019  INPUT-OUTPUT SECTION.
000020  FILE-CONTROL.
000021   SELECT VRAGEN-BEST ASSIGN TO "A:VRAGEN.DAT"
000022    ORGANIZATION IS INDEXED
000023     ACCESS MODE IS DYNAMIC
000024      RECORD KEY IS VRAAG-ID.
000025 DATA DIVISION.
000026  FILE SECTION.
000027  FD VRAGEN-BEST.
000028	01 VRAAG-RECORD.
000029   02 VRAAG-ID        picture XXXX.
000030   02 VRAAG PIC X(70).
000031      
000032   02 ANTWOORD.
000033      03 A PIC X(20).
000034      03 B PIC X(20).
000035      03 C PIC X(20).
000036      03 D PIC X(20).
000037   02 JUIST-ANTW PIC A.
000038             
000100  WORKING-STORAGE SECTION.
000101    01 TELLER PIC 9999 VALUE 0001.
000102    01 KEUZE PIC A.
000103    01 BUFFER PIC 9 VALUE 0. 
000200		01 DUMMY PIC X.
000201
000300* LINKAGE SECTION.
000400 PROCEDURE  DIVISION.
000500* DECLARATIVES.
000600* END DECLARATIVES.
000601
000700  MAIN.
000701        
000702  OPEN INPUT VRAGEN-BEST.
000703  DISPLAY "Hier komen de vragen aan."
000704   MOVE TELLER TO VRAAG-ID.  
000705   PERFORM READ-VRAGEN UNTIL BUFFER=1.
        
000708  CLOSE VRAGEN-BEST.
000709  
        READ-VRAGEN.
          
          DISPLAY VRAAG-ID "geef deze in:".
          ACCEPT VRAAG-ID.
         READ VRAGEN-BEST
          INVALID KEY DISPLAY "ERROR"
000706    NOT INVALID KEY PERFORM VRAGEN-PERFORM
000707   END-READ.
        ADD 1 TO BUFFER.

        END-READ-VRAGEN.
000710
000711 
000712
000817
000900 VRAGEN-PERFORM.

000000  DISPLAY "Vraag"VRAAG-ID.
000901  DISPLAY SPACE.
        DISPLAY VRAAG.
000902  DISPLAY "A. " A "B. " B "C. " C "D. " D.
000903  DISPLAY "Keuze:".
000904  ACCEPT KEUZE.
000905  IF KEUZE = JUIST-ANTW 
000906   THEN DISPLAY "Juist" 
000000         ADD 1 TO TELLER
000000          
000907   ELSE DISPLAY "Fout"
000908  END-IF.

000909 END-VRAGEN-PERFORM.
 
000909* VRAAG-LUS.
000   *  IF BUFFER >= 1
      *  THEN PERFORM VRAGEN-PERFORM
      *  END-IF.
000910  EINDE.
001000   DISPLAY "Druk op een toest om af te sluiten."
001001      	ACCEPT DUMMY.
001002     STOP RUN.
001003
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
