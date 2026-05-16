[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/COBOL file copy problems

_14 messages · 9 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### RM/COBOL file copy problems

- **From:** "Rob" <no.spam.pls@execpc.com>
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<37ffa524$0$79676@news.execpc.com>`

```
We're using RM/COBOL in our transaction processing systems and have taken to
periodically refreshing our test environment with production data. While
this refresh process generally works fine (we have a script that just copies
the files from our production environment to our test environment), on two
occasions we've had problems.

In one case, one of our big data files (over a gig) seems to have been
corrupted. The copy process did not report any errors and we have plenty of
disk space and i-nodes. The file was fine in production environment, but
appeared to have been truncated in our test environment and any applications
that tried to open that file would abend, effectively complaining that the
file was corrupted.

In another case several weeks later, a different, but equally large, data
file appears to have been truncated, too. But this time applications would
not complain about any problems, but the last 100,000+ records (about a
month worth of data, we've got several years of data in the file) were
missing. Again, no errors were reported during the refresh of our test
environment. Unfortunately, this time applications did not abend, so the
problem went undetected through all of our testing.

This is a vexing problem, because we can't reproduce it and we don't know
what the cause is. The only thing that I can dream of is that users might
still have files open, leaving the files in inconsistent states. In fact,
we've recently introduced nightly reporting of who still has what files open
(using the fuser command) and we've discovered that users haven't been
exiting applications properly. (With changes in our SOPs, the users are
logging off more consistently, now.) The problem with this theory is that I
suspected prior to executing this second conversion, so I actually rebooted
the system prior to doing the refresh, to effectively kick everyone off and
make sure that everything was clean. So I cannot imagine why the copying of
the data files didn't work.

Has anyone else seen strange problems copying RM/COBOL data files in SCO
Unix? Our environment is  RM/COBOL-85 - Version 6.09.01 for SCO Unix System
V R 3.2.2. Any suggestions would be greatly appreciated: Our confidence in
our test environment (to say nothing of our production backups) has been
severely shaken, and we'd love to figure out what the problem is.

Thanks.

Rob
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** "Rob" <no.spam.pls@execpc.com>
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<37ffbddf$0$79673@news.execpc.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
Needless to say, despite my comments about users being logged on, no one was
actually using the system during either incident. Both conversions were done
outside of business hours, though users had left their workstations without
logging off properly. Also, we do not have any background jobs that were
running, either.

Rob

Rob <no.spam.pls@execpc.com> wrote in message
news:37ffa524$0$79676@news.execpc.com...

> We're using RM/COBOL in our transaction processing systems and have taken
to
> periodically refreshing our test environment with production data. While
> this refresh process generally works fine (we have a script that just
copies
> the files from our production environment to our test environment), on two
> occasions we've had problems.
>
> ...
```

##### ↳ ↳ Re: RM/COBOL file copy problems

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<3800137D.298F5E3C@home.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <37ffbddf$0$79673@news.execpc.com>`

```


Rob wrote:
> 
Rob,

Not my bag because I'm not into multi-user. But I recall similar
problems with multi-user systems being corrupted,(quoted on the
NetExpress Answerlab). More often than not, the problem was related to
the server/multi-user software - not the compiler. You're looking at
RM/COBOL - just a suggestion, does the problem lie elsewhere ?

Jimmy, Calgary AB
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
    Was the copy over a network, or was did the data stay on one pc?  I have
noted that some networks allow undetected errors during a copy.  I have
never tried this (copy a file, check CRC) on a unix machine though.



Rob <no.spam.pls@execpc.com> wrote in message
news:37ffa524$0$79676@news.execpc.com...
> We're using RM/COBOL in our transaction processing systems and have taken
to
> periodically refreshing our test environment with production data. While
> this refresh process generally works fine (we have a script that just
copies
> the files from our production environment to our test environment), on two
> occasions we've had problems.
>
> In one case, one of our big data files (over a gig) seems to have been
> corrupted. The copy process did not report any errors and we have plenty
of
> disk space and i-nodes. The file was fine in production environment, but
> appeared to have been truncated in our test environment and any
applications
> that tried to open that file would abend, effectively complaining that the
> file was corrupted.
…[12 more quoted lines elided]…
> we've recently introduced nightly reporting of who still has what files
open
> (using the fuser command) and we've discovered that users haven't been
> exiting applications properly. (With changes in our SOPs, the users are
> logging off more consistently, now.) The problem with this theory is that
I
> suspected prior to executing this second conversion, so I actually
rebooted
> the system prior to doing the refresh, to effectively kick everyone off
and
> make sure that everything was clean. So I cannot imagine why the copying
of
> the data files didn't work.
>
> Has anyone else seen strange problems copying RM/COBOL data files in SCO
> Unix? Our environment is  RM/COBOL-85 - Version 6.09.01 for SCO Unix
System
> V R 3.2.2. Any suggestions would be greatly appreciated: Our confidence in
> our test environment (to say nothing of our production backups) has been
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: RM/COBOL file copy problems

- **From:** "Rob" <no.spam.pls@execpc.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<38013685$0$79672@news.execpc.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com>`

```
No, this was on a single PC (though we're going to start using a separate
machine for our testing environment, so that's good to know). I guess in the
future I will make the file verifications part of the refresh script, but it
just seems unnecessary to have to do it.

I'm still interested in whether someone else has experienced similar
problems, but it doesn't sound like it (at least so far).

Rob

Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote in message
news:7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com...
>     Was the copy over a network, or was did the data stay on one pc?  I
have
> noted that some networks allow undetected errors during a copy.  I have
> never tried this (copy a file, check CRC) on a unix machine though.
```

###### ↳ ↳ ↳ Re: RM/COBOL file copy problems

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<7tt5c6$1oo$3@ssauraab-i-1.production.compuserve.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com> <38013685$0$79672@news.execpc.com>`

```
    With such a massive file, so long as you are rebooting anyway, why not
do the copy before bringing up the multiuser portion of the operating
system. This is usually possible for maintance purposes.  Of course, I do
not know what this would do to caching.

    The errors that I was referring to were on files of the 30 Mgbyte order.
I would copy a 30Mb zip file, and test the CRC afterward.  I have found that
Novell (win98/95 and win NT) can be made totally reliable (checksum option).
I have not managed this yet with Microsoft network.  Will try TCP/IP next.

    Note that checksum option of Novell client32 requires Ethernet 802.2.


Rob <no.spam.pls@execpc.com> wrote in message
news:38013685$0$79672@news.execpc.com...
> No, this was on a single PC (though we're going to start using a separate
> machine for our testing environment, so that's good to know). I guess in
the
> future I will make the file verifications part of the refresh script, but
it
> just seems unnecessary to have to do it.
>
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: RM/COBOL file copy problems

- **From:** ray@noisp.com (Raymond Leech)
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<MPG.126c49baf051251a98969e@news>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com>`

```
If the copy was instituted from a MS workstation, try the copy option 
'/v' (verify) could help on large copies (I'm sure there's an equiv in 
SCO). If done from a workstation, the downside is double the network 
traffic. Small price for peace of mind.

ray

In article <7tpd1e$df5$2@ssauraab-i-1.production.compuserve.com>, 
RWSTYLES@COMPUSERVE.COM says...
>     Was the copy over a network, or was did the data stay on one pc?  I have
> noted that some networks allow undetected errors during a copy.  I have
> never tried this (copy a file, check CRC) on a unix machine though.
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991009213118.22857.00000110@ngol07.aol.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
In article <37ffa524$0$79676@news.execpc.com>, "Rob" <no.spam.pls@execpc.com>
writes:

>
>Has anyone else seen strange problems copying RM/COBOL data files in SCO
…[5 more quoted lines elided]…
>

I can't say for any particular environment, but the re-boot of the server to 
knock everyone off before the copy is likely to have left the files in an
'open'
state.  I know that when cancelling a program that has an ISAM file open, 
the ISAM file is left with a flag in the header indicating an active status.
You may need to do a rebuild or some form of recovery process to reset 
the file before doing any backup or copy.
```

##### ↳ ↳ Re: RM/COBOL file copy problems

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AWEAOD0euF3mLv6Oab9VET8oLS75@4ax.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <19991009213118.22857.00000110@ngol07.aol.com>`

```
On 10 Oct 1999 01:31:18 GMT, sff5ky@aol.comxxx123 (Sff5ky) wrote:

>In article <37ffa524$0$79676@news.execpc.com>, "Rob" <no.spam.pls@execpc.com>
>writes:
…[16 more quoted lines elided]…
>the file before doing any backup or copy.
If you reboot the machine then the file IS closed for the operating
system, and all buffers ARE written to the harddisk before shutting
down the machine.
The fact the the file has an internal flag with the count of logical
active "open" does not afect the copy of a file.

If he is missing some records is because the copy (operating system
dependent) did not work properly.
I have seen this happen in big files while copying across two machines
The only way to make sure that the copy is correct is to make
sure that nobody is using the file at the time of the copy, get the
sum of the file (in SCO is "sum -r") before the copy, and after the
copy do it again on the destination file and compare them.

And I also have to say that the previous times I saw this fail was not
with UNIX, but with Novell and WINNT, although I think it is not
directly related with the operating system...


FF
```

###### ↳ ↳ ↳ Re: RM/COBOL file copy problems

- **From:** ray@noisp.com (Raymond Leech)
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.126c4be7ca5e514098969f@news>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <19991009213118.22857.00000110@ngol07.aol.com> <AWEAOD0euF3mLv6Oab9VET8oLS75@4ax.com>`

```
Frederico,
Painfully I have learned that the statement should be "If you reboot... 
files WILL BE closed". Under NT, we have found occasions when files are 
left open after the application is shut down and also after the 
workstation crashes the files can be left open for a while. Generally 
they are freed by the time a user logs back in. This is due to a 
registry entry on the server that allows closed files to be cached.

I know the original discussion was about SCO but thought maybe someone 
would find this tip useful.

ray

In article <AWEAOD0euF3mLv6Oab9VET8oLS75@4ax.com>, 
frederico_fonseca@eudoramail.com says...
> If you reboot the machine then the file IS closed for the operating
> system, and all buffers ARE written to the harddisk before shutting
> down the machine.
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** "Albert Ratzlaff R." <albert@conexion.com.py>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<3801C15E.33887B34@conexion.com.py>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
Rob wrote:
> 
> <snip>
…[9 more quoted lines elided]…
> Rob

We have about a hundred clients running various flavors of both RM/COBOL
and SCO Unix. The number of reported problems is very small compared to
what I hear from other platforms and languages. So while I can't give
you a direct answer to your question, I don't think you should worry
about language and operating system. Your problem must be related to the
copy process. With such big files, one user can modify the file while it
is beeing copied, so the copy could be inconsistent. You don't mention
any problems with the original files.

Regards
Albert Ratzlaff
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<tDlM3.5094$UG5.364685@typ11.nn.bcandid.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
It might help to run "vutil -i *" on the files from time to time to see if
they need to be rebuilt.  Note the user count, it should reflect ONLY the
number of users who currently have the file open, but can remain > 0 if the
systems crashes or the application/user doesn't close the file after use.
After a lot of i-o and record deletes, you can rebuild them with
vutil -rebuild -k0 -a *  .  Check your user's guide  for options to use in
your shop, YMMV.

Rob <no.spam.pls@execpc.com> wrote in message
news:37ffa524$0$79676@news.execpc.com...
> In one case, one of our big data files (over a gig) seems to have been
> corrupted. The copy process did not report any errors and we have plenty
of
> disk space and i-nodes. The file was fine in production environment, but
> appeared to have been truncated in our test environment and any
applications
> that tried to open that file would abend, effectively complaining that the
> file was corrupted.
…[12 more quoted lines elided]…
> we've recently introduced nightly reporting of who still has what files
open
> (using the fuser command) and we've discovered that users haven't been
> exiting applications properly. (With changes in our SOPs, the users are
> logging off more consistently, now.) The problem with this theory is that
I
> suspected prior to executing this second conversion, so I actually
rebooted
> the system prior to doing the refresh, to effectively kick everyone off
and
> make sure that everything was clean. So I cannot imagine why the copying
of
> the data files didn't work.
>
> Has anyone else seen strange problems copying RM/COBOL data files in SCO
> Unix? Our environment is  RM/COBOL-85 - Version 6.09.01 for SCO Unix
System
> V R 3.2.2. Any suggestions would be greatly appreciated: Our confidence in
> our test environment (to say nothing of our production backups) has been
> severely shaken, and we'd love to figure out what the problem is.
```

##### ↳ ↳ Re: RM/COBOL file copy problems

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.sco.programmer
- **Message-ID:** `<XF4COFzajVY52hYvdubxDN=FNqKE@4ax.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com> <tDlM3.5094$UG5.364685@typ11.nn.bcandid.com>`

```
On Mon, 11 Oct 1999 08:29:56 -0500, "Warren Porter"
<warrenp123@netdoor123.com> wrote:

>It might help to run "vutil -i *" on the files from time to time to see if
It would be even greater help if the files were from
ACUBOBOL, which they are not.

The problem here is only to do with the copy, and eventually with the
fact the the files may be still open (and with records in the
buffers waitting to be written) while the copy is made.

FF
```

#### ↳ Re: RM/COBOL file copy problems

- **From:** AnhMy Tran <anhmytran@hotmail.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s0clf371hu282@corp.supernews.com>`
- **References:** `<37ffa524$0$79676@news.execpc.com>`

```
It is the first time I ever heard that someone can work with the files
opened by others. I do not know how to solve that problems. In companies
I have worked with, the users have no access to permanent data.

Besides, the followings are some suggestions:
1- It may be hardware problems, rather than programming problems.
   Solution:  purchase new equipments.
2- Re-design your system:
   a- Interactive data files should always be temporary data files.
   b- Temporary data files are always created as new.
   c- Temporary data files should be finished and validated periodically.
   d- Temporary-permanent update process should be done
      by batch programming at a fixed schedule.
   e- All data files should have back up coppies and destroyed carefully.

------------------  Posted via CNET Help.com  ------------------
                      http://www.help.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
