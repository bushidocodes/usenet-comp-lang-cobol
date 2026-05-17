[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Abend Error

_4 messages · 4 participants · 1997-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Abend Error

- **From:** "bing" <ua-author-610634@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<341A3837.41FB@bigfoot.com>`

```


Well, just thought I would throw this one out to get some help if I
could.

I am running a Y2K tool(on a non Y2K project) and doing an impact
analysis. This JCL puts the output to two PDS's and everytime I run the
job I get an Abend SE37 on one of those output files.

Since the SE37 is a size error I went back and reallocated the output
PDS and upped it to cylinders over tracks this time. The funny thing is
that whenever I try to give it a large number of cylinders it basically
won't let me(I'm using panel 3.2 to allocate it). I will allocate it to
800 cylinders(this PDS actually should do the trick with 300)) and even
play with the blocks. However if I go back in and take a look at the
PDS the allocation changes on me. It will drop down to anywhere from 36
to 80 cylinders from 800. Ops isn't doing this to me.

Does anyone know why the system would be doing this? There is plenty of
room on the volume to allow anywhere from 300 to 800 at least.

Thanks, Bing
```

#### ↳ Re: Abend Error

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1997-09-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc300d77ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<341A3837.41FB@bigfoot.com>`
- **References:** `<341A3837.41FB@bigfoot.com>`

```

Well I dunno why it's releasing space on you... BUT
an E37 means you don't have enough directory blocks for the number
of members in the PDS. You can increase cylinders to a million
but if you don't up the number of directory blocks you're going
to get E37's forever.
```

#### ↳ Re: Abend Error

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-09-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc300d77ec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<341A3837.41FB@bigfoot.com>`
- **References:** `<341A3837.41FB@bigfoot.com>`

```

bing wrote:
›
› [snippage]
›
› Since the SE37 is a size error I went back and reallocated the output
› PDS and upped it to cylinders over tracks this time.

This is the core of things.

What you ask, Grasshopper, is part of the Zen of programming... how
large is an output-file, eh? Try sending the output to tape and seeing
what you get; you might then adjust the JCL appropriately.

DD
```

#### ↳ Re: Abend Error

- **From:** "lars bjerges" <ua-author-6588782@usenetarchives.gap>
- **Date:** 1997-09-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc300d77ec-p4@usenetarchives.gap>`
- **In-Reply-To:** `<341A3837.41FB@bigfoot.com>`
- **References:** `<341A3837.41FB@bigfoot.com>`

```

Are you using SMS?
There are ways in which "big brother" will override your allocations
by means of e.g. "dataclass"-association.

You donï¿½t say if the two output files are two different members on
the same PDS.
Usually it is NOT a good idea to use more than one PDS-member
(in the same library) for output at the same time.

Lars


bing skrev i inlï¿½gg <341··.@big··t.com>...
› Well, just thought I would throw this one out to get some help if I
› could.  
…[18 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
