[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Command line

_6 messages · 4 participants · 1999-03_

---

### Command line

- **From:** Philip A Colbert <philip@colbert.u-net.com>
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F2DAB9.CBD7875D@colbert.u-net.com>`

```
Anyone know how to start batch or executable code from cobol,
(We are thinking about building a GUI front end for an old system)

thanks
Phil...................
```

#### ↳ Re: Command line

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f2f49c.331700543@news1.ibm.net>`
- **References:** `<36F2DAB9.CBD7875D@colbert.u-net.com>`

```
On Fri, 19 Mar 1999 23:16:09 +0000, Philip A Colbert
<philip@colbert.u-net.com> wrote:

>Anyone know how to start batch or executable code from cobol,
>(We are thinking about building a GUI front end for an old system)
…[3 more quoted lines elided]…
>


Please sir, may I have some more?.... Information? Platforms etc...
```

#### ↳ Re: Command line

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f2ecc5.12917371@netnews>`
- **References:** `<36F2DAB9.CBD7875D@colbert.u-net.com>`

```
'Twas Fri, 19 Mar 1999 23:16:09 +0000, when Philip A Colbert
<philip@colbert.u-net.com> illuminated comp.lang.cobol thusly:

>Anyone know how to start batch or executable code from cobol,
>(We are thinking about building a GUI front end for an old system)

What compiler and what operating system?  If you happen to be using Unisys
A Series the syntax is 

CALL SYSTEM WFL USING <param>
```

#### ↳ Re: Command line

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZHGI2.390$NB5.984535@storm.twcol.com>`
- **References:** `<36F2DAB9.CBD7875D@colbert.u-net.com>`

```
There is a command you can use which is pretty much similar on every system.
It is called HELP or in some strange dialects it can be referenced as a
single '?'. I have even seen it assigned to that weird row of keys at the
top of your keyboard with 'f' and numbers on them. In the United States they
usually assign a HRLP command or some English derivative to this command.
Navigation through the screens presented usually produces something of use.
```

##### ↳ ↳ Re: Command line

- **From:** Philip A Colbert <philip@colbert.u-net.com>
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F42BEE.883FB148@colbert.u-net.com>`
- **References:** `<36F2DAB9.CBD7875D@colbert.u-net.com> <ZHGI2.390$NB5.984535@storm.twcol.com>`

```
Sorry about that,
                        I have not been programming for long.
                        I would like to call a executable program (vb) from
microfocus cobol
                        running on an IBM pc.
```

###### ↳ ↳ ↳ Re: Command line

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qW%I2.589$NB5.1632551@storm.twcol.com>`
- **References:** `<36F2DAB9.CBD7875D@colbert.u-net.com> <ZHGI2.390$NB5.984535@storm.twcol.com> <36F42BEE.883FB148@colbert.u-net.com>`

```
>Sorry about that,
>                        I have not been programming for long.
…[3 more quoted lines elided]…
>

One guess would be:

           CALL 'C:\COMMAND.COM' 'C:\COBOLPRG.EXE' 'PARM VALUES'

Of course substituting double quotes for single quotes for necessary. This
example was a derivative of a primitive BASIC compiler which from the
documentation was the way it had to be done to allow for DOS commands such
as DIR and other commands to be executed.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
