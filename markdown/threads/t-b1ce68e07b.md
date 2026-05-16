[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you open a file in CICS?

_6 messages · 5 participants · 2004-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### How do you open a file in CICS?

- **From:** johnchittazhath@yahoo.com (John Varughese)
- **Date:** 2004-11-09T11:00:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4c71f2.0411091100.149af3d3@posting.google.com>`

```
How do you open a file in CICS?
How to submit a JCL from CICS program?
```

#### ↳ Re: How do you open a file in CICS?

- **From:** docdwarf@panix.com
- **Date:** 2004-11-09T14:13:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmr4tm$mlk$1@panix5.panix.com>`
- **References:** `<f4c71f2.0411091100.149af3d3@posting.google.com>`

```
In article <f4c71f2.0411091100.149af3d3@posting.google.com>,
John Varughese <johnchittazhath@yahoo.com> wrote:
>How do you open a file in CICS?

You hire someone who knows how to or send someone to a class where they 
will be trained to do so.

>How to submit a JCL from CICS program?

See above.

DD
```

##### ↳ ↳ Re: How do you open a file in CICS?

- **From:** "Ron" <NoMoSpam@Spamstopper.org>
- **Date:** 2004-11-09T17:29:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dImdnV8stJJyzwzcRVn_vA@giganews.com>`
- **References:** `<f4c71f2.0411091100.149af3d3@posting.google.com> <cmr4tm$mlk$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cmr4tm$mlk$1@panix5.panix.com...
> In article <f4c71f2.0411091100.149af3d3@posting.google.com>,
> John Varughese <johnchittazhath@yahoo.com> wrote:
…[9 more quoted lines elided]…
> DD

You could also RTFM. It isn't that hard.
```

###### ↳ ↳ ↳ Re: How do you open a file in CICS?

- **From:** docdwarf@panix.com
- **Date:** 2004-11-09T18:35:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmrk7r$9cj$1@panix5.panix.com>`
- **References:** `<f4c71f2.0411091100.149af3d3@posting.google.com> <cmr4tm$mlk$1@panix5.panix.com> <dImdnV8stJJyzwzcRVn_vA@giganews.com>`

```
In article <dImdnV8stJJyzwzcRVn_vA@giganews.com>,
Ron <NoMoSpam@Spamstopper.org> wrote:
>
><docdwarf@panix.com> wrote in message news:cmr4tm$mlk$1@panix5.panix.com...
…[12 more quoted lines elided]…
>You could also RTFM. It isn't that hard. 

I don't recall saying that this was the only answer... but it seems to me 
that someone was posting exam-questions and so I responded as I did.

DD
```

#### ↳ Re: How do you open a file in CICS?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-11-10T06:16:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<snikd.874818$Gx4.259153@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<f4c71f2.0411091100.149af3d3@posting.google.com>`
- **References:** `<f4c71f2.0411091100.149af3d3@posting.google.com>`

```


John Varughese wrote:

> How do you open a file in CICS?
> How to submit a JCL from CICS program?

Opening a file in CICS is not usually done by typical applications. 
In fact the command to do so is a system programming command, not an 
application programming command.  Without checking my manuals, it 
looks something like this:

EXEC CICS SET
     FILE (file-name)
     OPEN (or CLOSED)
     ENABLED (or DISABLED)
END-EXEC.

You can OPEN a file without ENABLE and also CLOSE a file without 
DISABLE.  A file that is CLOSED and ENABLED will automatically open 
when it is first referenced by an application program, although there 
are some exceptions related to CICS-maintained or user-maintained data 
tables.  CICS VSAM data tables are probably not something you're 
likely to use.

I've never needed to write a CICS program to submit batch JCL, but it 
is possible to do so.  You will probably need to have your friendly 
system programmers define a Destination Control Table entry to write 
your JCL to.  This topic is discussed periodically in 
bit.listserv.ibm-main.  You might want to try searching their archives.

http://groups.google.com/advanced_group_search

I hope that helps!
```

#### ↳ Re: How do you open a file in CICS?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-11-15T04:05:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20041114230533.23235.00000727@mb-m03.aol.com>`
- **References:** `<f4c71f2.0411091100.149af3d3@posting.google.com>`

```
>From: johnchittazhath@yahoo.com  (John Varughese)
>Date: 11/9/04 2:00 PM Eastern Standard Time

Talking mainframe here:

>How do you open a file in CICS?

You don't usually.  The system takes care of this mundane stuff most times. 
I've never written a CICS program where I've had to open or close a file.

>How to submit a JCL from CICS program?

SPOOL commands or a TS QUE to the internal reader - 

Now go forth and RTFM and your text book for the nitty gritty.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
