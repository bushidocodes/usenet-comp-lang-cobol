[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CObOL-NEWBIE need HELP fast !!! Please! Please! Bitte! Thank you..

_1 message · 1 participant · 1998-05_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### CObOL-NEWBIE need HELP fast !!! Please! Please! Bitte! Thank you..

- **From:** "tob..." <ua-author-17084190@usenetarchives.gap>
- **Date:** 1998-05-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<354bd02f.12054194@news.main-rheiner.de>`

```

Hello, ya cobol-cracks!

I魹ｽve got a problem with the programming language cobol!

Need fast help for creating a testprogram to learn
more about the functions of cobol.. input, output,
saving in files.. I can魹ｽt get it work.. (ANSI-Cobol)

I魹ｽve tried it with perform魹ｽs to split the program
into smaller parts.. but it doesn魹ｽt work.. as it should.

How do I make inputs and outputs (database) ?

------------------------------------------------------
Program: Get all costs of the 4 items (bill of costs).

"Cost-Item-mark":
- carpark
- administration
- stockroom, depot
- purchase

save this in a sequencial file with these specifications:
01 Costsfile.
05 Cost-Item-mark PIC X(15).
05 Date.
07 Year PIC 9(2).
07 Month PIC 9(2).
07 Day PIC 9(2).
05 Costs PIC 9(5)V99.

Where do I have to write this ? In the FILE SECTION ?
or in the WORKING-STORAGE SECTION ? Or in both ?

==Choose one:=======================

1 - INPUT new database=COSTS..
2 - OUTPUT of all costs of one item..
0 - End of Program.

=====================================

In my program the perform does not work properly !?

1 - INPUT new database=COSTS..
Input of the data with a screen-mask (but ANSI-Cobol).
Input: Cost-Item-mark, Date, Costs

with fault-operation: Year : 00-99
Month: 01-12
Day : 01-31

In addition to that SELECT should be used with OPTIONAL and OPEN
with EXTEND.

-------------------------------------

2 - OUTPUT of all costs of one item..
Output of all costs of one of the 4 items:


- Input of the "Cost-Item-mark"
- Input period "from".. "up to".. date.

-> then Output of all costs of the selected "Cost-Item-mark"
- carpark OR
- administration OR
- stockroom(depot) OR
- purchase.

How do I make it ?
Should one search the database sequencially until the condition is
true ?

-------------------------------------
Please help a cobol-newbie!
Thank you very much!

Please email me to:
Tob··.@cry··n.com
-------------------------------------



------------------------------------------------------
Deutsche Version meiner Hilfe-Anfrage
------------------------------------------------------

Hallo, ihr COBOL-Asse!

Brauche dringend Hilfe bei der Erstellung eines
Testprogramms um die Funktionweise von Cobol zu
verstehen.. Ein-, Ausgaben, Speichern in Dateien.

Ich bekomm魹ｽ es nicht hin.. (ANSI-Cobol)

Habe versucht mit perform魹ｽs das Programm in Unter-
programme zu teilen.. jedoch funzt es nicht so wie
ich will.

Wie mu魹ｽ ich au魹ｽerdem die Datenein-, und -ausgabe
programmieren ?

Bin f魹ｽr jede Hilfe dankbar!!!!

Tobias


----------------------------------------
PROGRAMM: Erfassen der Kosten von 4 Kostenstellen:

- Fuhrpark
- Verwaltung
- Lager
- Einkauf

in einer sequentiellen Datei mit folgenden Angaben:
_________________________________________
| Kostendatei |
--------------------------------------------------------------------------------|
| Kostenstellen- |______Datum_______| Kosten |
| bezeichung | Jahr | Monat | Tag | |
--------------------------------------------------------------------------------
| 1 - 15 | 16 - 21 | 22 - 27 |
--------------------------------------------------------------------------------

dh.

01 Kostendatei.
05 KStBezeichnung PIC X(15).
05 Datum.
07 Jahr PIC 9(2).
07 Monat PIC 9(2).
07 Tag PIC 9(2).
05 Kosten PIC 9(5)V99.

Aber wo mu魹ｽ ich das hinschreiben ?
In die FILE SECTION ? oder in die WORKING-STORAGE SECTION ?
Oder beides ?


==AUSWAHLMEN魹ｽ:=======================

1 - EINGABE VON Datens魹ｽtzen=KOSTEN..
2 - AUSGABE VON Gesamtkosten..
0 - Ende des Programms.

=====================================

Mein Auswahl-Men魹ｽ funzt nicht..
Geht das mit den Perform nicht so ?
Andere L魹ｽsungen ?


1 - EINGABE VON Datens魹ｽtzen=KOSTEN..
Eingabe der Daten 魹ｽber eine Bildschirmmaske.
Mit Fehlerbehandlung: Jahr : 00-99
Monat: 01-12
Tag : 01-31

Die SELECT-Klausel mu魹ｽ mit OPTIONAL angegeben werden und OPEN
mit dem Zusatz EXTEND.

-------------------------------------

2 - AUSGABE VON Gesamtkosten..
Ausgabe der Gesamtkosten einer Kostenstelle:
- Eingabe der Kostenstelle
- Eingabe des Zeitraums: Von.. bis.. Datum.

-> dann Ausgabe der Gesamtkosten der Kostenstelle im Zeitraum.


Wie mu魹ｽ man das programmieren ?
Jeden Datensatz sequentiell abfragen, ob og. Zustand true ist ?

-------------------------------------
VIELEN VIELEN DANK!!

Bitte Hilfe mailen an:
Tob··.@cry··n.com
-------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
