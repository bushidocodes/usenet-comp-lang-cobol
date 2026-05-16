[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# the code

_3 messages · 2 participants · 2006-07_

---

### the code

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-21T14:06:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9qg0l$c72$1@s1.news.oleane.net>`

```
       INPUT-OUTPUT SECTION.
        FILE-CONTROL.
	    SELECT FGCTAR ASSIGN TO RANDOM "fgctar01"
               ORGANIZATION INDEXED
               ACCESS DYNAMIC
               RECORD KEY GCTAR-CLE
               STATUS ST-GCTAR.
	    SELECT FGCART ASSIGN TO RANDOM "fgcart01"
               ORGANIZATION IS INDEXED
               ACCESS IS DYNAMIC
               RECORD KEY IS GCART-CLE
               ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES
		FILE STATUS IS FichierStatus.
            SELECT OUTART ASSIGN TO RANDOM "out-ess.txt"
                ORGANIZATION IS LINE SEQUENTIAL.
        DATA DIVISION.
	FILE SECTION.
	    COPY "FGCART.CPY".
	    COPY "FGCTAR.CPY".
        FD OUTART LABEL RECORD STANDARD.
       	01 OUT-ART.
            02 OUT-CLE		PIC X(12).
	    02 SEPAR2    	    	PIC X(1).
       *     02 OUT-INTITULE         PIC X(30).
	    02 SEPAR3    	    	PIC X(1).
            02 OUT-PUHT      	PIC 9(6).9(2).
	    02 SEPAR4    	    	PIC X(1).
       *	    02 OUT-PUTTC     	PIC 9(6).9(2).
	    02 SEPAR5    	    	PIC X(1).
	    02 OUT-TAR.
	        04 OUT-CLEART	PIC X(12).
		 04 OUT-CLETAR	PIC 9(3).

	
        WORKING-STORAGE SECTION.	
	01 FichierStatus     	PIC X(2).
	01 ST-GCTAR   		PIC X(2).
	    88 RecordFound   	VALUE "00".
	01 cpt 			PIC 9(3) VALUE 000.
	01 tmp 			PIC 9(6).9(2).
	
	01 FLAGTROUVE 		PIC 9 VALUE 0.
	
	
	PROCEDURE DIVISION.
	TRAITEMENT SECTION.
	DEBUT.
            OPEN INPUT FGCART.
	    OPEN INPUT FGCTAR.
            OPEN OUTPUT OUTART.
	    	
            MOVE ";" TO SEPAR2 SEPAR3 SEPAR4 SEPAR5.
	
	    PERFORM UNTIL GCART-CLE = HIGH-VALUES
	    MOVE LOW-VALUES TO GCART-CLE
	    START FGCART
	        KEY IS GREATER THAN GCART-CLE
		 INVALID KEY MOVE HIGH-VALUES TO GCART-CLE
	    END-START
	    PERFORM UNTIL GCART-CLE = HIGH-VALUES
	    READ FGCART
	        NEXT RECORD
		 AT END MOVE HIGH-VALUES TO GCART-CLE
		 NOT AT END
       * Lecture du 2eme fichier
                    MOVE GCART-CLE TO GCTAR-ART
		     MOVE 000 TO GCTAR-TAR
		     MOVE 0 TO FLAGTROUVE
       * Balayage de toutes les valeurs possibles de GCTAR-TAR
                    PERFORM VARYING cpt FROM 1 BY 1 UNTIL cpt = 999
		     MOVE cpt TO GCTAR-TAR
		     READ FGCTAR
		         INVALID KEY CONTINUE
		     END-READ
		     IF GCTAR-CLE = "154         154"
		         DISPLAY ST-GCTAR
		     END-IF
		     IF RecordFound
		         MOVE 1 TO FLAGTROUVE
		         MOVE GCART-CLE TO OUT-CLE
		         MOVE GCTAR-CLE TO OUT-TAR
		         MOVE GCTAR-PUHT TO OUT-PUHT
			  WRITE OUT-ART
		     END-IF
		     END-PERFORM
       * Si on a pas trouvï¿½ d'enregistrement
                    IF FLAGTROUVE = 0
		         MOVE GCART-CLE TO OUT-CLE
		         MOVE GCTAR-CLE TO OUT-TAR
		         MOVE GCTAR-PUHT TO OUT-PUHT
			  WRITE OUT-ART
		     END-IF

       * Fin de traitement du 2eme fichier
	    END-READ
	    END-PERFORM
	    END-PERFORM

	
	    CLOSE FGCART.
	    CLOSE FGCTAR.
            CLOSE OUTART.
        FIN-TRAITEMENT SECTION.
	
	SORTIE SECTION.
	AFFICHAGE.
	    DISPLAY "Fin du traitement ", ST-GCTAR.
	FIN-SORTIE SECTION.
```

#### ↳ Re: the code

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-07-26T10:01:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153933308.519653.49710@s13g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e9qg0l$c72$1@s1.news.oleane.net>`
- **References:** `<e9qg0l$c72$1@s1.news.oleane.net>`

```
Dear Jerome:
It could be that the record that has 154 has a strange hex code
character such as tab or form feed that results in the record not being
found...

for example:

154   <formfeed> 154.

When you setup the key to read, the read fails because the target file
record happens to contain some strange character junk such as low
values...

Maybe you should try using a start and a read next instead of relying
on an exact key read....

Chris.
Jerome wrote:
> INPUT-OUTPUT SECTION.
>         FILE-CONTROL.
…[105 more quoted lines elided]…
> 	FIN-SORTIE SECTION.
```

##### ↳ ↳ Re: the code

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-27T15:53:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaaggj$u82$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153933308.519653.49710@s13g2000cwa.googlegroups.com>`
- **References:** `<e9qg0l$c72$1@s1.news.oleane.net> <1153933308.519653.49710@s13g2000cwa.googlegroups.com>`

```
hcmason@sbcglobal.net a ï¿½crit :
> Dear Jerome:
> It could be that the record that has 154 has a strange hex code
…[14 more quoted lines elided]…
> Chris.

Chris,

Thank you for this answer, as I wrote, a programmer show me another way 
to parse the file. However, I would remember your solution to analyse my 
first program.

Thank you

best regards

Jerome
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
