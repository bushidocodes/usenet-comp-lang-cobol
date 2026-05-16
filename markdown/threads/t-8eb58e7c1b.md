[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with Fujitsu V4 editor/compiler (what else is new)

_9 messages · 6 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** "R. Hayes" <rmch@cadvision.com>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e925bd.0@news.cadvision.com>`

```
Is there any way to compile Fujitsu V4 source code WITHOUT having to delete
any information that is placed after column 72?

I am offloading some COBOL source from a Unisys 1100/2200 and don't really
want to trash all that info.  But it seems I have to or I get compile errors
in Fujitsu.

Thanks.
```

#### ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** emilne@my-dejanews.com
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cbkmb$nqq$1@nnrp1.dejanews.com>`
- **References:** `<36e925bd.0@news.cadvision.com>`

```
In article <36e925bd.0@news.cadvision.com>,

The SRF option lets you define the format for programs and copybooks as
- fixed - the tradional card image that ends in column 72
- variable - extends area B out to column 251
- free - eliminates fixed positions for sequence number, indicator, area A and
area B.  Each line can contain 251 characters.

The format for programs and copybooks can be different in any combination.

  "R. Hayes" <rmchXXX@cadvision.com> wrote:
> Is there any way to compile Fujitsu V4 source code WITHOUT having to delete
> any information that is placed after column 72?
…[7 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-yddxnInKVcle@Dwight_Miller.iix.com>`
- **References:** `<36e925bd.0@news.cadvision.com>`

```
On Fri, 12 Mar 1999 14:34:56, "R. Hayes" <rmch@cadvision.com> wrote:

> Is there any way to compile Fujitsu V4 source code WITHOUT having to delete
> any information that is placed after column 72?

Set your "View" options to ANSI standard.  That should fix you up.
```

#### ↳ Re: Help with Fujitsu V4 editor/compiler Part II

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cfddh$pa1$1@oak.prod.itd.earthlink.net>`
- **References:** `<36e925bd.0@news.cadvision.com>`

```

Is there an environment variable (or similar) for use with
FJ 4 PowerCOBOL to inform the compiler of the location
of COPY books? Setting the location in each form is not
a practical solution.
```

#### ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** "Joe Hunter" <@usaor.net>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VkbG2.317$a13.189170@news.sgi.net>`
- **References:** `<36e925bd.0@news.cadvision.com>`

```
Check out compiler switches.  I use columns 72 and after.  I do not remember
the exact one but I know it works.

Joe Hunter
```

##### ↳ ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** "R. Hayes" <rmch@cadvision.com>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e9907a.0@news.cadvision.com>`
- **References:** `<36e925bd.0@news.cadvision.com> <VkbG2.317$a13.189170@news.sgi.net>`

```
I did hunt through a few, but couldn't find it!

Let me know if you remember.

Joe Hunter <@usaor.net> wrote in message ...
>Check out compiler switches.  I use columns 72 and after.  I do not
remember
>the exact one but I know it works.
>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e9cbab.45059552@news1.ibm.net>`
- **References:** `<36e925bd.0@news.cadvision.com> <VkbG2.317$a13.189170@news.sgi.net> <36e9907a.0@news.cadvision.com>`

```
On Fri, 12 Mar 1999 15:10:20 -0700, "R. Hayes" <rmch@cadvision.com>
wrote:

>I did hunt through a few, but couldn't find it!
>
>Let me know if you remember.

Click on the compiler options, then choose SRF - you will be presented
with a screen with the valid options, your choice should probably be
FIX,FREE.

To get the EDITOR itself to work correctly open a file, then click the
OPTIONS, then the Environment setup.  Change your line length to 72.
```

##### ↳ ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ED1BFD.19EFCEF@NOSPAMhome.com>`
- **References:** `<36e925bd.0@news.cadvision.com> <VkbG2.317$a13.189170@news.sgi.net>`

```
Joe Hunter wrote:
> 
> Check out compiler switches.  I use columns 72 and after.  I do not remember
> the exact one but I know it works.
> 
> Joe Hunter

Different systems allow compiler switches to use columns 72 and after,
and/or columns 1-7.  But remember, these are expansions and it will be
harder to convert to a system which does not allow these.

And lots of people put maintenance codes in columns 73-80 or 1-7.  (at
the top they describe what this maintenance code does, and each line
changed has the code in the sequence area).
```

#### ↳ Re: Help with Fujitsu V4 editor/compiler (what else is new)

- **From:** sta.REMOVETHIS@a-info.dk (Steffen Arnecke)
- **Date:** 1999-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ec0817.38811404@news.uni2.dk>`
- **References:** `<36e925bd.0@news.cadvision.com>`

```

Yes, as I remember the manual there are defferent formats for the
source-code, where one is "free" (?) and can be used for comments
after col 72.

Still, I'm not sure, but check the manual regarding these formats.



"R. Hayes" <rmch@cadvision.com> wrote:

>Is there any way to compile Fujitsu V4 source code WITHOUT having to delete
>any information that is placed after column 72?
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
