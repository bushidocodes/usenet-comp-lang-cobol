[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convertor for coding COBOL FD Copy FIles to VB

_4 messages · 4 participants · 1997-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Migration and conversion`](../topics.md#migration) · [`VSAM, files, sorting`](../topics.md#files)

---

### Convertor for coding COBOL FD Copy FIles to VB

- **From:** "grwa..." <ua-author-15582803@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6638kf$49v$1@biffo.sol.co.uk>`

```

COBOL Copy File FD section conversions to VB

One of the most tedious tasks in this area is the re-creation of the
data files.

While you can use Access to do this, you usually end out with several
fields of the wrong length or the wrong data type. The alternative is
to hard code the file creations, which goes something like this:-


ï¿½ Set the Database name
StrDBName = "D:\VBFiles\Vhstock.mdb"
ï¿½ Set the Table Name
strTDName = "vsmas"
' erase db if it's there
Kill strDBName
' open ws and create db
Set ws = DBEngine.Workspaces(0)
Set Db = ws.CreateDatabase(strDBName, dbLangGeneral, dbVersion30)
'create a new table
Set td = Db.CreateTableDef(strTDName)
'create a new field in table
Set fl = td.CreateField("Vstmp_Reg", dbText, 8)
td.Fields.Append fl
Set fl = td.CreateField("Vstmp_Type", dbInteger)
td.Fields.Append fl
Db.TableDefs.Append td
ï¿½ Set the Index
Set ix = td.CreateIndex("vstmp_Reg")
Set fl = ix.CreateField("Vstmp_Reg")
ix.Required = True
ix.Fields.Append fl
td.Indexes.Append ix

Etc. Etc.

I have an in-house utility which I use to do most of this. If I
enhance this to allow the user to enter a COBOL Copy file name and
then produce a Private Sub cmdCreate_File.Click procedure which writes
all of the code necessary to do this would it be of much general
interest at $150?

Reply to grw··.@tay··o.uk
```

#### ↳ Re: Convertor for coding COBOL FD Copy FIles to VB

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1997-12-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aee2da78bf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6638kf$49v$1@biffo.sol.co.uk>`
- **References:** `<6638kf$49v$1@biffo.sol.co.uk>`

```

On Wed, 03 Dec 1997 17:26:28 GMT, grw··.@tay··t.com () wrote:

› COBOL Copy File FD section conversions to VB
› 
…[5 more quoted lines elided]…
› to hard code the file creations, which goes something like this:-
 
 
› Etc. Etc.
› 
…[4 more quoted lines elided]…
› interest at $150?

Probably not. The only scenario that I have for VB at present is to
front-end COBOL programs on the PC, and even then VB is not perfect,
made worse by all of those hundreds of API calls. Anyway, VB does the
pretty screen stuff and COBOL does the "man's" work of processing the
data and files. I suspect that similar scenarios exist elsewhere.
For less casual PC uses, the COBOL compilers do an excellent job, and
there's some excellent front-end packages out there as well.


Charles F Hankel
--------------------------------------
Hapless FAQer on the Wirral peninsular
```

#### ↳ Re: Convertor for coding COBOL FD Copy FIles to VB

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aee2da78bf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6638kf$49v$1@biffo.sol.co.uk>`
- **References:** `<6638kf$49v$1@biffo.sol.co.uk>`

```

Just curious. How will you convert the following:

01 THE-NUMBER pic s9(5)v99 comp-3.


grw··.@tay··t.com wrote in article <6638kf$49v$1.··.@bif··o.uk>...
› COBOL Copy File FD section conversions to VB
› 
…[11 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Convertor for coding COBOL FD Copy FIles to VB

- **From:** "theprogrammer" <ua-author-6588855@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aee2da78bf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aee2da78bf-p3@usenetarchives.gap>`
- **References:** `<6638kf$49v$1@biffo.sol.co.uk> <gap-aee2da78bf-p3@usenetarchives.gap>`

```

A gotcha... LOL!

To the best of my knowledge, VB (or any of the other non-mainframe based
languages) can handle packed decimal. I know that I make the mainframe
people transport numeric data as unpacked strings. Had to pause and think
about decoding over-punched numeric data when it reached my Visual BASIC
programs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
