[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# read/import a COBOL database

_3 messages · 3 participants · 2006-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### read/import a COBOL database

- **From:** Lorenzo Bettini <bettini@dsi.unifi.it>
- **Date:** 2006-10-11T15:27:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<egirgv$iug$1@news.cineca.it>`

```
Hi

I don't program in COBOL, but I need to read (and possibly convert in 
some text format, e.g., tab separated) a COBOL archive/database, of 
which I ignore the structure.

Is it possible to do this somehow?

many thanks in advance
	Lorenzo
```

#### ↳ Re: read/import a COBOL database

- **From:** "Heybub" <HeybubNOSPAM@gmail.com>
- **Date:** 2006-10-11T10:35:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12iq3p15qm664c7@news.supernews.com>`
- **References:** `<egirgv$iug$1@news.cineca.it>`

```
Lorenzo Bettini wrote:
> Hi
>
…[5 more quoted lines elided]…
>

Sure, but there is no such thing as a "COBOL database." COBOL can write 
files in any format. There are some file structures that are compiler 
dependent, used for internal processes.

If you have one of these internal formats (usually ISAM and its relatives), 
you are better off by having a COBOL programmer write you a back-pocket 
program to copy the file to a form you can understand. This new program will 
take less than an hour to code and test (more like ten minutes).
```

##### ↳ ↳ Re: read/import a COBOL database

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-11T19:41:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3meqi2tsbf30e0p9o4ac313ffgklu07l3i@4ax.com>`
- **References:** `<egirgv$iug$1@news.cineca.it> <12iq3p15qm664c7@news.supernews.com>`

```
On Wed, 11 Oct 2006 10:35:01 -0500, "Heybub" <HeybubNOSPAM@gmail.com>
wrote:

>Lorenzo Bettini wrote:
>> Hi
…[16 more quoted lines elided]…
>
This assuming that the FD's of the files are available, and also that
the record layout (if not the same as the FD's) is also available.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
