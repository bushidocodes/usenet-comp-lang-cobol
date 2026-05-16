[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ADISINIT

_3 messages · 2 participants · 2005-03_

---

### ADISINIT

- **From:** Wolf Grossi <ng-wg@magro-soft.com>
- **Date:** 2005-03-08T11:16:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<422d7b65$1@e-post.inode.at>`

```
Hi all,

building a new rts with MicroFocus ServerExpress-4.0 (64-bit) I use the 
following cob command:

cob -xe "" -O newrts.o -o newrts

newrts executes a
cobcall("./SERV-T1", argn, args);

SERV-T1.CBL contains a
DISPLAY "TEXT" AT 0101.

giving the error

mpServ: COBOL-Error at 2005-03-08 10:39:29
Execution error : file 'ADISINIT'
error code: 107, pc=0, call=1, seg=0
107     Operation not implemented in this Run-Time System

A DISPLAY without the 'AT' clause works fine.

Any hints?

Thanks for reading
WOLF
```

#### ↳ Re: ADISINIT

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-03-08T17:49:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VAlXd.611787$6l.197170@pd7tw2no>`
- **In-Reply-To:** `<422d7b65$1@e-post.inode.at>`
- **References:** `<422d7b65$1@e-post.inode.at>`

```
Wolf Grossi wrote:
> Hi all,
> 
…[4 more quoted lines elided]…
> Any hints?

Yes. Sign-up here and post your question under Server Express :-

http://www.cobolportal.com/microfocusforum/agreement.asp
```

#### ↳ Re: ADISINIT - done

- **From:** Wolf Grossi <ng-wg@magro-soft.com>
- **Date:** 2005-03-09T09:08:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<422eaf0a$1@e-post.inode.at>`
- **In-Reply-To:** `<422d7b65$1@e-post.inode.at>`
- **References:** `<422d7b65$1@e-post.inode.at>`

```
Thanks,
problem solved.
Wolf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
