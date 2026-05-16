[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF NE 3.1 Call fails to pass linkage

_6 messages · 4 participants · 2008-09 → 2008-10_

---

### MF NE 3.1 Call fails to pass linkage

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2008-09-28T14:41:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net>`

```
I have one program calling another - "call using link-area." - using a 
simple linkage:
01  link-area.
    03  link-company pic 9(3).
    03  link-lease-no pic 9(10).
In the called program, the same structure exists in the linkage section. 
When animating, stepping thru the call, the 1st reference to link-company in 
the called program gives the error "203   CALL parameter not supplied".  I 
cannot find error 203 anywhere, but the call should be working correctly.  I 
have current patches to my 3.1.  Any ideas what's happening?  TIA, Paul
```

#### ↳ Re: MF NE 3.1 Call fails to pass linkage

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2008-09-28T15:17:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48dfe66f$0$5483$bbae4d71@news.suddenlink.net>`
- **References:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net>`

```
===========================
More info - I wrote 2 very small test programs:
  ---------------------------
 calling program "call1.cbl":

       data division.
       working-storage section.
       01  link-area.
           03  link-company        pic 9(3).
           03  link-lease-no       pic 9(10).
       01  resp                    pic x value " ".
       procedure division.
           display "starting call1".
           move zeros to link-area.
           call "call2" using link-area.
           display link-area.
           display "press enter".
           accept resp.
           stop run.
  ---------------------------
called program "call2.cbl":

       data division.
       working-storage section.
       01  resp                    pic x value " ".
       linkage section.
       01  link-area.
           03  link-company        pic 9(3).
           03  link-lease-no       pic 9(10).
       procedure division.
           display "starting call2".
           display link-area.
           move all "123" to link-area.
           display link-area.
           display "press enter".
           accept resp.
           exit program.

=======================
"Paul H" <NoSpamphobergNoSpam@att.net> wrote in message 
news:48dfddc9$0$5483$bbae4d71@news.suddenlink.net...
I have one program calling another - "call using link-area." - using a
simple linkage:
01  link-area.
    03  link-company pic 9(3).
    03  link-lease-no pic 9(10).
In the called program, the same structure exists in the linkage section.
When animating, stepping thru the call, the 1st reference to link-company in
the called program gives the error "203   CALL parameter not supplied".  I
cannot find error 203 anywhere, but the call should be working correctly.  I
have current patches to my 3.1.  Any ideas what's happening?  TIA, Paul
```

##### ↳ ↳ Re: MF NE 3.1 Call fails to pass linkage

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2008-09-28T14:39:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3c5f5ac-595e-4cbe-852a-5c79fb5d0b6d@79g2000hsk.googlegroups.com>`
- **References:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net> <48dfe66f$0$5483$bbae4d71@news.suddenlink.net>`

```
On 28 Sep, 21:17, "Paul H" <NoSpamphobergNoS...@att.net> wrote:
> ===========================
> More info - I wrote 2 very small test programs:
…[48 more quoted lines elided]…
> have current patches to my 3.1.  Any ideas what's happening?  TIA, Paul

Shouldn't the called program have the statement "procedure division
using link-area." rather than just "procedure division"?
```

##### ↳ ↳ Re: MF NE 3.1 Call fails to pass linkage

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-28T17:41:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YsGdncSnrf89ZELVnZ2dnUVZ_rPinZ2d@posted.mid-floridainternet>`
- **References:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net> <48dfe66f$0$5483$bbae4d71@news.suddenlink.net>`

```

"Paul H" <NoSpamphobergNoSpam@att.net> wrote in message
news:48dfe66f$0$5483$bbae4d71@news.suddenlink.net...

[snip]

>   ---------------------------
> called program "call2.cbl":

[snip]

>        linkage section.
>        01  link-area.
>            03  link-company        pic 9(3).
>            03  link-lease-no       pic 9(10).
>        procedure division.

Changing the line above to:

        procedure division using link-area.

eliminated the problem on my older system.
```

###### ↳ ↳ ↳ Re: MF NE 3.1 Call fails to pass linkage

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2008-09-28T16:55:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48dffd36$0$5458$bbae4d71@news.suddenlink.net>`
- **References:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net> <48dfe66f$0$5483$bbae4d71@news.suddenlink.net> <YsGdncSnrf89ZELVnZ2dnUVZ_rPinZ2d@posted.mid-floridainternet>`

```
Thank you both - that took care of my problem.  I've been away from COBOL 
too long - but it's coming back.  Little details like this will drive me 
crazy.  Pau H.
=============================

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:YsGdncSnrf89ZELVnZ2dnUVZ_rPinZ2d@posted.mid-floridainternet...

"Paul H" <NoSpamphobergNoSpam@att.net> wrote in message
news:48dfe66f$0$5483$bbae4d71@news.suddenlink.net...

[snip]

>   ---------------------------
> called program "call2.cbl":

[snip]

>        linkage section.
>        01  link-area.
>            03  link-company        pic 9(3).
>            03  link-lease-no       pic 9(10).
>        procedure division.

Changing the line above to:

        procedure division using link-area.

eliminated the problem on my older system.
```

##### ↳ ↳ Re: MF NE 3.1 Call fails to pass linkage

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-10-01T00:37:48
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222817868@f1.n250.z2.fidonet.ftn>`
- **References:** `<48dfddc9$0$5483$bbae4d71@news.suddenlink.net> <48dfe66f$0$5483$bbae4d71@news.suddenlink.net>`

```
Hello Paul!

28 Sep 08 21:17, Paul H wrote to All:

 PH> ===========================
 PH> More info - I wrote 2 very small test programs:
 PH>   ---------------------------
 PH> called program "call2.cbl":

 PH>        data division.
 PH>        working-storage section.
 PH>        01  resp                    pic x value " ".
 PH>        linkage section.
 PH>        01  link-area.
 PH>            03  link-company        pic 9(3).
 PH>            03  link-lease-no       pic 9(10).
 PH>        procedure division.
 PH> =======================

All called modules MUST have producedure division using a b c etc.
in your case procedure division using link-area.




Vince
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
