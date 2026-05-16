[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dummy

_6 messages · 5 participants · 2004-10_

---

### Dummy

- **From:** "Ron S" <NoSpam@SpamStopper.org>
- **Date:** 2004-10-06T22:01:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com>`

```
So....I guess we're all agreed? There should be no problem using DD DUMMY for
an output file except sometimes you need a DCB which is hardly unpredictable. But, no one
knows why IBM, in the Enterprise COBOL manual, says results are unpredictable for
DD DUMMY output nor has anyone any experience with it not doing exactly what they
expect or "predict". Can we therefore say the manual is incorrect? Or at least mysterious?

I'm going to post this question on mvshelp see if anyone has a clue what this is supposed to mean.
```

#### ↳ Re: Dummy

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-10-07T05:09:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c49d.2218165$ic1.226989@news.easynews.com>`
- **References:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com>`

```
I have sent my question to my "usually reliable source" - but still haven't 
heard anything back.

One issue that *might* cause a problem is if you have a EXCEPTION DECLARATIVE. 
I am not certain if a DD DUMMY might "interfer" with that.  I know that IBM says 
to code

    EROPT=ACC

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/1.9.3

but most people do NOT actually do so.

As far as coding a DCB for a DD DUMMY file, at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/1.9.4.1

it says,
 "DCB attributes coded for a DD DUMMY do not override those coded in the FD 
entry of your COBOL program. "
```

##### ↳ ↳ Re: Dummy

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-10-07T12:30:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0410071130.807f504@posting.google.com>`
- **References:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com> <1c49d.2218165$ic1.226989@news.easynews.com>`

```
Bottom Posting


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<1c49d.2218165$ic1.226989@news.easynews.com>...
> I have sent my question to my "usually reliable source" - but still haven't 
> heard anything back.
…[36 more quoted lines elided]…
> > is supposed to mean.

As I remember it (many years ago) the reason for needing the DCB in
the JCL for an output file was to complete the DCB information,
specifically the blocksize, which was defined as zero in the FD to
allow variable blocking according to the JCL.

Robert
```

#### ↳ Re: Dummy

- **From:** "Pete Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2004-10-11T15:16:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1097460991.GoVk7xejNPd9kpRI5Gm2vg@teranews>`
- **References:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com>`

```
Ron,

I can't say for sure the following applies in this case, but it might...

Put yourself in the place of the manual writer.

A situation arises where you are not 100% sure of the outcome. You approach
the software developers and they are not entirely sure either. There are
many complex factors that make it nearly impossible to check all possible
code and see what happens or what the impacts are for non-compliance. What
is for certain is that if you do the RIGHT things, the correct results will
follow.

So you want to document that it is on the user's own head if he does not
comply, even though it COULD be OK.

The "standard" phrase for this is "results are unpredictable".

I have used this phrase when writing manuals, for exactly this scenario.
(The results may very well be predictable, but I can't predict them at time
of writng.)

BOTTOM LINE: Don't read too much into this phrase. If something works, then,
the empirical approach beats the theoretical one in much the same way as a
straight flush beats four aces... unexpectedly.

Pete.



"Ron S" <NoSpam@SpamStopper.org> wrote in message
news:KfadnQJ6EpI-LPncRVn_vA@giganews.com...
> So....I guess we're all agreed? There should be no problem using DD DUMMY
for
> an output file except sometimes you need a DCB which is hardly
unpredictable. But, no one
> knows why IBM, in the Enterprise COBOL manual, says results are
unpredictable for
> DD DUMMY output nor has anyone any experience with it not doing exactly
what they
> expect or "predict". Can we therefore say the manual is incorrect? Or at
least mysterious?
>
> I'm going to post this question on mvshelp see if anyone has a clue what
this is supposed to mean.
>
>
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Dummy

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-10-17T11:17:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0410171017.501f9710@posting.google.com>`
- **References:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com>`

```
I'm wondering if the recent intro of "environment variables" prompted
this CYA note in the COBOL manuals.

Jack.


"Ron S" <NoSpam@SpamStopper.org> wrote in message news:<KfadnQJ6EpI-LPncRVn_vA@giganews.com>...
> So....I guess we're all agreed? There should be no problem using DD DUMMY for
> an output file except sometimes you need a DCB which is hardly unpredictable. But, no one
…[4 more quoted lines elided]…
> I'm going to post this question on mvshelp see if anyone has a clue what this is supposed to mean.
```

##### ↳ ↳ Re: Dummy

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-10-18T15:15:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0410181415.276c4469@posting.google.com>`
- **References:** `<KfadnQJ6EpI-LPncRVn_vA@giganews.com> <8a2d426e.0410171017.501f9710@posting.google.com>`

```
One other anomaly using DUMMY:

If you concat a DUMMY file any other place but the last file position,
the first read of the DUMMY sends you to EOF and all succeeding
concats are not read.

Jack




jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0410171017.501f9710@posting.google.com>...
> I'm wondering if the recent intro of "environment variables" prompted
> this CYA note in the COBOL manuals.
…[11 more quoted lines elided]…
> > I'm going to post this question on mvshelp see if anyone has a clue what this is supposed to mean.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
