[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Procedure-pointer OS/390 and 0C4

_7 messages · 4 participants · 2005-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Procedure-pointer OS/390 and 0C4

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2005-02-21T08:34:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0502210834.58d69db4@posting.google.com>`

```
I have coded some lines

 
 copy-file:

 UPRO-upro-name1               procedure-pointer EXTERNAL.
 UPRO-upro-name2               procedure-pointer EXTERNAL.
 ... 
      
 Upro-Set-Pointer:

 Z-UPRO                          PIC X(8).

 ''INIT-ROUTINE  before all Calls''
                                         
 MOVE 'upro-name1'               TO       Z-UPRO
 SET  UPRO-name1                 TO ENTRY Z-UPRO
 
                                                
 MOVE 'upro-name2'               TO       Z-UPRO
 SET  UPRO-name1                 TO ENTRY Z-UPRO

 ....

 Upro Call Pointer:

 Call  UPRO-name1       using something


 I have two question. why get I  an error, if the Load-module isn't
there in the  UPRO-SET-POINTER Modul in the INIT-ROUTINE. I thought
the first time I  CALL     the UPRO-XYZ   I Link the Modul
Upro-nameXXX  and not in the   SET  command.

 The next question is, why get I an  0C4 on a customer-system , in the

          SET UPRO-NameXX    to    ENTRY Z-UPRO

 All Load-Modules are there.

 thanks 
 joerg
```

#### ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-21T10:36:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109010970.360764.212310@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<7f6b3f56.0502210834.58d69db4@posting.google.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com>`

```
> Z-UPRO                          PIC X(8).

> MOVE 'upro-name1'               TO       Z-UPRO
> MOVE 'upro-name2'               TO       Z-UPRO

How many characters are there in 'upro-name1'.  How many characters can
a PIC X(8) hold ?
```

##### ↳ ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2005-02-22T00:47:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0502220047.27be9108@posting.google.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com> <1109010970.360764.212310@o13g2000cwo.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message news:<1109010970.360764.212310@o13g2000cwo.googlegroups.com>...
> > Z-UPRO                          PIC X(8).
> 
…[4 more quoted lines elided]…
> a PIC X(8) hold ?

Upro-name1 or Upro-name2 are only  examples. The real names are
'A5POXXX' or 'C2POXXX'
```

##### ↳ ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2005-02-22T00:52:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0502220052.72a80735@posting.google.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com> <1109010970.360764.212310@o13g2000cwo.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message news:<1109010970.360764.212310@o13g2000cwo.googlegroups.com>...
> > Z-UPRO                          PIC X(8).
> 
…[4 more quoted lines elided]…
> a PIC X(8) hold ?

Upro-name1 or Upro-name2 are only  examples. The real names are
'A5POXXX' or 'C2POXXX'

On our system this program runs. It's seems a problem on a system of
our customer.
```

#### ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-02-22T22:03:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8304DF.22033622022005@knology.usenetserver.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com>`

```
In article <7f6b3f56.0502210834.58d69db4@posting.google.com>,
 Joerg.Brehe@set-software.de (j?rg brehe) wrote:

> I have coded some lines
> 
…[37 more quoted lines elided]…
>  joerg


The SET/TO ENTRY will cause an error if the module isn't available 
because the SET of a procedure pointer will try to load the module, 
initialized the runtime if necessary, create a new instance if 
reentrent, etc.

It will do everything a call would except transfer control to the first 
instruction at the entry point.

This is troublesome.  With the CALL verb, you could use ON OVERFLOW or 
ON EXCEPTION to trap a missing module.  With SET/ENTRY you cannot.

Perhaps the only way I know of to prevent the S806 is with an LE 
condition handler.

As to the SOC4 on the clients system -- well, I have no clue on that.  
It could be just about anything...
```

##### ↳ ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2005-02-23T05:25:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0502230525.5786ae12@posting.google.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com> <joe_zitzelberger-8304DF.22033622022005@knology.usenetserver.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-8304DF.22033622022005@knology.usenetserver.com>...
> In article <7f6b3f56.0502210834.58d69db4@posting.google.com>,
>  Joerg.Brehe@set-software.de (j?rg brehe) wrote:
…[58 more quoted lines elided]…
> It could be just about anything...

I have found it. There was an old modul Upro202 , which was not
compiled with the new compiler. I have delete the lines of the SET
Statement in the INIT-ROUTINE and no 0C4 occurs, then I have compiled
this modul Upro202 with the new compiler and put the SET statement
again in my source, and it works again well, no 0C4. I don't need this
modul, so i kill this old modul.

thanks for the above information. 

jï¿½rg
```

##### ↳ ↳ Re: Procedure-pointer OS/390 and 0C4

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2005-02-23T12:12:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iV2Td.8063$wi.4394@fe11.lga>`
- **In-Reply-To:** `<joe_zitzelberger-8304DF.22033622022005@knology.usenetserver.com>`
- **References:** `<7f6b3f56.0502210834.58d69db4@posting.google.com> <joe_zitzelberger-8304DF.22033622022005@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:

> In article <7f6b3f56.0502210834.58d69db4@posting.google.com>,
>  Joerg.Brehe@set-software.de (j?rg brehe) wrote:
…[61 more quoted lines elided]…
> 
If  memory serves (and it isn't that good these days),
a soc4 was known as an adder alph.

Perhaps that will help.

Warren Simmons
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
