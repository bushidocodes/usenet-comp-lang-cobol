[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol compilers for Linux

_12 messages · 6 participants · 2009-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### cobol compilers for Linux

- **From:** "Developer" <abuse@abuse.org>
- **Date:** 2009-06-26T11:55:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p%81m.3588$w01.1239@newsfe05.iad>`

```
At present I have open-cobol in the linux box and was wondering what else is available for the platform. I am using a 32-bit machine, but I could get a 64-bit one if pressed.
```

#### ↳ Re: cobol compilers for Linux

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-26T19:16:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad>`

```
On Jun 27, 6:55 am, "Developer" <ab...@abuse.org> wrote:
> At present I have open-cobol in the linux box and was wondering what else is available for the platform. I am using a 32-bit machine, but I could get a 64-bit one if pressed.
>
> --http://contract-developer.dyndns.biz

COB-IT
kobol
Fujitsu COBOL 7 for Linux
MicroFocus COBOL
```

##### ↳ ↳ Re: cobol compilers for Linux

- **From:** "Developer" <abuse@abuse.org>
- **Date:** 2009-06-26T20:29:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmg1m.119$WJ3.117@newsfe15.iad>`
- **In-Reply-To:** `<c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com>`

```
Any of them free?
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

- **From:** "don@higgins.net" <don@higgins.net>
- **Date:** 2009-06-27T07:37:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e86b282f-eb94-4e74-8ced-b90f4688082c@j14g2000vbp.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com> <vmg1m.119$WJ3.117@newsfe15.iad>`

```
On Jun 26, 11:29 pm, "Developer" <ab...@abuse.org> wrote:
> Any of them free?
>
…[20 more quoted lines elided]…
> - Show quoted text -

zcobol is free and supports all the mainframe data types including
HFP, BFP, and DFP floating point and up to quad word 128 bit integers
with EXTEND option.  It uses J2SE regular expression parser to
translate any COBOL  program into equivalent HLASM compatible macro
assembler source.  Then it uses z390 portable macro assembler and
zcobol macro library to assemble executable program that runs on z390
for Windows or Linux.  The assembler could also be ported to z/OS
HLASM systems.

zcobol is still in beta test stage but comes with a number of
regression test programs and EXEC CICS COBOL demo programs.  z390 is
written entirely on J2SE Java including GUI interface as well as
command line interface for Windos and Linux.

Don Higgins
don@higgins.net
www.zcobol.org www.z390.org
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-06-27T15:04:58-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rnnc45tgpjspslpt68vqfing8r9of9jifv@4ax.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com> <vmg1m.119$WJ3.117@newsfe15.iad> <e86b282f-eb94-4e74-8ced-b90f4688082c@j14g2000vbp.googlegroups.com>`

```
On Sat, 27 Jun 2009 07:37:06 -0700 (PDT), "don@higgins.net"
<don@higgins.net> wrote:

>On Jun 26, 11:29ï¿½pm, "Developer" <ab...@abuse.org> wrote:
>> Any of them free?
…[30 more quoted lines elided]…
>HLASM systems.

What are the usage statements for the HFP, BFP and DFP options?  Is
there an online resource for answering other questions about zcobol?
>
>zcobol is still in beta test stage but comes with a number of
…[6 more quoted lines elided]…
>www.zcobol.org www.z390.org
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

_(reply depth: 4)_

- **From:** "Developer" <abuse@abuse.org>
- **Date:** 2009-06-27T12:11:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q9u1m.158$066.72@newsfe08.iad>`
- **In-Reply-To:** `<e86b282f-eb94-4e74-8ced-b90f4688082c@j14g2000vbp.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com> <vmg1m.119$WJ3.117@newsfe15.iad> <e86b282f-eb94-4e74-8ced-b90f4688082c@j14g2000vbp.googlegroups.com>`

```
This zcobol is somewhat interesting. I was inquiring with my Linux 
distribution about gcc cobol as it tied into the gcc general compiler. I 
speculated that this would exist as the Ada compiler also used the gcc code 
generator.

I have Java EE on the Linux machine but I prefer native code generation if 
possible.
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

_(reply depth: 5)_

- **From:** "don@higgins.net" <don@higgins.net>
- **Date:** 2009-06-28T12:09:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4238f2fe-2c9f-4c6b-ae4d-ebc94be55859@t13g2000yqt.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com> <vmg1m.119$WJ3.117@newsfe15.iad> <e86b282f-eb94-4e74-8ced-b90f4688082c@j14g2000vbp.googlegroups.com> <Q9u1m.158$066.72@newsfe08.iad>`

```
On Jun 27, 3:11 pm, "Developer" <ab...@abuse.org> wrote:
> This zcobol is somewhat interesting. I was inquiring with my Linux
> distribution about gcc cobol as it tied into the gcc general compiler. I
…[57 more quoted lines elided]…
> - Show quoted text -

The online documentation for zcobol is on www.zcobol.org When you
install z390 which includes zcobol from www.z390.org it includes
zcobol directory with demo and test sub-directories with COBOL
programs you can compile and execute on Windows or Linux with J2SE
or EE as only other requirement.  All the z390 and zocobol  sources
are included as open source under GPL.  The extensions used for FP
include FLOAT-SHORT, FLOAT-LONG, and FLOAT-EXTENDED which default to
DFP but can be changed to HFP or BFP using option FLOAT(DECIMAL/HEX/
BINARY).  Any of the 9 floating point types can be explicitly
specified using FLOAT-HEX-?, FLOAT-DECMIAL-?, or FLOAT-BINARY-? which
is the syntax specified in draft COBOL 2009 standard. COMP-1 is FLOAT-
HEX-SHORT and COMP-2 is FLOAT-HEX-LONG for compatibility with legacy
mainframe COBOL. In addition to FP extensions you can specify COMP
with S9(19-39) resulting in quad word 128 bit integer type.

As Bill Klein pointed out to me privately I should add that zcobol is
still very much in early stage of development and does not pass all
the NIST COBOL ANSI 1985 tests yet.  But there are a good number of
demo and test programs included plus another dozen EXEC CICS COBOL
programs which you can run on Windows or Linux with zCICS transaction
manager included in z390.  Melvyn Maltz and I presented zcobol and
zcics at SHARE in Austin in March, and I presented it again  at WAVV
in Orlando in May.

Now back to work on zcobol.  This week  I hope to add all the COPY
options for zcobol inluding COPY member OF/IN library and COPY
REPLACING so all the SM???? NIST programs will convert without errors
and all 459 NIST COBOL ptograms will convert without errors.
Then it will be on to getting them all clean compiled and then
executed.

Don Higgins
don@higgins.net
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-27T14:11:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bea7a2e-33ee-41df-b5ca-0af54af62c98@y34g2000yqd.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com> <vmg1m.119$WJ3.117@newsfe15.iad>`

```
On Jun 27, 3:29 pm, "Developer" <ab...@abuse.org> wrote:
> Any of them free?

Let Google be your friend.

Note it is COBOL-IT not COB-IT as I had first said.

Also tinyCobol



> --http://contract-developer.dyndns.biz
>
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: cobol compilers for Linux

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2009-06-28T11:22:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h27cpb$aik$1@news.dmz.bit.nl>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <c158cdb7-53d4-48e4-a76d-d7830e53a3fc@x1g2000prh.googlegroups.com>`

```
riplin wrote:

> On Jun 27, 6:55ï¿œam, "Developer" <ab...@abuse.org> wrote:
>> At present I have open-cobol in the linux box and was wondering what
…[8 more quoted lines elided]…
> MicroFocus COBOL

You might add Tiny Cobol to that list.
```

#### ↳ Re: cobol compilers for Linux

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-06-27T19:24:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba2b8587-9f56-4834-9d5f-9eafd9f540b1@d32g2000yqh.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad>`

```
On Jun 27, 2:55 am, "Developer" <ab...@abuse.org> wrote:
> At present I have open-cobol in the linux box and was wondering what else is available for the platform. I am using a 32-bit machine, but I could get a 64-bit one if pressed.
>
> --http://contract-developer.dyndns.biz

It would still be adviseable for you to develop (and test) your Cobol
applications in Windows platform... and 'deploy' it (as is) in Linux
box later using Wine.
```

##### ↳ ↳ Re: cobol compilers for Linux

- **From:** "Developer" <abuse@abuse.org>
- **Date:** 2009-06-27T19:47:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OQA1m.4192$oQ6.2191@newsfe12.iad>`
- **In-Reply-To:** `<ba2b8587-9f56-4834-9d5f-9eafd9f540b1@d32g2000yqh.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <ba2b8587-9f56-4834-9d5f-9eafd9f540b1@d32g2000yqh.googlegroups.com>`

```
I prefer to run it as a native Linux application with its ability to support 
multiple users etc. via a terminal or a web based session.
```

###### ↳ ↳ ↳ Re: cobol compilers for Linux

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-28T00:26:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a6babe6-154a-40d5-acb5-8b19361069fe@e21g2000yqb.googlegroups.com>`
- **References:** `<p%81m.3588$w01.1239@newsfe05.iad> <ba2b8587-9f56-4834-9d5f-9eafd9f540b1@d32g2000yqh.googlegroups.com> <OQA1m.4192$oQ6.2191@newsfe12.iad>`

```
On Jun 28, 2:47 pm, "Developer" <ab...@abuse.org> wrote:
> I prefer to run it as a native Linux application with its ability to support
> multiple users etc. via a terminal or a web based session.

Native Linux applications on a server can be accessed from ssh
sessions or from putty on a Windows client. Text mode Accept/Display
or SP/2 applications avoid the need for switching between keyboard and
mouse.

Several dozen users can run on a moderate single CPU system because it
has low resource requirements.

Running CGI applications in Cobol is also quite easy.


> --http://contract-developer.dyndns.biz
>
…[13 more quoted lines elided]…
> > box later using Wine.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
