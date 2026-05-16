[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Begginer's question!!

_12 messages · 7 participants · 1998-11_

---

### Begginer's question!!

- **From:** "Filipe Martins" <Silnox@Mail.Telepac.pt>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<720066$8jb$1@duke.telepac.pt>`

```

I saw a MicroFocus Cobol File that had the following definition (printed by
Micro Focus Rebuild (/n switch) utility):

File : FSTFOAR.DAT
  Organization - Indexed
  Recording mode - Fixed
  Record length -   114
  Keys description :
  Key           Start             Length
    0:              1                +15
    1:              6                +10
                     1                 +5
As I am new to Cobol, my question is:
        How this is done in Cobol ?

Please answer me, if you can.

            Thanking you in advance
                        Filipe Martins
```

#### ↳ Re: Begginer's question!!

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nWN02.386$LY1.340@news1.atlantic.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt>`

```
       program-id. fstfoar.
       environment division.
       input-output section.
       file-control.
           select fstfoar-file
               assign to "FSTFOAR.DAT"
               organization indexed
               access dynamic
               record key primary-key
               alternate alt-key = key-field-2 key-field-1.
       data division.
       file section.
       fd fstfoar-file
           recording mode fixed.
       01 fstfoar-record.
         05 primary-key.
           10 key-field-1          pic x(5).
           10 key-field-2          pic x(10).
         05 rest-of-record         pic x(99).
       procedure division.
           open output fstfoar-file
           close fstfoar-file
           stop run
           .

File : FSTFOAR.DAT
  Organization - Indexed
  Recording mode - Fixed
  Record length -   114
  Keys description :
  Key           Start             Length
    0:              1                +15
    1:              6                +10
                    1                 +5

Filipe Martins wrote in message <720066$8jb$1@duke.telepac.pt>...
>
>I saw a MicroFocus Cobol File that had the following definition (printed by
…[18 more quoted lines elided]…
>
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

##### ↳ ↳ Re: Begginer's question!!

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3643adef.0@news1.ibm.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net>`

```

Rick Smith wrote in message ...
>       program-id. fstfoar.
>       environment division.
…[7 more quoted lines elided]…
>               alternate alt-key = key-field-2 key-field-1.

The 'alternate' clause above must be some new-fangled
extension or up-and-cumming standards feature.
Or is it just a MicroFocus feature? and since when?
Please enlighten me. Thanks.

>       data division.
>       file section.
…[25 more quoted lines elided]…
>>I saw a MicroFocus Cobol File that had the following definition (printed
by
>>Micro Focus Rebuild (/n switch) utility):
>>
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Begginer's question!!

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZkW02.1765$Tk.1712537@news2.mia.bellsouth.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
>
>Rick Smith wrote in message ...
…[14 more quoted lines elided]…
>Please enlighten me. Thanks.

It's a Micro Focus extension, *sorely* needed.  Version 1.2 of the new
standard has a similar feature:

    ALTERNATE RECORD KEY alt-key SOURCE IS key-field-2 key-field-1.

I hope they leave it in there.  READ PREVIOUS, also *sorely* needed, is
in there too.  I'm concerned they are going to take PREVIOUS out, and
to me that would trivialize INDEXED files for real database use.
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36470310.0@news1.ibm.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <ZkW02.1765$Tk.1712537@news2.mia.bellsouth.net>`

```

Judson McClendon wrote in message ...
>Leif Svalgaard wrote:
>>
…[22 more quoted lines elided]…
>I hope they leave it in there.

What would good too (and orthogonal as well) is that this would work with
any
key including the PRIMARY key.
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-VkPNdde9dDtd@Dwight_Miller.iix.com>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <ZkW02.1765$Tk.1712537@news2.mia.bellsouth.net>`

```
On Sat, 7 Nov 1998 11:40:41, "Judson McClendon" 
<judmc123@bellsouth.net> wrote:

> I hope they leave it in there.  READ PREVIOUS, also *sorely* needed, is
> in there too.  I'm concerned they are going to take PREVIOUS out, and
> to me that would trivialize INDEXED files for real database use.


The last draft I was able to obtain before they removed it from the 
site still contains the "split key" and the read previous.  I 
anticipate, however, that the split key manipulation will be an 
optional item as some indexed file access methods will not tolerate it
(ie VSAM).
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<727m02$a4p@dfw-ixnews6.ix.netcom.com>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <ZkW02.1765$Tk.1712537@news2.mia.bellsouth.net> <Jl0PnHJ5PvPd-pn2-VkPNdde9dDtd@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Sat, 7 Nov 1998 11:40:41, "Judson McClendon"
><judmc123@bellsouth.net> wrote:
…[12 more quoted lines elided]…
>

Both split key and read previous will (probably) be in the next Standard but
BOTH will probably be in the "processor dependent" list - which is a
replacement for the old "hardware dependent" list - but now basically means
it is optional.

As to "vsam doesn't support it" - I want to remind you that the COBOL
Standard has (in the past) placed requirements that implementors had to
"build to".  For example, the VS COBOL II option of "SIMVRDS" was a method
of providing variable length relative files BEFORE vsam supported it (on
MVS).
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-eRzw0sOfJkug@Dwight_Miller.iix.com>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <ZkW02.1765$Tk.1712537@news2.mia.bellsouth.net> <Jl0PnHJ5PvPd-pn2-VkPNdde9dDtd@Dwight_Miller.iix.com> <727m02$a4p@dfw-ixnews6.ix.netcom.com>`

```
On Mon, 9 Nov 1998 21:14:07, "William M. Klein" 
<wmklein@ix.netcom.com> wrote:

> As to "vsam doesn't support it" - I want to remind you that the COBOL
> Standard has (in the past) placed requirements that implementors had to
> "build to".  For example, the VS COBOL II option of "SIMVRDS" was a method
> of providing variable length relative files BEFORE vsam supported it (on
> MVS).

That's true - but the "processor" dependent area now will allow 
vendors to claim something is processor dependent in order not to 
provide support - something I know you have sounded off about before. 
 I want to call additional attention to that fact.  It defeats 
Standard COBOL.  

While I agree there WILL be some things that are TRULY - what I would 
rather call "Platform" dependent - the latitude that is allowed in 
this area should be severly limited.
```

###### ↳ ↳ ↳ Re: Begginer's question!!

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-QdvdOpf9JhX2@Dwight_Miller.iix.com>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net>`

```
On Sat, 7 Nov 1998 02:18:10, "Leif Svalgaard" <leif@ibm.net> wrote:

> 
> Rick Smith wrote in message ...
…[15 more quoted lines elided]…
> 

It's been available in MicroFocus COBOL since 2.5 and probably before.
 It varies from the new proposed standard only slightly.
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<727fu8$rc7$1@news.igs.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <Jl0PnHJ5PvPd-pn2-QdvdOpf9JhX2@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote in message ...

>> The 'alternate' clause above must be some new-fangled
>> extension or up-and-cumming standards feature.
…[5 more quoted lines elided]…
> It varies from the new proposed standard only slightly.


There is an equivalent in Fujitsu but phrased slightly differently.
I know that you know about it Thane, but perhaps others do not.

    SELECT DTRK-FILE ASSIGN TO DTRK-IDENTIFICATION
       ORGANIZATION IS INDEXED
       ACCESS IS DYNAMIC
       FILE STATUS IS DTRK-STATUS
       RECORD KEY IS DTRK-KEY
       ALTERNATE KEY IS
                                DTRK-SHOW-FLAG, DTRK-TARE-DATE
                                DTRK-IN-TIME, DTRK-KEY
       ALTERNATE RECORD KEY IS DTRK-DISPATCH-KEY
                                WITH DUPLICATES.

The main difference is that the MF version has a name
given to the key, while the Fujitsu version does not. I think
the Fujitsu method is the one in the new standard, though
I think it inferior.  It makes it a lot more awkward to use,
as the read has no name to reference ... you have to
list the components of the key.
```

###### ↳ ↳ ↳ Re: Begginer's question!!

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dDoxbdcv0LYL@Dwight_Miller.iix.com>`
- **References:** `<720066$8jb$1@duke.telepac.pt> <nWN02.386$LY1.340@news1.atlantic.net> <3643adef.0@news1.ibm.net> <Jl0PnHJ5PvPd-pn2-QdvdOpf9JhX2@Dwight_Miller.iix.com> <727fu8$rc7$1@news.igs.net>`

```
On Mon, 9 Nov 1998 19:32:15, "Donald Tees" <donald@willmack.com> 
wrote:

> The main difference is that the MF version has a name
> given to the key, while the Fujitsu version does not. I think
…[4 more quoted lines elided]…
>

The draft of the standard that I have allows you to assign a "name" to
this area, but it is done differently than MF does it.
```

#### ↳ Re: Begginer's question!!

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<721hni$ks2$1@news.igs.net>`
- **References:** `<720066$8jb$1@duke.telepac.pt>`

```
How is *what* done in Cobol?  Create the file?
Post the message? Run the rebuild utility?  See Micro Focus?

Filipe Martins wrote in message <720066$8jb$1@duke.telepac.pt>...
>
>I saw a MicroFocus Cobol File that had the following definition (printed by
…[21 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
