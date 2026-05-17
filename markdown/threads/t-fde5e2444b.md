[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VSAM loading optimization

_6 messages · 6 participants · 1997-09 → 1997-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### VSAM loading optimization

- **From:** "mur..." <ua-author-3122474@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34313887.335043998@nntp.noc.netcom.net>`

```

I have a Cobol II program that is loading a VSAM file using the speed
option. The program reformats records during the load so I cannot use
IDCAMS. Is there any suggested way to speed it up.

Thanks,

Murray
```

#### ↳ Re: VSAM loading optimization

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fde5e2444b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34313887.335043998@nntp.noc.netcom.net>`
- **References:** `<34313887.335043998@nntp.noc.netcom.net>`

```

Murray Bob wrote:
› 
› I have a Cobol II program that is loading a VSAM file using the speed
…[5 more quoted lines elided]…
› Murray

Could you write the reformatted records to a flat file out of your
program and then use IDCAMS load utility stuff in a subsequent step? The
total time might be less and the freespace would be all lined up also.
Maybe I don't understand the situation fully as to what the reformat is
and how intricatly it is mixed into the load.

John
```

#### ↳ Re: VSAM loading optimization

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fde5e2444b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34313887.335043998@nntp.noc.netcom.net>`
- **References:** `<34313887.335043998@nntp.noc.netcom.net>`

```

Murray Bob wrote:
› 
› I have a Cobol II program that is loading a VSAM file using the speed
…[5 more quoted lines elided]…
› Murray

Murray,

Since you used the words 'load' and 'speed' I will assume you're starting with
an empty cluster. Here's a couple ideas:

Whenever possible, I like to write a flat physical-sequential file and use
IDCAMS REPRO to load it (doing so will probably negate the need for SPEED - no
pun intended). I'm sure this would be faster than writing them from your COBOL
program. Read on...

Whether or not you use this method, it's a *very* good idea to make sure the
records being added are already in key sequence. If you can't sort the input to
your COBOL program, or if the input is from multiple sources, the flat file
method facilitates this 'cause you can sort it before the REPRO. If this isn't
an option for you, consider adding an internal sort to your COBOL program;
instead of writing the records directly to your VSAM file, release them to the
sort, then return the records (which will now be in key sequence) and write the
sorted records to your VSAM file. This may help a lot.

Also, if the records are already sorted (do you detect a theme?), define your
cluster with zero percent CI/CA freespace to do the load, then ALTER it
afterwards to the desired freespace.

You can also experience potentially great performance gains by increasing the
size and/or number of data and/or index buffers. How you do this depends
somewhat on the physical and logical structure of your VSAM file but is worth
looking into.

Hope this helps a little...I'm sure you'll get a bunch more helpful hints...

Cheers :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: VSAM loading optimization

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fde5e2444b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34313887.335043998@nntp.noc.netcom.net>`
- **References:** `<34313887.335043998@nntp.noc.netcom.net>`

```



Murray Bob wrote in article
<343··.@nnt··m.net>...
› I have a Cobol II program that is loading a VSAM file using the speed
› option. The program reformats records during the load so I cannot use
› IDCAMS. Is there any suggested way to speed it up.
›

Years and years and years ago we converted from a tape update system to
VSAM. The tape update was FASTER, because adds of records under VSAM are
very very slow. We commissioned an assembler king to write us some ASM
code to do what we call "MASS ADDS". This sped it up FANTASTICALLY.

If you don't have someone who can do that, you may consider adding the
records to a tape file then REPROing back to VSAM when the update is
complete.
```

#### ↳ Re: VSAM loading optimization

- **From:** "a&b dossett" <ua-author-17071730@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fde5e2444b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34313887.335043998@nntp.noc.netcom.net>`
- **References:** `<34313887.335043998@nntp.noc.netcom.net>`

```

Bob

1. Open the file for OUTPUT, not I-O
2. Use ACCESS IS SEQUENTIAL
3. Records must be in key sequence.
4. Specify data buffers in your JCL, but not index buffers.
5. If the file is being used for subsequent online update, do specify
enough
freespace otherwise you will suffer from CI and CA splits.

Andy



Murray Bob wrote in article
<343··.@nnt··m.net>...
› I have a Cobol II program that is loading a VSAM file using the speed
› option.  The program reformats records during the load so I cannot use
…[5 more quoted lines elided]…
›
```

#### ↳ Re: VSAM loading optimization

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-10-04T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fde5e2444b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<34313887.335043998@nntp.noc.netcom.net>`
- **References:** `<34313887.335043998@nntp.noc.netcom.net>`

```

As others have already written, use OUTPUT, pre-sort your records, write
sequentially, and override BUFND in your JCL. Make that BUFND as high as
is reasonable, at least a full track worth, preferably a full cylinder
worth.

One other thing to be careful about is freespace. It is a good idea to
allocate freespace if you are going to be doing updates, particularly
inserts. However, you can trip yourself up by leaving too much freespace
to allow good density of packing on your DASD. This depends greatly on the
relationship between your max record size, track size, CI size, CA size,
and the freespace parameters you use.

In extreme examples, you can end up with one record per cylinder. This
wouldn't happen in real life, but I've seen one record/track more than
once. When you get a situation like this, your loads are *very* slow (not
to mention you use more extents than you thought you would...)

Murray Bob wrote in article
<343··.@nnt··m.net>...
› I have a Cobol II program that is loading a VSAM file using the speed
› option.  The program reformats records during the load so I cannot use
…[5 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
