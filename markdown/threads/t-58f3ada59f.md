[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VB file MVS<-->UNIX

_9 messages · 5 participants · 2001-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### VB file MVS<-->UNIX

- **From:** k1-tsutsumi@nri.co.jp (K.Tsutsumi)
- **Date:** 2001-09-20T05:23:10-07:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bfed4ca2.0109200423.25206b1e@posting.google.com>`

```
I'm now in a project which transfer mainframe(Hitachi mvs(vos/3)) 
cobol system to unix(UP-UX11) hitachi cobol environment.
I have a difficulty about variable block(VB) file conversion.

 Unix cobol environment needs RDW(record descriptor words) to 
handle variable block file.  But when the file is transfered 
via FTP from mainframe to unix, RDW is dropped. 
 So they need another transfer way which keep RDW during 
transfer or convert a data before transfer to include RDW 
within application data, and rebuild it after transfer. Same 
problem exist about from unix to mainframe.

 Now I know the way to convert a data, and rebuild it. But that 
way need a program for each different format file. So I want 
common way to transfer VB data. Does anyone know more convenient
way?  And what is the typical way to transfer?
```

#### ↳ Re: VB file MVS<-->UNIX

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-09-20T15:52:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010920115207.04239.00002827@nso-co.aol.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com>`

```
In article <bfed4ca2.0109200423.25206b1e@posting.google.com>,
k1-tsutsumi@nri.co.jp (K.Tsutsumi) writes:

> Unix cobol environment needs RDW(record descriptor words) to 
>handle variable block file.  But when the file is transfered 
…[5 more quoted lines elided]…
>

Does the RDW get stripped when doing a BINARY transfer?
I would think that the best thing to do is flatten out the file to the same 
length across the whole file and append the original RDW to 
each record before the FTP process.   Then on the receiving side,
rebuild the Variable file from the Fixed file.   This is because
I have found that some PC-ish systems wrap the RDW around 
each record to enable read backwards as well as read forwards.

The BINARY option is not such a good thing since you are working between an
EBCDIC and ASCII platform.   You would have to handle EBCDIC/ASCII
translations of your Display formatted fields and retain the original values 
of the Packed/Binary/Hex fields.
```

##### ↳ ↳ Re: VB file MVS<-->UNIX

- **From:** k1-tsutsumi@nri.co.jp (K.Tsutsumi)
- **Date:** 2001-09-20T22:01:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfed4ca2.0109202101.328e640a@posting.google.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com>`

```
sff5ky@aol.comxxx123 (Sff5ky) wrote in message news:<20010920115207.04239.00002827@nso-co.aol.com>...
 
> Does the RDW get stripped when doing a BINARY transfer?

Yes, it's stripped.

> I would think that the best thing to do is flatten out the file to the same 
> length across the whole file and append the original RDW to 
> each record before the FTP process.   Then on the receiving side,
> rebuild the Variable file from the Fixed file.   

That's just the way we are trying. Anyone know the utility 
that work like this?

> The BINARY option is not such a good thing since you are working between an
> EBCDIC and ASCII platform.   You would have to handle EBCDIC/ASCII
> translations of your Display formatted fields and retain the original values 
> of the Packed/Binary/Hex fields.

But if transfered by ASCII mode, does FTP know the field is EBCDIC 
or Packed or ...? Does FTP change all fields of data as it thinks
fields are all EBCDIC character?
So FTP must be with binary option, and change fields before or after
tranfer. Is this right?
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-21T00:39:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9oejpf$6ti$1@slb6.atl.mindspring.net>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com>`

```
With the Micro Focus "mainframe development targeted products", there are
several utilities that are provided - and that I think you will need to
"emulate" if you are in another environment.  Before listing them, there is
one question that I would ask you - Do you have any MVS programs that do
negative subscripting to get at the RDW itself?  If so, you need to have a
Unix compiler that will "emulate" this environment for you (Again Micro
Focus has such an option - I don't know about the other PC products).

Things that you will need:

1) Two programs that will add and delete RDW fields when
uploading/downloading (See MF VRECGEN)

2) A program that will do "intelligent" ASCII/EBCDIC conversion (change PIC
X fields, fix sign-nibbles if needed for numeric Packed/Display fields, NOT
change binary fields)  This routine will need to handle multiple record
descriptions under the same FD. (See Micro Focus WFL)

3) A program that will correctly handle mainframe VSAM (or indexed) files -
especially those with multiple alternate indices

  ***

This is not (and is NOT intended to be) an "ad" for Micro Focus solutions to
these problems.  (In truth and fact, MF provides these for Windows
products - not for Unix products).  It is intended to point you to the
direction that you could look for the specifications for ALL the various
tools you need for this type of "conversion".

A couple other alternatives:

A) For each file that you want to transfer, create a "quick and dirty"
program that reads the file as defined and creates a new file with
 - RDW as a separate field
 - all numeric data as USAGE DISPLAY with SIGN IS SEPARATE
 - then look at the CODE-SET STANDARD-1 or EBCDIC (if you have it) syntax
 ... then you just transfer that with normal ASCII/EBCDIC conversion and
"reconstitute" it on the other platform

B) Look at finding a tool that does "remote access" for data files, so you
can leave the files on one platform - but use them on multiple platforms.

  ***

P.S.  I just noticed that your email ID has "jp".  Do be aware that there
are ALSO issues related to DBCS or "national" character sets being different
on different platforms.  Shift-JIS, Unicode, ISO-10646, IBM DBCS, etc.   I
know of NO tool that "correctly" converts such data.

P.P.S.  Back to the original "RDW question" - if your COBOL compiler (on
both platforms) supports the
   RECORD VARYING IN SIZE
        syntax as well as
  RECORD CONTAINS

then switching to RECORD VARYING IN SIZE *may* make it unnecessary to worry
about the RDW at all.
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

_(reply depth: 4)_

- **From:** k1-tsutsumi@nri.co.jp (K.Tsutsumi)
- **Date:** 2001-09-21T06:57:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfed4ca2.0109210557.14bc9692@posting.google.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com> <9oejpf$6ti$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9oejpf$6ti$1@slb6.atl.mindspring.net>...

> Before listing them, there is
> one question that I would ask you - Do you have any MVS programs that do
> negative subscripting to get at the RDW itself?  If so, you need to have a
> Unix compiler that will "emulate" this environment for you (Again Micro
> Focus has such an option - I don't know about the other PC products).

You mean a program which use the RDW within it?
I think I don't have that program.

> A couple other alternatives:
> 
…[6 more quoted lines elided]…
> "reconstitute" it on the other platform

I didn't know above way. I refered manual, and understand the way.

Anyway, thank you for reply.
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-09-21T10:41:48+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tlrlqtkjohsehaomdlkn3defrivi24r3e1@4ax.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com>`

```
On 20 Sep 2001 22:01:55 -0700 k1-tsutsumi@nri.co.jp (K.Tsutsumi) wrote:

:>sff5ky@aol.comxxx123 (Sff5ky) wrote in message news:<20010920115207.04239.00002827@nso-co.aol.com>...
 
:>> Does the RDW get stripped when doing a BINARY transfer?

:>Yes, it's stripped.

:>> I would think that the best thing to do is flatten out the file to the same 
:>> length across the whole file and append the original RDW to 
:>> each record before the FTP process.   Then on the receiving side,
:>> rebuild the Variable file from the Fixed file.   

:>That's just the way we are trying. Anyone know the utility 
:>that work like this?

You could probably code up some IEBGENER statements.

Or, perhaps, write a COBOL program to do it.

:>> The BINARY option is not such a good thing since you are working between an
:>> EBCDIC and ASCII platform.   You would have to handle EBCDIC/ASCII
:>> translations of your Display formatted fields and retain the original values 
:>> of the Packed/Binary/Hex fields.

:>But if transfered by ASCII mode, does FTP know the field is EBCDIC 
:>or Packed or ...? Does FTP change all fields of data as it thinks
:>fields are all EBCDIC character?

FTP does not know. It will change all, including packed and binary fields

:>So FTP must be with binary option, and change fields before or after
:>tranfer. Is this right?

The best approach would be to write a program that will convert a non-display
fields to display and ship the result. This should not be at all difficult if
you have the record descriptions.
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

_(reply depth: 4)_

- **From:** k1-tsutsumi@nri.co.jp (K.Tsutsumi)
- **Date:** 2001-09-26T04:05:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfed4ca2.0109260305.7426b462@posting.google.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com> <tlrlqtkjohsehaomdlkn3defrivi24r3e1@4ax.com>`

```
Binyamin Dissen <postingid@dissensoftware.com> wrote in message 

> :>That's just the way we are trying. Anyone know the utility 
> :>that work like this?
> 
> You could probably code up some IEBGENER statements.

Can IEBGENER handle RDW and put it into the application data?
 
> The best approach would be to write a program that will convert a non-display
> fields to display and ship the result. This should not be at all difficult if
> you have the record descriptions.

By that way should I make a program for each different format data?
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-09-27T19:31:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t5n6rtk9ns7unqts3vp4q1mknn0hfi5qap@4ax.com>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com> <tlrlqtkjohsehaomdlkn3defrivi24r3e1@4ax.com> <bfed4ca2.0109260305.7426b462@posting.google.com>`

```
On 26 Sep 2001 04:05:55 -0700 k1-tsutsumi@nri.co.jp (K.Tsutsumi) wrote:

:>Binyamin Dissen <postingid@dissensoftware.com> wrote in message 

:>> :>That's just the way we are trying. Anyone know the utility 
:>> :>that work like this?
 
:>> You could probably code up some IEBGENER statements.

:>Can IEBGENER handle RDW and put it into the application data?

Don't think so, but it can make them fixed records.
 
:>> The best approach would be to write a program that will convert a non-display
:>> fields to display and ship the result. This should not be at all difficult if
:>> you have the record descriptions.

:>By that way should I make a program for each different format data?

Yes, as you would have to make a conversion routine for each data anyway.
```

###### ↳ ↳ ↳ Re: VB file MVS<-->UNIX

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-09-21T11:48:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YNFq7.15$T%.40532@paloalto-snr1.gtei.net>`
- **References:** `<bfed4ca2.0109200423.25206b1e@posting.google.com> <20010920115207.04239.00002827@nso-co.aol.com> <bfed4ca2.0109202101.328e640a@posting.google.com>`

```
K.Tsutsumi <k1-tsutsumi@nri.co.jp> wrote in message
news:bfed4ca2.0109202101.328e640a@posting.google.com...
> sff5ky@aol.comxxx123 (Sff5ky) wrote in message
news:<20010920115207.04239.00002827@nso-co.aol.com>...
>
>
> > The BINARY option is not such a good thing since you are working between
an
> > EBCDIC and ASCII platform.   You would have to handle EBCDIC/ASCII
> > translations of your Display formatted fields and retain the original
values
> > of the Packed/Binary/Hex fields.
>
…[4 more quoted lines elided]…
> tranfer. Is this right?

For a reasonably decent explanation of EBCDIC/ASCII and COBOL/IEEE datatypes
conversion issues, see my article at http://www.flexus.com/ebd2asc.html

You have about six different ways to do what you want to do, it's just that
once you pick a method, you'll have to follow it all the way through.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
