[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Net Express Printing

_11 messages · 7 participants · 2002-12 → 2003-02_

---

### Net Express Printing

- **From:** "Stan_A" <Stan_nospam_Archer@hotmail.com>
- **Date:** 2002-12-30T04:48:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MeQP9.161038$qF3.11704@sccrnsc04>`

```
All,

Evaluating Net Express compiler and find only capability is to print to
prn/lpt1/lpt2/lpt3

How does one assign to a plain old Windows printer that is attached to a USB
port ? or a network printer ? or just plain old default printer of Windows ?


Tried to look in the online manuals - just about every section that I
thought might include the topic to no avail.


Any help would be greatly appreciated.

Thanks in advance !
```

#### ↳ Re: Net Express Printing

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-30T05:04:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04>`

```
On Mon, 30 Dec 2002 04:48:44 UTC, "Stan_A" 
<Stan_nospam_Archer@hotmail.com> wrote:

> All,
> 
…[13 more quoted lines elided]…
> Thanks in advance !

The easiest way to print through the Windows print subsystem is to use
the PC_PRINTER_xxx calls that are documented in the library routines. 
They have been around since the 3.4 Workbench days
```

##### ↳ ↳ Re: Net Express Printing

- **From:** "Stan_A" <Stan_nospam_Archer@hotmail.com>
- **Date:** 2002-12-30T05:52:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RaRP9.556469$QZ.80190@sccrnsc02>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net>`

```
Lorne,

Thanks for pointing that out. I never, ever could have found that on my own.
Call me stupid or humble but I can't imagine anyone finding that without
asking.

Will try to figure it out from here but my first impression with printing
and the complexity of the gui screen design makes for a bad first taste. If
you don't mind I may post another question later, respectfully as ever.


<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net...
> On Mon, 30 Dec 2002 04:48:44 UTC, "Stan_A"
> <Stan_nospam_Archer@hotmail.com> wrote:
…[6 more quoted lines elided]…
> > How does one assign to a plain old Windows printer that is attached to a
USB
> > port ? or a network printer ? or just plain old default printer of
Windows ?
> >
> >
…[13 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: Net Express Printing

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-30T18:12:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-C6I82dZzOcdC@h24-82-204-17.wp.shawcable.net>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <RaRP9.556469$QZ.80190@sccrnsc02>`

```
IIRC your best way to get the selection of a particular printer is to 
set the "oprn command" variable to force selection of a printer

01    open-command pic x(4) comp-x.

                 move 4 to open-command
                  call "pc_printer_open" using
                       os2-printer-handle
                       os2-document-title
                       open-command
                       by value 0 size 4
                       returning return-status

Note, the "printer handle" is a binary pointer to the printer, not 
something like "lpt1"

You can also obtain the device context for the printer and use that to
issue an API command

Lorne

On Mon, 30 Dec 2002 05:52:49 UTC, "Stan_A" 
<Stan_nospam_Archer@hotmail.com> wrote:

> Lorne,
> 
…[40 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: Net Express Printing

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-12-30T18:37:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E10923F.5C3D1587@shaw.ca>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <RaRP9.556469$QZ.80190@sccrnsc02>`

```


Stan_A wrote:

> Lorne,
>
…[7 more quoted lines elided]…
>

As an extension to Lorne's suggestion there are three alternatives for you.

1. Crystal Reports - just had it confirmed from two N/E users that they use this
for
preference. On the plus side it handles ODBC access to DB Tables. All comments
one reads about Crystal appear 'positive'.

2. OLE - MS Word - one which I'm giving consideration to. Go to the Micro Focus
site and read White Papers - Wayne Rippen on using MS Word, (and Excel for
producing graphs). As backup to this the IDE contains a menu item for 'Tools"
---> Type Library Assistant. You can extract a list of data types and all
methods associated with using MS Word. (It's comprehensive - contains 20,906
lines of source !). My own inclination would be to wrap the above code in a new
class." MS Word" and do invokes from business logic to this class.

3. PC_PRINT - works fine for me, (changing font styles, sizes etc.), as I'm not
into traditional accounting sub controls. If you want a sample, e-mail me
privately. Note, the Word approach above, like Crystal, allows you to view
before printing. PC_PRINT doesn't have this feature.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Net Express Printing

- **From:** "Stan_A" <Stan_nospam_Archer@hotmail.com>
- **Date:** 2002-12-30T06:28:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JIRP9.557967$NH2.37869@sccrnsc01>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net>`

```
Well Lorne, I have to admit at encountering much frustration with MF
documentation. I could even hazard a name for the "MF" initials at this
point.

Still nothing tells me (stupid me or humble me) how to define the printer.
It seems the example shows a call to a routine referencing a printer and the
printer handle is defined in their example as  X(4).

Now I could be thick here but is X(4) not the length of say 'lpt1' ?

In short, I still don't see a good example of how to code a simple select of
the printer and the working storage definitions to open, write to and close
the printer.

I did find in the online help but not in the 'additional software' portion
of the tutorial section. Not able to find anything good in the Appendix B
More Features worthwhile. I did see in it the words 'COBOL system library
routines' but no help in using them. Only going to the Help in the IDEand
typing in "pc_printer" and searching got me something to chew on. But, as I
said - nothing that seems what I am looking for. Perhaps if I got some sleep
and looked it over again Monday morning something will sink in. Thanks
again,

Stan


<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net...
> On Mon, 30 Dec 2002 04:48:44 UTC, "Stan_A"
> <Stan_nospam_Archer@hotmail.com> wrote:
…[6 more quoted lines elided]…
> > How does one assign to a plain old Windows printer that is attached to a
USB
> > port ? or a network printer ? or just plain old default printer of
Windows ?
> >
> >
…[13 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: Net Express Printing

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-30T02:18:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E101D79.4020405@Sympatico.ca>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <JIRP9.557967$NH2.37869@sccrnsc01>`

```
Stan, if LPT1 works, then the net use statement should.  IE- in your 
autoexec, assign network printer to a specific LPT.  Have you tried 
putting a network printer name into working storage, and assigning the 
file to the data name?

Donald


Stan_A wrote:

>Well Lorne, I have to admit at encountering much frustration with MF
>documentation. I could even hazard a name for the "MF" initials at this
…[70 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Net Express Printing

_(reply depth: 4)_

- **From:** "Stan_A" <Stan_nospam_Archer@hotmail.com>
- **Date:** 2002-12-30T17:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qp%P9.166735$qF3.12238@sccrnsc04>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <JIRP9.557967$NH2.37869@sccrnsc01> <3E101D79.4020405@Sympatico.ca>`

```
Donald,

Thanks for the net use tip - I've used it before but the only problem is you have to track someone down who has the \\servername\printername path. You gave me an idea though - maybe someone out there knows the answer, is there a file in Windows that stores the path to the network (shared) printer that could be opened, read and that path taken and accepted into the program in a dynamic way ?

I'd really like to get away from having to print to LPT ports at all though, my new traveling printer is USB.


Stan



  "Donald Tees" <Donald_Tees@Sympatico.ca> wrote in message news:3E101D79.4020405@Sympatico.ca...
  Stan, if LPT1 works, then the net use statement should.  IE- in your autoexec, assign network printer to a specific LPT.  Have you tried putting a network printer name into working storage, and assigning the file to the data name?

  Donald


  Stan_A wrote:

Well Lorne, I have to admit at encountering much frustration with MF
documentation. I could even hazard a name for the "MF" initials at this
point.

Still nothing tells me (stupid me or humble me) how to define the printer.
It seems the example shows a call to a routine referencing a printer and the
printer handle is defined in their example as  X(4).

Now I could be thick here but is X(4) not the length of say 'lpt1' ?

In short, I still don't see a good example of how to code a simple select of
the printer and the working storage definitions to open, write to and close
the printer.

I did find in the online help but not in the 'additional software' portion
of the tutorial section. Not able to find anything good in the Appendix B
More Features worthwhile. I did see in it the words 'COBOL system library
routines' but no help in using them. Only going to the Help in the IDEand
typing in "pc_printer" and searching got me something to chew on. But, as I
said - nothing that seems what I am looking for. Perhaps if I got some sleep
and looked it over again Monday morning something will sink in. Thanks
again,

Stan


<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net...
  
On Mon, 30 Dec 2002 04:48:44 UTC, "Stan_A"
<Stan_nospam_Archer@hotmail.com> wrote:

    
All,

Evaluating Net Express compiler and find only capability is to print to
prn/lpt1/lpt2/lpt3

How does one assign to a plain old Windows printer that is attached to a
      
USB
  
port ? or a network printer ? or just plain old default printer of
      
Windows ?
  
Tried to look in the online manuals - just about every section that I
thought might include the topic to no avail.


Any help would be greatly appreciated.

Thanks in advance !
      
The easiest way to print through the Windows print subsystem is to use
the PC_PRINTER_xxx calls that are documented in the library routines.
They have been around since the 3.4 Workbench days
```

###### ↳ ↳ ↳ Re: Net Express Printing

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-31T17:39:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212311739.c836ebc@posting.google.com>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <JIRP9.557967$NH2.37869@sccrnsc01> <3E101D79.4020405@Sympatico.ca> <qp%P9.166735$qF3.12238@sccrnsc04>`

```
"Stan A" <Stan nospam Archer@hotmail.com> wrote

> Still nothing tells me (stupid me or humble me) how to define the 
> printer.
…[4 more quoted lines elided]…
> Now I could be thick here but is X(4) not the length of say 'lpt1' ?

The 'Printer Handle' is a 4 byte hardware address that will point to a
structure held in memory somewhere.  It is set to the required value
when the printer is opened and this value must be correct for all
subsequent actions.  ie it has nothing to do with any specific name
and it must not be set to any value by the programmer (except possibly
low-values after closing the printer).
```

#### ↳ Re: Net Express Printing

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-12-30T07:10:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MNicnSxK-pJX2I2jXTWcpA@giganews.com>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04>`

```

"Stan_A" <Stan_nospam_Archer@hotmail.com> wrote in message
news:MeQP9.161038$qF3.11704@sccrnsc04...
> All,
>
…[3 more quoted lines elided]…
> How does one assign to a plain old Windows printer that is attached to a
USB
> port ? or a network printer ? or just plain old default printer of Windows
?
>
>
…[6 more quoted lines elided]…
> Thanks in advance !

If all else fails, try RPV --

http://www.rpvreport.com/
```

#### ↳ Re: Net Express Printing

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-01T13:33:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2469307.1044106403@dbforums.com>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04>`

```

If the printer goes of the type " host-based " that doesn't give support
to DOS, you only will get generating in file and printing for an
utilitarian one any of WinDOS
(for instance PRINT). most of HP's gives support to the way DOS, since
be made the due association LPTn in Windows.

Marcos A.S.
Brasil
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
