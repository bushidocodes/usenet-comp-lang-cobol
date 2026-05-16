[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

_5 messages · 5 participants · 2005-06_

---

### What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

- **From:** dibalok@gmail.com
- **Date:** 2005-06-11T01:01:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118476896.252649.244650@z14g2000cwz.googlegroups.com>`

```
Hi,
I have declared some WS variables and a filler in a COBOL program. I
have initialised the filler as "VALUE SPACES". The problem is when i am
writing those WS Variables & the filler into a output file, i am
getting NULL in the filler.But when i am initialising the filler with
"VALUE ALL SPACES", Spaces are coming in the output file.
All i want to know, whether there is any difference between "VALUE
SPACES" and "VALUE ALL SPACES". If there are no differences then what
might be the possible cause for NULL values that are coming in the
filler.

Regards,
Dib
```

#### ↳ Re: What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2005-06-11T11:32:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kp0ma118ts8487jvtpquburncomu22n73i@4ax.com>`
- **References:** `<1118476896.252649.244650@z14g2000cwz.googlegroups.com>`

```
On 11 Jun 2005 01:01:36 -0700, dibalok@gmail.com enlightened us:

>Hi,
>I have declared some WS variables and a filler in a COBOL program. I
…[10 more quoted lines elided]…
>Dib

For os390 mainframe Cobol (all versions that I know of), there is no
difference between a working storage definition of VALUE SPACES and
VALUE ALL SPACES.  That is, if you have a field defined as FILLER PIC
X(20) VALUE SPACES, you'll get a field of 20 spaces.  Same thing if
you say VALUE ALL SPACES or VALUE SPACE.

First, what is the hex value you are seeing for the NULLS?  If it is
X'00', then look in your code for a move that might be moving LOW
VALUES to the group level name of the data description containing the
FILLER field.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


"I had a nightmare last night. I dreamed Dolly Parton 
was my mother and I was a bottle-baby."
--Henry Youngman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-06-11T17:47:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AsFqe.18923$1B2.18729@fe10.news.easynews.com>`
- **References:** `<1118476896.252649.244650@z14g2000cwz.googlegroups.com>`

```
In any standard-conforming compiler, there is never a difference between 
"spaces" and "all spaces" (both are "figurative constant" syntax).

Therefore, if you have an initial VALUE clause, with VALUE SPACES (in 
Working-Storage *not* File Section), then nothing should be placing nulls 
(low-value) in the filler items.

My best guess (without seeing your entire code) is that you are:

A) using a VALUE clause in WS
B) you "fill in" the non-Filler fields under the group item
C) you then MOVE the individual (filled-in) items to a record under your FD
D) write the file out

In this case, you are never "moving" the filler fields from WS to the file 
(before writing).

The other possibility is that you have a VALUE SPACES phrase under an FD - 
rather than WS.  In this case, many compilers (not the Standard) allow you to do 
this - as an extension BUT the VALUE clause is ignored (and will never cause 
spaces to be in the filler items).

There are probably several other possible causes of the symptom you are seeing. 
If you have an interactive debugger, I would use it - and "watch" the values in 
your filler items and see when they change from an initial spaces to nulls.
```

##### ↳ ↳ Re: What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-06-11T18:22:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QZFqe.5240$jS1.1969@newssvr17.news.prodigy.com>`
- **References:** `<1118476896.252649.244650@z14g2000cwz.googlegroups.com> <AsFqe.18923$1B2.18729@fe10.news.easynews.com>`

```
If this program is not a 'standalone executable' and is in fact a module
called with CALL  modulename, if modulename's PROGRAM-ID  does not contain
the IS INITIAL clause, the initial values will only be 'as per VALUE
statements'  the first time it is called in a run unit, or the first time it
is called after a CANCEL.

I know you did not state this as part of your question, but it wouldn't be
the first time someone has omitted something important
```

##### ↳ ↳ Re: What is the difference between "VALUE SPACES" and "VALUE ALL SPACES" ?

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2005-06-15T06:52:17+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42AFB401.3000804@fujitsu-siemens.com>`
- **References:** `<1118476896.252649.244650@z14g2000cwz.googlegroups.com> <AsFqe.18923$1B2.18729@fe10.news.easynews.com>`

```


William M. Klein schrieb:
> 
> The other possibility is that you have a VALUE SPACES phrase under an FD - 
…[7 more quoted lines elided]…
> 

The new standard allows VALUE clause in FILE and LINKAGE SECTION: these 
VALUE clauses are ignored unless there is an INITIALIZE ... VALUE WITH 
FILLER statement or an ALLOCATE ... INITIALIZED statement, where the 
VALUE-clause are used as initial values.

Best wishes
Rosa
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
