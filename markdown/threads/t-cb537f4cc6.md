[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Variable Length Output Records

_4 messages · 4 participants · 1998-12_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Help Variable Length Output Records

- **From:** David Warring <David_Warring@hotmail.com>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366A0230.633A3F5A@hotmail.com>`

```
Just a quickie...

I have a recurring Client requirement to create a file of  character
delimited output records. These are to be constructed from existing
working storage fields. Trimming of the fields is also required, to
produce fields. The records may be of (greatly) varying length. E.g.

aaa1|bbbb1|cccc .... |zzz1
aaaaa2|bbbbbbbbbb2|cccc .... |zz2

Language choices are Cobol or Cobol! The customer is using a VAX/VMS
Cobol compiler, although a Cobol-85 compliant solution is preferred.

Is this possible? What's the best approach. Any help appreciated.
```

#### ↳ Re: Help Variable Length Output Records

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ebvn$88q$1@news.igs.net>`
- **References:** `<366A0230.633A3F5A@hotmail.com>`

```
Check out the STRING verb.  Remember to move
space to the receiving field first, as it will not clear
to the end of field.  A quick example:

01 a    picture x(10) value "data".
01 b    picture x(10) value "dat".
01 c    picture x(15) value space.

string a delimited by " "
          "." delimited by length
          b delimited by space
     into
           c.


David Warring wrote in message <366A0230.633A3F5A@hotmail.com>...
>Just a quickie...
>
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help Variable Length Output Records

- **From:** casten@usfca.edu (John Casten)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<casten-0812981446120001@138.202.137.168>`
- **References:** `<366A0230.633A3F5A@hotmail.com> <74ebvn$88q$1@news.igs.net>`

```
> David Warring wrote in message <366A0230.633A3F5A@hotmail.com>...
> >Just a quickie...
…[18 more quoted lines elided]…
> >
here's how I handle it.  I wrote a program that loads class lists for the
USF web site (check it out -
http://www.usfca.edu/schedules/scheduleindex.shtml)

INPUT-OUTPUT SECTION.
FILE-CONTROL.

    SELECT HTML-FILE
       ASSIGN           DUMMY
    .
"dummy" is a placeholder, as I create many many files using the same
select.  The ASSIGN clause is required.

DATA DIVISION.
FILE SECTION.

FD  HTML-FILE
    RECORD VARYING 1 TO 340 DEPENDING REC-LENGTH
    VALUE OF ID WS-FILESPEC.
01  HTML-REC                   PIC X(340).

WORKING-STORAGE SECTION.              
01  PROGRAM-CONTROL-DATA.

01  HTML-STUFF.
    03  REC-LENGTH             PIC 9(09)  COMP.
    03  HTML-OPEN              PIC X(06)  VALUE '<HTML>'.
    03  HTML-CLOSE             PIC X(07)  VALUE '</HTML>'.
    03  HEAD-OPEN              PIC X(06)  VALUE '<HEAD>'.
    03  HEAD-CLOSE             PIC X(07)  VALUE '</HEAD>'.
    03  TITLE-OPEN             PIC X(07)  VALUE '<TITLE>'.
    03  TITLE-CLOSE            PIC X(08)  VALUE '</TITLE>'.
    03  H1-OPEN                PIC X(04)  VALUE '<H1>'.
    03  H1-CLOSE               PIC X(05)  VALUE '</H1>'.
    03  H2-OPEN                PIC X(04)  VALUE '<H2>'.
    03  H2-CLOSE               PIC X(05)  VALUE '</H2>'.
    03  H3-OPEN                PIC X(04)  VALUE '<H3>'.
    03  H3-CLOSE               PIC X(05)  VALUE '</H3>'.
    03  BODY-OPEN              PIC X(06)  VALUE '<BODY>'.
    03  BODY-CLOSE             PIC X(07)  VALUE '</BODY>'.
    03  PRE-OPEN               PIC X(05)  VALUE '<PRE>'.
    03  PRE-CLOSE              PIC X(06)  VALUE '</PRE>'.
    03  ULIST-OPEN             PIC X(04)  VALUE '<UL>'.
    03  ULIST-CLOSE            PIC X(05)  VALUE '</UL>'.
    03  TABLE-OPEN             PIC X(20)  VALUE '<TABLE WIDTH="100%">'.

here's one example:

    OPEN OUTPUT HTML-FILE

    MOVE 6                     TO REC-LENGTH
    WRITE HTML-REC           FROM HTML-OPEN

*   MOVE 6                     TO REC-LENGTH
    WRITE HTML-REC           FROM HEAD-OPEN

    MOVE TITLE-LENGTH          TO REC-LENGTH
    WRITE HTML-REC           FROM TITLE

    MOVE 7                     TO REC-LENGTH
    WRITE HTML-REC           FROM HEAD-CLOSE

    MOVE 6                     TO REC-LENGTH
    WRITE HTML-REC           FROM BODY-OPEN

in building details, I don't personally like STRING, tho' it works fine in
most cases.  To get the correct rec length, you would need to use STRING
... WITH POINTER, and then subtract 1 from the final value, since your
working-storage pointer item has the position (address) of the next byte.

Here is my problem with STRING:
say you have this:
    03  WS-CITY  PIC X(13)  VALUE 'San Francisco'.

If you STRING this delimited size, no problem, you just end up with alot
of white space (in most cases, i.e. Fresno), which in an HTML document is
a very bad thing.  If you delimit it by ' ' (one space), then you get
'San' in your output.  If you delimit it by '  ' (2 spaces) you get
nothing.  You would need to move the field to a 15 byte field to get it to
work in all cases.  Phooey.  I prefer the following:

    MOVE H2-OPEN               TO H2 
(this in lieu of moving spaces to H2, we be padded honey)
    MOVE SK-DEPT-TRANS         TO H2 (5:40)
                                  HOLD-DEPT-TRANS

    MOVE 44                    TO H2-PTR
    PERFORM UNTIL H2 (H2-PTR:1) > SPACE
               OR H2-PTR < 1
       SUBTRACT 1 FROM H2-PTR
    END-PERFORM
    ADD 1 TO H2-PTR
    MOVE H2-CLOSE              TO H2 (H2-PTR:5)

    ADD H2-PTR 4 GIVING REC-LENGTH

    WRITE HTML-REC           FROM H2

In an ideal world I would remove all of the magic numbers, but you get the idea
```

#### ↳ Re: Help Variable Length Output Records

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366a3066.361928064@news1.ibm.net>`
- **References:** `<366A0230.633A3F5A@hotmail.com>`

```
On Sun, 06 Dec 1998 15:04:00 +1100, David Warring
<David_Warring@hotmail.com> wrote:

>Just a quickie...
>
…[11 more quoted lines elided]…
>Is this possible? What's the best approach. Any help appreciated.

Yes.  Construct your data using STRING and then output it to a "Line
Sequential" file.  Yes - for those wondering VMS COBOL does support
this construct.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
