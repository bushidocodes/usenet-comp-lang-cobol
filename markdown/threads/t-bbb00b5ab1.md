[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Net Express / Dialog System context help

_3 messages · 3 participants · 1999-10_

---

### RE: Net Express / Dialog System context help

- **From:** Peter van Zeeland <peter.van.zeeland@cmg.nl>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6DE2D20B5851D2119BB300A0C9DAF698513150@NL-AMB-MAIL01>`

```


> : 	This may look stupid, but we do it all the time.
> : 	There is really no point in distributing a small external table
…[17 more quoted lines elided]…
> 
	Okay.
	Let's have a look at how microsoft does it.
	Why not browse the developer network cd set. You will find language
specifice tables at SOURCE level, and burnt-in language specific
EXECUTABLES.

	Am I right or am I right ?





 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

#### ↳ Re: Net Express / Dialog System context help

- **From:** "Stephen Dennis" <sdennis@svdltd.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LVZI3.110$YI2.3863@sea-read.news.verio.net>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF698513150@NL-AMB-MAIL01>`

```
Peter van Zeeland <peter.van.zeeland@cmg.nl> wrote in message
news:6DE2D20B5851D2119BB300A0C9DAF698513150@NL-AMB-MAIL01...
>
> Okay.
…[5 more quoted lines elided]…
> Am I right or am I right ?

You will find language specific tables, and they are 'burned' into the
executable, however looking at what Microsoft does rather argues against
your own point, and here's why:

In the Windows Program case, every user-visible string in the program is put
into a seperate 'string table' in a seperate text RC source file. The
program that uses those strings does so by reference to a particular entry
in the table....by unique number.

Those string tables are translated seperately into various languages
seperately from the source code. In fact, the only way Microsoft has a
chance of supporting such a broad array of languages is to use this
approach. For most Pan-European languages, no re-compile of the source is
necesary (some German phrases tend to be long-winded and sometimes the
dialogs box need to be made larger...fortunately, the dialogs themselves are
part of the same RC file). Translation into Japanese, Korean, Traditional
and Simplified Chinese can have farther reaching effects on the source code.

The resource compiler takes these strings (for whichever language you happen
to be building for) and creates an in-memory image (RES). The linker pretty
much tacks this in-memory image onto the end of the executable like a
fashion accessory.

These fashion accessories can be stripped off and new ones put in their
place quite automatically. I know the resource tools for 16-bit allowed you
to edit resources in an already-built executable. I'm fairly certain that
this capability exists in the 32-bit tools...as least from a third party.

There are strings which are -not- put into the resource file. FTP/HTTP/HTML
protocol or format-oriented strings that are spelled out in a standard
somewhere that cannot and should not be changed. These are things that the
user will never see.

Having a seperate files has the following disadvantages:

1. Seperate files (particularly a lot of little ones) waste space on the
disk due to fragmentation. Game like Doom, Quake, Half-Life have invented
blob-files as a way of collecting all these little pieces into one big file.
Without a blob file, these games would take 2-5 times more disk space due to
fragmentation of the file system. For example, a little 512 byte image
that's dealth with in the source code seperately becaues it's used on 14
different monsters in 500 different places would still consume an entire
disk allocation unit if stored seperately.

2. Seperate files increase you load time. Another file(s) for the OS to
find, security check, and make available to you.

3. Distribution problem. Having two files that must be installed in sync and
kept in sync in the face of users and later installs. This creates new error
situations and potential support calls.

However, for user-visible strings, the advantages of a seperate file are
clear. And, in the Microsoft case, they solved some of the disadvantages by
having it be seperately tacked onto the end of your program. You
must -still- ask the operating system for access to your own resources.
Those resources must -still- be opened and accessed seperately. They
are -not- typically loaded into memory with the program. Or there may be an
option to do so, but if that option is available, it's probably only the
critical error messages that are loaded at program load time.

Sorry for the long rambling message.
```

##### ↳ ↳ Re: Net Express / Dialog System context help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F4E395.97D269EE@home.com>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF698513150@NL-AMB-MAIL01> <LVZI3.110$YI2.3863@sea-read.news.verio.net>`

```
Stephen Dennis wrote:
> 
> Peter van Zeeland <peter.van.zeeland@cmg.nl> wrote in message
…[5 more quoted lines elided]…
> Sorry for the long rambling message.

No it wasn't. I found it very informative.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
