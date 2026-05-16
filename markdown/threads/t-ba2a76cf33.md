[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# To Dashwood

_2 messages · 2 participants · 2009-02_

---

### To Dashwood

- **From:** J Weirich <weirich_j@hotmail.com>
- **Date:** 2009-02-24T07:39:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36555d9e-c268-44a7-83ec-f15d9c98fcb7@v13g2000yqm.googlegroups.com>`

```
Howdy, and thanks for the freeware.

Found this:

       01  SALES-ID-RECORD.
           02  SIE-MSTR-DATA.
             05  SIE-BANK-CD           PIC 9(7).
             05  SIE-BANK-LID          PIC 9(7).
             05  SIE-PORTFOLIO-NBR     PIC 9(7).
             05  SIE-ACCT-STATUS       PIC 9.
             05  SIE-FILLER1           PIC X.
             05  SIE-INT-TYPE          PIC X.
             05  SIE-KEY.
                 10  SIE-KEY-FILE-NBR  PIC 999-.
                 10  SIE-KEY-SSN       PIC 9(9).
                 10  SIE-KEY-GUAR      PIC XX.
                 10  SIE-KEY-SEQ       PIC 99.
                 10  SIE-KEY-LOAN-NO   PIC 99.
             05  SIE-NAME.
                 10  SIE-LNAM         PIC X(20).
                 10  SIE-FNAM          PIC X(11).
                 10  SIE-MID           PIC X.
             05  SIE-ACTY-CD           PIC 99.
             05  SIE-PROJECTED-BAL     PIC 9(9).99-.

Yeilds:

    cobdata.COBOLEngine.Version 2.0.0.07
    Lvl Name                            Pos Len Typ Oc
   1 01 SALES-ID-RECORD                   1  86
   2 02 SIE-MSTR-DATA                     1  86
   3 05 SIE-BANK-CD                       1   7
   4 05 SIE-BANK-LID                      8   7
   5 05 SIE-PORTFOLIO-NBR                15   7
   6 05 SIE-ACCT-STATUS                  22   1
   7 05 SIE-FILLER1                      23   1
   8 05 SIE-INT-TYPE                     24   1
   9 05 SIE-KEY                          25  19
  10 10 SIE-KEY-FILE-NBR                 25   4
  11 10 SIE-KEY-SSN                      29   9
  12 10 SIE-KEY-GUAR                     38   2
  13 10 SIE-KEY-SEQ                      40   2
  14 10 SIE-KEY-LOAN-NO                  42   2
  15 05 SIE-NAME                         44  32
  16 10 SIE-LNAM                         44  20
  17 10 SIE-FNAM                         64  11
  18 10 SIE-MID                          75   1
  19 05 SIE-ACTY-CD                      76   2
  20 05 SIE-PROJECTED-BAL                78   9
        Record length                        86

Line 20 is wrong, it should be length of 13.  If I change SIE-
PROJECTED-BAL to PIC 999999999.99- it works:

    cobdata.COBOLEngine.Version 2.0.0.07
    Lvl Name                            Pos Len Typ Oc
   1 01 SALES-ID-RECORD                   1  90
   2 02 SIE-MSTR-DATA                     1  90
   3 05 SIE-BANK-CD                       1   7
   4 05 SIE-BANK-LID                      8   7
   5 05 SIE-PORTFOLIO-NBR                15   7
   6 05 SIE-ACCT-STATUS                  22   1
   7 05 SIE-FILLER1                      23   1
   8 05 SIE-INT-TYPE                     24   1
   9 05 SIE-KEY                          25  19
  10 10 SIE-KEY-FILE-NBR                 25   4
  11 10 SIE-KEY-SSN                      29   9
  12 10 SIE-KEY-GUAR                     38   2
  13 10 SIE-KEY-SEQ                      40   2
  14 10 SIE-KEY-LOAN-NO                  42   2
  15 05 SIE-NAME                         44  32
  16 10 SIE-LNAM                         44  20
  17 10 SIE-FNAM                         64  11
  18 10 SIE-MID                          75   1
  19 05 SIE-ACTY-CD                      76   2
  20 05 SIE-PROJECTED-BAL                78  13
        Record length                        90

Again, thanks!
```

#### ↳ Re: To Dashwood

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-02-27T23:59:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70pvc2Fhr6hvU1@mid.individual.net>`
- **References:** `<36555d9e-c268-44a7-83ec-f15d9c98fcb7@v13g2000yqm.googlegroups.com>`

```
J Weirich wrote:
> Howdy, and thanks for the freeware.
>
…[76 more quoted lines elided]…
> Again, thanks!

Thanks for the feedback.

I'm sorry about delayed response; I have been too busy to check the forum 
recently.

I agree that this is wrong; please accept my apology. I'll pass your mail on 
to Robert, (who wrote the engine code) and see if he has time to fix it. It 
might be caused by the fact that it is the last entry, but I have many 
records where it isn't incorrect.

If Robert can't get to it, I'll have a look as soon as I can.

Meantime, thanks again for letting us know.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
