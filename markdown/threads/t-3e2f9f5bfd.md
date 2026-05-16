[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL access use of MS Common Dialog

_5 messages · 3 participants · 2001-02_

---

### PowerCOBOL access use of MS Common Dialog

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-02-02T04:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010201230021.21405.00001899@nso-mj.aol.com>`

```
I am looking for a sample PowerCOBOL project that makes use of 
the MS Common Dialog control for File Open/Save processing,
Font selection, and Printer Control.
This is not a homework assignment.  I just haven't spent the time with
the GUI side of what FujiCOBOL has to offer.  If there is a site other 
than the adtools.com web-site that I might be able to peruse, please 
point me in that direction.
Thanks to all for your time and assistance.
```

#### ↳ Re: PowerCOBOL access use of MS Common Dialog

- **From:** alain.reymond-nospam@ceia.com (Alain Reymond)
- **Date:** 2001-02-02T10:29:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a7a8bba.1155151@news.skynet.be>`
- **References:** `<20010201230021.21405.00001899@nso-mj.aol.com>`

```
Have a look at the 'powercobol common dialog 6' thread in this
newsgroup. This was a few days ago and we discussed this problem.

Here is part of an example :

Thank you for your indications. I immediately discovered what you
explain in your second paragraph. I am unable to control if the user
pressed OK or Cancel except using the return-code status.

First activate the CancelError property. 
Then, call the common dialog and immediately after, control the
return-code status. If the user selected Ok, the return-code value is
0, if he selected Cancel, the return-code is not set to 0.

The only problem is that you first receive a warning message :
"CommonDialog. Cancel was selected."
Just press Ok and ignore the message.

It seems to work. Hereunder is a example:

 01  ReturnValue         PIC S9(4) COMP-5.
 01  DisplayReturnValue1  pic +9999999999.
 01  DisplayReturnValue2  pic +9999999999.
 01  STYL    PIC S9(9) COMP-5.
 01  M-TITLE PIC X(15) VALUE "Message".
 01  RET     PIC S9(9) COMP-5.
 01  str     pic x(80).
 PROCEDURE       DIVISION.

     COMPUTE STYL = POW-DMOK + POW-DMNOICON
     
     move POW-True to "CancelError" of CommonDialog1
     INVOKE CommonDialog1 "ShowOpen"
     move return-code to DisplayReturnValue2
     move "CancelError" of CommonDialog1 to DisplayReturnValue1
     string 
     	"CancelError : "
     	DisplayReturnValue1
     	" return-code : "
     	DisplayReturnValue2
     	delimited by size
     	into str
     end-string
     INVOKE POW-SELF "DisplayMessage"
         USING str M-TITLE STYL
         RETURNING RET


>I am looking for a sample PowerCOBOL project that makes use of 
>the MS Common Dialog control for File Open/Save processing,
…[5 more quoted lines elided]…
>Thanks to all for your time and assistance.
```

##### ↳ ↳ Re: PowerCOBOL access use of MS Common Dialog

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-02-02T16:37:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010202113736.06978.00001413@nso-fd.aol.com>`
- **References:** `<3a7a8bba.1155151@news.skynet.be>`

```
In article <3a7a8bba.1155151@news.skynet.be>, alain.reymond-nospam@ceia.com
(Alain Reymond) writes:

>
>Have a look at the 'powercobol common dialog 6' thread in this
>newsgroup. This was a few days ago and we discussed this problem.
>

Thanks for the reminder.  I just went back in my archive and found the
very thread.  In fact I had responded there in a very general form as
I personally have never worked with this control in any COBOL program.

I would be interested to see a sample/shell/ripped-down program that 
at least points me to the syntax for calling the control to open a file/save a
file
and do the print thing.   I am in a search mode for a co-worker who has
been assigned the 'opportunity' to explore the GUI side of the Fujitsu 
COBOL Software suite. 

My current focus is entirely mainframe platform migration from one 
mainframe environment to another (with conversion from '74 to '85 syntax).
Our efforts are further complicated by the fact that we have written 
a large volume of code using vender specific extensions to the language 
that do not have equivalent syntax on the target environment.

Apologies for taking the short route to finding solutions here and
thanks for the response.
```

###### ↳ ↳ ↳ Re: PowerCOBOL access use of MS Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-03T04:17:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rDLe6.635$kz4.80309@newsread1.prod.itd.earthlink.net>`
- **References:** `<3a7a8bba.1155151@news.skynet.be> <20010202113736.06978.00001413@nso-fd.aol.com>`

```
You really don't need examples.

Once you get the control placed on the form with a name of, say,
"CommonDiaglog1", then type CommonDiaglog1 in your program, highlight
the name, and right-click. You are immediately presented with all
possible methods and properties (after clicking one more time).

But here's an example:

   MOVE POW-TRUE TO 'CancelError' of CommonDialog1.
   INVOKE COMMONDIALOG1 "ShowOpen"
   MOVE "FileName" OF commondialog1 TO FILEID.
   MOVE 'CancelError' OF COMMONDIALOG1 TO RETURN-VALUE.
```

###### ↳ ↳ ↳ Re: PowerCOBOL access use of MS Common Dialog

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-02-03T17:58:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010203125819.27298.00001422@nso-fq.aol.com>`
- **References:** `<rDLe6.635$kz4.80309@newsread1.prod.itd.earthlink.net>`

```
In article <rDLe6.635$kz4.80309@newsread1.prod.itd.earthlink.net>, "Jerry P"
<jerryp@bisusa.com> writes:

>
>Once you get the control placed on the form with a name of, say,
…[3 more quoted lines elided]…
>

This is exactly the kind of information that I am looking for.
Again, not having been thru the PowerCOBOL tutorial or Getting Started
Guide; I have no idea of how this stuff works.
I am merely seeking to gather information to pass along to a co-worker
who is actually charged with the task of discovery.

Thanks for your help.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
