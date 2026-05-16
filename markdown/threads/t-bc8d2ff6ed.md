[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PROG. FUNCT. KEYS IN RMCOBOL FOR NT

_6 messages · 3 participants · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** Erie <73042.311@CompuServe.COM>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com>`

```
I was just wondering if there is a way that anyone knows of to 
program function keys when running RMCOBOL for Windows NT vs. 6.5.
We are currently moving from an older system where our users had 
this ability.  So, if anyone has any idea of how to do this please 
help.  And, thanks in advance for all you help.
```

#### ↳ Re: PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** frederico_fonseca@eudoramail.com (Frederico Fonseca)
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376197d7.588126@news.indigo.ie>`
- **References:** `<emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com>`

```
On Fri, 11 Jun 1999 12:08:53 -0400, Erie <73042.311@CompuServe.COM>
wrote:

>I was just wondering if there is a way that anyone knows of to 
>program function keys when running RMCOBOL for Windows NT vs. 6.5.
>We are currently moving from an older system where our users had 
>this ability.  So, if anyone has any idea of how to do this please 
>help.  And, thanks in advance for all you help.
It is possible.(except for some key that the Windows does not allow
you to use).

It is easy.
Just read the Runtime User Manual that is supplied with the runtime.

FF
```

#### ↳ Re: PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7js3h4$7dt$1@news.imp.ch>`
- **References:** `<emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com>`

```
Hello Erie

I changed from RMCobol 5.32 for Dos to RmCobol 6.51 for Windows.
Our programs are running under Win98.
We use since the beginning the Function Key from F1 to F30. Our NCR
Keyboards have these Function Keys. You can generate them also with
combined keys like CNTRL and F2 = F22
We could use all the Functon Keys with Version 6.51 except F20 and F30.
These keys seem not to be available under 6.51.
With NT we have no experience.

Have a nice weekend

john@casagrande.ch

Erie <73042.311@CompuServe.COM> schrieb in im Newsbeitrag:
emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com...
> I was just wondering if there is a way that anyone knows of to
> program function keys when running RMCOBOL for Windows NT vs. 6.5.
> We are currently moving from an older system where our users had
> this ability.  So, if anyone has any idea of how to do this please
> help.  And, thanks in advance for all you help.
```

##### ↳ ↳ Re: PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** Erie <73042.311@CompuServe.COM>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eF1l7Umt#GA.361@nih2naac.compuserve.com>`
- **References:** `<7js3h4$7dt$1@news.imp.ch>`

```
Thanks to all who have tried to help.  Although, I don't think I 
made my question clear enough.  What I meant was that I want to 
define a function key such as F12, to have the value of say "^CR".
So, when a user presses the F12 key this value will be sent to the
program.  Anyone have any idea of how to do this in RMCOBOL for 
Windows????  Thanks in advance for any help.
```

###### ↳ ↳ ↳ Re: PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** frederico_fonseca@eudoramail.com (Frederico Fonseca)
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376549e0.547082@news.indigo.ie>`
- **References:** `<7js3h4$7dt$1@news.imp.ch> <eF1l7Umt#GA.361@nih2naac.compuserve.com>`

```
On Mon, 14 Jun 1999 08:55:50 -0400, Erie <73042.311@CompuServe.COM>
wrote:

>Thanks to all who have tried to help.  Although, I don't think I 
>made my question clear enough.  What I meant was that I want to 
…[3 more quoted lines elided]…
>Windows????  Thanks in advance for any help.
Read the Runtime User Manual that you have received.
Configuration files.
It can be done (until a certain point).

FF
```

#### ↳ Re: PROG. FUNCT. KEYS IN RMCOBOL FOR NT

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ju6mq$pmj$1@news.imp.ch>`
- **References:** `<emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com>`

```
Hy Erie,

for a little help please read the following sample:

      **********************************
      *  TESTPROGRAM FOR FUNCTION-KEYS  *  RM
      **********************************
      ***
      ***    FOR DOCUMENTATION I MENTIONED SOME VALUES OF OFTEN
      ***    USED KEYS .....
      ***
       WORKING-STORAGE SECTION.
      ***
       01  W-WORK.
           05  W-ESC-KEY                 PIC 9(2)  VALUE 0.
               88 ESC-HELP                 VALUE 1.
               88 ESC-CONFIRM         VALUE 7.
               88 ESC-STOP                 VALUE 9.
               88 ESC-FINISHED         VALUE 9 27.
               88 ESC-BACK               VALUE 10 52.
               88 ESC-ENTER              VALUE 13.
               88 ESC-FIELD-NEXT     VALUE 0 13 53 56.
               88 ESC-FINISHED         VALUE 27.
               88 ESC-ARROW-BACK       VALUE 52.
               88 ESC-ARROW-FORWARD    VALUE 53.
               88 ESC-LINE-NEXT        VALUE 53.
               88 ESC-HOME             VALUE 54.
               88 ESC-NEXT             VALUE 52 53 67 68.
               88 ESC-FORWARD          VALUE 13 53 68.
               88 ESC-BACK             VALUE 52 67.
               88 ESC-PGUP             VALUE 67.
               88 ESC-PGDN             VALUE 68.
               88 ESC-CTL-HOME         VALUE 81.
               88 ESC-END              VALUE 82.
               88 ESC-CTL-END          VALUE 83.
               88 ESC-CON-ERROR        VALUE 98.
               88 ESC-TIME-OVER        VALUE 99.
           05  FIELD                   PIC X(5).
*****************************************************
       PROCEDURE DIVISION.
       TEST-1.
           DISPLAY "ENTER A WORD,  THE VALUE OF THE FUNCTION KEY"
                                       LINE  1 POSITION  2.
           DISPLAY "OR THE KEY WILL BE STORED IN FIELD W-ESC"
                                       LINE  2 POSITION  2.

       TEST-2.
           ACCEPT FIELD                LINE  5 POSITION 29
                                       TIME 2500
                                       NO BEEP ECHO
                                       UPDATE TAB PROMPT "."
                                    ON EXCEPTION W-ESC-KEY
                                       CONTINUE.
           IF   ESC-STOP
                GO TO TEST-90.
           IF   ESC-BACK
                GO TO TEST-1.
           IF   ESC-FINISHED
                GO TO TEST-EXIT.
           IF   ESC-TIME-OVER
                DISPLAY "THIS HAPPENS IF YOU DID NOT PRESSE A KEY"
                                        LINE 15 POSITION  1
                DISPLAY "WITHIN ABOUT 20 SEC. (TIME 2500)"
                                        LINE 16 POSITION  1.
           GO TO TEST-2.
       TEST-90.
           DISPLAY "I LIKE GO TO'S !!!" LINE 20 POSITION  1.
           STOP RUN.
       TEST-EXIT.
           EXIT.

hope it helps.

greetings john@casagrande.ch
Erie <73042.311@CompuServe.COM> schrieb in im Newsbeitrag:
emdd0SCt#GA.349@nih2naaa.prod2.compuserve.com...
> I was just wondering if there is a way that anyone knows of to
> program function keys when running RMCOBOL for Windows NT vs. 6.5.
> We are currently moving from an older system where our users had
> this ability.  So, if anyone has any idea of how to do this please
> help.  And, thanks in advance for all you help.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
