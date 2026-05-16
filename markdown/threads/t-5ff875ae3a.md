[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and code

_9 messages · 4 participants · 2004-10_

---

### COBOL and code

- **From:** "scorpion53061" <scorpion_53061@nospamhereeveryahoo.com>
- **Date:** 2004-10-01T14:42:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<415db8d9$1@news.mcleodusa.net>`

```
WE have a program a programmer wrote for us. He is long gone.

We hired another one but it appears the source for the file is misisng or he 
took it with him. I understand there are decompilers out there for this sort 
of thing. Is there a free or cheap one I could use.

The environment is RISC6000 running AIX 5.1
```

#### ↳ Re: COBOL and code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-10-01T20:25:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q2j7d.373792$yk.62946@news.easynews.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net>`

```
I know about "de-compilers" for IBM mainframe (MVS) COBOL's - but none for AIX 
5.1.
```

##### ↳ ↳ Re: COBOL and code

- **From:** "scorpion53061" <scorpion_53061@nospamhereeveryahoo.com>
- **Date:** 2004-10-01T16:24:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<415dd0a7$1@news.mcleodusa.net>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <Q2j7d.373792$yk.62946@news.easynews.com>`

```
would you tell me what you know....


perhaps they will work. It is standard MicroFocus COBOL.


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:Q2j7d.373792$yk.62946@news.easynews.com...
>I know about "de-compilers" for IBM mainframe (MVS) COBOL's - but none for 
>AIX 5.1.
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL and code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-10-01T22:37:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y_k7d.379127$yk.63713@news.easynews.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <Q2j7d.373792$yk.62946@news.easynews.com> <415dd0a7$1@news.mcleodusa.net>`

```
No - it doesn't work for Micro Focus COBOL.  Although with Micro Focus, if you 
have an .idy file, then you *may* be able to get source out of that.

To get current information on the IBM mainframe product, see:

 http://www.source-recovery.com/
```

###### ↳ ↳ ↳ Re: COBOL and code

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-02T17:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hjmtl0tl69gvbi1er9anf2r1ck8s3nr11d@4ax.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <Q2j7d.373792$yk.62946@news.easynews.com> <415dd0a7$1@news.mcleodusa.net>`

```
On Fri, 1 Oct 2004 16:24:16 -0500, "scorpion53061"
<scorpion_53061@nospamhereeveryahoo.com> wrote:

>It is standard MicroFocus COBOL.

You're out of luck. The debug file (.idy) doesn't contain source
names.
```

#### ↳ Re: COBOL and code

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-01T22:29:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net>`

```
On Fri, 1 Oct 2004 14:42:50 -0500, "scorpion53061"
<scorpion_53061@nospamhereeveryahoo.com> wrote:

>WE have a program a programmer wrote for us. He is long gone.
>
…[4 more quoted lines elided]…
>The environment is RISC6000 running AIX 5.1 

What compiler? Brand name is good enough.

Was it compiled with the debugger option on?

A decompiler cannot recover information that doesn't exist in machine
code. Without debugging information, you'll get a program that
compiles but has meaningless names.
```

##### ↳ ↳ Re: COBOL and code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-10-01T22:38:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N%k7d.1884044$ic1.193982@news.easynews.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message 
news:p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com...
> On Fri, 1 Oct 2004 14:42:50 -0500, "scorpion53061"
> <scorpion_53061@nospamhereeveryahoo.com> wrote:
>
<snip>
>
> A decompiler cannot recover information that doesn't exist in machine
> code. Without debugging information, you'll get a program that
> compiles but has meaningless names.
>

For a company that does exactly what Robert says can't be done (but as far as I 
know is limited to IBM mainframe COBOL missing source code), see:

http://www.source-recovery.com/
```

###### ↳ ↳ ↳ Re: COBOL and code

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-02T01:34:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b1sl05qdbr8gu9t0ben2dtrgs0ems49r8@4ax.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com> <N%k7d.1884044$ic1.193982@news.easynews.com>`

```
On Fri, 01 Oct 2004 22:38:40 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message 
>news:p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com...
…[13 more quoted lines elided]…
>http://www.source-recovery.com/

A glance at their marketing demo confirms everything I said. 

http://www.source-recovery.com/srcn-coboleq.html
```

###### ↳ ↳ ↳ Re: COBOL and code

_(reply depth: 4)_

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2004-10-02T16:51:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cfqdnckzj729osLcRVn-jg@adelphia.com>`
- **In-Reply-To:** `<6b1sl05qdbr8gu9t0ben2dtrgs0ems49r8@4ax.com>`
- **References:** `<415db8d9$1@news.mcleodusa.net> <p9mrl0tbh966526ncm4t1adi3k2tf2ktb4@4ax.com> <N%k7d.1884044$ic1.193982@news.easynews.com> <6b1sl05qdbr8gu9t0ben2dtrgs0ems49r8@4ax.com>`

```
Robert Wagner wrote:

>On Fri, 01 Oct 2004 22:38:40 GMT, "William M. Klein"
><wmklein@nospam.netcom.com> wrote:
…[32 more quoted lines elided]…
>
Robert,
My company used this technology for recovering a couple of lost programs 
at Y2K time.  If you send them record descriptions that use the names 
you want to have in the program, they will "fit" the generated names to 
the "desired" names.  While this does not fix everything, it can 
certainly help.

You are left with procedure-names and some items like level-66, 
level-77, and level-88 to fix yourself, but it will give you a leg up on 
the job of understanding a program with lost source code.

All of that said, while we had a number of executable programs for which 
we could not easily find the source, we did find over 90% after more 
exhaustive searches.  (In most cases, the programs did not follow our 
rules of having the source program and executable use the same name, or 
the source never got transferred from old libraries to the newest ones.

I would try hard to track down that original programmer.  It is almost 
certain that she / he left the source code behind, and maybe the 
original poster simply doesn't know where to look.  If the programmer 
didn't leave the code behind (a bad practice for both him and the 
company), she / he may well have a copy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
