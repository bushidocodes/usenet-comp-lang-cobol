[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# java as subroutines for legacy programs.

_5 messages · 5 participants · 1999-11_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### java as subroutines for legacy programs.

- **From:** Set.KuoLern@mail.uob.com.sg (kuolern)
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.java.databases,comp.lang.java.programmer,comp.lang.cobol
- **Message-ID:** `<3839fe31.5727565@news.pacific.net.sg>`

```
hi,

our cobol programs in HPUX and VB on NT has common need for the same
subroutines. We are exploring the posibility of writing the subroutine
in JAVA. This routines are required to access orocle database.

The issue is 
1. How do we manage the database connection? that is, if the routine
is used 100 time in a calling program, we don't want to connect 100
times.
2. Is there existing interface layer between MicroFocus cobol ver5 to
java?

Pls advise. 

thanks.
```

#### ↳ Re: java as subroutines for legacy programs.

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.java.databases,comp.lang.java.programmer,comp.lang.cobol
- **Message-ID:** `<383ADCBD.567@saif.com>`
- **References:** `<3839fe31.5727565@news.pacific.net.sg>`

```
kuolern wrote:
> 
> hi,
…[14 more quoted lines elided]…
> thanks.

We are just beginning to design an "application server" tier for this
type of need.  Java and Java-beans will run on this server to perform
the common tasks of reading/writing to our oracle databases.  

I think my company has choosen IBM's Websphere and VA-Java for running
this middle tier.

Our driving need, is that this will also support many concurrent users
on the internet!  Since the internet is our ultimate goal, we are also
designing multiple firewall's into the system.

Pete
```

##### ↳ ↳ Re: java as subroutines for legacy programs.

- **From:** David Sanders <dsanders@legacyj.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.java.databases,comp.lang.java.programmer,comp.lang.cobol
- **Message-ID:** `<383C3318.77C1F019@legacyj.com>`
- **References:** `<3839fe31.5727565@news.pacific.net.sg> <383ADCBD.567@saif.com>`

```
Our Cobol compiler, called PERCobol, supports Java and JavaBeans.  It
enables Cobol to run in the Java environment and has support for EXEC-SQL
through JDBC.  It could be what you are looking for.

Visit our site at:  www.legacyj.com

Thanks,

David Sanders
LegacyJ Corporation
www.legacyj.com
```

#### ↳ Re: java as subroutines for legacy programs.

- **From:** "J. S. Jensen" <jsjensen@saba.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.java.databases,comp.lang.java.programmer,comp.lang.cobol
- **Message-ID:** `<383B15CB.6F4FD123@saba.com>`
- **References:** `<3839fe31.5727565@news.pacific.net.sg>`

```
kuolern wrote:

> We are exploring the posibility of writing the subroutine in JAVA. This
> routines are required to access orocle database.

Good idea.

> 1. How do we manage the database connection? that is, if the routine is
> used 100 time in a calling program, we don't want to connect 100 times.

Yes, you will need to create a native wrapper.  The best way (in my
opinion) to implement this is to have a Java database connection daemon
with a persistent database connection, and then make native calls into it
via a named pipe, a socket, or RMI.

> 2. Is there existing interface layer between MicroFocus cobol ver5 to
> java?

These are few and far in between, but I've never personally come across a
good one.  Why don't you just talk local domain sockets to a java process
for database access/subroutines?
```

#### ↳ Re: java as subroutines for legacy programs.

- **From:** Paul Butkiewicz <pbutkiewicz@quoininc.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.java.databases,comp.lang.java.programmer,comp.lang.cobol
- **Message-ID:** `<383C34D1.71143932@quoininc.com>`
- **References:** `<3839fe31.5727565@news.pacific.net.sg>`

```
kuolern wrote:

> hi,
>
…[13 more quoted lines elided]…
> thanks.

What about simply using CORBA?  I know an IDL binding for cobol has been
defined, and I'm sure various ORB's support it.

Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
