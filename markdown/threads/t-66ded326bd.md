[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting dates with COBOL functions

_5 messages · 5 participants · 2003-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Converting dates with COBOL functions

- **From:** Alexander Meins <un.cr.281202@blue-seal.com>
- **Date:** 2003-01-21T19:41:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1401740.YLZbmJ6qnC@blue-seal.com>`

```
Hello,

I need to convert a PIC 9(8) date field YYYYMMDD into something that
I can use in an SQL-statement, like DD.MM.YYYY. I know that I can redefine 
this field and move the day, month and year to a new field seperately. But 
I thought that one of the "new" functions on COBOL (z/os) could do that 
more elegantly (like INTEGER-OF-DATE etc.).

But none of the functions I looked at seem to work for this.

Is there a function to do this?

A.
```

#### ↳ Re: Converting dates with COBOL functions

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-21T16:33:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sd6dnRTIfuDfVrCjXTWcjA@giganews.com>`
- **References:** `<1401740.YLZbmJ6qnC@blue-seal.com>`

```

"Alexander Meins" <un.cr.281202@blue-seal.com> wrote in message
news:1401740.YLZbmJ6qnC@blue-seal.com...
> Hello,
>
…[8 more quoted lines elided]…
> Is there a function to do this?

Uh, no. But it's one line of code, so why bother with a function?
```

##### ↳ ↳ Re: Converting dates with COBOL functions

- **From:** "Jaap Treur" <j.j.treur@wanadoo.nl>
- **Date:** 2003-01-22T11:21:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_8vX9.26949$g9.281077@pollux.casema.net>`
- **References:** `<1401740.YLZbmJ6qnC@blue-seal.com> <sd6dnRTIfuDfVrCjXTWcjA@giganews.com>`

```
The most simple way is a STRING - statement...

"JerryMouse" <nospam@bisusa.com> schreef in bericht
news:sd6dnRTIfuDfVrCjXTWcjA@giganews.com...
>
> "Alexander Meins" <un.cr.281202@blue-seal.com> wrote in message
…[4 more quoted lines elided]…
> > I can use in an SQL-statement, like DD.MM.YYYY. I know that I can
redefine
> > this field and move the day, month and year to a new field seperately.
But
> > I thought that one of the "new" functions on COBOL (z/os) could do that
> > more elegantly (like INTEGER-OF-DATE etc.).
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Converting dates with COBOL functions

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2003-01-25T10:34:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tem43v4fdqmqll307vm47gnihgapc6ercn@4ax.com>`
- **References:** `<1401740.YLZbmJ6qnC@blue-seal.com>`

```
On Tue, 21 Jan 2003 19:41:35 +0100, Alexander Meins
<un.cr.281202@blue-seal.com> wrote:

>Hello,
>
…[10 more quoted lines elided]…
>A.

Why use a function, when a one line instruction can do it for you.
IMO we have a legitimate case for using MOVE CORRESPONDING here
      
      
      
      
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      If things appear to be going well, you obviously have overlooked something.
      
        (Another Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

##### ↳ ↳ Re: Converting dates with COBOL functions

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-25T07:51:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v351edo4pr4q79@corp.supernews.com>`
- **References:** `<1401740.YLZbmJ6qnC@blue-seal.com> <tem43v4fdqmqll307vm47gnihgapc6ercn@4ax.com>`

```

Volker Bandke <vbandke@bsp-gmbh.com> wrote in message
news:tem43v4fdqmqll307vm47gnihgapc6ercn@4ax.com...
> On Tue, 21 Jan 2003 19:41:35 +0100, Alexander Meins
> <un.cr.281202@blue-seal.com> wrote:
…[4 more quoted lines elided]…
> >I can use in an SQL-statement, like DD.MM.YYYY. I know that I can
redefine
> >this field and move the day, month and year to a new field seperately.
But
> >I thought that one of the "new" functions on COBOL (z/os) could do that
> >more elegantly (like INTEGER-OF-DATE etc.).
…[8 more quoted lines elided]…
> IMO we have a legitimate case for using MOVE CORRESPONDING here

The new FUNCTION LOCALE-DATE requires only one line
in the procedure division. No redefinitions in the data division.
One entry in SPECIAL-NAMES, I think. I don't know if it is available.

Why? International portablility.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
