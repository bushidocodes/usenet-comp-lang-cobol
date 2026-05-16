[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Free COBDATA Tool on COBOL21 site

_5 messages · 3 participants · 2013-01_

---

### Free COBDATA Tool on COBOL21 site

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-01-16T22:45:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<alnb69F20ipU1@mid.individual.net>`

```
I was informed today that the COBDATA tool at: .

http://primacomputing.co.nz/cobol21

...has not  been working for some downloads

The problem was because it was not intended to run on 64 bit platforms.

If anyone has tried to download and use this tool on a 64 bit platform, 
please accept my apologies. The web site should have been clear it was a 32 
bit implementation only, but at the time we built it there were not so many 
64 bit systems around.

Anyway, I have fixed it and it should now be downloadable to 32 and 64 bit 
platforms from Windows XP onwards. (I can't guarantee Win 98...)

Pete.
```

#### ↳ Re: Free COBDATA Tool on COBOL21 site

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2013-01-19T11:41:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1iflf8t4n6s9pk7vhnhcjpcncld3k4j94t@4ax.com>`
- **References:** `<alnb69F20ipU1@mid.individual.net>`

```
On Wed, 16 Jan 2013 22:45:43 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I was informed today that the COBDATA tool at: .
>
…[9 more quoted lines elided]…
>64 bit systems around.

Since I have x86 (32 bit) program directories on my x64 systems,
shouldn't your x32 programs work on 64 bit systems if the right
installation magic is done?

Clark Morris
>
>Anyway, I have fixed it and it should now be downloadable to 32 and 64 bit 
>platforms from Windows XP onwards. (I can't guarantee Win 98...)
>
>Pete.
```

##### ↳ ↳ Re: Free COBDATA Tool on COBOL21 site

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-01-20T13:58:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<am0tq0F7ielU1@mid.individual.net>`
- **References:** `<alnb69F20ipU1@mid.individual.net> <1iflf8t4n6s9pk7vhnhcjpcncld3k4j94t@4ax.com>`

```
Clark F Morris wrote:
> On Wed, 16 Jan 2013 22:45:43 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
> installation magic is done?

The "installation magic" can't do anything about a 32 bit program that tries 
to  load a 64 bit library... :-)

The COBDATA application has COBOL and C# components  in it. (The source is 
downloadable from COBOL21)

The C# was built to run on "AnyCPU". When it is installed on a 64 bit 
system, it runs as a 64 bit application. However, the COBOL uses a 32 bit 
native runtime. As soon as the COBOL tries to call C# it crashes and 
burns...

By rebuilding the C# to target a 32 bit processor, everything runs 
correctly. (It is using 32 bit code irrespective of the processor so it runs 
on both 32 and 64 bit platforms.)

Most people have no idea of the complexity which is under the covers to 
allow your new 64 bit platform to run 32 bit applications. It is really 
quite amazing but it does require some consideration from developers if they 
are using mixed languages across platforms. Some developers actually build 
two versions and detect at install time which one to install.

C# on its own would be fine, if it is built as targeting "AnyCPU". It will 
run as managed 32 or 64 bit code depending on the processor, and the CIL is 
appropriately JIT compiled to the right CLR and loaded at run time. It 
doesn't require "installation" or any other "magic" :-)

Unfortunately for me, the COBOL legacy is a millstone round  my neck that 
ties everything to 32 bit, even though it can run on a 64 bit platform, 
thanks to OS support from Windows.

If I was prepared to invest in a new CIL generating COBOL compiler (which I 
am not... they are outrageously expensive when CIL generating compilers for 
other languages (C#, VB.Net...) are free... and I am moving away from COBOL 
anyway, so it is a hard to pill to swallow further investment into it...) 
then I could create true 64 bit applications and components and the problem 
wouldn't arise.

The bottom line for me is that anything I use that has legacy components in 
it has to be targeted for "x86" (32 bit) architecture. Largely for that 
reason, I am upping the priority on converting the remaining COBOL 
components to C#, but it is a large amount of work and has some risks 
attached.

My mixed language applications CAN run on 32 or 64 bit, but the only way I 
will unleash the full power of 64 bit is to remove the COBOL.

It may be worth noting in passing that 32 bit applications running on 64 bit 
platforms will suffer a slight decrease in performance. (mostly undetectable 
by humans). This is a bit counter-intuitive (you might expect a more 
powerful processor to run faster; it does, but this is offset by extra work 
it has to do to allow your 32 bit stuff to execute...). On the few 
applications I have developed to test the new platforms, there is a 
noticeable increase in performance when 64 bit apps run on 64 bit platforms. 
A particular test where I ran identical functionality developed as 32 and 64 
bit managed code, showed around 15% better in 64 bit. However, you can't 
infer much from a sample of one, and it is just an indication.

Pete.
```

###### ↳ ↳ ↳ Re: Free COBDATA Tool on COBOL21 site

- **From:** Waldek Hebisch <hebisch@math.uni.wroc.pl>
- **Date:** 2013-01-21T02:17:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kdi8f4$mup$1@z-news.wcss.wroc.pl>`
- **References:** `<alnb69F20ipU1@mid.individual.net> <1iflf8t4n6s9pk7vhnhcjpcncld3k4j94t@4ax.com> <am0tq0F7ielU1@mid.individual.net>`

```
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
> 
> It may be worth noting in passing that 32 bit applications running on 64 bit 
…[8 more quoted lines elided]…
> infer much from a sample of one, and it is just an indication.

This is badly worded: 32 bit code running on 64-bit processor will
run as fast as on similar 32-bit processor.  In fact, if you code
the _same_ instructions as 32-bit or 64-bit, then 32-bit version
will be faster.  On CPU-intensive code 64-bit version should
be faster (of order 10-20%) becase 64-bit mode has new features
(mainly more registers) and uses more efficient software
conventions (32-bit mode is stuck with less efficient conventions
to keep backwards compatibility).  On memory intensive code
32-bit version frequently will win because nomally 32-bit data
takes less space and consequently there is less data to move
then in 64-bit version (but there are exceptions: I have a program
where data items nicely fit in 64-bit words, but need complex
data structure (bigger than 64-bits) in 32-bit mode).

Anyway, if the 32-bit programs run slower than 64-bit ones it
is normally not due some inefficiency of 64-bit system in
handling 32-bit code, rather it due to extra features available
in 64-bit mode.  Or, if you prefer, inefficiency is in the
32-bit instructions, not in the processor.

I wrote "normally" above because there is some inefficency in
mixing 32-bit and 64-bit code: you need to sets of libraries,
which takes more memory.  But on modern systems this is unlikely
to have measurable impact on performance.
```

###### ↳ ↳ ↳ Re: Free COBDATA Tool on COBOL21 site

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-01-21T16:55:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<am3shqFrr4rU1@mid.individual.net>`
- **References:** `<alnb69F20ipU1@mid.individual.net> <1iflf8t4n6s9pk7vhnhcjpcncld3k4j94t@4ax.com> <am0tq0F7ielU1@mid.individual.net> <kdi8f4$mup$1@z-news.wcss.wroc.pl>`

```
Waldek Hebisch wrote:
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>>
…[35 more quoted lines elided]…
> to have measurable impact on performance.

Thanks for your comments.

As always, I call them like I see them; my post is based on my  experience. 
(I was careful to state that a single sample is not representative of a 
case...)

Most people expect stuff to run faster on a 64 bit processor. My point was 
that this expectation isn't always met when running 32 bit apps.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
