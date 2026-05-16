[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fd description error, please help!

_9 messages · 9 participants · 2000-09 → 2000-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### fd description error, please help!

- **From:** yesplease151@my-deja.com
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
please help! this is my fd description:
 FD BORROWED-FILE
    RECORD CONTAINS 80 CHARACTERS
    LABEL RECORDS ARE STANDARD
    DATA RECORD IS BORROWED-REC
    VALUE OF FILE-ID "A:BORROWED.DAT".

i keep getting a description error.  can anyone please tell me what i
am doing wrong?  thank you!


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: fd description error, please help!

- **From:** "Matteo" <lena_sas@iol.it>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ugry5.1382$Q23.30940@news.infostrada.it>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
  FD BORROWED-FILE
     RECORD CONTAINS 80 CHARACTERS
     LABEL RECORDS IS STANDARD
     DATA RECORD IS BORROWED-REC
     VALUE OF FILE-ID IS "A:BORROWED.DAT".


Ciao
Matteo

"I computer sanno contare solo da 0 ad 1.  Il resto e' illusione."

<yesplease151@my-deja.com> wrote in message
news:8qddgl$4fk$1@nnrp1.deja.com...
> please help! this is my fd description:
>  FD BORROWED-FILE
…[10 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: fd description error, please help!

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qdmij$4go$1@news.igs.net>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
What compiler, on what platform?

yesplease151@my-deja.com wrote in message <8qddgl$4fk$1@nnrp1.deja.com>...
>please help! this is my fd description:
> FD BORROWED-FILE
…[10 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: fd description error, please help!

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G4yy5.3188$5p.16291@news2.mia>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com> <8qdmij$4go$1@news.igs.net>`

```
Do you have a 01 RECORD-DESCRIPTION  PIC xxx ?

donald tees <donald@willmack.com> wrote in message
news:8qdmij$4go$1@news.igs.net...
> What compiler, on what platform?
>
…[15 more quoted lines elided]…
>
```

#### ↳ Re: fd description error, please help!

- **From:** "pwmeister" <pwm@nomail.se>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfdkg$224$1@news1.enator.se>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
maybe a SELECT clause is missing in your Environment Division.
Or you omitted a data description entry after your FD clause.
FD BORROWED-FILE
...
01 BORROWED-REC.
     05 ....                             PIC ..
     ...

pm


yesplease151@my-deja.com wrote in message <8qddgl$4fk$1@nnrp1.deja.com>...
>please help! this is my fd description:
> FD BORROWED-FILE
…[10 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: fd description error, please help!

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CB109C.5C8C09F4@worldnet.att.net>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
yesplease151@my-deja.com wrote:
> 
> please help! this is my fd description:
…[7 more quoted lines elided]…
> am doing wrong?  thank you!

Umm, I'm just guessing here, but shouldn't the filename be
"A:\BORROWED.DAT" ?
```

##### ↳ ↳ Re: fd description error, please help!

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CB5D31.A6010799@brazee.net>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com> <39CB109C.5C8C09F4@worldnet.att.net>`

```


Arnold Trembley wrote:

> yesplease151@my-deja.com wrote:
> >
…[14 more quoted lines elided]…
> http://arnold.trembley.home.att.net/

I am not familiar with that clause, but if it only allows absolute file
locations, and not relative file locations, it doesn't understand the OS.
```

#### ↳ Re: fd description error, please help!

- **From:** J M Pittman <jmpittmanii@mindspring.com>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D023FF.24A8E5D2@mindspring.com>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
Try 'VALUE OF TITLE "A:BORROWED.DAT"'.

yesplease151@my-deja.com wrote:

> please help! this is my fd description:
>  FD BORROWED-FILE
…[9 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: fd description error, please help!

- **From:** rmiller@linux.ca (Robaire)
- **Date:** 2000-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39db72e4.54995169@news1.qc.sympatico.ca>`
- **References:** `<8qddgl$4fk$1@nnrp1.deja.com>`

```
I'm almost certain that I know the answer to this problem.
However, it bothers me that you have not yet responded to the
clarifications requested by other people trying to help you.
So, I defer to these senior members of the community who are awaiting
information from you.

Gentlemen, please check with Donald Nelson,
(bottom of page 44 - I'm sure you have it).
Then you can decide whether or not to deliver the answer.

Robaire


On Thu, 21 Sep 2000 16:37:43 GMT, yesplease151@my-deja.com wrote:

>please help! this is my fd description:
> FD BORROWED-FILE
…[10 more quoted lines elided]…
>Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
