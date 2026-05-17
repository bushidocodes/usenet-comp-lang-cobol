[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for best text search/replace method

_4 messages · 4 participants · 1996-08_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Looking for best text search/replace method

- **From:** "brian hawco" <ua-author-15700140@usenetarchives.gap>
- **Date:** 1996-08-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<321AB6EA.745A@fox.nstn.ns.ca>`

```

Hi
I'm trying to determine the best utility/program/method to use to search
for and possibly replace a string of text in several hundred COBOL
programs. I would like something that would allow me to use wildcards and
search thru any copy libraries that a program may be using. Any
suggestions would be welcome. (At this point, I'm looking at using one of
either: Norton FileFind / Grep / Workbench / ISPF.)

Thanks,
Brian
```

#### ↳ Re: Looking for best text search/replace method

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-08-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3da3e6dd2a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<321AB6EA.745A@fox.nstn.ns.ca>`
- **References:** `<321AB6EA.745A@fox.nstn.ns.ca>`

```

Brian Hawco wrote:

› I'm trying to determine the best utility/program/method to use to search
› for and possibly replace a string of text in several hundred COBOL
› programs. I would like something that would allow me to use wildcards and
› search thru any copy libraries that a program may be using. Any
› suggestions would be welcome.

Hi. You don`t say what environment you`re running on, but this is exactly what
the Unix "sed" command is for - it`s an extremely powerful non-interactive
editor. A version of it exists in the MKS Toolkit for the PC and I expect there
is a Gnu version and/or other PD versions also.

Cheers, Kev.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own. I doubt that anyone else would want them.
STUFF FOR SALE: Here!
```

#### ↳ Re: Looking for best text search/replace method

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-08-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3da3e6dd2a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<321AB6EA.745A@fox.nstn.ns.ca>`
- **References:** `<321AB6EA.745A@fox.nstn.ns.ca>`

```

Brian Hawco wrote:
: I'm trying to determine the best utility/program/method to use to search
: for and possibly replace a string of text in several hundred COBOL
: programs.

Previous suggestions sound good. I have found PERL _very_ useful for
serious text manipulation; it's a full-featured programming language
that runs on many platforms and has even more powerful pattern features
than 'sed'. I've used a PERL program to find and replace string
patterns across a whole directory at a time.

(If you want to pursue this, go to the comp.lang.perl newsgroup which will
have _many_ text-manipulation wizards waiting to help you.)

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

#### ↳ Re: Looking for best text search/replace method

- **From:** "mg..." <ua-author-17087263@usenetarchives.gap>
- **Date:** 1996-08-25T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3da3e6dd2a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<321AB6EA.745A@fox.nstn.ns.ca>`
- **References:** `<321AB6EA.745A@fox.nstn.ns.ca>`

```

In <321··.@fox··s.ca>, Brian Hawco writes:
› ... to search for and possibly replace a string of text in several hundred COBOL
› programs...

You also mentioned ISPF... so, if you are on a mainframe and if you also
have File Aid installed, that would be your best tool for the job.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
