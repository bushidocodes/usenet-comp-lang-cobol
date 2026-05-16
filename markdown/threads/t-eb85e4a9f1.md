[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Partitioned Dataset

_4 messages · 4 participants · 2004-08_

---

### Partitioned Dataset

- **From:** sameer_bon@rediffmail.com (sameer)
- **Date:** 2004-08-13T10:27:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf573a0d.0408130927.32ec065c@posting.google.com>`

```
Hi,

   Can you tell me whether we can access PDS member in Cobol program.
If we can, what should be DD statement in JCL & File definition in
Cobol program.

Thanks
Sameer.
```

#### ↳ Re: Partitioned Dataset

- **From:** docdwarf@panix.com
- **Date:** 2004-08-13T14:04:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfivrk$rv5$1@panix5.panix.com>`
- **References:** `<bf573a0d.0408130927.32ec065c@posting.google.com>`

```
In article <bf573a0d.0408130927.32ec065c@posting.google.com>,
sameer <sameer_bon@rediffmail.com> wrote:
>Hi,
>
>   Can you tell me whether we can access PDS member in Cobol program.
>If we can, what should be DD statement in JCL & File definition in
>Cobol program.

Please do your own homework.

DD
```

#### ↳ Re: Partitioned Dataset

- **From:** "Mike" <NoMoreSpam@SpamStopper.Org>
- **Date:** 2004-08-13T16:58:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A-ednQuxvMjmpIDcRVn_vQ@giganews.com>`
- **References:** `<bf573a0d.0408130927.32ec065c@posting.google.com>`

```
>    Can you tell me whether we can access PDS member in Cobol program.
> If we can, what should be DD statement in JCL & File definition in
…[3 more quoted lines elided]…
> Sameer.

Jeez. It wouldn't take you more than 10 minutes to test this yourself.
How the heck are we supposed to know what your file definition should look like?
You didn't tell us anything about your dataset.
```

#### ↳ Re: Partitioned Dataset

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-08-14T06:31:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yliTc.445019$Gx4.68777@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<bf573a0d.0408130927.32ec065c@posting.google.com>`
- **References:** `<bf573a0d.0408130927.32ec065c@posting.google.com>`

```


sameer wrote:
> Hi,
> 
…[5 more quoted lines elided]…
> Sameer.


//SYS001 DD DSN=SOME.PDS.NAME(MEMBER),DISP=SHR

SELECT SYS001-INPUT-FILE ASSIGN TO SYS001.

FD  SYS001-INPUT-FILE
     BLOCK CONTAINS 0 RECORDS.

01  SYS001-INPUT-RECORD     PIC X(80).

What are you really trying to do?  The example above will work, but 
doesn't cover all the possible cases.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
