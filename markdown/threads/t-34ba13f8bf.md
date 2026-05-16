[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help With Printers

_3 messages · 3 participants · 2000-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help With Printers

- **From:** Chris T. <ctaliercio@my-deja.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<861t5o$6p5$1@nnrp1.deja.com>`

```
What is the easiest method for obtaining information about a given
printer? For example, I have the printer name 'MyPrinter' and I want to
find out that MyPrinter is actually mapped to \\NETWORKMACHINE\HP5.

I know that I can read the WIN.INI file (the [PrinterPorts] section),
but I have been told that this will not be compatible with NT
workstations.

I have also tried the EnumPrinters WINAPI, calling it with
PRINTER_ENUM_NAME and PRINTER_INFO_5 set, but I cannot seem to get this
to work.

Does anybody have a working example of this code, or perhaps a better
way of doing this?

All help is greatly appreciated.

Thanks,
Chris


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Help With Printers

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86202r$bkb$1@news.cerf.net>`
- **References:** `<861t5o$6p5$1@nnrp1.deja.com>`

```
"Chris T." <ctaliercio@my-deja.com> wrote in message
news:861t5o$6p5$1@nnrp1.deja.com...
> What is the easiest method for obtaining information about a given
> I have also tried the EnumPrinters WINAPI, calling it with
> PRINTER_ENUM_NAME and PRINTER_INFO_5 set, but I cannot seem to get this
> to work.

You may post something spesific to show what you have tried. Other than that
you would benefit from taking a look at GetProfileString, DevMode and
ExtDeviceMode. This is the reliable API for WinNT 4.x and 3.51, while
EnumPrinters works great for Win9x and may be Win2000.

Cheesle
```

#### ↳ Re: Help With Printers

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uz%g4.14595$Dv1.382064@news2.rdc1.on.home.com>`
- **References:** `<861t5o$6p5$1@nnrp1.deja.com>`

```

"Chris T." <ctaliercio@my-deja.com> wrote in message
news:861t5o$6p5$1@nnrp1.deja.com...
> What is the easiest method for obtaining information about a given
> printer? For example, I have the printer name 'MyPrinter' and I want to
…[20 more quoted lines elided]…
> Before you buy.

       IDENTIFICATION DIVISION.
       PROGRAM-ID.  COUNTPRT.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
      * Operating System. WINDOWSNT
       Special-Names.
           call-convention 74 is APIentry
           call-convention 74 is expentry
            .
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       78  PRINTER-ENUM-LOCAL              value h"00000002".
       78  PRINTER-ENUM-NETWORK            value h"00000040".
       78  PRINTER-ENUM-NAME               value h"00000008".
       78  PRINTER-ENUM-SHARED             value h"00000020".
       01  szName                  pic x(30) value low-value.
       01  arrPrinterInfo.
         05  strPrinterInfo4 occurs 10.
           10  P4-pPrinterName     pointer.
           10  P4-pServerName      pointer.
           10  P4-dwAttributes     pic  9(9) comp-5.

       01  dwNeeded                pic  9(9) comp-5 value 10.
       01  dwReturned              pic  9(9) comp-5 value 0.
       01  bResult                 pic  9(9) comp-5  value 0.

       01  strLen                  pic  9(9) comp-5  value 0.

       LINKAGE SECTION.
       01  szPrinterName           pic x(80).
       01  szServerName            pic x(80).


       PROCEDURE DIVISION.
       MAIN.
           Call APIentry "EnumPrintersA" using
               by value         PRINTER-ENUM-NAME
               by reference     szName
               by value         4 size 4
               by reference     arrPrinterInfo
               by value         length of arrPrinterInfo
               by reference     dwNeeded
               by reference     dwReturned
               returning        bResult
           End-Call

           Display "There are " dwReturned " printers"
           Perform varying dwReturned from dwReturned by -1
             until dwReturned < 1
               If P4-pPrinterName (dwReturned) <> NULL
                   Set address of szPrinterName to
                       P4-pPrinterName (dwReturned)
                   Move 0 to strLen
                   Inspect szPrinterName tallying strLen
                       for characters before initial low-value
                   Display szPrinterName (1:strLen)
               End-If
           End-Perform
           Stop Run.


- Karl Wagner

P.S. This was originally posted on April 24, 1998. A search of dejanews for
EnumPrinter in past articles would also provide this code sample.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
