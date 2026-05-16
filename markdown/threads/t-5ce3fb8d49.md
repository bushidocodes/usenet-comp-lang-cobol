[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acuserver on Linux

_3 messages · 2 participants · 1999-09_

---

### Acuserver on Linux

- **From:** "Robert Annandale" <rob_a@unipharm.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f0f270$0$6415@fountain.mindlink.net>`

```
I recently installed Acuserver 4.2.0 for Linux ELF RedHat 5-Intel
on our RedHat 5.2 Server.
We used to have Acuserver 4.2.0 successfuly running on SCO 5.05.
There were no problems on the SCO box.

I used the same a_srvcfg file on the Linux box as I used on the SCO box.
This is because I anticipate opening more than 32 files at once and SCO's
Acuserver configuration successfully catered for that.

I can see Acuserver running on the Linux box and it does allow a connection
however as soon as a second user attempts to connect, Acuserver sends
an error to the server console announcing ' /etc/Acuserver  Too many files
opened'
On the client side, a 94.10 (74 status code) appears.
This indicates  Too many files open by the current process. (open)
Each user only opens 9 files.

My MAX-FILES in a_srvcfg is set to 127, way greater than the default 32.
Yet this problem still occurs.

I suspect that my Linux kernel has a restriction on the number of files
that each process can open, perhaps a security feature....

Does anyone have Linux/Acuserver experience/suggestions.

_________________________
Robert Annandale

I have never let my schooling interfere with my education - Mark Twain.
```

#### ↳ Re: Acuserver on Linux

- **From:** "Pete Withey" <peterw@acucorp.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sr2mb$a7m$1@news.cerf.net>`
- **References:** `<37f0f270$0$6415@fountain.mindlink.net>`

```
Robert:

  One thing rings a bell here. The default for MAX_FILES is 32 unless
changed.  Try running acuserver with a trace and make sure that the a_srvcfg
file is being picked up.  You do this by starting acuserver:

acuserve -start -t3 -l -e errfl

And then reproducing the behavior and looking at "errfl" (any name will do)
If it is getting the correct config file then check the
max_files_per_process kernal tuning parameter (if Linux has one).  I don't
know the specific name for it nor do I know for sure if Linux has it but
most UNIX's seem to.  Hope this is helpful.  If not give us a call at
1-800-399-7220.

Peter Withey
Sr. Technical Support Analyst
Acucorp Technical Support

Robert Annandale <rob_a@unipharm.com> wrote in message
news:37f0f270$0$6415@fountain.mindlink.net...
> I recently installed Acuserver 4.2.0 for Linux ELF RedHat 5-Intel
> on our RedHat 5.2 Server.
…[7 more quoted lines elided]…
> I can see Acuserver running on the Linux box and it does allow a
connection
> however as soon as a second user attempts to connect, Acuserver sends
> an error to the server console announcing ' /etc/Acuserver  Too many files
…[19 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Acuserver on Linux

- **From:** "Robert Annandale" <rob_a@unipharm.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f11c74$0$6415@fountain.mindlink.net>`
- **References:** `<37f0f270$0$6415@fountain.mindlink.net> <7sr2mb$a7m$1@news.cerf.net>`

```
Yuppers, the a_srvcfg file was not being picked up.
Thanks for the trace info'.

RBA.

> Robert:
>
>   One thing rings a bell here. The default for MAX_FILES is 32 unless
> changed.  Try running acuserver with a trace and make sure that the
a_srvcfg
> file is being picked up.  You do this by starting acuserver:
>
> acuserve -start -t3 -l -e errfl
>
> And then reproducing the behavior and looking at "errfl" (any name will
do)
> If it is getting the correct config file then check the
> max_files_per_process kernal tuning parameter (if Linux has one).  I don't
…[16 more quoted lines elided]…
> > This is because I anticipate opening more than 32 files at once and
SCO's
> > Acuserver configuration successfully catered for that.
> >
…[3 more quoted lines elided]…
> > an error to the server console announcing ' /etc/Acuserver  Too many
files
> > opened'
> > On the client side, a 94.10 (74 status code) appears.
…[19 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
