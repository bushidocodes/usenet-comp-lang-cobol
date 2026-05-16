[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXTFH TRACE - MF netx

_5 messages · 3 participants · 2001-12_

---

### EXTFH TRACE - MF netx

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2001-12-04T16:02:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ws6P7.249251$W8.9026648@bgtnsc04-news.ops.worldnet.att.net>`

```
    Does anybody know how to view the trace file that Net Express 3.1
creates
when you add the line "TRACE=ON" to the extfh.cfg file.  It has the
extension
.XFH, and is a binary file, not a text file.

    Windows version.
```

#### ↳ Re: EXTFH TRACE - MF netx

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-04T17:48:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0D0CFD.A7E3F89C@shaw.ca>`
- **References:** `<ws6P7.249251$W8.9026648@bgtnsc04-news.ops.worldnet.att.net>`

```


Russell Styles wrote:

>     Does anybody know how to view the trace file that Net Express 3.1
> creates
…[4 more quoted lines elided]…
>     Windows version.

I have used it, but forget how. So I'll dabble and get back to you in due
course.

To be perfectly truthful, although the feature is there it really doesn't
help you greatly, unless you are delving into bits and bytes. Given that
you follow your own set pattern for coding programs, (e.g. you handle
Masterfile edits in a standard fashion), doing an Animate against the
source is probably a much easier way to follow the problem.
Familiarization with your own programming style tends to point you at
your problem, given the information from the Animator.

Particularly with OO, the trace givers you a HUGE trace list when you are
into something like handling a string (CharacterArray) as it jumps to and
fro between many, many methods.

Jimmy
```

#### ↳ Re: EXTFH TRACE - MF netx

- **From:** "Robert Sales" <Robert.Sales@merant.com>
- **Date:** 2001-12-05T09:35:43
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ukq9b$eri$1@hyperion.eu.merant.com>`
- **References:** `<ws6P7.249251$W8.9026648@bgtnsc04-news.ops.worldnet.att.net>`

```
There's currently no facility available to our users to do anything with the
trace information.  This was really developed so that, in the case of any
problems, the user could send this stuff to us to analyse and hopefully to
get to the root of the problem.
Internally we do have a 'trace replay' facility but this has so far not been
made available externally - a probable product enhancement at some future
date.
```

#### ↳ Re: EXTFH TRACE - MF netx

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-06T03:22:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0EE4F6.3A48E613@shaw.ca>`
- **References:** `<ws6P7.249251$W8.9026648@bgtnsc04-news.ops.worldnet.att.net>`

```


Russell Styles wrote:

>     Does anybody know how to view the trace file that Net Express 3.1
> creates
…[4 more quoted lines elided]…
>     Windows version.

Russell,

My apologies for previous message - Should have read your Subject matter
more closely. I started to read up on Trace and then saw the reference to
EXTFH - and that rang a bell about your subject matter. I have no
knowledge of EXTFH so any contribution I would make would be irrelevant.
I've only used Trace directly from the IDE and solely with OO. Plus I see
EXTFH Trace is handled slightly differently.

Nevertheless, it still holds true. Unless you've got a real 'weirdo', a
consistency of your own programming style and stepping through Animator
will probably assist you better. It's a little like taking on the old
challenge of using 'D' in column 7.

The only person I am aware of who uses EXTFH is Ken Mullins. Ken, have
you ever used TRACE with the external file handler ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: EXTFH TRACE - MF netx

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2001-12-06T14:10:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c0fc355.0@newsman.viper.net>`
- **References:** `<ws6P7.249251$W8.9026648@bgtnsc04-news.ops.worldnet.att.net> <3C0EE4F6.3A48E613@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
> The only person I am aware of who uses EXTFH is Ken Mullins. Ken, have
> you ever used TRACE with the external file handler ?


I have used the trace option when starting fileshare via the command prompt,
but now I use the FSSERVICE service for Windows NT and up...Try looking in
FSScreen.lst dataset and see if trace entries are placed there...This
dataset is where the FS Service puts it's messages...

kenmullins
newnan, ga USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
