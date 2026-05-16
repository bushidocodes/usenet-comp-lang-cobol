[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# convert from rmcobol

_9 messages · 4 participants · 2005-05 → 2005-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### convert from rmcobol

- **From:** "Maurizio Giacobbe" <maug7@yahoo.it>
- **Date:** 2005-05-30T15:24:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org>`

```
May you help me to convert a rmcobol file in a .txt file ?

I use NE but it doesn't read rmcobol file.

Thank,

           Maurizio Giacobbe
```

#### ↳ Re: convert from rmcobol

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-05-30T18:28:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org>`

```
On Mon, 30 May 2005 15:24:09 +0000 (UTC), "Maurizio Giacobbe"
<maug7@yahoo.it> wrote:

>May you help me to convert a rmcobol file in a .txt file ?
>
…[4 more quoted lines elided]…
>           Maurizio Giacobbe

Easy.


If this is a once off.
Create a program with RM/COBOL that reads the RMCOBOL file, and saves
the records into a sequential file (line or record).
Bear in mind that you may need to convert some numeric formats like
COMP-6 to valid MF formats. Preferrably convert all numerics to
numeric edited with leading/trailing sign.


If you are keeping the application in RM/COBOL working, then look at
the use of RELATIVITY to access the files. This will enable your MF
programs to access the RM files directly using ODBC.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: convert from rmcobol

- **From:** "Maurizio Giacobbe" <maug7@yahoo.it>
- **Date:** 2005-05-31T06:08:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com>`

```
I don't have RM/Cobol compiler but the Microfocus NetExpress 3.1

Do you know if exist some tool or utility that reads RMcobol files ?

Thank,

            Maurizio Giacobbe
```

###### ↳ ↳ ↳ Re: convert from rmcobol

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-05-31T07:51:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org>`

```
On Tue, 31 May 2005 06:08:20 +0000 (UTC), "Maurizio Giacobbe"
<maug7@yahoo.it> wrote:

>I don't have RM/Cobol compiler but the Microfocus NetExpress 3.1
>
>Do you know if exist some tool or utility that reads RMcobol files ?
RELATIVITY

www.liant.com


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: convert from rmcobol

_(reply depth: 4)_

- **From:** "Maurizio Giacobbe" <maug7@yahoo.it>
- **Date:** 2005-05-31T13:44:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e69246b1eddd4964d993847014c2f6d.69693@mygate.mailgate.org>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org> <jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com>`

```
I have tried relativity but i do not succeed to read rmcobol files,

Exist a small free compiler for rmcobol files? thank you.

                  Maurizio 
```

###### ↳ ↳ ↳ Re: convert from rmcobol

_(reply depth: 5)_

- **From:** epc8@juno.com
- **Date:** 2005-06-01T16:48:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1117669735.473421.187680@f14g2000cwb.googlegroups.com>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org> <jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com> <5e69246b1eddd4964d993847014c2f6d.69693@mygate.mailgate.org>`

```


Maurizio Giacobbe wrote:
> I have tried relativity but i do not succeed to read rmcobol files,
>
…[6 more quoted lines elided]…
> Posted via Mailgate.ORG Server - http://www.Mailgate.ORG

A program (released under GPL) claims to be able to read these files.
It might (or might not) work for you.

http://www.janes.demon.co.uk/
```

###### ↳ ↳ ↳ Re: convert from rmcobol

_(reply depth: 6)_

- **From:** "Maurizio Giacobbe" <maug7@yahoo.it>
- **Date:** 2005-06-03T06:39:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18552da980e7809642655b89afd8b4c3.69693@mygate.mailgate.org>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org> <jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com> <5e69246b1eddd4964d993847014c2f6d.69693@mygate.mailgate.org> <1117669735.473421.187680@f14g2000cwb.googlegroups.com>`

```
Thank, i'have already tried this utility.

It works good, but it does not convert all data correctly when there
are 3 numbers consecutives that are equal (eg. 111 is converted 11).

                  Maurizio
```

###### ↳ ↳ ↳ Re: convert from rmcobol

_(reply depth: 7)_

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2005-06-06T08:46:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e8f3$42a4455a$422aa88a$28619@FUSE.NET>`
- **In-Reply-To:** `<18552da980e7809642655b89afd8b4c3.69693@mygate.mailgate.org>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org> <jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com> <5e69246b1eddd4964d993847014c2f6d.69693@mygate.mailgate.org> <1117669735.473421.187680@f14g2000cwb.googlegroups.com> <18552da980e7809642655b89afd8b4c3.69693@mygate.mailgate.org>`

```
Maurizio Giacobbe wrote:
> Thank, i'have already tried this utility.
> 
…[5 more quoted lines elided]…
> 
If you are trying to read a RM/Cobol index file into a
flat file (without the index keys), you might use the utility
that is provided with the runtime.

command line=

(runtime folder)\RUNCOBOL (runtimefolder)\RECOVER2 A="(indexfile)"

This should create a non-indexed file with only the data.

Good Luck,
Bob.
```

###### ↳ ↳ ↳ Re: convert from rmcobol

_(reply depth: 8)_

- **From:** "Maurizio Giacobbe" <maug7@yahoo.it>
- **Date:** 2005-06-06T13:45:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e2b5cf3622f682e9fe0fb8aade849ee.69693@mygate.mailgate.org>`
- **References:** `<d629b5bc41f60b515eba923d398ad8d9.69693@mygate.mailgate.org> <o3jm911bg9o9g9o3vc7lns2vlb7iesp3cj@4ax.com> <96d23bad5dc11e72e5848a6cc092ebee.69693@mygate.mailgate.org> <jb2o911mbtqdu74nenhc4810hl9bsscaam@4ax.com> <5e69246b1eddd4964d993847014c2f6d.69693@mygate.mailgate.org> <1117669735.473421.187680@f14g2000cwb.googlegroups.com> <18552da980e7809642655b89afd8b4c3.69693@mygate.mailgate.org> <8e8f3$42a4455a$422aa88a$28619@FUSE.NET>`

```
Thank, i have found a old rmcobol compiler and now i read good the
files.

               Maurizio
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
