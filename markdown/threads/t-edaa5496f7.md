[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MFCOBOL calling C - HELP!!

_4 messages · 3 participants · 1999-03_

---

### MFCOBOL calling C - HELP!!

- **From:** "J. Mark Holder" <holdm@interpath.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37018012.CEE93768@interpath.com>`

```
Original environment:
MFCobol 3.2.50 for OS/2 and IBM CICS/OS2 2csd7 and DB2/2
- had MF/CICS 16bit programs calling 16bit VisualAge C/C++ wrapper to
32bit VisualAge C/C++ pgm.

New envrironment (for Y2K reasons):
MFCobol 4.0?? (its the latest release) for OS/2 and IBM CICS/OS2 latest
release and DB2/2
- finally figured out compile options, but unable to link due to
unresolved externals for 16bit C calls.

MF on-line docs don't help. Does anybody have an example of the COBOL->C
for OS/2 call syntax (all 32bit). C->COBOL would be nice too. Or tell me
where I might find the litature. Not scared to read the "book", just
please tell me which book.

All responses are appreciated!!!

J. Mark Holder
holdm@interpath.com
```

#### ↳ Re: MFCOBOL calling C - HELP!!

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370275f5@news1.us.ibm.net>`
- **References:** `<37018012.CEE93768@interpath.com>`

```
J. Mark,

The following is a module that I use to interface with IBM Personal
Communications CPI-C entry-points, which I believe are written in C.  This
module is written to support multiple platforms (OS/2 and Windows, both 16
and 32 bit), by using the MF conditional compile syntax.  I believe the
calling-convention that you want to use is "35".

Hope it helps...

Thanks - Todd



       identification division.
       program-id.                     c3p41cal.
       environment division.

      ******************************************************************
      * Calling Convention notes:                                      *
      *     0  - Default calling convention.                           *
      *     3  - Pascal calling convention.                            *
      *     8  - Causes called module to be statically linked.         *
      *    11  - Combincation of calling-conventions 3 & 8.            *
      *    35  - OS/2 32-bit C calling convention - stack parm passing.*
      ******************************************************************
       special-names.

      $if platform = "WIN16"
      $display ***** - Conditional Compile for Windows 32-bit
           call-convention 2 is calcon.
      $end

      $if platform = "WIN32"
      $display ***** - Conditional Compile for Windows 32-bit
           call-convention 2 is calcon.
      $end

      $if platform = "OS216"
      $display ***** - Conditional Compile for OS/2 16-bit
           call-convention 3 is calcon.
      $end

      $if platform = "OS232"
      $display ***** - Conditional Compile for OS/2 32-bit
           call-convention 35 is calcon.
      $end

       data division.

       working-storage section.
       01  ws-load-dll-ptr             usage procedure-pointer.
       01  ws-cubed-name               pic x(8) value 'C3P41CAL'.
       01  ws-first-time-sw            pic x    value 'n'.
           88  first-time                       value 'n'.
           88  not-first-time                   value 'y'.

       01  ws-subroutines.
           03  c3commsg-sub            pic x(8) value 'C3COMMSG'.
           03  c3bascal-sub            pic x(8) value 'c3bascal'.

           copy 'c3comlgw.cpy'.


       linkage section.
           copy 'c3shrcpi.cpy'.


       procedure division.
       0000-load-entry-points  section.

      *----------------------------------------------------------------*
      * This section of code will load the appropriate .DLL that       *
      * contains CPIC entry-points, depending upon the Operating       *
      * System and the mode (16/32 bit) that is being utilized.        *
      *                                                                *
      * CPIC support DLL's for Personal Communications, Version 4.1:   *
      *                                                                *
      *     OS2   - 16 bit - CPIC.DLL                                  *
      *     OS2   - 32 bit - CPIC32.DLL                                *
      *     WIN95/98/NT - 16 bit - not supported                       *
      *     WIN95/98/nt - 32 bit - WCPIC32.DLL                         *
      *                                                                *
      *----------------------------------------------------------------*
      $if platform = "WIN16"
      $display ***** - Conditional Compile for Windows 16-bit
               set ws-load-dll-ptr     to null
      $end

      $if platform = "WIN32"
      $display ***** - Conditional Compile for Windows 32-bit
               set ws-load-dll-ptr     to entry "WCPIC32.DLL"
      $end

      $if platform = "OS216"
      $display ***** - Conditional Compile for OS/2 16-bit
               set ws-load-dll-ptr     to entry "CPIC.DLL"
      $end

      $if platform = "OS232"
      $display ***** - Conditional Compile for OS/2 32-bit
               set ws-load-dll-ptr     to entry "CPIC.DLL"
      $end

           move +0                     to return-code.
           goback.
       0000-exit.
           exit.


      ******************************************************************
      * Personal Communications, Version 4.1 System Management entrys: *
      ******************************************************************

      ******************************************************************
      * This call will set the conversation security password.         *
      ******************************************************************
       entry 'xcscsp-entry'            using conversation-id
                                             security-password
                                             security-password-length
                                             cm-retcode.

           call calcon 'cmscsp'        using conversation-id
                                             security-password
                                             security-password-length
                                             cm-retcode
           end-call.
           goback.

      ******************************************************************
      * This call will set the conversation security user-id.          *
      ******************************************************************
       entry 'xcscsu-entry'            using conversation-id
                                             security-user-id
                                             security-user-id-length
                                             cm-retcode.

           call calcon 'cmscsu'        using conversation-id
                                             security-user-id
                                             security-user-id-length
                                             cm-retcode
           end-call.
           goback.

      ******************************************************************
      * This call will set the conversation security type.             *
      ******************************************************************
       entry 'xcscst-entry'            using conversation-id
                                             conversation-security-type
                                             cm-retcode.

           call calcon 'cmscst'        using conversation-id
                                             conversation-security-type
                                             cm-retcode
           end-call.
           goback.





J. Mark Holder wrote in message <37018012.CEE93768@interpath.com>...
>Original environment:
>MFCobol 3.2.50 for OS/2 and IBM CICS/OS2 2csd7 and DB2/2
…[18 more quoted lines elided]…
>
```

#### ↳ Re: MFCOBOL calling C - HELP!!

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3701adb3.193129841@news1.ibm.net>`
- **References:** `<37018012.CEE93768@interpath.com>`

```
On Tue, 30 Mar 1999 20:53:23 -0500, "J. Mark Holder"
<holdm@interpath.com> wrote:

>Original environment:
>MFCobol 3.2.50 for OS/2 and IBM CICS/OS2 2csd7 and DB2/2
…[7 more quoted lines elided]…
>unresolved externals for 16bit C calls.

You seem to be on an all things blue path... might I suggest IBM's
Visual Age COBOL as the cleanest solution?
```

##### ↳ ↳ Re: MFCOBOL calling C - HELP!!

- **From:** "J. Mark Holder" <holdm@interpath.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3702E590.51234BB6@interpath.com>`
- **References:** `<37018012.CEE93768@interpath.com> <3701adb3.193129841@news1.ibm.net>`

```
Appreciate the concern, but that option only creates another problem -
integration of a new platform plus cost. I contend my delima still stands -
what is the calling convention between Cobol 32bit and C/C++ 32bit on OS/2.

potential sol'n: see Mr Lucas response to original post.

Thanks for your time - Mark

Thane Hubbell wrote:

> On Tue, 30 Mar 1999 20:53:23 -0500, "J. Mark Holder"
> <holdm@interpath.com> wrote:
…[13 more quoted lines elided]…
> Visual Age COBOL as the cleanest solution?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
