[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Serial POS Printer

_6 messages · 3 participants · 2000-03_

---

### Serial POS Printer

- **From:** Bob7536@aol.com
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bfl99$efo$1@nnrp1.deja.com>`

```
Hi Folks,
I have an NCR 7193 thermal receipt serial printer. Let
me
give you a little background. We started with a DOS product and I would
handle the receipt printer by setting the following:
SELECT RECEIPT-PRINTER ASSIGN TO "LPT1:"
ORGANIZATION IS LINE SEQUENTIAL
FILE STATUS IS RECEIPT-PRINTER-FILE-STATUS.
I would then in the AUTOEXEC.BAT uses the MODE command to redirect the
serial
port to the printer port (ie. MODE LPT1:=COM1: ).
This worked great I could look at the RECEIPT-PRINTER-FILE-STATUS to
determine if the printer was "on" or "off" line.
I then converted the code to the Win9x world and found the redirection
would
not work so I made the following change:
SELECT RECEIPT-PRINTER ASSIGN TO "COM1:"
ORGANIZATION IS LINE SEQUENTIAL
FILE STATUS IS RECEIPT-PRINTER-FILE-STATUS.
This seemed to work fine, except for one thing if the printer was off-
line (
paper out or door open ) the RECEIPT-PRINTER-FILE-STATUS was still
coming
back as okay.
I have tried using the COBOL byte streaming to query the printer about
its
status but this seems to slow the printer down alot. Any thoughts ?
Thanks,
Bob Hennessey


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Serial POS Printer

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rqRC4.750$Id7.14571@news.swbell.net>`
- **References:** `<8bfl99$efo$1@nnrp1.deja.com>`

```
Have you tried sending the printout to LPT1, "Capturing" the printer
port and spooling the results to COM1?

In this scenario, you shouldn't care whether the printer is out of
paper.

<Bob7536@aol.com> wrote in message news:8bfl99$efo$1@nnrp1.deja.com...
> Hi Folks,
> I have an NCR 7193 thermal receipt serial printer. Let
> me
> give you a little background. We started with a DOS product and I
would
> handle the receipt printer by setting the following:
> SELECT RECEIPT-PRINTER ASSIGN TO "LPT1:"
> ORGANIZATION IS LINE SEQUENTIAL
> FILE STATUS IS RECEIPT-PRINTER-FILE-STATUS.
> I would then in the AUTOEXEC.BAT uses the MODE command to redirect
the
> serial
> port to the printer port (ie. MODE LPT1:=COM1: ).
> This worked great I could look at the RECEIPT-PRINTER-FILE-STATUS to
> determine if the printer was "on" or "off" line.
> I then converted the code to the Win9x world and found the
redirection
> would
> not work so I made the following change:
…[3 more quoted lines elided]…
> This seemed to work fine, except for one thing if the printer was
off-
> line (
> paper out or door open ) the RECEIPT-PRINTER-FILE-STATUS was still
> coming
> back as okay.
> I have tried using the COBOL byte streaming to query the printer
about
> its
> status but this seems to slow the printer down alot. Any thoughts ?
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Serial POS Printer

- **From:** Bob7536@aol.com
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bibjt$c0f$1@nnrp1.deja.com>`
- **References:** `<8bfl99$efo$1@nnrp1.deja.com> <rqRC4.750$Id7.14571@news.swbell.net>`

```
Hi Jerry,
No I have not tried this. Is there a windows setting for capturing the
LPT port and sending it to the COM port ?
Thank,
Bob Hennessey


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Serial POS Printer

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bmvro$f0h$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<8bfl99$efo$1@nnrp1.deja.com> <rqRC4.750$Id7.14571@news.swbell.net> <8bibjt$c0f$1@nnrp1.deja.com>`

```
    I no longer have the original message.  I am assuming that you are
trying
to use a DOS program in a windows command prompt.  As near as I can tell,
DOS programs have NO access to windows serial printers.  You have to run the
various mode commands in the one, lone, command prompt accessing the
serial device.

    Third party serial drivers could change the rules I suppose.

    Also, MF dos runtime 3.4 seems to be unable to access
a serial port AT ALL on NT.

    Ironically, the best luck I ever had with a serial printer was
when I put the printer on a Novell server.  I called it LPT3 from
my program.



<Bob7536@aol.com> wrote in message news:8bibjt$c0f$1@nnrp1.deja.com...
> Hi Jerry,
> No I have not tried this. Is there a windows setting for capturing the
…[6 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Serial POS Printer

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhqlp$d9g$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<8bfl99$efo$1@nnrp1.deja.com>`

```
    Did you also use the "MODE COM1:96,N,8,1,P" command (for 9600 baud).
The trailing ",P"
makes a big difference when printing more than one line at a time.

    Of course, in this case, an offline printer will cause a write to hang
the pc.
You use this before the redirect.

    You did not say which compiler.  If you are using MF 3.4, HOW do we
access the com port
when running on NT?




<Bob7536@aol.com> wrote in message news:8bfl99$efo$1@nnrp1.deja.com...
> Hi Folks,
> I have an NCR 7193 thermal receipt serial printer. Let
…[30 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Serial POS Printer

- **From:** Bob7536@aol.com
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bibn3$c0o$1@nnrp1.deja.com>`
- **References:** `<8bfl99$efo$1@nnrp1.deja.com> <8bhqlp$d9g$1@ssauraab-i-1.production.compuserve.com>`

```
Hi Russell,
If you use the mode command to redirect the printer it seems to have no
effect in Windows.
Thanks,
Bob Hennessey


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
