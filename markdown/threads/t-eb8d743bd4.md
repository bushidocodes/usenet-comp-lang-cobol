[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CompaqCobol (VMS)

_15 messages · 6 participants · 2005-04 → 2005-05_

---

### CompaqCobol (VMS)

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T11:06:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4l7c0.1j8.1@ahr.rsli.de>`

```
I have a screen layout coded in the SCREEN SECTION. This layout is
processed in the PROCEDURE DIVISION by "DISPLAY SCREEN-1" and by "ACCEPT
SCREEN-1".

After processing the operator's input, the program needs to reject
invalid entries. So I loop back to the DISPLAY and ACCEPT of the screen,
providing an error message explaining what value is inacceptable.

Is there any (easy) way to place the cursor in the field where the
inappropriate value was entered?

Thanks a lot in advance,

Volker
```

#### ↳ Re: CompaqCobol (VMS)

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2005-04-26T11:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de>`

```
Hi,

I've never actually used it myself, but the CURSOR IS clause in the
Special-Names paragraph may be what you're looking for?

Regards Richard Maher

"Volker N. Englisch" <englisch.ahr@gmx.de> wrote in message
news:d4l7c0.1j8.1@ahr.rsli.de...
> I have a screen layout coded in the SCREEN SECTION. This layout is
> processed in the PROCEDURE DIVISION by "DISPLAY SCREEN-1" and by "ACCEPT
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: CompaqCobol (VMS)

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T15:10:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4llkc.2pk.2@ahr.rsli.de>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com>`

```
Richard Maher wrote:

>> Is there any (easy) way to place the cursor in the field where the
>> inappropriate value was entered?

> I've never actually used it myself, but the CURSOR IS clause in the
> Special-Names paragraph may be what you're looking for?

Unfortunately there seems to be no CURSOR IS clause in CompaqCobol - at
least the documentation doesn't mention it.

Volker
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

- **From:** docdwarf@panix.com
- **Date:** 2005-04-26T09:51:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lh0a$gei$1@panix5.panix.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de>`

```
In article <d4llkc.2pk.2@ahr.rsli.de>,
Volker N. Englisch <englisch.ahr@gmx.de> wrote:
>Richard Maher wrote:
>
…[7 more quoted lines elided]…
>least the documentation doesn't mention it.

http://h71000.www7.hp.com/DOC/73final/documentation/pdf/cobol_refman.pdf

http://h71000.www7.hp.com/DOC/73final/documentation/pdf/cobol_um.pdf

http://www.google.com/search?hl=en&q=cursor+compaq+cobol&spell=1

... all seem to disagree.

DD
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 4)_

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T16:24:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lq08.nc.1@ahr.rsli.de>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de> <d4lh0a$gei$1@panix5.panix.com>`

```
docdwarf@panix.com> wrote:
> Volker N. Englisch <englisch.ahr@gmx.de> wrote:
> >Richard Maher wrote:
…[7 more quoted lines elided]…
>>Unfortunately there seems to be no CURSOR IS clause in CompaqCobol -
at
>>least the documentation doesn't mention it.
>
>
http://h71000.www7.hp.com/DOC/73final/documentation/pdf/cobol_refman.pdf
> http://h71000.www7.hp.com/DOC/73final/documentation/pdf/cobol_um.pdf
> http://www.google.com/search?hl=en&q=cursor+compaq+cobol&spell=1
>
> ... all seem to disagree.

Indeed they do. I had a search over the HTML version, and it wasn't
found. Sorry.

Volker
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-04-26T11:21:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lm9f$jsb$1@panix5.panix.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4llkc.2pk.2@ahr.rsli.de> <d4lh0a$gei$1@panix5.panix.com> <d4lq08.nc.1@ahr.rsli.de>`

```
In article <d4lq08.nc.1@ahr.rsli.de>,
Volker N. Englisch <englisch.ahr@gmx.de> wrote:
>docdwarf@panix.com> wrote:
>> Volker N. Englisch <englisch.ahr@gmx.de> wrote:

[snip]

>>>Unfortunately there seems to be no CURSOR IS clause in CompaqCobol - at
>>>least the documentation doesn't mention it.
…[9 more quoted lines elided]…
>found. Sorry.

Such things happen... you might be surprised by the things that I have 
missed.

DD
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 4)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-04-26T07:37:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114526261.451117.92880@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d4lh0a$gei$1@panix5.panix.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de> <d4lh0a$gei$1@panix5.panix.com>`

```
Volker,

you need a simple trick to solve this problem  ---- when you display
the error
message that pertains to the Name-field, then you must ACCEPT that
field
after displaying the message. Likewise, when you display an error
message
for the City-field, then you must ACCEPT that field after displaying
the message.

case in point:

display "You must enter the name to proceed" at 2301
accept S1-name with beep

OR

display "You must enter the city name to proceed" at 2301
accept S1-city with beep

hope these information helps.

Kellie.
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-26T16:22:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Utbe.1132013$za2.182999@news.easynews.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de> <d4lh0a$gei$1@panix5.panix.com> <1114526261.451117.92880@g14g2000cwa.googlegroups.com>`

```
Kellie,
  The DISPLAY at NNNN

format is (usually) incompatible with the

  DISPLAY screen-name

format.  Although this will depend upon the vendor.
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 6)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-04-26T09:48:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114534118.556810.291840@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<_Utbe.1132013$za2.182999@news.easynews.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de> <d4lh0a$gei$1@panix5.panix.com> <1114526261.451117.92880@g14g2000cwa.googlegroups.com> <_Utbe.1132013$za2.182999@news.easynews.com>`

```
Bill,

the display at nnnn is performed in the error handling routine ---
followed by the ACCEPT to a specific field in the screen-name ---
it has nothing to do with display screen-name, and it is compatible
with three of my cobol compilers (Micro Soft, Micro Focus and
fujitsu), I think it should work just fine with Compaq Cobol as well.

Regards, Kellie.
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

- **From:** "Don Braffitt" <don.braffitt@hp.com>
- **Date:** 2005-05-02T14:59:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1115071151.175769.135600@z14g2000cwz.googlegroups.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com> <d4llkc.2pk.2@ahr.rsli.de>`

```
> Unfortunately there seems to be no CURSOR IS clause in CompaqCobol -
> at least the documentation doesn't mention it.

CURSOR IS is supported in HP COBOL (formerly Compaq COBOL) V2.8 on
OpenVMS Alpha and OpenVMS I64.

The details are in the Jan-2005 doc update

http://h71000.www7.hp.com/doc/82final/6296/6296pro_012.html#index_x_184

If you find any inconsistencies in the Jan-2005 doc update, contact
the doc group

http://h71000.www7.hp.com/doc/contactus.html

- Don Braffitt
  project leader, HP COBOL, SORT32, Hypersort for OpenVMS, Tru64 UNIX
```

##### ↳ ↳ Re: CompaqCobol (VMS)

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T16:33:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lqg2.ls.1@ahr.rsli.de>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com>`

```
Hi,

thank you very much, that was it. I didn't find that statement while
searching the language guide, but I was wrong and obviously unable to
find it.

Volker

"Richard Maher" <maher_rj@hotspamnotmail.com> schrieb im Newsbeitrag
news:d4l703$pb5$1@nwrdmz01.dmz.ncs.ea.ibs-infra.bt.com...
> Hi,
>
…[8 more quoted lines elided]…
> > processed in the PROCEDURE DIVISION by "DISPLAY SCREEN-1" and by
"ACCEPT
> > SCREEN-1".
> >
> > After processing the operator's input, the program needs to reject
> > invalid entries. So I loop back to the DISPLAY and ACCEPT of the
screen,
> > providing an error message explaining what value is inacceptable.
> >
…[8 more quoted lines elided]…
>
```

#### ↳ Re: CompaqCobol (VMS)

- **From:** docdwarf@panix.com
- **Date:** 2005-04-26T07:34:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4l8ve$d7e$1@panix5.panix.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de>`

```
In article <d4l7c0.1j8.1@ahr.rsli.de>,
Volker N. Englisch <englisch.ahr@gmx.de> wrote:

[snip]

>Is there any (easy) way to place the cursor in the field where the
>inappropriate value was entered?

Maybe.  Please post some of the code you have now that is failing to do 
this.

DD
kk
```

##### ↳ ↳ Re: CompaqCobol (VMS)

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T15:07:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4llkc.2pk.1@ahr.rsli.de>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l8ve$d7e$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> Volker N. Englisch <englisch.ahr@gmx.de> wrote:
>
…[4 more quoted lines elided]…
> do this.

Here comes an entire test code. When the user enters something in the
NAME field, but leaves the CITY field empty, the message shows the
mistake, but the cursor is again placed in the NAME field. I'd like the
cursor to be in the (erroneous) CITY field.

Please pardon the upper case only, the terminal I used recently for
entering the code was a very ancient one :-)

Volker

       IDENTIFICATION DIVISION.
       PROGRAM-ID.      T1.
       AUTHOR.          EH41.
       DATE-WRITTEN.    26-APR-2005.
       DATE-COMPILED.
       SECURITY.        EDP.
      *
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77  W-OK                        PIC X(01).
       77  W-MESSAGE                   PIC X(79).
       01  W-DAT-NAME                  PIC X(30).
       01  W-DAT-CITY                  PIC X(30).
      *
       SCREEN SECTION.
       01  SCREEN-1 BLANK SCREEN.
           03 FILLER  LINE 03 COLUMN 01 PIC X(79) FROM W-MESSAGE.
           03 FILLER  LINE 10 COLUMN 01 VALUE "NAME:".
           03 FILLER  LINE 12 COLUMN 01 VALUE "CITY:".
           03 S1-NAME LINE 10 COLUMN 07 PIC X(30) USING W-DAT-NAME
                                        HIGHLIGHT UNDERLINE AUTO.
           03 S1-CITY LINE 12 COLUMN 07 PIC X(30) USING W-DAT-CITY
                                        HIGHLIGHT UNDERLINE AUTO.
      *
       PROCEDURE DIVISION.
       T1-1000.
           MOVE SPACES TO W-MESSAGE.
           MOVE SPACES TO W-DAT-NAME.
           MOVE SPACES TO W-DAT-CITY.
       T1-1100.
           MOVE "J" TO W-OK.
           DISPLAY SCREEN-1.
           ACCEPT  SCREEN-1.
           MOVE SPACES TO W-MESSAGE.
           IF W-DAT-NAME EQUAL SPACES THEN
                MOVE "NAME MUST NOT BE BLANK" TO W-MESSAGE
                MOVE "N" TO W-OK
           END-IF.
           IF W-OK EQUAL "J" THEN
             IF W-DAT-CITY EQUAL SPACES THEN
                MOVE "CITY MUST NOT BE BLANK" TO W-MESSAGE
                MOVE "N" TO W-OK
             END-IF
           END-IF.
           IF W-OK EQUAL "N" THEN GO TO T1-1100.
           STOP RUN.
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

- **From:** docdwarf@panix.com
- **Date:** 2005-04-26T09:48:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lgqh$mi1$1@panix5.panix.com>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l8ve$d7e$1@panix5.panix.com> <d4llkc.2pk.1@ahr.rsli.de>`

```
In article <d4llkc.2pk.1@ahr.rsli.de>,
Volker N. Englisch <englisch.ahr@gmx.de> wrote:
>docdwarf@panix.com wrote:
>> Volker N. Englisch <englisch.ahr@gmx.de> wrote:
…[7 more quoted lines elided]…
>Here comes an entire test code.

Hmmmmm... smells like homework to me.

>When the user enters something in the
>NAME field, but leaves the CITY field empty, the message shows the
>mistake, but the cursor is again placed in the NAME field. I'd like the
>cursor to be in the (erroneous) CITY field.

I'll take a guess and say the difficulty is in ACCEPTing the entire screen 
again here:

[snip]

>       T1-1100.
>           MOVE "J" TO W-OK.
>           DISPLAY SCREEN-1.
>           ACCEPT  SCREEN-1.

... instead of addressing the field you need.

DD
```

###### ↳ ↳ ↳ Re: CompaqCobol (VMS)

_(reply depth: 4)_

- **From:** "Volker N. Englisch" <englisch.ahr@gmx.de>
- **Date:** 2005-04-26T16:23:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4lq07.nc.1@ahr.rsli.de>`
- **References:** `<d4l7c0.1j8.1@ahr.rsli.de> <d4l8ve$d7e$1@panix5.panix.com> <d4llkc.2pk.1@ahr.rsli.de> <d4lgqh$mi1$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> Volker N. Englisch <englisch.ahr@gmx.de> wrote:
>>docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
> Hmmmmm... smells like homework to me.

No, it isn't. That was about 30 years ago :-)

> >When the user enters something in the
> >NAME field, but leaves the CITY field empty, the message shows the
> >mistake, but the cursor is again placed in the NAME field. I'd like
the
> >cursor to be in the (erroneous) CITY field.
>
> I'll take a guess and say the difficulty is in ACCEPTing the entire
screen
> again here:
>
> ... instead of addressing the field you need.

Thanks, I will check that out.

Volker
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
