[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF 3.2 FP Problems

_7 messages · 7 participants · 1998-01 → 1998-02_

---

### MF 3.2 FP Problems

- **From:** "wa..." <ua-author-8406840@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6albue$49v@news.inforamp.net>`

```

I am a mainframer with 15 years experience on MVS, etc., and after
early retirement am getting familiar with Micro Focus. Creating my
own sequential test files under SPFPC, I find that at run-time, my
references to locations in the input records are offset by a two-char
group that is interposed between recs, and displaces sucessive input
recs 2 posns to the right (or procedure div references 2 to the left,
if you prefer) on each read. Would someone who understands this
kindly explain it to me, and how to correct it.

Walt Woods
Toronto.
```

#### ↳ Re: MF 3.2 FP Problems

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6albue$49v@news.inforamp.net>`
- **References:** `<6albue$49v@news.inforamp.net>`

```

In you Select/Assign statement change

Organization Sequential
to
Organization Line Sequential

The PC doesn't have QSAM, so instead of RDW (Record Descriptor Words) and
other mainframe methods of telling where one record ends and the next
begins, they use CR/LF (carriage Return/Line Feed) control characters
between each record.

Alternatively, with Micro Focus COBOL, you can use the SEQUENTIAL directive
to tell the compiler what type of sequential files you have.

I hope that this helps.

P.S. Micro Focus (but not SPFPC) can create/read files without the CR/LF -
but then you won't be able to view or edit them outside your COBOL program.

Walt Woods wrote in message <6albue$4.··.@new··p.net>...
› I am a mainframer with 15 years experience on MVS, etc., and after
› early retirement am getting familiar with Micro Focus.  Creating my
…[9 more quoted lines elided]…
›
```

#### ↳ Re: MF 3.2 FP Problems

- **From:** "sff..." <ua-author-4762962@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6albue$49v@news.inforamp.net>`
- **References:** `<6albue$49v@news.inforamp.net>`

```

It is likely that you need to add a statement in the SELECT to indicate that
the
file ORGANIZATION is LINE SEQUENTIAL to have the software automatically
deal with the CR/LF characters.
```

#### ↳ Re: MF 3.2 FP Problems

- **From:** "a..." <ua-author-17084061@usenetarchives.gap>
- **Date:** 1998-01-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6albue$49v@news.inforamp.net>`
- **References:** `<6albue$49v@news.inforamp.net>`

```

In article ,
vba··.@bsp··h.com (Volker Bandke) wrote:

› On Tue, 27 Jan 1998 19:18:38, wa··.@inf··p.net (Walt Woods) wrote:
› 
…[13 more quoted lines elided]…
› 

What you have to do in SPF/PC to get a PC file that looks like a
mainframe FB file is define a new file profile in SPF/PC that
specifies RECORD FORMAT of L (length delimited) and a max record
length of whatever you want for a logical record length. Files you
create using such a profile will have no CR-LF between records.

>From the SPF/PC Primary option panel,select
0 SPF/PC PARMS, then 7 PROFILES. Copy an existing profile, give it a
new name, then edit its record format and max record length. When you
go to create a new file, either use the profile name as the file
extension or enter it on the profile line when when you edit the file.
```

#### ↳ Re: MF 3.2 FP Problems

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6albue$49v@news.inforamp.net>`
- **References:** `<6albue$49v@news.inforamp.net>`

```

On 27 Jan 1998 19:18:38 GMT, wa··.@inf··p.net (Walt Woods) wrote:

› I am a mainframer with 15 years experience on MVS, etc., and after
› early retirement am getting familiar with Micro Focus.  Creating my
…[5 more quoted lines elided]…
› kindly explain it to me, and how to correct it.  


There are subtlies with MF COBOL and sequential records. If you
specify LINE ADVANCING or LINE SEQUENTIAL in your select, then
anything with a value of x"00" - x"20" is ignored, and not returned on
a read. A HEX view of the file may show the data, but reading does
not return it. I suggest you specify RECORD SEQUENTIAL in your
select, and either forget, or manually add the CR LF (X"0d0a") at the
end of every record.
```

##### ↳ ↳ Re: MF 3.2 FP Problems

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0fd9bbe6d-p5@usenetarchives.gap>`
- **References:** `<6albue$49v@news.inforamp.net> <gap-e0fd9bbe6d-p5@usenetarchives.gap>`

```

Thane Hubbell wrote in article
<34d··.@new··m.net>...
› On 27 Jan 1998 19:18:38 GMT, wa··.@inf··p.net (Walt Woods) wrote:
› 
…[19 more quoted lines elided]…
› 

Amazing. For years, I have just been adding two bytes, that
I call The Microfocus Filler. Maybe, like Doc suggests, I should
start taking the bus.

Ross

http://www.geocities.com/Hollywood/Set/7185/
```

##### ↳ ↳ Re: MF 3.2 FP Problems

- **From:** "a..." <ua-author-17074539@usenetarchives.gap>
- **Date:** 1998-02-04T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0fd9bbe6d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0fd9bbe6d-p5@usenetarchives.gap>`
- **References:** `<6albue$49v@news.inforamp.net> <gap-e0fd9bbe6d-p5@usenetarchives.gap>`

```

On Wed, 04 Feb 1998 03:54:57 GMT, red··.@i··.net (Thane Hubbell)
wrote:

› On 27 Jan 1998 19:18:38 GMT, wa··.@inf··p.net (Walt Woods) wrote:
› 
…[18 more quoted lines elided]…
› 

Walt's problem is more likely to be that the data file is defined as
Organization Sequential (or not declared, which defaults to sql), and
the MF system default is to expect sequential files to have no
embedded control characters -- MF call this 'record sequential' -- so
the CRLF character pair are being included in the data which is
returned.

You can tell the system to expect a text file, so the CRLF is
discarded, either by using the phrase ORGANIZATION LINE SEQUENTIAL in
the Select (e.g. select myfile organization line sequential assign
whatever...), or by using the compile directive SEQUENTIAL"LINE".

Writing a Line Seqential record adds the CRLF, and removes any
trailing spaces. Read does the inverse. This can be changed by
runtime switch, as can handling of bytes with value between x00 and
x20.

Al
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
