[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [z/os] Finding location of DB2 specific copybooks

_4 messages · 4 participants · 2008-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### [z/os] Finding location of DB2 specific copybooks

- **From:** miguel.laiz@gmail.com
- **Date:** 2008-06-12T04:19:46-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<3914fb05-f83c-4c2e-85b3-6e34364c0e05@25g2000hsx.googlegroups.com>`

```
Hi all!

First, I'm not sure if I've directed this post to the correct groups
of COBOL and DB2. My apologies in that case.

Question:

I know that during precompilation and compilation of a cobolprogram
that contains SQL-statements, there are usually a bunch of
hostvariables (made from declgen) along with the copy SQLCA and
sometimes also one or several SQLDA:s.

I've been looking around and can't seem to find in which library /
libraries the actual source copy-book(s) of SQLCA och SQLDA are
located. I'm guessing either in the core compiler libraries or in the
DB2 installation.

I have also checked the what joblibs that are provided in the
compilation JCL.
Joblibs: IGY.SIGYCOMP, CEE.SCEERUN

Mostly out of curiousity I'd like to know the location(s) from where
the compiler gets (include / copy) the copybooks for DB2, CICS and
such.

Versions:

Z/os 1.9.0
DB2 8.1
Enterprise Cobol 3.4.1

Cheers
Miguel
```

#### ↳ Re: Finding location of DB2 specific copybooks

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-06-15T10:08:51-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<3fde8c66-232d-4330-a333-d6dbb99103bd@m73g2000hsh.googlegroups.com>`
- **References:** `<3914fb05-f83c-4c2e-85b3-6e34364c0e05@25g2000hsx.googlegroups.com>`

```
On 12 Jun, 12:19, miguel.l...@gmail.com wrote:
> Hi all!
>
…[30 more quoted lines elided]…
> Miguel

The copybooks will be stored in the same place as your Cobol code.
```

##### ↳ ↳ Re: Finding location of DB2 specific copybooks

- **From:** "Mark A" <nobody@nowhere.com>
- **Date:** 2008-06-15T15:46:13-04:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<Yie5k.8433$s77.3487@bignews3.bellsouth.net>`
- **References:** `<3914fb05-f83c-4c2e-85b3-6e34364c0e05@25g2000hsx.googlegroups.com> <3fde8c66-232d-4330-a333-d6dbb99103bd@m73g2000hsh.googlegroups.com>`

```
"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:3fde8c66-232d-4330-a333-d6dbb99103bd@m73g2000hsh.googlegroups.com...
> The copybooks will be stored in the same place as your Cobol code.

I believe that he is talking about includes that are specific to DB2. I 
think they are included by the DB2 pre-compiler.
```

##### ↳ ↳ Re: Finding location of DB2 specific copybooks

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-06-15T20:50:44-03:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<giab54puq7l7s5vhv6mtf9s7rfr5a1emkt@4ax.com>`
- **References:** `<3914fb05-f83c-4c2e-85b3-6e34364c0e05@25g2000hsx.googlegroups.com> <3fde8c66-232d-4330-a333-d6dbb99103bd@m73g2000hsh.googlegroups.com>`

```
On Sun, 15 Jun 2008 10:08:51 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 12 Jun, 12:19, miguel.l...@gmail.com wrote:
>> Hi all!
…[33 more quoted lines elided]…
>The copybooks will be stored in the same place as your Cobol code.

Check the SYSLIB concatenations for your pre-compiler and compiler. If
you are using the compile option where the compile calls the SQL
interpreter, there may be other source library DD statements involved.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
