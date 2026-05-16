[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SUM clause in REPORT WRITER - Problems

_3 messages · 2 participants · 2004-12_

---

### SUM clause in REPORT WRITER - Problems

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-12-21T18:39:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NGneYC9flB@jpberlin-l.willms.jpberlin.de>`

```

Using Fujitsu's COBOL 3.0, I want to write a REPORT using REPORT  
WRITER. The compiler flags the SUM clauses in the CONTROL FOOTING  
FINAL, this way or that way.

Here is the relevant part of the program -- the data names are of  
course all in German -- parts of the WORKING-STORAGE SECTION and the  
full REPORT SECTION.



[code]
 WORKING-STORAGE SECTION.

 01  Je-Gespraech   .
     02 Merker  DISPLAY.
        03 Tarifklasse           PIC X.
           88 ist-Ortsgespraech      VALUE 'L'.
           88 ist-Ferngespraech      VALUE 'D'.
     02 Betraege    COMP.
        03 Tarif                 PIC 9V9(5) .
        03 Grundpreis            PIC 9(6)V99  .
        03 Basissteuer           PIC 9(6)V99  .
        03 Entfernungssteuer     PIC 9(6)V99  .
        03 Summe                 PIC 9(6)V99  .

 01  Kumuliert       COMP.
     02 Basissteuer           PIC 9(12)V99  .
     02 Entfernungssteuer     PIC 9(12)V99  .
     02 Summe                 PIC 9(12)V99  .




 REPORT SECTION.

 RD  Ausgabereport
        CONTROLS ARE FINAL
        .
 01  Einzige-Zeile   LINE PLUS 1 TYPE DETAIL
        .
     02 Dauer              PIC ZZZ.ZZ9   COLUMN  1
                        SOURCE Gespraechsdauer
                        .
     02 Tarifklasse     PIC X            COLUMN   9
                        SOURCE Tarifklasse OF Je-Gespraech
                        .
     02 Tarif              PIC 9,9999    COLUMN  10
                        SOURCE Tarif  OF Je-Gespraech
                        .
     02 Grundpreis         PIC ZZZ.ZZZ.ZZ9,99  COLUMN 18
                        SOURCE Grundpreis OF Je-Gespraech
                        .
     02 Basissteuer        PIC ZZZ.ZZZ.ZZ9,99  COLUMN 38
                        SOURCE Basissteuer OF Je-Gespraech
                        .
     02 Entfernungssteuer  PIC ZZZ.ZZZ.ZZ9,99  COLUMN 58 BLANK WHEN ZERO
                        SOURCE Entfernungssteuer OF Je-Gespraech
                        .
     02 Summe              PIC ZZZ.ZZZ.ZZ9,99  COLUMN 78
                        SOURCE Summe OF Je-Gespraech
                        .

 01  Summenzeile LINE PLUS 2 TYPE CONTROL FOOTING FINAL
     .
     02 Grundpreis-R       PIC ZZZ.ZZZ.ZZ9,99  COLUMN 18
                        SUM  Grundpreis OF Ausgabereport  RESET ON FINAL
                        .
     02 Basissteuer-R       PIC ZZZ.ZZZ.ZZ9,99  COLUMN 38
                        SUM    Basissteuer OF Ausgabereport RESET ON FINAL
                        .
     02 Entfernungssteuer-R  PIC ZZZ.ZZZ.ZZ9,99  COLUMN 58 BLANK WHEN ZERO
                        SUM    Entfernungssteuer OF Ausgabereport  RESET ON FINAL
                        .
     02 Summe-R              PIC ZZZ.ZZZ.ZZ9,99  COLUMN 78
                        SUM    Summe OF Ausgabereport  RESET ON FINAL
                        .

[/code]

The above, i.e. the SUM-clauses in "Summenzeile", are flagged by the  
Fujitsu-Compiler (Version 3.0) like this:

TelcoBM.COB 126: JMN2414I-S  IF 'UPON' IS NOT SPECIFIED IN SUM CLAUSE,  
  DATA-NAME 'GRUNDPREIS' IN REPORT SECTION MUST BE SUM COUNTER.
  DATA -NAME IGNORED.
TelcoBM.COB 129: JMN2414I-S  IF 'UPON' IS NOT SPECIFIED IN SUM CLAUSE,
  DATA-NAME 'BASISSTEUER' IN REPORT SECTION MUST BE SUM COUNTER.
  DATA-NAME IGNORED.
TelcoBM.COB 132: JMN2414I-S  IF 'UPON' IS NOT SPECIFIED IN SUM CLAUSE,
  DATA-NAME 'ENTFERNUNGSSTEUER' IN REPORT SECTION MUST BE SUM COUNTER.
  DATA-NAME IGNORED.
TelcoBM.COB 135: JMN2414I-S  IF 'UPON' IS NOT SPECIFIED IN SUM CLAUSE,
  DATA-NAME 'SUMME' IN REPORT SECTION MUST BE SUM COUNTER.
  DATA-NAME  IGNORED.


When I add "UPON Einzige-Zeile" it comes with another error message:

[code]
 01  Summenzeile LINE PLUS 2 TYPE CONTROL FOOTING FINAL
     .
     02 Grundpreis-R       PIC ZZZ.ZZZ.ZZ9,99  COLUMN 18
                        SUM  Grundpreis OF Ausgabereport UPON Einzige-Zeile RESET ON FINAL
                        .
     02 Basissteuer-R       PIC ZZZ.ZZZ.ZZ9,99  COLUMN 38
                        SUM    Basissteuer OF Ausgabereport UPON Einzige-Zeile RESET ON FINAL
                        .
     02 Entfernungssteuer-R  PIC ZZZ.ZZZ.ZZ9,99  COLUMN 58 BLANK WHEN ZERO
                        SUM    Entfernungssteuer OF Ausgabereport  UPON Einzige-Zeile  RESET ON FINAL
                        .
     02 Summe-R              PIC ZZZ.ZZZ.ZZ9,99  COLUMN 78
                        SUM    Summe OF Ausgabereport UPON Einzige-Zeile  RESET ON FINAL
                        .
[/code]


126: JMN2413I-S  IF 'UPON' IS SPECIFIED IN SUM CLAUSE,
   IDENTIFIER 'GRUNDPREIS' IN SUM CLAUSE MUST
   NOT BE DATA-NAME IN REPORT SECTION.   IDENTIFIER IGNORED.
129: JMN2413I-S  IF 'UPON' IS SPECIFIED IN SUM CLAUSE,
   IDENTIFIER 'BASISSTEUER' IN SUM CLAUSE MUST
   NOT BE DATA-NAME IN REPORT SECTION. IDENTIFIER IGNORED.
132: JMN2413I-S  IF 'UPON' IS SPECIFIED IN SUM CLAUSE,
   IDENTIFIER 'ENTFERNUNGSSTEUER' IN SUM CLAUSE MUST
   NOT BE DATA-NAME IN REPORT SECTION. IDENTIFIER IGNORED.
135: JMN2413I-S  IF 'UPON' IS SPECIFIED IN SUM CLAUSE,
   IDENTIFIER 'SUMME' IN SUM CLAUSE MUST
   NOT BE DATA-NAME IN REPORT SECTION. IDENTIFIER IGNORED.


   What's up? I think this is correct COBOL code. Isn't it?


MfG,
L. Willms

Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Das Buch, das in der Welt am ehesten verboten zu werden verdiente, wï¿½re ein Katalogus von verbotenen Bï¿½chern. -G.C.Lichtenberg
```

#### ↳ Re: SUM clause in REPORT WRITER - Problems

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-12-21T13:14:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqa3n3$2ffa$1@si05.rsvl.unisys.com>`
- **References:** `<9NGneYC9flB@jpberlin-l.willms.jpberlin.de>`

```
Can't speak to the Fujitsu implementation, but I run into problems with
Unisys MCPvm COBOL85 because the four source fields in Summenzeile aren't
sufficiently/correctly qualified using either of your two examples.   Our
compiler liked, for example, "Grundpreis-R ... SUM Grundpreis OF
Einzige-Zeile RESET ON FINAL."   I also ran into a problem because
"Gespraechsdauer" isn't declared anywhere, and added it to "Betraege".

Once I fixed those things up it compiled OK for me.  Didn't try running it,
though.

    -Chuck Stevens

 "Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9NGneYC9flB@jpberlin-l.willms.jpberlin.de...
>
> Using Fujitsu's COBOL 3.0, I want to write a REPORT using REPORT
…[70 more quoted lines elided]…
>                         SUM    Entfernungssteuer OF Ausgabereport  RESET
ON FINAL
>                         .
>      02 Summe-R              PIC ZZZ.ZZZ.ZZ9,99  COLUMN 78
…[28 more quoted lines elided]…
>                         SUM  Grundpreis OF Ausgabereport UPON
Einzige-Zeile RESET ON FINAL
>                         .
>      02 Basissteuer-R       PIC ZZZ.ZZZ.ZZ9,99  COLUMN 38
>                         SUM    Basissteuer OF Ausgabereport UPON
Einzige-Zeile RESET ON FINAL
>                         .
>      02 Entfernungssteuer-R  PIC ZZZ.ZZZ.ZZ9,99  COLUMN 58 BLANK WHEN ZERO
>                         SUM    Entfernungssteuer OF Ausgabereport  UPON
Einzige-Zeile  RESET ON FINAL
>                         .
>      02 Summe-R              PIC ZZZ.ZZZ.ZZ9,99  COLUMN 78
>                         SUM    Summe OF Ausgabereport UPON Einzige-Zeile
RESET ON FINAL
>                         .
> [/code]
…[25 more quoted lines elided]…
> Das Buch, das in der Welt am ehesten verboten zu werden verdiente, w�re
ein Katalogus von verbotenen B�chern. -G.C.Lichtenberg
```

##### ↳ ↳ Re: SUM clause in REPORT WRITER - Problems

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-12-21T22:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NKprxKuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<9NGneYC9flB@jpberlin-l.willms.jpberlin.de> <cqa3n3$2ffa$1@si05.rsvl.unisys.com>`

```
.     Am  21.12.04
 schrieb  charles.stevens@unisys.com (Chuck Stevens)
     bei  /COMP/LANG/COBOL
      in  cqa3n3$2ffa$1@si05.rsvl.unisys.com
   ueber  Re: SUM clause in REPORT WRITER - Problems


   Thank you very much for looking into my problem.

CS> Can't speak to the Fujitsu implementation, but I run into problems
CS> with Unisys MCPvm COBOL85 because the four source fields in
CS> Summenzeile aren't sufficiently/correctly qualified using either of
CS> your two examples.

CS> Our compiler liked, for example, "Grundpreis-R
CS> ... SUM Grundpreis OF Einzige-Zeile RESET ON FINAL."

   That was my original try (repeated after reading your message), but  
with the same result.

   Originally I also didn't have the "-R" suffixes on the CONTROL  
FOOTING; I had experimented with different forms of qualification.

   With these suffixes, the elements of the DETAIL group should be  
sufficiently qualified by the REPORT name, I thought.

   But NOW! finally! I have come to grips with the problem. I had a  
look again at the REPORT WRITER tutorial at
   http://www.csis.ul.ie/cobol/lectures/ReportWriterSSWeb.htm
   and found there, later confirmed by Syntax Rule for the SUM CLAUSE  
in COBOL-85 (Section 3.19 and 3.19.3 (1) on page XIII-52), as the  
Fujitsu compiler said again and again in its error messages: the SUM  
clause may not reference an item in the REPORT SECTION if that item  
does not itself have a SUM clause.  An item with only the SOURCE or  
VALUE clause is not allowed. The 2002 standard seems to have relaxed  
the rules. That's what Fujitsu's error message 2114 wanted to convey  
me. The other error message is prompted by the third paragraph of that  
rule (1): "If the UPON phrase is specified, any identifiers in the  
associated SUM clause must not be sum counters", and consequently be  
outside of the REPORT.

   So, by specifying the same items in "Betraege OF Je-Gespraech"  
which are referenced as SOURCE in the DETAIL line, as referenced by  
SUM in the CONTROL FOOTING, the compilation finally went thru without  
serious errors.


CS> I also ran into a problem because "Gespraechsdauer" isn't declared
CS> anywhere, and added it to "Betraege".

   That field was in the FILE SECTION. Thanks for adding it.


CS> Once I fixed those things up it compiled OK for me.  Didn't try
CS> running it, though.

   So the Fujitsu 3.0 seems to be more strict with the COBOL-85 rules  
than yours...



Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Die Arbeit in weiï¿½er Haut kann sich nicht dort emanzipieren, wo sie
in schwarzer Haut gebrandmarkt wird."     - Karl Marx     12.11.1866
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
