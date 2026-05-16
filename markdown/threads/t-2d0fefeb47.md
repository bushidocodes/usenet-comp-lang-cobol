[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interfacing with AutoCAD

_6 messages · 4 participants · 1999-09_

---

### Interfacing with AutoCAD

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf02f8$449dcb00$d43763c3@default>`

```
Has anyone ever done the above, or at least
read a drawing file into a Cobol program as data.
I'd be very suprised if anyone can answer this.
```

#### ↳ Re: Interfacing with AutoCAD

- **From:** john.e.freeman@attcanada.net
- **Date:** 1999-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37e566a6.21403931@news.attcanada.net>`
- **References:** `<01bf02f8$449dcb00$d43763c3@default>`

```
On 19 Sep 1999 15:41:22 GMT, "Simon R Hart" <hart1@technologist.com>
wrote:

>Has anyone ever done the above, or at least
>read a drawing file into a Cobol program as data.
>I'd be very suprised if anyone can answer this.


Yes.  Done much the same way as in Basic or C, using binary mode file
IO.  Since you mentioned AutoCad, I'm assumimng a PC based COBOL
compiler with a set of OS routines that ships with it, such as with
Microfocus COBOL or Realia COBOL, for example.  This is just like the
low level routines which ship with PC based Basic or C.

If you're wondering about potentially enormous and variable file sizes
in COBOL, note that this method bypasses the standard COBOL file
system - which is designed to handle business data, not binary or
graphics data.  I'm sure someone out there could update this, as its
been a while since I did this, however, here is a solution I used some
years ago using MF version 2.6 (I think).

1) Define a linkage section variable in the MAIN program which is one
bye long: PIC X.   

2)  Call an external memory allocation function.  You might want to
find the file size first, then allocate enough blocks of memory to
hold it. 

3)  Change the address of the linkage byte to the address returned by
the memory function using the SET statement.

4)  Using the binary file IO routines, read bytes from the file
specifying the linkage section byte as the target buffer.  The binary
routine will load offsetting from this address.  You will probably
have to load in chunks.  (This may have changed by now)

By the way, the usage of the SET statement, as well as the binary file
and the memory function, are documented in the MF COBOL manuals.

No, this isn't native COBOL, however, a so-called native C memory
function on a PC is very different in behavoir from a C memory
function on a VAX 4300.  The point is, can you do it?  Yes you can.
Cool eh?  

EF.
```

#### ↳ Re: Interfacing with AutoCAD

- **From:** maxomtech@wiscasset.net
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s5dh8$f9f$1@nnrp1.deja.com>`
- **References:** `<01bf02f8$449dcb00$d43763c3@default>`

```
Yes, sort-of, in AutoCAD (at least thru version 13) you have the ability
to define a Material List. Thru an 'AutoLisp' program (I think it is
built into to AutoCAD), you can (and I have several clients that do),
export this material list to a "LINE SEQUENTAIL" file.  We use this
facility to import Part Information and Bills of Material directly into
our COBOL apps.

Hope it helps

Chris Loy
Maxom Holdings, Inc.
http://www.maxom.com




In article <01bf02f8$449dcb00$d43763c3@default>,
  "Simon R Hart" <hart1@technologist.com> wrote:
> Has anyone ever done the above, or at least
> read a drawing file into a Cobol program as data.
> I'd be very suprised if anyone can answer this.
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: Interfacing with AutoCAD

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf03fa$e41434a0$e4cbac3e@default>`
- **References:** `<01bf02f8$449dcb00$d43763c3@default> <7s5dh8$f9f$1@nnrp1.deja.com>`

```


maxomtech@wiscasset.net wrote in article <7s5dh8$f9f$1@nnrp1.deja.com>...
> Yes, sort-of, in AutoCAD (at least thru version 13) you have the ability
> to define a Material List. Thru an 'AutoLisp' program (I think it is
…[10 more quoted lines elided]…
> 

Chris,

Can this be done using Automation?, and like wise can the data retreived
from the
material list be re-written to the file after modifing the data, therefore
changing the image drawing file?.

Simon R Hart
Eaton.
```

#### ↳ Re: Interfacing with AutoCAD

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E67B5E.8BD3E4F3@home.com>`
- **References:** `<01bf02f8$449dcb00$d43763c3@default>`

```
Simon R Hart wrote:
> 
> Has anyone ever done the above, or at least
> read a drawing file into a Cobol program as data.
> I'd be very suprised if anyone can answer this.

Simon,

I don't know about "reading it in as data", but I do have a requirement
from my user to 'open' a drawing associated with a particular oil/gas
plant vessel. I'll probably be using the Win API "CreateProcess" to open
it. (My Vessel records hold the filenames of AutoCad drawings).

If you're trying to get the AutoCad data in, (it's some years ago
that I was doing something for somebody with the data - navigation
equipment associated with Air Traffic Control), then I think it might be
fairly complex - as I recall, there are numerous data types in AutoCad.
For starters, check latest AutoCad manuals/on-line help - probably has a
feature to put out an ascii-delimited or equivalent.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Interfacing with AutoCAD

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf03f9$f2cca0a0$e4cbac3e@default>`
- **References:** `<01bf02f8$449dcb00$d43763c3@default> <37E67B5E.8BD3E4F3@home.com>`

```


James J. Gavan <jjgavan@home.com> wrote in article
<37E67B5E.8BD3E4F3@home.com>...
> Simon R Hart wrote:
> > 
…[18 more quoted lines elided]…
> Jimmy, Calgary AB

Jimmy;

Can you remmber if you could ever write data to the AutoCAD dwg
file? 

Simon R Hart
Eaton.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
