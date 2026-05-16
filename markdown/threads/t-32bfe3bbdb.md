[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about ISPF/PDF editor usage for COPY/PASTE within two session

_11 messages · 8 participants · 2002-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** calvin5867705@yahoo.com (link)
- **Date:** 2002-10-26T21:43:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5d879bfe.0210262043.29ba86b7@posting.google.com>`

```
How can I share the information between two ISPF/PDF sessions ?

For exmaple, If I have one PDF session open right now. I put C Command
for one lines copying from.  Then I open the second session (press F2
key )and the corresponding file, and put A Command. When i press enter
key. I get the message "COPY/MOVE PENDING". which means the copy is
not successful.

Can anyone tell me what is the problem for that ? Or I need any
profile setting ???

Thanks a lot for your answer.

(It runs perfect within one seesion editor.)
```

#### ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** gregjohnson@comcast.net
- **Date:** 2002-10-27T01:14:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rv0nru8iptvef16er4hn8l71437fqukoao@4ax.com>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com>`

```
You have to use the CUT and PASTE commands on the command line when
you have muliple sessions open.



On 26 Oct 2002 21:43:38 -0700, calvin5867705@yahoo.com (link) wrote:

>How can I share the information between two ISPF/PDF sessions ?
>
…[11 more quoted lines elided]…
>(It runs perfect within one seesion editor.)
```

#### ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-10-27T07:12:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WlMu9.8094$VJ5.459303@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com>`

```

link <calvin5867705@yahoo.com> wrote in message news:5d879bfe.0210262043.29ba86b7@posting.google.com...
> How can I share the information between two ISPF/PDF sessions ?
>
…[11 more quoted lines elided]…
> (It runs perfect within one seesion editor.)

I usually require this capability when transferring blocks of code
from one PDS member to another.

I have 3 techniques which I find useful, depending on the situation.

1  I copy PDS member #1 in its entirety to the end of PDS member #2.
    Then I clean up PDS member #2.  I block delete the lines I don't want.
    When I find some old member #1 code that I want to keep, I block move it
     to where it needs to be.

2  I open both PDS members in the same PDS, even if I have to move
    one of them in temporarily from another PDS.  When I find some code
    that I want to keep, I CC the block and enter CRE TT on the command line
    and hit <Enter>.  That creates a new PDS member called TT containing
    the code I want to transfer.  Then I click over to my other session,
    enter A at my insert point, and type MOVE TT on the command line.
    Once I've got this going, and have a number of such moves, I simply
    use PF12 to restore the commands so that I don't have to keep typing them.

3  I use straight cut-and-paste or copy-and-paste.  For example, if I have 9 lines
    to move or copy, I highlight it and cut it (deleting the blank lines created),
    or copy it, find my insert point, type I9 to create the necessary blank lines,
    and then paste.

The only difficult part is to stay focused on the task when it gets repetitive.
```

##### ↳ ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-10-27T13:52:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KcSu9.1254$mN6.358505@newssrv26.news.prodigy.com>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com> <WlMu9.8094$VJ5.459303@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message
news:WlMu9.8094$VJ5.459303@bgtnsc05-news.ops.worldnet.att.net...

> The only difficult part is to stay focused on the task when it gets
repetitive.

Thank you for sharing. I thought it was only me had that problem.

Maybe we could form a support group.....OK, I'll go first...

"My name is Michael, and I am a daydreamer...I haven't had a daydream in
thirteen days..."


MCM
```

#### ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-10-27T11:09:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com>`

```
On 26 Oct 2002 21:43:38 -0700 calvin5867705@yahoo.com (link) wrote:

:>How can I share the information between two ISPF/PDF sessions ?

:>For exmaple, If I have one PDF session open right now. I put C Command
:>for one lines copying from.  Then I open the second session (press F2
:>key )and the corresponding file, and put A Command. When i press enter
:>key. I get the message "COPY/MOVE PENDING". which means the copy is
:>not successful.

:>Can anyone tell me what is the problem for that ? Or I need any
:>profile setting ???

You would have to program it.

ISPF/PDF Edit does not have a copy from screen to screen function.

You can use the CUT and PASTE macros to do the trick, but this will involve
first completing the CUT function on the source screen, SWAPping, and issuing
the PASTE function.
```

##### ↳ ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-10-27T21:56:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0210272156.631af2d8@posting.google.com>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com> <pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com>`

```
Some other thoughts that may be useful:

You can cut multiple times before pasting and the aggregate lines cut
will appear in the pasted PDS member in the same order that they were
cut.

BTW, if you cut and don't paste, and cut again later in the same ISPF
session, both cuts will appear in the pasted PDS member.

As I recall, you can avoid the above situation by using a name in the
cut command, i.e.: cut cutnbr1. If you cut again, use another name.
When you paste, though, you must use the appropriate name to recall
the desired data.

Jack

Binyamin Dissen <postingid@dissensoftware.com> wrote in message news:<pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com>...
> On 26 Oct 2002 21:43:38 -0700 calvin5867705@yahoo.com (link) wrote:
> 
…[17 more quoted lines elided]…
> the PASTE function.
```

###### ↳ ↳ ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-10-29T03:59:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Jnv9.32819$Mb3.1409979@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com> <pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com> <8a2d426e.0210272156.631af2d8@posting.google.com>`

```

Jack Sleight <jacksleight@hotmail.com> wrote in message news:8a2d426e.0210272156.631af2d8@posting.google.com...
> Some other thoughts that may be useful:
>
…[5 more quoted lines elided]…
> session, both cuts will appear in the pasted PDS member.

I don't believe that that is the default.

IIRC, to do it as you say, you must elect cumulative cut/copy
by setting an optional parameter.

Otherwise, a second cut or copy without an intervening paste
will overlay and negate the first cut or copy.

However, I don't remember if it is a Windows option
(don't think so), an ExtraPC! option, or (probably) an ISPF option.
```

###### ↳ ↳ ↳ Question about ISPF/PDF editor usage for COPY/PASTE within two session

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-10-29T16:28:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0210291628.7d980878@posting.google.com>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com> <pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com> <8a2d426e.0210272156.631af2d8@posting.google.com> <3Jnv9.32819$Mb3.1409979@bgtnsc04-news.ops.worldnet.att.net>`

```
Hi Hugh,

I use ISPF for OS/390 and multiple cuts w/1 paste works Just as I've outlined.

Regards, Jack.



"Hugh Candlin" <no@spam.com> wrote in message news:<3Jnv9.32819$Mb3.1409979@bgtnsc04-news.ops.worldnet.att.net>...
> Jack Sleight <jacksleight@hotmail.com> wrote in message news:8a2d426e.0210272156.631af2d8@posting.google.com...
> > Some other thoughts that may be useful:
…[17 more quoted lines elided]…
> (don't think so), an ExtraPC! option, or (probably) an ISPF option.
```

###### ↳ ↳ ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

_(reply depth: 5)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-10-30T00:45:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mYFv9.13271$VJ5.789972@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com> <pv9nruof2ivho0t6hks5rmr3ub08u7qf7u@4ax.com> <8a2d426e.0210272156.631af2d8@posting.google.com> <3Jnv9.32819$Mb3.1409979@bgtnsc04-news.ops.worldnet.att.net> <8a2d426e.0210291628.7d980878@posting.google.com>`

```

Jack Sleight <jacksleight@hotmail.com> wrote in message news:8a2d426e.0210291628.7d980878@posting.google.com...
> Hi Hugh,
>
> I use ISPF for OS/390 and multiple cuts w/1 paste works Just as I've outlined.

I don't doubt it for a second.  I just don't think it is the default.
I seem to remember discovering a menu item which you could check
to enable/disable the cumulative feature.

Possibly the default is established by the systems programmer,
in which case it is quite possible that your default would differ from mine.

I do not in any way dispute the existence of cumulative cut/copy and paste.
```

###### ↳ ↳ ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

_(reply depth: 6)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-10-30T13:35:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021030083500.24115.00001796@mb-md.aol.com>`
- **References:** `<mYFv9.13271$VJ5.789972@bgtnsc05-news.ops.worldnet.att.net>`

```
Hugh Candlin writes ...

>Jack Sleight <jacksleight@hotmail.com> wrote in message
>news:8a2d426e.0210291628.7d980878@posting.google.com...
…[15 more quoted lines elided]…
>

The EDSET (a.k.a. EDITSET) lets you set cut / paste defaults (along with some
other attributes); I beleive the IBM-supplied defaults may have changed from
the original ones in a recent release.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Question about ISPF/PDF editor usage for COPY/PASTE within two session

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-10-28T15:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<apjjem$7sq$1@peabody.colorado.edu>`
- **References:** `<5d879bfe.0210262043.29ba86b7@posting.google.com>`

```

On 26-Oct-2002, calvin5867705@yahoo.com (link) wrote:

> For exmaple, If I have one PDF session open right now. I put C Command
> for one lines copying from.  Then I open the second session (press F2
> key )and the corresponding file, and put A Command. When i press enter
> key. I get the message "COPY/MOVE PENDING". which means the copy is
> not successful.

Use the cut and paste commands for this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
