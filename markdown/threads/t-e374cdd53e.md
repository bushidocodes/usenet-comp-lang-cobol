[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question : Binary Format?

_10 messages · 5 participants · 1999-05_

---

### Question : Binary Format?

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ti023.6236$vM1.10850@ozemail.com.au>`

```
Hi Newsgroup,
Can anybody help me with this one? An IBM mainframe running MVS and COBOL 3
can output a COBOL file in "Ascii" or "Binary" Format as a text file
readable on an Ms DOS machine. This is done by an "emulator". Because some
of the COBOL numerical datafields are "COMP" Ascii isnt suitable, so
"Binary" was chosen. But what is the character set for "Binary"? I need to
be able to read the "Binary Format" text file and convert back to Ascii on
my Ms DOS PC system. I will read the text file in COBOL as a single Ascii
character record sequential file, convert each character, then move the data
into an indexed file with the same structure as it had on the mainframe.

Any ideas on what "binary format" would be? I asked them to look up the
manual, but no response.
Thankyou for your help
David
david@dandm.co.nz
```

#### ↳ Re: Question : Binary Format?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ia6h3$k80@sjx-ixn10.ix.netcom.com>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au>`

```
If you define all the numeric fields (on the mainframe) as USAGE DISPLAY -
SIGN IS LEADING SEPARATE - and then take the EBCDIC (not ASCII) file and
download it to a PC using EBCDIC/ASCII conversion, you will have a "totally
usable" PC file.
```

##### ↳ ↳ Re: Question : Binary Format?

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9k123.6253$vM1.10935@ozemail.com.au>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <7ia6h3$k80@sjx-ixn10.ix.netcom.com>`

```
Thanks Bill,
I can suggest this to the company with the mainframe who is distributing the
file. However I may have to take what they give me and convert it at my end.
David.

William M. Klein wrote in message <7ia6h3$k80@sjx-ixn10.ix.netcom.com>...
>If you define all the numeric fields (on the mainframe) as USAGE DISPLAY -
>SIGN IS LEADING SEPARATE - and then take the EBCDIC (not ASCII) file and
…[12 more quoted lines elided]…
>> readable on an Ms DOS machine. This is done by an "emulator". Because
some
>> of the COBOL numerical datafields are "COMP" Ascii isnt suitable, so
>> "Binary" was chosen. But what is the character set for "Binary"? I need
to
>> be able to read the "Binary Format" text file and convert back to Ascii
on
>> my Ms DOS PC system. I will read the text file in COBOL as a single Ascii
>> character record sequential file, convert each character, then move the
…[7 more quoted lines elided]…
>> david@dandm.co.nz
```

###### ↳ ↳ ↳ Re: Question : Binary Format?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3748b0b1.432000920@news1.ibm.net>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <7ia6h3$k80@sjx-ixn10.ix.netcom.com> <9k123.6253$vM1.10935@ozemail.com.au>`

```
On Mon, 24 May 1999 12:48:00 +1200, "David Mowat" <david@dandm.co.nz>
wrote:


>>> of the COBOL numerical datafields are "COMP" Ascii isnt suitable, so
>>> "Binary" was chosen. But what is the character set for "Binary"? I need
…[9 more quoted lines elided]…
>>> manual, but no response.

Since you mentioned converting to an indexed file, I suspect you have
some COBOL on the PC, would it by chance be MicroFocus?

Given the FD from the mainframe you can run it through "WFL" under
MicorFocus COBOL and create your indexed file directly from the
mainframe.
```

###### ↳ ↳ ↳ Re: Question : Binary Format?

_(reply depth: 4)_

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o5323.6282$vM1.11059@ozemail.com.au>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <7ia6h3$k80@sjx-ixn10.ix.netcom.com> <9k123.6253$vM1.10935@ozemail.com.au> <3748b0b1.432000920@news1.ibm.net>`

```
Thane Hubbell wrote in message <3748b0b1.432000920@news1.ibm.net>...
>On Mon, 24 May 1999 12:48:00 +1200, "David Mowat" <david@dandm.co.nz>
>wrote:
…[7 more quoted lines elided]…
>>>> my Ms DOS PC system. I will read the text file in COBOL as a single
Ascii
>>>> character record sequential file, convert each character, then move the
>>>data
>>>> into an indexed file with the same structure as it had on the
mainframe.
>>>>
>>>> Any ideas on what "binary format" would be? I asked them to look up the
…[7 more quoted lines elided]…
>mainframe.


Yes I have MicroFocus (Microsoft vs5.0) COBOL on the PC and the FD from the
mainframe. Is "WFL" a microfocus utility? How can I use it?
```

###### ↳ ↳ ↳ Re: Question : Binary Format?

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37493f6a.468543431@news1.ibm.net>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <7ia6h3$k80@sjx-ixn10.ix.netcom.com> <9k123.6253$vM1.10935@ozemail.com.au> <3748b0b1.432000920@news1.ibm.net> <o5323.6282$vM1.11059@ozemail.com.au>`

```
On Mon, 24 May 1999 14:47:50 +1200, "David Mowat" <david@dandm.co.nz>
wrote:

>Yes I have MicroFocus (Microsoft vs5.0) COBOL on the PC and the FD from the
>mainframe. Is "WFL" a microfocus utility? How can I use it?
>

I do not know if WFL was included with the Microsoft versoin of
MicroFocus or not.

In MF it was ALT F9 from the workbench menu.

First you need to put the FD into a program (any program) and compile
it.  Then using the .IDY created, you can "create" a format in WFL to
convert.  It's fairly self explanitory once you start the WFL.
```

###### ↳ ↳ ↳ Re: Question : Binary Format?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ic5gg$a92@dfw-ixnews12.ix.netcom.com>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <7ia6h3$k80@sjx-ixn10.ix.netcom.com> <9k123.6253$vM1.10935@ozemail.com.au> <3748b0b1.432000920@news1.ibm.net> <o5323.6282$vM1.11059@ozemail.com.au> <37493f6a.468543431@news1.ibm.net>`

```
I think that WFL was *NOT* included in the (long passed) Microsoft product.
I think it was based on the Micro Focus "Toolset" product - while WFL was
just included in the "Workbench" product. The same is true (as I recall -
but again this is from long ago) for CHARSET(EBCDIC) support (which might
provide another solution to this problem).  I think that the compiler will
accept this, but that the run-time won't handle it.
```

#### ↳ Re: Question : Binary Format?

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vJj23.2078$6y2.30554@storm.twcol.com>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au>`

```

David Mowat wrote in message ...
>Hi Newsgroup,
>Can anybody help me with this one? An IBM mainframe running MVS and COBOL 3
…[3 more quoted lines elided]…
>"Binary" was chosen. But what is the character set for "Binary"? I need to


There is no character set for BINARY. It is either ASCII or EBCDIC. These
formats can be corrupted by the transfer mode, which is ASCII or BINARy (AKA
IMAGE) under FTP. The IND$GET transfer protocol also allows for ASCII
translation, in most cases you will want this off to protect the binary data
within. In the absence of a nice utility to do it for you, a custom
translator will most likely need to be created. If it is a single record
format file this should be relatively easy.
```

##### ↳ ↳ Re: Question : Binary Format?

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Srs23.9095$vM1.14272@ozemail.com.au>`
- **References:** `<ti023.6236$vM1.10850@ozemail.com.au> <vJj23.2078$6y2.30554@storm.twcol.com>`

```
Thanks Jeff,
It is just EBCDIC!

Jeff wrote in message ...
>
>David Mowat wrote in message ...
>>Hi Newsgroup,
>>Can anybody help me with this one? An IBM mainframe running MVS and COBOL
3
>>can output a COBOL file in "Ascii" or "Binary" Format as a text file
>>readable on an Ms DOS machine. This is done by an "emulator". Because some
…[5 more quoted lines elided]…
>formats can be corrupted by the transfer mode, which is ASCII or BINARy
(AKA
>IMAGE) under FTP. The IND$GET transfer protocol also allows for ASCII
>translation, in most cases you will want this off to protect the binary
data
>within. In the absence of a nice utility to do it for you, a custom
>translator will most likely need to be created. If it is a single record
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Question : Binary Format?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990525210350.08345.00004975@ngol02.aol.com>`
- **References:** `<vJj23.2078$6y2.30554@storm.twcol.com>`

```
In article <vJj23.2078$6y2.30554@storm.twcol.com>, "Jeff" <a@a.com> writes:

>
>There is no character set for BINARY. It is either ASCII or EBCDIC. These
…[7 more quoted lines elided]…
>

Not only do yu have to be concerned with the download bringin the information
down correctly, but you also have to take into account the big-endian / little
endian loading of binary fields (left to right or right to left )

Mainframe format (AFAIK) is always least significant byte is on the rightmost
position of the field.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
