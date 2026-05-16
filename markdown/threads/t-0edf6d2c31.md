[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus sending printer commands

_6 messages · 4 participants · 2002-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus sending printer commands

- **From:** "PamelaRose" <prose@splatzone.com>
- **Date:** 2002-04-11T04:07:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y_7t8.43$2c.41484@newshog.newsread.com>`

```
Hi Everybody,
I need to print a report in landscape mode because it is 132 chr$ wide. I
cant figure out how to tell the printer to do this. I was looking in the
help area and found some code but I do not seem to be entering it correctly.

my code......

       100-MAIN-ROUTINE.
           OPEN INPUT EMP-DATA-IN
                OUTPUT PRINT-FILE
                CALL "PC_WIN_PRINT_FILE_EXT" LPT1 BTHIRD.DET BY VALUE 1
           PERFORM 200-INITILIZATION-RTN
           PERFORM 500-PRINT-COST-REPORT-HEADER


what I found .......
****************************************************************************
**************
Opens a printer channel, giving it a document name and displaying the
printer-options dialog box in the Windows environment.

Syntax:


CALL "PC_WIN_OPEN_PRINTER_EXT" USING printer-handle

doc-name

BY VALUE options SIZE 2

RETURNING status-code

Parameters:


printer-handle PIC XX COMP-5.
doc-name PIC X(m).
options numeric literal.
status-code See status-code.

Parameters on Entry:


doc-name The document name given to the spooled job.  The name must be
null-terminated.

options A switch to select the printer options dialog box:

0 No extended options
 1 Show printer options dialog, enabling user to setup printer.
****************************************************************************
**************
any help would be appreciated. This stuff is sooooo frustrating.

Thanks in advance

PamelaRose
�>-'-,-'->-'-,----
```

#### ↳ Re: Microfocus sending printer commands

- **From:** "PamelaRose" <prose@splatzone.com>
- **Date:** 2002-04-11T22:55:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lvot8.108$2c.99375@newshog.newsread.com>`
- **References:** `<y_7t8.43$2c.41484@newshog.newsread.com>`

```
Hi everybody

An update

(god I hope Im not talking to my self.......  I hate it when I do that   ; )

 my  new code......

       01  PRINTER-CONTROLS.
             05  PRINTER-HANDLE         PIC X(4)  VALUE 'LPT1'.
             05  DOC-NAME              PIC X(15) VALUE SPACES.
      *

       500-PRINT-COST-REPORT-HEADER.
           ADD 1 TO PAGE-CTR
           MOVE 'BTHIRD.DET' TO DOC-NAME
             CALL "PC_WIN_OPEN_PRINTER_EXT"
                  USING PRINTER-HANDLE DOC-NAME BY VALUE 1
           MOVE PAGE-CTR TO PAGE-CTR-OUT
           WRITE PRINT-RECORD FROM COST-REPORT-HEADER-1
                               AFTER ADVANCING 2 LINES



but it is not working right. It compiles ok then I get a file not found or
in
index  error and the program crashes. Funny thing though I printed a listing
seconds after it crashed once and it came out in landscape. the first and
only time MF, (a great abbreviation) ever printed like that. So the printer
got the message.


any help would be appreciated. This stuff is sooooo frustrating.

Thanks in advance
PamelaRose
�>-'-,-'->-'-,----

Boldly going where  PamelaRose has never gone before.





PamelaRose <prose@splatzone.com> wrote in message
news:y_7t8.43$2c.41484@newshog.newsread.com...
> Hi Everybody,
> I need to print a report in landscape mode because it is 132 chr$ wide. I
> cant figure out how to tell the printer to do this. I was looking in the
> help area and found some code but I do not seem to be entering it
correctly.
>
> my code......
…[10 more quoted lines elided]…
>
****************************************************************************
> **************
> Opens a printer channel, giving it a document name and displaying the
…[31 more quoted lines elided]…
>
****************************************************************************
> **************
> any help would be appreciated. This stuff is sooooo frustrating.
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Microfocus sending printer commands

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-12T03:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CB64F57.86506EB@shaw.ca>`
- **References:** `<y_7t8.43$2c.41484@newshog.newsread.com> <lvot8.108$2c.99375@newshog.newsread.com>`

```


PamelaRose wrote:

> Hi everybody
>
> An update
>
> (god I hope Im not talking to my self.......  I hate it when I do that   ; )

Well not quite - Yet <G>.

Exactly which compiler are you using. Can't be Net Express because the alpha
listing I see has only :-

PC_WIN_CHAR_TO_OEM
PC_WIN_INIT
PC_WIN_OEM_TO_CHAR

All current printer routines are referred to as :-

PC_PRINT_xxxx, or
PC_PRINTER_xxx

Thought you might be using the DOS Compiler V 3.1, but from the alpha listing,
(I'm going from the books, don't have the software loaded),  that only has :-

PC_WIN_ABOUT
PC_WIN_HANDLE

Without being able to tie it down,  suggestions :-

(1) Perhaps that "LPT1" above should read "LPT1:" (COLON after the 'one')
(2) try assigning the printer to a (disk) filename rather than a device
(3) Your earlier message said :-
      OPEN OUTPUT PRINT-FILE
       CALL "PC_WIN_PRINT_FILE_EXT" LPT1 BTHIRD.DET BY VALUE 1

    Exactly how did you specify the file entry : -

    select line-printer
    assign to filename/or LPT1:
    etc.......

    BUT...... if you are using PC_WIN...etc.... calls, they are CONTROLLING the
printer and you shouldn't have a file reference for the printer as well !

Sorry, I can't be more helpful. Any Micro Focus lurkers from California, Quebec
or Newbury looking in ? Please help the lady.

Jimmy, Calgary AB

>  my  new code......
>
…[95 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Microfocus sending printer commands

- **From:** "PamelaRose" <prose@splatzone.com>
- **Date:** 2002-04-12T05:01:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Ttt8.133$2c.125934@newshog.newsread.com>`
- **References:** `<y_7t8.43$2c.41484@newshog.newsread.com> <lvot8.108$2c.99375@newshog.newsread.com> <3CB64F57.86506EB@shaw.ca>`

```
Hi Jim

Thanks for your help.

I am running Micro Focus Animator Vrsion2  Vs; ANM2 8.2.75
and it says  Running on windows 95  (but I am actually running win 95SE)

The compiler says its  Micro Focus COBOL Version 3.4.18     L2.5   Rev 000

(know how to change to a font in MS Outlook to give a Zed Zero with a
slash!�� on a newsgroup?)

The code I showed you was a subroutine to print the headers

in the input-output section  I declaired

      *
                      SELECT PRINT-FILE ASSIGN TO PRINTER.
      *
and that does work to send lines to the printer


Then an FD of

      *
       FD PRINT-FILE.
      *
       01  PRINT-RECORD                PIC X(132).
      *
      *
then a
.
      *
       01  PRINTER-CONTROLS.
             05  PRINTER-HANDLE         PIC X(5)  VALUE 'LPT1:'.
             05  DOC-NAME              PIC X(10) VALUE SPACES.
      *

and finially the subroutine........

       500-PRINT-COST-REPORT-HEADER.
           ADD 1 TO PAGE-CTR
           MOVE 'BTHIRD.DET' TO DOC-NAME
             CALL "PC_WIN_OPEN_PRINTER_EXT"
                  USING PRINTER-HANDLE DOC-NAME BY VALUE 1
           MOVE PAGE-CTR TO PAGE-CTR-OUT
           WRITE PRINT-RECORD FROM COST-REPORT-HEADER-1
                               AFTER ADVANCING 2 LINES

down below where I put "what I found" and seperated it from the rest of the
text with *************  was what I found in the help section of Micro
Focus.  There were 6 or more differant "functions" listed to send or get
parameters to/from the printer   ack nak out of paper   ect ect ect.

I added the colon and still got the run time error

               Called program file not found in drive/directory  [ERROR 173]

But as I siad one time that happened and I almost imedately printed out a
listing to take to school (I am always late) the    listing came out in
landscape mode and that had NEVER happened before so its getting the
message. I the error box there is a continue option, but its not available
(dimmed)  besides the ok option that throws me out.

Sooooooooooooo  perhaps I search for  "PC_WIN_OPEN_PRINTER_EXT"   and put it
on my A drive ? The drive the program "knows about"   ie

      *
       FILE-CONTROL.  SELECT DEPT-INFO-TABLE-FILE
                             ASSIGN TO 'A:\BFIRST.SOR'
                               ORGANIZATION IS LINE SEQUENTIAL.
      *
                      SELECT EMP-DATA-IN
                               ASSIGN TO 'A:\BSECOND.SOR'
                                 ORGANIZATION IS LINE SEQUENTIAL.
      *
                      SELECT DIV-INFO-TABLE-FILE
                               ASSIGN TO 'A:\DIVINFO.DAT'
                                 ORGANIZATION IS LINE SEQUENTIAL.
      *
                      SELECT FAC-INFO-TABLE-FILE
                               ASSIGN TO 'A:\FACINFO.DAT'
                                 ORGANIZATION IS LINE SEQUENTIAL.
      *
                      SELECT PRINT-FILE ASSIGN TO PRINTER.
      *


 I want to thank you for your very informative and helpful reply and
sugestions

a new friend in Connecticut

PamelaRose
�>-'-,-'->-'-,----




James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3CB64F57.86506EB@shaw.ca...
>
>
…[6 more quoted lines elided]…
> > (god I hope Im not talking to my self.......  I hate it when I do that
; )
>
> Well not quite - Yet <G>.
>
> Exactly which compiler are you using. Can't be Net Express because the
alpha
> listing I see has only :-
>
…[9 more quoted lines elided]…
> Thought you might be using the DOS Compiler V 3.1, but from the alpha
listing,
> (I'm going from the books, don't have the software loaded),  that only has
:-
>
> PC_WIN_ABOUT
…[16 more quoted lines elided]…
>     BUT...... if you are using PC_WIN...etc.... calls, they are
CONTROLLING the
> printer and you shouldn't have a file reference for the printer as well !
>
> Sorry, I can't be more helpful. Any Micro Focus lurkers from California,
Quebec
> or Newbury looking in ? Please help the lady.
>
…[18 more quoted lines elided]…
> > but it is not working right. It compiles ok then I get a file not found
or
> > in
> > index  error and the program crashes. Funny thing though I printed a
listing
> > seconds after it crashed once and it came out in landscape. the first
and
> > only time MF, (a great abbreviation) ever printed like that. So the
printer
> > got the message.
> >
…[11 more quoted lines elided]…
> > > I need to print a report in landscape mode because it is 132 chr$
wide. I
> > > cant figure out how to tell the printer to do this. I was looking in
the
> > > help area and found some code but I do not seem to be entering it
> > correctly.
…[6 more quoted lines elided]…
> > >                 CALL "PC_WIN_PRINT_FILE_EXT" LPT1 BTHIRD.DET BY VALUE
1
> > >            PERFORM 200-INITILIZATION-RTN
> > >            PERFORM 500-PRINT-COST-REPORT-HEADER
…[4 more quoted lines elided]…
> >
****************************************************************************
> > > **************
> > > Opens a printer channel, giving it a document name and displaying the
…[32 more quoted lines elided]…
> >
****************************************************************************
> > > **************
> > > any help would be appreciated. This stuff is sooooo frustrating.
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microfocus sending printer commands

_(reply depth: 4)_

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2002-04-17T13:09:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0204171209.238569e1@posting.google.com>`
- **References:** `<y_7t8.43$2c.41484@newshog.newsread.com> <lvot8.108$2c.99375@newshog.newsread.com> <3CB64F57.86506EB@shaw.ca> <5Ttt8.133$2c.125934@newshog.newsread.com>`

```
Hi,

I've not used the COBOL 3.1. PC_WIN... routines but am familiar with
the similar NetExpress PC_PRINT... I've had a quick look at the
specification of the routines (we do have the 3.1. compiler) and there
is certainly an error in your WorkingStorage ...


"PamelaRose" <prose@splatzone.com> wrote in message news:<5Ttt8.133$2c.125934@newshog.newsread.com>...
> then a
> .
…[4 more quoted lines elided]…
>       *

the spec. has 
             printer-handle           pic x(2) comp-5

it is the handle of the printer that has been opened, i.e. an output
parameter and you wouldn't set it (other than perhaps initialise to
zero) prior to the call. In addition the "options" parameter is a bit
flag: bit 0 selects a printer dialog box; 1 a font dialog box; 2
portrait; and 3 landscape with the proviso that you cannot use the
orientation bits (2,3) if you set bit 0. This latter is probably
logical because I suspect that if you select the printer dialog then
the printer dialog will offer an orientation selection (somewhere).

You also seem to be confusing the use of the PC_WIN routines with the
standard FILE SELECT/ASSIGN and WRITE. When using the PC_WIN routines
you do not need the FILE SELECT etc.; the PC_WIN routines deal with
all accesses to the output device.

You would use PC_WIN_PRINTER_EXT to open the printer, returning the
printer-handle and then PC_WIN_WRITE_PRINTER to send a record of data
to the printer, providing the printer-handle (and NOT the COBOL
"WRITE") and finally PC_WIN_CLOSE_PRINTER. Actually you may also need
PC_WIN_PRINTER_CONTROL to do line feeds form feeds etc. after each
record (PC_WIN_WRITE...)

hope this helps...

graham


> 
> and finially the subroutine........
…[57 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microfocus sending printer commands

_(reply depth: 5)_

- **From:** Jean.Villemaire@microfocus.com (Jean Villemaire)
- **Date:** 2002-04-18T10:16:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ffc1cab.0204180916.6705be4e@posting.google.com>`
- **References:** `<y_7t8.43$2c.41484@newshog.newsread.com> <lvot8.108$2c.99375@newshog.newsread.com> <3CB64F57.86506EB@shaw.ca> <5Ttt8.133$2c.125934@newshog.newsread.com> <8a02b0a1.0204171209.238569e1@posting.google.com>`

```
Pamela,

If I read your original post you are asking how can I use the
PC_WIN_PRINT_FILE_EXT library call to print a file in landscape mode.

If this is still your question what I would do in your program is
generate your output file as a physical file and then use the call. 
The PC_WIN_PRINT_FILE_EXT will send your file to the printer.

The syntax should be as follows;

call "PC_WIN_PRINT_FILE_EXT"
     using by reference fi-file-name,
           by reference "Name of my document" & x"0",
           by value X size 2

Where fi-filename is a pic x(n) data item that will contain the name
of your file
Where X is the options that you want to use.  X can have the following
values;

Set of bits to set printer options:

Bit Decimal description
3   8       Print in landscape orientation
2   4       Print in portrait orientation
1   2       Display font dialog box
0   1       Display a printer control dialog box

Bits 2 and 3 cannot be used with bit 0 set.

So in your case X should have a value of 8, to print in landscape
mode.

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
