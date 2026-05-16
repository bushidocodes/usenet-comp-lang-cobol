[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Help

_5 messages · 5 participants · 2005-04 → 2005-05_

---

### IBM Help

- **From:** Floyd Johnson <floydj@netins.net>
- **Date:** 2005-04-29T20:08:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Auwce.141$8g.64@news01.roc.ny>`

```
I have student who has received a very attractive internship offer (i.e. 
room and board, transportation, and a small salary) because of the 
training I provided him in COBOL a year ago.  We worked with Fujitsu 
COBOL in the PC environment - both the student version and the 
professional version.

However, the internship includes work with TSO, IPSF (?), ReXX, etc. 
There is no opportunity on campus to become familiar with these tools. 
The internship site knows this is not part of his background, but he 
wants to be as prepared as possible as he starts his summer activities. 
  Can you suggest any web sites that could help him understand how these 
differ from PC products and prepare to use these new environments and 
utilities.

Thank you for any ideas or leads.

Floyd Johnson
```

#### ↳ Re: IBM Help

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-29T20:19:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wFwce.1460452$za2.232831@news.easynews.com>`
- **References:** `<Auwce.141$8g.64@news01.roc.ny>`

```
First of all where are you (or more importantly the student) located?  There may 
be some mainframe sites OR some education opportunites to help with this.

Then for some books (that might help), I think the "Murach" books are as good as 
any for "intro" stuff (and for an intern could be used BOTH as a "preview" and 
as a refernce later on).  See (at Amazon.com - for example)

 - Murach's MVS Tso: Concepts and Ispf (MVS TSO)

 - Murach's OS/390 and z/OS JCL

Also (depending upon the shop) of interest is:

  - Murach's CICS for the COBOL Programmer

Finally,

 - Murach's Structured COBOL

might be useful for the student to see what is (and by inference - is not) 
available with IBM Mainframe COBOL - compared to Fujitsu or other workstation 
COBOL's.

NOTE WELL:
   I do NOT think that the "Murach" books are the BEST books for any of these 
individual topics - but as a "group" I think they are probably as good or even 
better than any other similar "set of books" for an "introduction today, 
reference tomorrow".
```

#### ↳ Re: IBM Help

- **From:** epc8@juno.com
- **Date:** 2005-04-29T15:36:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114814207.180068.312360@f14g2000cwb.googlegroups.com>`
- **References:** `<Auwce.141$8g.64@news01.roc.ny>`

```

Floyd Johnson wrote:
> I have student who has received a very attractive internship offer
(i.e.
> room and board, transportation, and a small salary) because of the
> training I provided him in COBOL a year ago.  We worked with Fujitsu
…[4 more quoted lines elided]…
> There is no opportunity on campus to become familiar with these
tools.
> The internship site knows this is not part of his background, but he
> wants to be as prepared as possible as he starts his summer
activities.
>   Can you suggest any web sites that could help him understand how
these
> differ from PC products and prepare to use these new environments and

> utilities.
>
> Thank you for any ideas or leads.
>
> Floyd Johnson

Rexx is the easy one. Other than the newsgroup comp.lang.rexx, see

Rexx Language Association  http://www.rexxla.org/
Open Object Rexx http://www.oorexx.org/

Rexx is available on a wide variety of platforms. The core language
should be very portable. There are a number of free interpreters which
run on Windows such as Regina, Reginald and now Open Object Rexx.

IMO, a helpful topic to look at in regards to moving from PC to
Mainframe is
Decimal Arithmetic  http://www2.hursley.ibm.com/decimal/
```

#### ↳ Re: IBM Help

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-05-01T16:40:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d530qd0qor@news1.newsguy.com>`
- **References:** `<Auwce.141$8g.64@news01.roc.ny>`

```

In article <Auwce.141$8g.64@news01.roc.ny>, Floyd Johnson <floydj@netins.net> writes:
> I have student who has received a very attractive internship offer (i.e. 
> room and board, transportation, and a small salary) because of the 
…[4 more quoted lines elided]…
> However, the internship includes work with TSO, IPSF (?), ReXX, etc. 

It's ISPF - a character-based full-screen editor and IDE.  ISPF is
one of what Bezroukov calls the "Eastern Orthodox editors": a
family of source-code editors (mostly derived from the unrelated but
similar ISPF for TSO and XEDIT for CMS) which share significant look
and feel.  (Bezroukov's terminology and opinions are idiosyncratic,
but his site[1] does give something of a feel for the differences
between the IBM mainframe editors and the major Unix editors.)

It's been quite some time since I did anything significant with ISPF,
though I have used OS/400's SEU, another (lesser) member of the
family, recently.  So take the rest of this with a grain of salt.

Some of the notable features of ISPF and relations:

- They're designed for block-mode terminals.  Consequently, while
they support full-screen editing, changes to lines on the screen
actually take effect when the user presses an action key, like Enter
or a page-scrolling key.

- They have a command line for more complex editing tasks.

- They have a left margin area on the screen with line numbers.  The
line numbers can be overtyped with commands such as "I" to insert
lines below the overtyped line.

- They can "fold" the source view, hiding ranges of lines so that,
for example, you might have only section headers on the screen at one
point; then you could unfold one section to view its contents.

The only free editor of this type I know of is THE, The Hessling
Editor, which is based on XEDIT.[2]  It'd give your student a feel
for the ISPF UI, though.

There are commercial ISPF ports to other platforms (back around 1985
I had one for PC DOS, which I used for several years), so there might
be a free one out there which I haven't run into.


TSO (Time Sharing Option) is an add-on for MVS (Multiple Virtual
Storage), one of the major IBM mainframe OSes.  MVS isn't designed
for interactive use; TSO provides that.  Typically TSO is used to
run ISPF so you can do program development and that sort of thing
on MVS systems.


IBM's manuals for ISPF and TSO are available from IBM's website
somewhere.  There might be online tutorials, too.


Someone else has already noted that there are numerous free Rexx
implementations, tutorials, etc available.  THE also supports Rexx
macros.


I'm a Unix programmer by preference, and Unix and Windows are where I
do most of my work, but I quite enjoy switching gears once in a while
and doing a little mainframe (or even OS/400) development.  Some
people find changing their work habits difficult and annoying - which
I understand - but I hope your student finds the mainframe environ-
ment palatable.  Even if his career takes him in other directions, I
think it will be a useful experience.


1. http://www.softpanorama.org/Editors/index.shtml
2. http://sourceforge.net/projects/hessling-editor
```

##### ↳ ↳ Re: IBM Help

- **From:** "Fred Exley" <fexly221@msn.com>
- **Date:** 2005-05-01T16:56:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<117ar62od369gc4@corp.supernews.com>`
- **References:** `<Auwce.141$8g.64@news01.roc.ny> <d530qd0qor@news1.newsguy.com>`

```

"Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
news:d530qd0qor@news1.newsguy.com...
>
> In article <Auwce.141$8g.64@news01.roc.ny>, Floyd Johnson <floydj@netins.net> 
…[76 more quoted lines elided]…
> Michael Wojcik                  michael.wojcik@microfocus.com

I use an ISPF type editor ported to Windows called Kedit (not to be confused 
with the Unix editor with the same name).  All the power of ISPF, and a Rexx 
scripting capability is built in.  Personally I think it's the best pc-based 
editor of all.  http://www.kedit.com/
-Fred
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
