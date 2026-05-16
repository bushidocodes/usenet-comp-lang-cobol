[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RMCobol handling BIG indexed files

_8 messages · 4 participants · 2000-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### RMCobol handling BIG indexed files

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8d6lj8$rcv$1@news1.xs4all.nl>`

```
Is there a limitation on the size of indexed files?

We are the 256 user version of RMCobol 6.61 for Unix

It appears that we can not write new records in an indexed file that is
1.528.373.184 bytes big.


kind regards,
Anton Rusbach
```

#### ↳ Re: RMCobol handling BIG indexed files

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<IYGJ4.78$sj3.1022@client>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl>`

```
What operating system? RM/COBOL version 6.61 for UNIX can support files over
2GB if the operating system can support large files.

==============================================
Robert  Heady                                   r.heady@liant.com


Anton wrote in message <8d6lj8$rcv$1@news1.xs4all.nl>...
>Is there a limitation on the size of indexed files?
>
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: RMCobol handling BIG indexed files

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8defhu$lkr$1@news1.xs4all.nl>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client>`

```
Hi Robert,

> What operating system? RM/COBOL version 6.61 for UNIX can support files
over
> 2GB if the operating system can support large files.

AT&T Unix handles files up to 2Gb, by the indexed file that causes troubles,
appears to have a max of 1.5Gb

Your company now says I have to change the RUN-FILES attribute
FILE-LOCK-LIMIT to 4096 (now 07FFFFFFEh) to gain data-space(?!)

regards,
Anton Rusbach

>
> ==============================================
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Sv: RMCobol handling BIG indexed files

- **From:** "B. Figueiredo" <benja@private.dk>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8dia0g$e6t$1@news101.telia.com>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client> <8defhu$lkr$1@news1.xs4all.nl>`

```
Maybe you should check whether Unix has a file size limit. Just type
"ulimit" at the UNIX-command prompt.

Regards
Benjamin Nyrup

Anton <a.rusbach@coss.nl> skrev i en
nyhedsmeddelelse:8defhu$lkr$1@news1.xs4all.nl...
> Hi Robert,
>
…[4 more quoted lines elided]…
> AT&T Unix handles files up to 2Gb, by the indexed file that causes
troubles,
> appears to have a max of 1.5Gb
>
…[27 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: RMCobol handling BIG indexed files

_(reply depth: 4)_

- **From:** "Gerald Moull" <gerald@moull.freeserve.co.uk>
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8diu7r$v0g$1@news7.svr.pol.co.uk>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client> <8defhu$lkr$1@news1.xs4all.nl> <8dia0g$e6t$1@news101.telia.com>`

```

Anton,

You also need to have a Block size in the file large enough.  You may find a
default size of 512 has been used.  You'll need to make sure it is something
like 2 or 4K to enable the maximum size.

Gerald


B. Figueiredo <benja@private.dk> wrote in message
news:8dia0g$e6t$1@news101.telia.com...
> Maybe you should check whether Unix has a file size limit. Just type
> "ulimit" at the UNIX-command prompt.
…[8 more quoted lines elided]…
> > > What operating system? RM/COBOL version 6.61 for UNIX can support
files
> > over
> > > 2GB if the operating system can support large files.
…[21 more quoted lines elided]…
> > > >It appears that we can not write new records in an indexed file that
is
> > > >1.528.373.184 bytes big.
> > > >
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: RMCobol handling BIG indexed files

_(reply depth: 5)_

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<WyjL4.24$Od.540@client>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client> <8defhu$lkr$1@news1.xs4all.nl> <8dia0g$e6t$1@news101.telia.com> <8diu7r$v0g$1@news7.svr.pol.co.uk>`

```
Anton,

For indexed files the maximum file size depends on the block size used for
the file.  This is the formula for computing the maximum size an indexed
file:

 (MAX_LOCK_BYTE / (BlockSize + 256)) * BlockSize = maximum file size

The default value for MAX_LOCK_BYTE for file versions 0 and 2 is  x7FFFEBFD
or decimal 2,147,478,525.

The larger the block size, the closer the file size will approach the
MAX_LOCK_BYTE.

Examples:

 BlockSize = 512
                       (2147478525 / (512 + 256)) * 512    =   1,431,652,350
bytes   (1.33 GB)

 BlockSize =  4096
                       (2147478525 / (4096 + 256)) * 4096 =   2,021,156,258
bytes  (1.88 GB)
```

###### ↳ ↳ ↳ Re: RMCobol handling BIG indexed files

_(reply depth: 6)_

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8dmcus$cnt$1@news1.xs4all.nl>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client> <8defhu$lkr$1@news1.xs4all.nl> <8dia0g$e6t$1@news101.telia.com> <8diu7r$v0g$1@news7.svr.pol.co.uk> <WyjL4.24$Od.540@client>`

```
Dear Robert,

Thank you for this clear explanation!

I can change the blocksize while the file is not used, but do I re-compile any programs? 
(We do not use the BLOCK CONTAINS in any FD.)

report of rmmapinx.cob:

  8 empty Blocks may be needed for a Write operation.               
  Open For Modify Count = 1.                                        
                                                                    
Detail Information:                                                 
  File version number = 0.                                          
  Minimum read version number = 0.                                  
  Minimum write version number = 0.                                 
  Disk Block Increment Size = 632 Bytes.                            
  Allocation Increment = 8 Blocks.                                  
  Recoverability/Performance Strategy:                              
    Data are forced to the system only when necessary.              
      Force Write Data Blocks = No.                                 
      Force Write Index Blocks = No.                                
      Force to Disk = No.                                           
      Force File Closed = No.                                       
                                                                    
Key Information:                                                    
     Key   Segment  Starting  Segment    Key    Tree   Duplicates   
   Number  Number   Position  Length   Length  Height  Permitted?   
     ---     ---      -----     ---      ---     --        ---      
    Prime      1          1      19       19      6        No       


kind regards,

Anton Rusbach


Robert Heady <r.heady@liant.com> schreef in berichtnieuws WyjL4.24$Od.540@client...
> Anton,
> 
…[97 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: RMCobol handling BIG indexed files

_(reply depth: 4)_

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8dmd2e$cpi$1@news1.xs4all.nl>`
- **References:** `<8d6lj8$rcv$1@news1.xs4all.nl> <IYGJ4.78$sj3.1022@client> <8defhu$lkr$1@news1.xs4all.nl> <8dia0g$e6t$1@news101.telia.com>`

```
Dear Benjamin,

ulimit says 'unlimited' but by now I already know AT&T Unix does have a
maximum of 2Gb.

kind regards,
Anton Rusbach

B. Figueiredo <benja@private.dk> schreef in berichtnieuws
8dia0g$e6t$1@news101.telia.com...
> Maybe you should check whether Unix has a file size limit. Just type
> "ulimit" at the UNIX-command prompt.
…[8 more quoted lines elided]…
> > > What operating system? RM/COBOL version 6.61 for UNIX can support
files
> > over
> > > 2GB if the operating system can support large files.
…[21 more quoted lines elided]…
> > > >It appears that we can not write new records in an indexed file that
is
> > > >1.528.373.184 bytes big.
> > > >
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
