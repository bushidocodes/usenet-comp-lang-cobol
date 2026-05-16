[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# question about dynamic array

_8 messages · 4 participants · 2005-06_

---

### question about dynamic array

- **From:** Roby66 <NOSPAM@libero.it>
- **Date:** 2005-06-01T15:20:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7kco0$pl$1@newsreader.mailgate.org>`

```
Hi, I'm roby...
I was studying cobol language in order to port a vb application to cobol
application using cobol-85.
First of all I wanted to test some code about cobol array management.
I'm trying to porting vb array management (redim preserve) to cobol
I know using of occurs time and depending on instruction
I wrote this code and it seems doesn't store data correctly
into array when index exceeded size
I thought I only need to change INDEX-VALUE to change array dimension

thanks for help


       IDENTIFICATION DIVISION.
       PROGRAM-ID. STR01.
       AUTHOR. ROBY.
           INSTALLATION. ROME.
           DATE-WRITTEN. 30/05/2005.
           DATE-COMPILED. 31/05/2005.
           SECURITY. NONE.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. AMD-SEMPRON.
       OBJECT-COMPUTER. AMD-SEMPRON.
      *SPECIAL-NAMES. DECIMAL-POINT IS COMMA.
       SPECIAL-NAMES. CURRENCY SIGN IS "E".

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 POS PIC 99.
       77 INDEX-VALUE PIC 99.
       77 CT PIC 99 VALUE 0.

       01 INPUT-STRING PIC X(20).
       01 KEY-PRESSED PIC X.

       01 TABLE-STRING.
	  02 TAB01 OCCURS 1 TO 3 TIMES DEPENDING ON INDEX-VALUE.
	     05 NAME PIC X(20) VALUE SPACES.

       01 PRINT-LINE.
	  02 FILLER PIC X(10)  VALUE "RECORD #".
	  02 OUT-NUMBER PIC 99.
	  02 FILLER PIC X(3)   VALUE SPACES.
	  02 OUT-NAME PIC X(20).


       PROCEDURE DIVISION.

	   MOVE 1 TO INDEX-VALUE.

       START-INPUT.
           DISPLAY "INSERT YOUR DATA (MAX 50)"
	   ACCEPT INPUT-STRING FROM CONSOLE
	   DISPLAY "INPUT = '" INPUT-STRING "'"

	   IF INPUT-STRING = " " GO TO END-OF-PROGRAM.
	   PERFORM SAVE-DATA
	   GO TO START-INPUT.

       PRINT-DATA.
	   MOVE 1 TO CT
      	   PERFORM UNTIL CT = INDEX-VALUE
               MOVE CT TO OUT-NUMBER
               MOVE NAME(CT) TO OUT-NAME
               DISPLAY PRINT-LINE
	       ADD 1 TO CT
           END-PERFORM.
           DISPLAY "END-PERFORM".
       PRINT-DATA-EX.
 	   EXIT.

       SAVE-DATA.
	   MOVE INPUT-STRING TO NAME(INDEX-VALUE)
	   DISPLAY "DATA STORE AT INDEX " INDEX-VALUE
	   ADD 1 TO INDEX-VALUE.
       SAVE-DATA-EX.
	   EXIT.

       END-OF-PROGRAM.
	   PERFORM PRINT-DATA
           DISPLAY "PRESS ANY KEY"
           ACCEPT KEY-PRESSED FROM CONSOLE
	   STOP RUN.
```

#### ↳ Re: question about dynamic array

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-06-01T13:29:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kLine.9276$iA6.2752@newssvr19.news.prodigy.com>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org>`

```
"Roby66" <NOSPAM@libero.it> wrote in message
news:d7kco0$pl$1@newsreader.mailgate.org...
> I thought I only need to change INDEX-VALUE to change array dimension

Changing INDEX-VALUE will change the maximum subscript you may access, but
the table (that's what BASIC arrays are usually called by COBOL programmers)
may never have more than 'max' elements as specified in the "OCCURS  min to
max"  clause; e.g.,

>   02 TAB01 OCCURS 1 TO 3 TIMES DEPENDING ON INDEX-VALUE.

You may never have more than three valid elements in this table.

MCM
```

##### ↳ ↳ Re: question about dynamic array

- **From:** Roby66 <NOSPAM@libero.it>
- **Date:** 2005-06-01T15:41:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7kdvu$2pg$1@newsreader.mailgate.org>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org> <kLine.9276$iA6.2752@newssvr19.news.prodigy.com>`

```

>
>You may never have more than three valid elements in this table.
>

Is there another way to use dynamic array in cobol ?
Or this force to me to declare statically an array ?

Roby
```

###### ↳ ↳ ↳ Re: question about dynamic array

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-06-01T13:56:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j8jne.9438$iA6.9337@newssvr19.news.prodigy.com>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org> <kLine.9276$iA6.2752@newssvr19.news.prodigy.com> <d7kdvu$2pg$1@newsreader.mailgate.org>`

```
"Roby66" <NOSPAM@libero.it> wrote in message
news:d7kdvu$2pg$1@newsreader.mailgate.org...
>
> >
…[4 more quoted lines elided]…
> Or this force to me to declare statically an array ?

Not in the sense you, as a BASIC-language programmer, would understand
'dynamic array'

The only way to do this in COBOL is to use a COBOL compiler which supports
calls to the current operating system to do your own memory
allocation/reallocation/deallocation and then use POINTER data types to
access that data.

Yes, you could find some programmer to create the code needed, and structure
it to resemble BASIC. But any such code will perforce be limited to a
specific compiler on a specific target operating system.

Or, instead of using a 'memory' table/array, you could use a random-access
file; see ORGANIZATION SEQUENTIAL ACCESS RANDOM RELATIVE KEY IS
relative-key-name in your SELECT statements.
```

###### ↳ ↳ ↳ Re: question about dynamic array

_(reply depth: 4)_

- **From:** Roby66 <NOSPAM@libero.it>
- **Date:** 2005-06-01T16:18:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7kg5b$2pg$2@newsreader.mailgate.org>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org> <kLine.9276$iA6.2752@newssvr19.news.prodigy.com> <d7kdvu$2pg$1@newsreader.mailgate.org> <j8jne.9438$iA6.9337@newssvr19.news.prodigy.com>`

```


>Or, instead of using a 'memory' table/array, you could use a random-access
>file; see ORGANIZATION SEQUENTIAL ACCESS RANDOM RELATIVE KEY IS
>relative-key-name in your SELECT statements.

Yes, right, seems to be the best solution.
Anyway I have to port this vb application on mainframe.
At the moment I don't know anything about it.
I only know new application has to be developed
using cobol II, I think cobol 85.
Customer sent me a source code is running on
their system and I suppose is standard ansi85.

Last question, If I use temp indexed files, how can I removed them
at the end of processing ?
```

###### ↳ ↳ ↳ Re: question about dynamic array

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-06-01T17:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pxmne.119170$Yr4.75689@fe07.news.easynews.com>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org> <kLine.9276$iA6.2752@newssvr19.news.prodigy.com> <d7kdvu$2pg$1@newsreader.mailgate.org> <j8jne.9438$iA6.9337@newssvr19.news.prodigy.com> <d7kg5b$2pg$2@newsreader.mailgate.org>`

```
If you are talking about "VS COBOL II" on an IBM mainframe, you should know that 
compiler is out-of-service and has been for many years.  The currently supported 
IBM compiler (that does include the '85 Standard *PLUS* intrinsic functions 
*PLUS* Object orientation PLUS lots of extensions) is "Enterprise COBOL". You 
will need to find out exactly which compiler is your target - to know what you 
can and cannot code.
```

###### ↳ ↳ ↳ Re: question about dynamic array

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-06-01T08:14:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7kjdi$gd4$1@si05.rsvl.unisys.com>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org> <kLine.9276$iA6.2752@newssvr19.news.prodigy.com> <d7kdvu$2pg$1@newsreader.mailgate.org> <j8jne.9438$iA6.9337@newssvr19.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:j8jne.9438$iA6.9337@newssvr19.news.prodigy.com...

> Or, instead of using a 'memory' table/array, you could use a random-access
> file; see ORGANIZATION SEQUENTIAL ACCESS RANDOM RELATIVE KEY IS
> relative-key-name in your SELECT statements.

Not in *standard* COBOL (though this, or close variations of this, is a
common extension).

The only ACCESS MODE allowed for ORGANIZATION SEQUENTIAL files in standard
'74, '85 or '02 COBOL is SEQUENTIAL.  See ANSI X3.23-1974 page IV-4, ANSI
X3.23-1985 page VII-7, and ISO/IEC 1989:2002 page 212 for the applicable
syntax diagrams.

However, you could substitute ORGANIZATION RELATIVE for ORGANIZATION
SEQUENTIAL into the above syntax and come up with standard COBOL.

    -Chuck Stevens
```

#### ↳ Re: question about dynamic array

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-06-01T18:03:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yLmne.11002$iA6.3818@newssvr19.news.prodigy.com>`
- **References:** `<d7kco0$pl$1@newsreader.mailgate.org>`

```
Just noticed...

"Roby66" <NOSPAM@libero.it> wrote in message
news:d7kco0$pl$1@newsreader.mailgate.org...
> Hi, I'm roby...
> I'm trying to porting vb array management (redim preserve) to cobol
...
[anither message.]..
>Anyway I have to port this vb application on mainframe..
...
>I only know new application has to be developed
>using cobol II, I think cobol 85.
>Customer sent me a source code is running on
>their system and I suppose is standard ansi85

???

Not sure I understand your situation entirely, but let me hazard a guess:

Customer sent you COBOL source code of ..what, what they use now?  And you
need to integrate some capability currently available in a VB program into
that software?

Not ever having seen any of this, or even sure if I understand the situation
correctly, two things come to mind...

1. There is such a thing as "Mainframe BASIC".  IIRC, it's not terribly
popular or powerful, but it's out there somewhere.
2. Instead of screwing around with a port, might be easier and surely will
be more maintainable long-term to forget about 'porting,'  bite the bullet
and just write the required logic in COBOL from scratch. (Disclaimer: I am a
notorious critic of 'verb-for-verb' port/translation efforts).

FWIW, if your BASIC is well written, your COBOL code - if equally
well-written - will look a lot like the BASIC code with which you
start.(I've often said "Well-written BASIC looks a lot like well-written
COBOL. Badly-written BASIC looks a lot like, well, badly-written  BASIC".

(Also FWIW: dynamic memory allocation and pointer variables ARE available
with IBM mainrame COBOL).

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
