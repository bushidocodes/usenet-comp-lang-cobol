[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Learning JCL

_8 messages · 7 participants · 1998-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Learning JCL

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lvl64$c9k$1@fep5.clear.net.nz>`

```

Question for Mainfraimers,

The difference between Client/Server & Mainframe seems to be : MVS,
ISPF/TSO, & JCL.
Does one (1)pick these things up on the job, (2)learn them from books,
(3)get formal on the job training???
Also there is a cheap book at Amazon :-
Introduction to the IBM 360 Computer and Os/JCL : Job Control Language
by judith Rattenbury, published 1974. $9.35.
Would this book give me an intro to JCL?
Thanks
```

#### ↳ Re: Learning JCL

- **From:** "scom..." <ua-author-2666089@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6lvl64$c9k$1@fep5.clear.net.nz>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz>`

```

David Mowat writes ...

› Question for Mainfraimers,
›
› The difference between Client/Server & Mainframe seems to be : MVS,
› ISPF/TSO, & JCL.

Well, not exactly. There are various "flavors" of Client-Server, and several
"flavors" of mainframe. Even in the IBM world, "mainframe" might refer to any
of these current operating systems: MVS, OS/390, VM/ESA, VSE/ESA (and probably
others, since it's difficult to be sure you're always referring to a current
(i.e.: supported) system. Informally, people would say MVS, VM, VSE. For most
intent and purposes, from an applications programmer perspective, OS/390 is the
same as MVS, just the most recent version.

TSO is the OS/390 interactive, command line oriented, user interface. ISPF is a
full-screen front end that makes TSO more "user friendly".

JCL is the OS/390 interface to automate running a series of programs in the
batch, more or less unattended.

› Does one (1)pick these things up on the job, (2)learn them from books,
› (3)get formal on the job training???

All of the above are possible. Few universities teach these topics anymore, but
some training companies provide instructor led training on IBM mainframe
topics. [Ahem. Shameless commercial... check out our website at
www.trainersfriend.com all of our course descriptions and outlines are online
there, including information on OS/390 JCL and TSO/ISPF.]


› Also there is a cheap book at Amazon :-
› Introduction to the IBM 360 Computer and Os/JCL : Job Control Language
› by judith Rattenbury, published 1974. $9.35.
› Would this book give me an intro to JCL?

I don't know that particular book, but the title looks to be about 20 years out
of date. The S/360 first came out around 1963 or '64. It has been supplanted by
a series of machines that evolved from that technology. The "OS" referred to in
the title was an antecedent to MVS, and some of the JCL from those days is
still valid, but there have been vast changes since that version of the
operating system. I would look for more recent books, the general concensus
favorite seems to be the JCL book by Gary DeWard Brown.

› Thanks
› --

You're welcome.



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: SCo··.@a··.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Learning JCL

- **From:** "lo..." <ua-author-465212@usenetarchives.gap>
- **Date:** 1998-06-15T09:41:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a0ce99b79f-p2@usenetarchives.gap>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz> <gap-a0ce99b79f-p2@usenetarchives.gap>`

```

In article <199··.@lad··l.com>,
sco··.@a··.com (S Comstock) wrote:
›
I have been using the JCL book by Gary DeWard Brown (the "blue Brown book")
for over 10 years. It covers everything and is easy to read.


› David Mowat writes ...
› 
…[59 more quoted lines elided]…
› 


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Learning JCL

- **From:** "mixx..." <ua-author-17074640@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6lvl64$c9k$1@fep5.clear.net.nz>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz>`

```

On Sun, 14 Jun 1998 04:59:43, "David Mowat"
wrote:

› Does one (1)pick these things up on the job, (2)learn them from books,
› (3)get formal on the job training???
All of the above! JCL isn't difficult, although ISPF tailoring can
get a bit hairy.

› Introduction to the IBM 360 Computer and Os/JCL : Job Control Language
› by judith Rattenbury,
› Would this book give me an intro to JCL?
›
Yep, it's decent, although a lot has been added since then. The best
book is still GC28-1479.

=Dwight=
X1=L, X2=L & the domain is phonetic
```

##### ↳ ↳ Re: Learning JCL

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-06-19T09:03:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a0ce99b79f-p4@usenetarchives.gap>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz> <gap-a0ce99b79f-p4@usenetarchives.gap>`

```

MIX··.@EYE··S.COM wrote:
› 
› On Sun, 14 Jun 1998 04:59:43, "David Mowat" 
…[5 more quoted lines elided]…
› get a bit hairy.

Actually, ISPF file tailoring is quite easy, if you remember the NOFT
parm. The problem with FT is in those lines which require an ampersand.
Make these seperate skeletons, include them with an "FTINCL xxx NOFT"
and all is well.

mickey

› 
›› Introduction to the IBM 360 Computer and Os/JCL : Job Control Language
…[7 more quoted lines elided]…
› X1=L, X2=L & the domain is phonetic
```

###### ↳ ↳ ↳ Re: Learning JCL

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-06-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a0ce99b79f-p5@usenetarchives.gap>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz> <gap-a0ce99b79f-p4@usenetarchives.gap> <gap-a0ce99b79f-p5@usenetarchives.gap>`

```

Mickey wrote:
› 
› 
…[6 more quoted lines elided]…
› 
Double ampersands are easier:


// SET IPADDR=&IPADDR
...

//FTP exec pgm=ftp,parm=&&IPADDR


This tailors to

// SET IPADDR=135.66.44.22

//FTP exec pgm=FTP,PARM=&IPADDR

This allows the Operators to change the IP at the top of the JCL and
have it automatically go though the JCL. Temporary files are a real cow
with &&&&TEMP becoming &&TEMP but I just stopped using temporary files
and put clean ups in appropriate places for the files.

ISPF anyone....
Ken
```

###### ↳ ↳ ↳ Re: Learning JCL

_(reply depth: 4)_

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-06-20T09:59:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a0ce99b79f-p6@usenetarchives.gap>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz> <gap-a0ce99b79f-p4@usenetarchives.gap> <gap-a0ce99b79f-p5@usenetarchives.gap> <gap-a0ce99b79f-p6@usenetarchives.gap>`

```

Ken Foskey wrote:
› 
› Mickey wrote:
…[27 more quoted lines elided]…
› ISPF anyone....


That's why I use seperate skeletons for ampersands and temp files. Much
less confusing.

mickey
```

#### ↳ Re: Learning JCL

- **From:** "lo..." <ua-author-44593@usenetarchives.gap>
- **Date:** 1998-06-14T23:31:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a0ce99b79f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<6lvl64$c9k$1@fep5.clear.net.nz>`
- **References:** `<6lvl64$c9k$1@fep5.clear.net.nz>`

```

In article <6lvl64$c9k$1.··.@fep··t.nz>,
"David Mowat" wrote:
› 
› Question for Mainfraimers,
…[12 more quoted lines elided]…
› 

David,

Go to:
http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IEA1B503/CONTEN
TS

They wrote the book.

David


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
