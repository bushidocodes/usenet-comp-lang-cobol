[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Server Express & Oracle 9i

_2 messages · 2 participants · 2002-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Server Express & Oracle 9i

- **From:** "Michael Woods" <mikedamnwoods@hotmail.com>
- **Date:** 2002-09-03T04:46:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L8Xc9.79953$gb.27651@news2.central.cox.net>`

```
Has anyone used Micro Focus Server Express and Oracle 9I together? I'm
trying to compile a .gnt and .exe with dynamically linked libraries on HP-UX
11.11 (on an hp 9000) but have had some problems. The Srever Express
documentation doesn't mention Oracle 9i when explaining the cobsql compiler
directive. The cobsql directive calls the Oracle procob command to
preprocess my sql code.  The problem is, all my sql code is in my gnt and my
exe should be linked with Oracle libraries. It seems that some of the Oracle
libraries have functions that are undefined (if I do a  "nm libsql32.sl" I
can see functions that are undefined). Is this normal or do these libraries
need to be rebuilt?
```

#### ↳ Re: Server Express & Oracle 9i

- **From:** "Paul Barnett" <paul.barnett@microfocus.nospam.com>
- **Date:** 2002-09-04T10:28:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<al4jun$dsd$1@hyperion.microfocus.com>`
- **References:** `<L8Xc9.79953$gb.27651@news2.central.cox.net>`

```
If you look in $ORACLE_HOME/precomp/lib you will find make files
ins_precomp.mk and env_precomp.mk

You will also find a file called cobsqlintf.o which contains the entry
points SQLADR and SQLBEX

For running gnt code or debugging etc you need to rebuild the Server Express
run time using the supplied make files to make an executable called 'rtsora'

For running programs compiled to executables, you need to link in
cobsqlintf.o

Hope this helps.

"Michael Woods" <mikedamnwoods@hotmail.com> wrote in message
news:L8Xc9.79953$gb.27651@news2.central.cox.net...
> Has anyone used Micro Focus Server Express and Oracle 9I together? I'm
> trying to compile a .gnt and .exe with dynamically linked libraries on
HP-UX
> 11.11 (on an hp 9000) but have had some problems. The Srever Express
> documentation doesn't mention Oracle 9i when explaining the cobsql
compiler
> directive. The cobsql directive calls the Oracle procob command to
> preprocess my sql code.  The problem is, all my sql code is in my gnt and
my
> exe should be linked with Oracle libraries. It seems that some of the
Oracle
> libraries have functions that are undefined (if I do a  "nm libsql32.sl" I
> can see functions that are undefined). Is this normal or do these
libraries
> need to be rebuilt?
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
