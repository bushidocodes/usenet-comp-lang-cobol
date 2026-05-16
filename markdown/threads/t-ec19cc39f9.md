[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SYS$TRNLNM in VAXCOBOL

_3 messages · 3 participants · 1999-06_

---

### SYS$TRNLNM in VAXCOBOL

- **From:** jmahony@objectservices.com (John Mahony)
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fpx93.247$e9.107555@WReNphoon3>`

```
I am trying figure out the COBOL syntax to use the VMS System services
SYS$TRNLNM.  I haven't programmed in COBOL in years and have no VAXCOBOL or
VMS System Service documentation.  I am not sure how to handle the itemlst
parameter.  If anyone has a code snipet which does this it would be greatly
appreciated.



   -**** Posted from RemarQ, http://www.remarq.com/?a ****-
 Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: SYS$TRNLNM in VAXCOBOL

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-r1Tmdr1Xknww@Dwight_Miller.iix.com>`
- **References:** `<fpx93.247$e9.107555@WReNphoon3>`

```
On Tue, 15 Jun 1999 19:02:32, jmahony@objectservices.com (John Mahony)
wrote:

> I am trying figure out the COBOL syntax to use the VMS System services
> SYS$TRNLNM.  I haven't programmed in COBOL in years and have no VAXCOBOL or
…[3 more quoted lines elided]…
>

Type HELP at the VMS prompt, then type system_services, then 
$TRNLNM and it will give you complete help.  It looks something like 
this:

 SYSTEM_SERVICES

  $TRNLNM

       Returns information about a logical name.

       On Alpha systems, this service accepts 64-bit addresses.

       Format

         SYS$TRNLNM  [attr] ,tabnam ,lognam ,[acmode] ,[itmlst]

       C Prototype

         int sys$trnlnm  (unsigned int *attr, void *tabnam, void

                         *lognam, unsigned char *acmode, void 
*itmlst);

---------------------------
This might help some:

        call "sys$trnlnm" using
                by reference trnlnm-log-attr
                by descriptor "LNM$SYSTEM"
                by descriptor 
SYSLOCKED-LOGICAL-NAME(1:syslocked-log-nam-len)
                omitted
                by reference trnlnm-itemlist
                giving trnlnm-sys-call-result
        end-call.



-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: SYS$TRNLNM in VAXCOBOL

- **From:** "Phil Howell" <phowell@snowyhydro.com.au>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kksh7$kta$1@news.mel.aone.net.au>`
- **References:** `<fpx93.247$e9.107555@WReNphoon3>`

```

John Mahony wrote in message ...
>I am trying figure out the COBOL syntax to use the VMS System services
>SYS$TRNLNM.  I haven't programmed in COBOL in years and have no VAXCOBOL or
…[3 more quoted lines elided]…
>

    01  lnm_itmlst.
        03  filler                      pic s9(4) comp value 255.
        03  filler                      pic s9(4) comp value
                                            external lnm$_string.
        03  filler                      pointer value reference ws_tmp_buf.
        03  filler                      pointer value reference
ws_tmp_buf_len.
*   Terminator
        03  filler                      pic s9(9) comp value 0.

 Buffer UTL_CHECK_APPL_AVAILABILITY.COB                Insert        Forward

    call "sys$trnlnm" using
        by reference lnm$m_case_blind
        by descriptor "LNM$SYSTEM"
        by descriptor ws_tmp_buf2(1:ws_tmp_buf2_len)
        by reference psl$c_exec
        by reference lnm_itmlst
        giving result_status

    if result_status = ss$_nolognam then
        move spaces to ws_tmp_buf
 Buffer UTL_CHECK_APPL_AVAILABILITY.COB                Insert        Forward
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
