[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# translante cobol files to txt of mdb files

_6 messages · 6 participants · 1999-12_

---

### translante cobol files to txt of mdb files

- **From:** "Perfect" <nikolaas.coenegrachts@student.kuleuven.ac.be>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<945645582.679982@marvin>`

```
Hi,

Could somebody give me some info how I can translate cobol data files to a
format wich can be accesed in MS access.

Thank you
```

#### ↳ Re: translante cobol files to txt of mdb files

- **From:** Dirk Munk <munk@home.nl>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385D70E6.822FF07B@home.nl>`
- **References:** `<945645582.679982@marvin>`

```
I'm afraid there is no such thing as "a Cobol datafile". The way these
files are structured is most of the time compiler and / or operating
system depended. For instance indexed files may have their indexes as a
part of the data file itself, or as separate files. So it al depends on
what compiler was used when the files were created.

Regards,

Dirk

Perfect wrote:
> 
> Hi,
…[4 more quoted lines elided]…
> Thank you
```

#### ↳ Re: translante cobol files to txt of mdb files

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ud1gzrxS$GA.282@cpmsnbbsa02>`
- **References:** `<945645582.679982@marvin>`

```
What I would do is this.

1: Take the COBOL Source code and find the FD (or WS) record definition for
the file.

2: Create a new version of the original FD with all non-display fields
translated into display fields.  For easy Import into MS Access, add a
constant tab, comma, tilde, or whatever character inbetween the fields of
the file.

3: Write a new COBOL program using that new file definition, MOVEing the old
FD fields into the new FD fields, and then "write" out the records to a .txt
file.

4: Open MS Access and use the Import feature.  If you added a delimiting
character between the fields, MS Access will automatically parse the fields.
You'll have to go through each field and change them from TEXT to whatever
else they need to be in the final MS Access product, but you'll be well on
your way to having your data ready for use.  (If you didn't add a delimiting
character, on Import, you'll have a lot of work to do defining the size of
each field, but that's just typing work, not really a big problem.)

5: If you don't hae the original COBOL Source code (the file definition, in
particular), you are in bad shape.  Take the object code, and disassemble it
and try and work out the original file FD from the assembly language.




Perfect <nikolaas.coenegrachts@student.kuleuven.ac.be> wrote in message
news:945645582.679982@marvin...
> Hi,
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: translante cobol files to txt of mdb files

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385DBD39.8395F0@siber.com>`
- **References:** `<945645582.679982@marvin>`

```
Perfect wrote:
> 
> Hi,
…[4 more quoted lines elided]…
> Thank you

Yes, Siber Systems sells a number of Data File converters
that do just what you want -- they convert Cobol data files
to CVS (comma-separated values) and DBF formats. Both of these 
formats are gladly accepted by MS Access. Currently we can read
FSC and MF data files. RM and ACU data file readers are in works.

More on this at http://www.siber.com/sct/datafile/

Regards,
Vadim Maslov
```

#### ↳ Re: translante cobol files to txt of mdb files

- **From:** stevenln@aol.com (StevenLN)
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991220012211.29404.00000041@ng-ci1.aol.com>`
- **References:** `<945645582.679982@marvin>`

```
Do accomplish the task, assuming that the "COBOL Datafile" (previous poster is
correct that there is no such thing - Cobol does not have an intrinsic file
structure) is located on an OS/390 or VSE host, or possibly an AS/400 (ok, I am
an IBM big-iron bigot), is to use one of the reporting tools generally
available in the environment, such as FOCUS or EasyTrieve, to write a
comma-separated-value file (*.CSV), download that to the PC or LAN, and then
open it with that file type in ACCESS.   Of course, you can also do this, with
much more manual coding, in COBOL.  If you choose that route, check out the
MOVE...CORResponding option to easy the coding and make it more amenable to
layout changes in the future.
```

#### ↳ Re: translante cobol files to txt of mdb files

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385FF790.1CA5@NOSPAMguysoftware.com>`
- **References:** `<945645582.679982@marvin>`

```
Perfect wrote:
> 
> Hi,
> 
> Could somebody give me some info how I can translate cobol data files to a
> format wich can be accesed in MS access.


You could try a generic parser/converter like ParseRat 
(http://www.guysoftware.com/parserat.htm)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
