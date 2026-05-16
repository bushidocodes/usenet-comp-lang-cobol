[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# problem of file open !

_9 messages · 5 participants · 1999-11_

---

### problem of file open !

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3827244B.AEEE4F96@eii.fr>`

```
Hi

I have a mf COBOL program that opens 2
files (open input). This prog can be
called from 3 different situations.

1/ When it is called from a local
asynchronous terminal, the file status
is 00 when openingthe files. normal.
everything is ok.

2/ When it is called from the french
minitel, it is the same. no problem.

3/ When it is called from an apache
server thru CGI-bin, the open returns 00
for one file and 39 for the second file
!

How can I get that 39 status code since
it is the same physical file that is
correct in the 2 other situations ???

Does anybody have any ideas ???

thanks

Christophe
```

#### ↳ Re: problem of file open !

- **From:** Tracy Jennings <Tracy.Jennings@eds.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38274C11.B34AB095@eds.com>`
- **References:** `<3827244B.AEEE4F96@eii.fr>`

```
Typically '39' is a file attribute problem. Are you sure that the
platform where you are executing the program from has the file defined
properly ? Is this file being opened up for output or input ?

webmaster wrote:

> Hi
>
…[25 more quoted lines elided]…
> Christophe
```

#### ↳ Re: problem of file open !

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<807mip$24s$1@news.inet.tele.dk>`
- **References:** `<3827244B.AEEE4F96@eii.fr>`

```
Could the SELECT or FD be different. Is it the same program in all
situations?

Regards
Ib

webmaster skrev i meddelelsen <3827244B.AEEE4F96@eii.fr>...
>Hi
>
…[26 more quoted lines elided]…
>
```

##### ↳ ↳ Re: problem of file open !

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3827D34D.E09631A6@eii.fr>`
- **References:** `<3827244B.AEEE4F96@eii.fr> <807mip$24s$1@news.inet.tele.dk>`

```
It is the same program on the same server with the same files !

This prog can be called from different situations : sometime it does
open the files and sometimes it does not !

Ib Tanding wrote:

> Could the SELECT or FD be different. Is it the same program in all
> situations?
…[33 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: problem of file open !

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<809rk6$rc9$1@news.inet.tele.dk>`
- **References:** `<3827244B.AEEE4F96@eii.fr> <807mip$24s$1@news.inet.tele.dk> <3827D34D.E09631A6@eii.fr>`

```
Hi,
You say, it is the same program. You are receiving an error. The error tells
you that something is wrong with the file attributes. When the program
executes from one place, you receive an error, but from 2 other places - no
error.

I am convinced that your focus should be at the environment - not at the
program.

Please look into the environment settings.

Regards
Ib

webmaster skrev i meddelelsen <3827D34D.E09631A6@eii.fr>...
>It is the same program on the same server with the same files !
>
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: problem of file open !

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991109173218.19242.00000104@ngol03.aol.com>`
- **References:** `<809rk6$rc9$1@news.inet.tele.dk>`

```
In article <809rk6$rc9$1@news.inet.tele.dk>, "Ib Tanding" <ib@tanding.dk>
writes:

>Hi,
>You say, it is the same program. You are receiving an error. The error tells
…[6 more quoted lines elided]…
>

What is the possibility that the server where the error occurs does not
have rights to the directory?
I had a similar situation where a Netwrok Pc appeared to be properly logged
into the network but did not have all the proper drive mappings.
Because of hte missing drive mappings the program failed to run.
```

###### ↳ ↳ ↳ Re: problem of file open !

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<808oll$hng$1@nnrp1.deja.com>`
- **References:** `<3827244B.AEEE4F96@eii.fr> <807mip$24s$1@news.inet.tele.dk> <3827D34D.E09631A6@eii.fr>`

```
In article <3827D34D.E09631A6@eii.fr>,
  webmaster@eii.fr wrote:
> It is the same program on the same server with the same files !
>
> This prog can be called from different situations : sometime it does
> open the files and sometimes it does not !
<snip>
> > >3/ When it is called from an apache
> > >server thru CGI-bin, the open returns 00
…[5 more quoted lines elided]…
> > >correct in the 2 other situations ???

So stop staring at the files and at your program! If the same program
with the same file works differently in another situation, then the
situation is the problem, not the program!

Now, where is the difference? I don't know your environment, but I'd
guess there is some security package on your apache server? Some sort of
firewall? Or a codepage translation? Does the server start a process on
your client which corrupts some storage or does some security check or
virus check?

You should talk to your server- and intranet-people and ask them the
questions above. Maybe you have a trace tool and may have a look at the
storage near the variables of your program.

Good luck, this could cause you further headache!
```

###### ↳ ↳ ↳ Re: problem of file open !

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38295FAB.2BBB3E4B@eii.fr>`
- **References:** `<3827244B.AEEE4F96@eii.fr> <807mip$24s$1@news.inet.tele.dk> <3827D34D.E09631A6@eii.fr>`

```
I do understand that we might have an environment problem, but in fact,
my program should open  2 files that have got the same right (same group
same owner same right) and located in the same directory.

The status 39 when opening occurs only with one of the 2 files ! So what
can be different within this 2 files ? Why can I open both of them
sometimes (local or french Minitel) and only one from httpd as it is the
same COBOL program ?

thanks for your ideas...

webmaster wrote:

> It is the same program on the same server with the same files !
>
…[40 more quoted lines elided]…
> > >
```

###### ↳ ↳ ↳ Eureka !

_(reply depth: 4)_

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382991F0.2F8BACCE@eii.fr>`
- **References:** `<3827244B.AEEE4F96@eii.fr> <807mip$24s$1@news.inet.tele.dk> <3827D34D.E09631A6@eii.fr> <38295FAB.2BBB3E4B@eii.fr>`

```
Thanks everybody, I have found out our configuration problem !!!

When my prog is run by apache the COBCONFIG variable was not set and we do
need it with the following line in the conf file :
set isam_open_key_check=FALSE

I do not know why but I can not open some files without that parameter.

Do anybody know why that paramter is necessary for properly opening some
files which are anyway correctly defined since made with rebuild with no
problem ?

Thanks

webmaster wrote:

> I do understand that we might have an environment problem, but in fact,
> my program should open  2 files that have got the same right (same group
…[53 more quoted lines elided]…
> > > >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
