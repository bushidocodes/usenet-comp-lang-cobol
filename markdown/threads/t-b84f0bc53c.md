[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with COBOL85 Error Codes

_3 messages · 3 participants · 1999-09_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Help with COBOL85 Error Codes

- **From:** "J. Keith Jackson" <jkeithj@bellsouth.net>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdCH3.8333$E85.102162@news1.mia>`
- **References:** `<nauH3.9069$OU1.73830@news4.mia> <01bf08ad$f7c96a80$e13563c3@default>`

```
Simon:

Thanks for the reply.  In the interim I discovered the problem.  Apparently
to run this program, SHARE.EXE must be loaded.  I had failed to include that
in my AUTOEXEC.BAT on the notebook.

But, for the sake of completeness:

>Where the data files are when you try running on the laptop, where they
>are when you run them on the desktop

Laptop:  Program in C:\CMSPRG, data in C:\CMSFIL.
Original Desktop:  C:\CMSPRG and D:\CMSFIL.
Win98 Desktop:  D:\CMSPRG and D:\CMSFIL.

The appropriate file was edited to reflect the location of the data files.
I've done this before with no problem.

>What the data files do, and their names

The data files are databases, with various names too numerous to include.

>Are the data files in the same folder as the executing program file(s)?

No, they are in a different one as noted above.

>The error codes are compiler specific, you need to find out which compiler
>or "flavour" you are using.

I have no clue about that.

But as I said, I discovered that apparently SHARE.EXE must be loaded in
order for this app to function.  I still don't understand why "recovering"
them would change this, but...as long as I have it working I won't ask.

Again, thank you for your response.

J. Keith Jackson
jkeithj@bellsouth.net
```

#### ↳ Re: Help with COBOL85 Error Codes

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KzKH3.18$iG2.1314@client>`
- **References:** `<nauH3.9069$OU1.73830@news4.mia> <01bf08ad$f7c96a80$e13563c3@default> <cdCH3.8333$E85.102162@news1.mia>`

```
J. Keith Jackson <jkeithj@bellsouth.net> wrote in message
news:cdCH3.8333$E85.102162@news1.mia...
[snip]
> But as I said, I discovered that apparently SHARE.EXE must be loaded in
> order for this app to function.  I still don't understand why "recovering"
> them would change this, but...as long as I have it working I won't ask.

Mr. Jackson:

I cannot speak for GEAC, but I think I have some insight into this
particular situation.

This is a multiuser accounting package that you are moving from one machine
to another.  And, therein lies the source of the symptoms you are
experiencing.

The multiuser file system used by the package, in order to communicate with
other (potential) users on the same network, must record in each file
overhead that the particular file is open in a shared mode by a user.  This
is really not an issue on the network since it is, after all, a multiuser
file system.  This is just a means to communicate with other cooperative
processes (in this case, other users attached to the network at your office)
that the files are being used by more than one user, and that certain steps
must be taken by each cooperating process to assure integrity of the data.
If something happens while a user has a file open on your network (for
instance, the user turns off his PC without exiting the accounting package)
these markers remain in the file overhead.  This is of little consequence on
the network, since the other users continue on their merry way.

However, you took home a snapshot of the files, at least some of which were
still marked as being open by some user.  But now your configuration
indicates that you are not on a network, and therefore are not in a
situation where other users might indeed have files open.  This clearly
indicates that a file integrity problem might exist and the file system
refuses to go on without having run the recovery program.  The recovery
program, having gained exclusive, rather than shared, access to the file,
can safely reset the markers that indicate other users have the file open.

By installing SHARE you are fooling the file system into thinking that a
multiuser environment exists (the other user could be another process on the
same machine), so the existence of the markers does not, by itself, indicate
an integrity problem.

What to do?

Fisrt, you must be quite cautious that you are not losing transactions when
you take work home.  Apparently you are the single user of this system at
work, so this is an issue that you can control.

Second, you should run the recovery program at work on all files when no
users are using the package.  This will reset the markers that have built up
over the months.

Please be assured that while this has been an inconvenience for you, it is
better in the long run for a file system -- responsible for holding your
company's vital data -- err on the side of caution.

Best regards,
Tom Morrison
Liant Software Corporation
```

#### ↳ Re: Help with COBOL85 Error Codes

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ss9kg$2if$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<nauH3.9069$OU1.73830@news4.mia> <01bf08ad$f7c96a80$e13563c3@default> <cdCH3.8333$E85.102162@news1.mia>`

```
    This is just a shot in the dark, but some cobol runtimes keep track of
how many times a database has been opened and closed, and if a mismatch is
found for some reason (user turns pc off without exiting program, program
abends, program ends without closing data files) it assumes that the
databases are corrupt and wants to have them rebuilt.  But when on a network
(share loaded), that rule is not enforced.


J. Keith Jackson <jkeithj@bellsouth.net> wrote in message
news:cdCH3.8333$E85.102162@news1.mia...
> Simon:
>
> Thanks for the reply.  In the interim I discovered the problem.
Apparently
> to run this program, SHARE.EXE must be loaded.  I had failed to include
that
> in my AUTOEXEC.BAT on the notebook.
>
<SNIP>

> But as I said, I discovered that apparently SHARE.EXE must be loaded in
> order for this app to function.  I still don't understand why "recovering"
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
