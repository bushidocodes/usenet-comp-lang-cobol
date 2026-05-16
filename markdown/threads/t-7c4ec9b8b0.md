[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/COBOL85 PROBLEM?

_2 messages · 2 participants · 2001-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### RM/COBOL85 PROBLEM?

- **From:** "������������������������ ���������������������" <dksoft@otenet.gr>
- **Date:** 2001-05-24T09:54:45+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eiau6$o86$1@usenet.otenet.gr>`

```
Running an application in Rm/Cobol with Runtime Dos 10 users and operating
system Ms-Win 2000 Professional or
win 2000 Server i receive a message (COBOL ERROR 30,MS-DOS ERROR 87) when i
print to a share printer of another machine.

The printer name can be LPT1(normal execution) ,
LPT3(ubnormal execution),\\machine name\share printer name(ubnormal
execution).

Can anybody solve this problem.
Thanks
```

#### ↳ Re: RM/COBOL85 PROBLEM?

- **From:** Michael Allen <m.allen@liant.com>
- **Date:** 2001-05-24T15:52:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0D7480.184F33@liant.com>`
- **References:** `<9eiau6$o86$1@usenet.otenet.gr>`

```
We were able to duplicate your problem, for which we have two potential
solutions:

1) Upgrade to the 32 bit Windows runtime.  The Windows runtime has been
specifically designed and tested for 32 bit Windows operating systems like
Win2K, NT, 9x, etc. - and does not exhibit this behavior.  The current version
is 7.00.03.  See http://www.liant.com/ for more information.

2) The other solution gets a little ugly. Here's how we were able to get the
DOS runtime to print to a networked printer from Windows 2K.  Also note that
this is not specific to 2000, but also fails on NT 4.0.  It does not appear to
fail on 9x.

First, go to Control Panel -> Printers, and select "Add Printer".
I selected a "local" printer - even though eventually, it's won't be.
Now, select an unused "Local Port".  I used LPT3:  I suppose you could use any
one of the unused ports.  You may even be able to create a new one using "Add
Port...". Click "Next", and pick the appropriate printer driver type... then
just follow the prompts until you're done.
After that, open a "Command Prompt" (DOS box), and type "net use LPT3:
\\machine_name\share_printer_name".

In your COBOL program, set your printer name to LPT3: (or use an environment
variable), and you should now be able to print to the device.

Hope that helps,
-Michael

"ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½" wrote:

> Running an application in Rm/Cobol with Runtime Dos 10 users and operating
> system Ms-Win 2000 Professional or
…[8 more quoted lines elided]…
> Thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
