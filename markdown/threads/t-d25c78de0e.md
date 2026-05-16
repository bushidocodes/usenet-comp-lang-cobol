[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ascii symbols for Windows

_9 messages · 4 participants · 1999-11_

---

### Ascii symbols for Windows

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38224B65.280B2617@home.com>`

```
Does anybody know if there is a table which you can use to 'translate'
ascii symbols to the Windows GUI equivalent, e.g :-

	characters for cents, degree symbol (temperatures), or
	pick up the British pound sign in N. America, etc...

I know for instance that if I use tab x'09' it will show up as a black
blob, if I don't hide/position it; So assume Windows must be doing some
sort of equivalence. ( x"0d0a' or x'00' function as you would expect
them to). 

Jimmy, Calgary AB
```

#### ↳ Re: Ascii symbols for Windows

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vttcb$hd1$1@news.cerf.net>`
- **References:** `<38224B65.280B2617@home.com>`

```
James J. Gavan wrote in message <38224B65.280B2617@home.com>...
>Does anybody know if there is a table which you can use to 'translate'
>ascii symbols to the Windows GUI equivalent, e.g :-

Windows has two functions for this;

    OemToAnsi
and
    AnsiToOem

Which both take two null terminated character strings as arguments.

You have twin functions that works on buffers as well.

No magic at all.

Cheesle
```

#### ↳ Re: Ascii symbols for Windows

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822EA2A.23C62C47@NOSPAMhome.com>`
- **References:** `<38224B65.280B2617@home.com>`

```
James J. Gavan wrote:
> 
> Does anybody know if there is a table which you can use to 'translate'
…[10 more quoted lines elided]…
> Jimmy, Calgary AB

Windows can change.  I have a couple of web pages of chararacters on my
wall, but those pages are now gone from the web.  Just a quick search
found http://www.epsb.edmonton.ab.ca/schools/ottewell/chart.htm which
gives them in HTML format - in dos editors you can usually do ALT-171
for ï¿½.

I find that I like to spell coï¿½rdinate the way I was taught.  So I went
to a Windows editor, used the character mapping facility to create the
letter I wanted, and saved the word in a file.  When I was writing this
message, I opened that file, copied the word, and pasted it in this
message.

Another thing I do is use a hex editor to create all possible characters
(ASCII or EBCDIC) in a file.  A little experimenting will show me which
characters will print, and how they show in different printers.
```

#### ↳ Re: Ascii symbols for Windows

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38228370.27942514@news1.attglobal.net>`
- **References:** `<38224B65.280B2617@home.com>`

```
On Fri, 05 Nov 1999 03:05:07 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Does anybody know if there is a table which you can use to 'translate'
>ascii symbols to the Windows GUI equivalent, e.g :-
>

Sp2 can do it. <G>
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Ascii symbols for Windows

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vv1qg$2us$1@news.cerf.net>`
- **References:** `<38224B65.280B2617@home.com> <38228370.27942514@news1.attglobal.net>`

```
Thane Hubbell wrote in message <38228370.27942514@news1.attglobal.net>...
>Sp2 can do it. <G>

Sp2 replaces the ui, I believe James were looking for a utility to transfer
strings, and for that case AnsiToOem / OemToAnsi, or excuse me, it should be
CharToOem and OemToChar (oldtimer) is the appropriate tool and easily
accessible through the user32.dll, which all windows installations has.

No need for extras.

Cheesle
```

##### ↳ ↳ Re: Ascii symbols for Windows

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38249B90.25CE1386@home.com>`
- **References:** `<38224B65.280B2617@home.com> <38228370.27942514@news1.attglobal.net>`

```


Thane Hubbell wrote:
> 
> On Fri, 05 Nov 1999 03:05:07 GMT, "James J. Gavan" <jjgavan@home.com>
…[6 more quoted lines elided]…
> Sp2 can do it. <G>

Thane, 

Now let me correct your message :-

Sp2 can do it, so also should any COBOL compiler that provides GUI
tools. <G>

Thanks Howard and Cheesle.
 
-  as Cheesle suggests, CharToOem and OemToChar - but it would be nice
to have a pointer in the on-line to these features. Same goes for me
wanting to handshake with a TextEditor - why would I look under
'CreateProcess", the term is meaningless in a business sense.

- Howard - My! So there is something interesting happening up in
Edmonton (http://www.epsb.edmonton.ab.ca/schools/ottewell/chart.htm),
other than those guys/gals waffling in the Alberta Provincial
Legislature.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Ascii symbols for Windows

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804mql$oph$1@news.cerf.net>`
- **References:** `<38224B65.280B2617@home.com> <38228370.27942514@news1.attglobal.net> <38249B90.25CE1386@home.com>`

```
James J. Gavan wrote in message <38249B90.25CE1386@home.com>...
>-  as Cheesle suggests, CharToOem and OemToChar - but it would be nice
>to have a pointer in the on-line to these features. Same goes for me
>wanting to handshake with a TextEditor - why would I look under
>'CreateProcess", the term is meaningless in a business sense.

Eh, Jimmy, I got lost here. What do you mean by saying:

    "But it would be nice to have a pointer in the on-line to these
features"

Could it be more online than being installed on any Windows computer?

What is "Handshake with a TextEditor"

Have I lost something?

 Cheesle
```

###### ↳ ↳ ↳ Re: Ascii symbols for Windows

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3827A9EB.66EC56D@home.com>`
- **References:** `<38224B65.280B2617@home.com> <38228370.27942514@news1.attglobal.net> <38249B90.25CE1386@home.com> <804mql$oph$1@news.cerf.net>`

```


Cheesle wrote:
> 
> James J. Gavan wrote in message <38249B90.25CE1386@home.com>...
…[5 more quoted lines elided]…
> Eh, Jimmy, I got lost here. What do you mean by saying:

Ok Cheesle - the above was the shorthand version; now the long-hand :-

I'm designing initially, then programming. So I convert data files from
RM/COBOL to NetExpress. Where possible I'm even generating new codes
using Dictionaries. When finished I give user a message box. 'Files
converted, see error-listing-X (if applicable) and ascii-delimited files
a,b,c,d,e, etc..' He presses OK and I STOP RUN. So he has to get to my
files through Explorer.

Then I pause; hey, I could automate this better. I'll generate the files
above but having finished, I'll come up with a dialog which will let him
view the ascii files, error files and also allow him to add new records
to a Description File which will clean-up the error-files when he
re-runs. (This without exiting the transfer process).

Now I go to the on-line help looking for a likely source - bring up an
editor, call an editor, link to another package, use OLE - nah! it wants
me to hard-code to the Registry, (and I want to use Notepad/Word to test
it, and he will be using his favourite editor, the pathname being held
in a default file). I look and look, for a suitable 'English
expression'. I give up and ask Merant through Answerlab - use
'CreateProcess' comes back the answer - who the hell would associate my
'English' need with a funky Windows word like 'CreateProcess'.

I seem to recall that in a past life, one WMK, confessed to Pete
Dashwood as having written manuals. Similarly the on-line help is
written by tech-writers who are too close to COBOL. They should be
written by tech-writers, perhaps on a contractual basis to the compiler
vendors, who haven't a clue what COBOL is about. (I've made this
recommendation to Merant, resulting from a questionnaire they sent out).
There's a big difference between programmers working for compiler
vendors, and us developers at the other end of the stick.

This business of vendor programmer v. developer programmer; following is
my favourite from Class EntryField :--

EntryField Methods : autoswipe
Switch auto swipe on or off depending on the boolean parameter. 
Using Parameters
lnkAutoSwipeState PIC 99 COMP-5 
-------------------------------------
EntryField Method IsAutoswipe
Return auto swipe state. 
Returning Parameter
lnkAutoSwipeState PIC 99 COMP-5 
--------------------------------------

Very informative isn't it ? The source of the above - comment statements
made by the vendor programmer in the source of Class entryfield.cbl. And
as I recall, I didn't find anything in the Microsoft SDK about 'autoing'
or 'swiping'. The vendor programmer knows exactly what it means. Above
is contained in Class Book which shows hierarchies and methods for each
class, but no other reference in on-line help. Now, if I install Dialog
System, which is not default installation, and I don't use it, there is
quite a bit about autoswipe. Basically I could fill an entry field with
a prompt "yyyy/mm/dd". 

Ok - so you are going to say I've got to get to know Windows (or the
SDK). No - if I am going to become an 'expert' let it be in COBOL - I'll
look at the Windows stuff as I find a need for it.

I hope you aren't lost now <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Ascii symbols for Windows

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<808bf4$7t6$1@news.cerf.net>`
- **References:** `<38224B65.280B2617@home.com> <38228370.27942514@news1.attglobal.net> <38249B90.25CE1386@home.com> <804mql$oph$1@news.cerf.net> <3827A9EB.66EC56D@home.com>`

```
James J. Gavan wrote in message <3827A9EB.66EC56D@home.com>...
>Ok - so you are going to say I've got to get to know Windows (or the
>SDK). No - if I am going to become an 'expert' let it be in COBOL - I'll
>look at the Windows stuff as I find a need for it.

Not necessarily, but for certain parts it is definitely a benefit.

>I hope you aren't lost now <G>

Well, I wouldn't claim to be an expert of your problems though :-)

But, you got the answers you needed or...

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
