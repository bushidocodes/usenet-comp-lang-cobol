[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multi Line fields

_3 messages · 2 participants · 2007-03_

---

### Multi Line fields

- **From:** jmoore207@gmail.com
- **Date:** 2007-03-13T05:15:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173788119.681442.302070@s48g2000cws.googlegroups.com>`

```
Does anyone have an example of how you define a multi-line field in
AcuCobol. This is in a unix environment. This will be a description
field that will be 6 lines of 60 characters. I was told that it would
"auto wrap". Any help would be appreciated.
```

#### ↳ Re: Multi Line fields

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-03-13T22:01:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BaFJh.16549$DN.10177@pd7urf2no>`
- **In-Reply-To:** `<1173788119.681442.302070@s48g2000cws.googlegroups.com>`
- **References:** `<1173788119.681442.302070@s48g2000cws.googlegroups.com>`

```
jmoore207@gmail.com wrote:
> Does anyone have an example of how you define a multi-line field in
> AcuCobol. This is in a unix environment. This will be a description
> field that will be 6 lines of 60 characters. I was told that it would
> "auto wrap". Any help would be appreciated.
> 
Don't know Acu COBOL but did find the following as an example 
(scrlprgm.cbl/zip) at the Acu site :-

       * Description of screen controls.
        01 Big-Screen.
           03 LABEL "Using the Windows API from COBOL"
              LINE 3 COL 35.
           03 LABEL "Top:"
              LINE 5 COL 40.
           03 ENTRY-FIELD VALUE "Top"    SIZE 10 CELLS.
           03 LABEL "Extreme Left:"
              LINE 15 COL 1.
           03 ENTRY-FIELD VALUE "Left"   SIZE 10 CELLS.
           03 LABEL "Extreme Right:"
              LINE 15 COL 120.
           03 ENTRY-FIELD VALUE "Right"  SIZE 10 CELLS.
           03 LABEL "Bottom:"
              LINE 45 COL 40.
           03 ENTRY-FIELD VALUE "Bottom" SIZE 10 CELLS.


As shown above, is that how you are specifying EntryFields ? If that's 
the case then to get an MLE (Multiple Line Entryfield), specify the 
WIDTH as 60 cells. Not sure how you get your bottom Line, but assuming 
you start at say 'Line 10, Col 20', then to get six lines you need an 
entry 'Line 16, Col 20'.

Note an MLE is an extension of an entry-field (SLE = Single Line 
Entryfield). Somewhere in your syntax you should be able to turn 
"ENTRY-FIELD' into "MULTIPLE-LINE-ENTRYFIELD" or perhaps "MLE".

If you get that far, when you enter data, as soon as you hit the 61st 
character of each line it should indeed wrap-around. (It's calling the 
control an MLE that automatically gives you wrap-around).

Just picked up on this one, smssrc.zip/demosend.cbl  :-

        SCREEN      SECTION.
        01  TEXT-SCREEN.

            03      LABEL
                    LINE             02
                    COL              02
                    TITLE            "Text to send".

            03      EDIT-BOX         ENTRY-FIELD
                    LINE             04
                    COL              02
                    SIZE             40
                    LINES            08
                    VALUE            MESSAGE-TXT
                    MULTILINE
                    MAX-TEXT         160
                    3-D
                    USE-RETURN.

            03      LABEL
                    LINE             14
                    COL              02
                    TITLE            "Phone".

            03      ENTRY-FIELD
                    LINE             14
                    COL              12
                    SIZE             30
                    VALUE            DEST-PHONE
                    3-D.

            03      SendBtn          PUSH-BUTTON
                    LINE             17
                    COL              02
                    SIZE             10
                    TITLE            "S&end"
                    SELF-ACT
                    EXCEPTION-VALUE  = 13.

            03      ExitBtn          PUSH-BUTTON
                    LINE             17
                    COL              32
                    SIZE             10
                    TITLE            "E&xit"
                    SELF-ACT
                    EXCEPTION-VALUE  = 27.

'EDIT-BOX' contains a reference to 'MULTILINE' - perhaps that's what you 
are after ?

HTH

Jimmy
```

##### ↳ ↳ Re: Multi Line fields

- **From:** jmoore207@gmail.com
- **Date:** 2007-03-14T09:33:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173890005.985341.277860@p15g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<BaFJh.16549$DN.10177@pd7urf2no>`
- **References:** `<1173788119.681442.302070@s48g2000cws.googlegroups.com> <BaFJh.16549$DN.10177@pd7urf2no>`

```
On Mar 13, 6:01 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> jmoore...@gmail.com wrote:
> > Does anyone have an example of how you define a multi-line field in
…[92 more quoted lines elided]…
> Jimmy

Thanks for the help Jimmy. I got it to work. Also, thanks to Doc. Here
is how I did it.
Working-Storage.
       01 entry-tbl.
          05 entry-table occurs 6 times  pic x(60).

Screen Section
       01 screen-2.
          02  entry-1, entry-field, using multiple entry-table
               line 10 column 12, size 60, lines 6.


       accept-select-4.
           set environment "SCREEN" to "PROMPT= ".
           display box at 009011 size 62 lines 8.
           display prompt-4.
           display screen-2.
           accept screen-2.
           evaluate key-status
           when enter-key
           when down-arrow-key
           when tab-key
               if entry-tbl not = spaces
                   move entry-tbl to ws-web-item-long-desc
               end-if
               set environment "SCREEN" to "PROMPT=_"


         main-logic-exit.
              inititalize entry-rbl.
              display screen-2.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
