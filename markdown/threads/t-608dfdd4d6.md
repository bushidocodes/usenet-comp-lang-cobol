[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol/AIX 4.1/DCE problem

_2 messages · 2 participants · 1996-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol/AIX 4.1/DCE problem

- **From:** "dean..." <ua-author-17087283@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55lmtr$tqc@kettle.magna.com.au>`

```

Hi,

We've been writing MF COBOL 3.2 apps with Encina/DCE and C code for some months
on AIX 3.2.5. Recently we've moved to AIX 4.1.4 and the new DCE 2.1. Now, some
of our code breaks. The code that actually fails is in a DCE function
"uuid_to_string". If we call the same code from C it all works fine - it's
only from COBOL that it fails. We were advised that we should move to the
new MF COBOL 4.0 on AIX 4 - we did this with no success. Has anyone else seen
these sorts of problems? Below is a program (very similar to that
shown in the MF COBOL DCE Programmer's Guide) that breaks on AIX 4.1.4:

---------- uuid.cbl --------------

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
* UUID test
*
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
identification division.
$set sourceformat(fixed)
copy "dce.cpy".
$set sourceformat(free)

program-id. FMDGETUUID.

environment division.

data division.

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

working-storage section.

01 ws-size1 pic 9(9) comp-5.
01 ws-size2 pic 9(9) comp-5.
01 ws-count pic 9(9) comp-5.
01 ws-fcntr pic 9(9) comp-5.
01 ws-tcntr pic 9(9) comp-5.
01 ws-status usage uns-long.
01 ws-length usage uns-long.
01 ws-uuid usage uuid-t.
01 ws-uuid-text pic x(50).

01 ls-uuid-short pic x(32).
01 ws-uuid-ptr usage data-pointer.

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*linkage section.


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

*procedure division using ls-uuid-short.
procedure division.

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

A000-MAIN-LINE SECTION.

display "------ calling uuid_create -------"
call "uuid_create" using
by reference ws-uuid
by reference ws-status

if ws-status NOT = 0
display "FMDGETUUID uuid_create Failed with status = "
ws-status
perform Z000-FINISH
end-if
* display "ws-uuid = " ws-uuid

display "------ calling uuid_to_string -------"
call "uuid_to_string" using
by reference ws-uuid
by reference ws-uuid-ptr
by reference ws-status

if ws-status NOT = 0
display "FMDGETUUID uuid_to_string Failed with status = "
ws-status
perform Z000-FINISH
end-if

display "------ calling CBL_DCE_STRING_COPY -------"
move length of ws-uuid-text to ws-length
call "CBL_DCE_STRING_COPY" using
ws-uuid-ptr
ws-uuid-text
ws-length
ws-status

display "ws-uuid-text = " ws-uuid-text

move 1 to ws-fcntr ws-tcntr
move spaces to ls-uuid-short
move FUNCTION LENGTH(ws-uuid-text) to ws-size1
move FUNCTION LENGTH(ls-uuid-short) to ws-size2
if ws-size1 > ws-size2
move ws-size2 to ws-count
else
move ws-size1 to ws-count
end-if

perform ws-count times
if ws-uuid-text(ws-fcntr:1) NOT = "-"
move ws-uuid-text(ws-fcntr:1) to ls-uuid-short(ws-tcntr:1)
add 1 to ws-tcntr
end-if
add 1 to ws-fcntr
end-perform

display ls-uuid-short
perform Z000-FINISH.

A000-EXIT.
EXIT.

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Z000-FINISH SECTION.
exit program.

Z000-EXIT.
exit.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

----------- Makefile --------------------

#
# Makefile to build uuid
#
#-------------------------------------------------------------------------

FMD_STD_ROOT = /btal/dev/fmd/fmdd_rel/std/v0002000

INCLUDE_DIR = $$FMD_STD_ROOT/ref

include $(FMD_STD_ROOT)/ref/$(OS)_rules.mak
include $(FMD_STD_ROOT)/ref/rules_encina.mak

Article Unavailable
```

#### ↳ Re: MF Cobol/AIX 4.1/DCE problem

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-608dfdd4d6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<55lmtr$tqc@kettle.magna.com.au>`
- **References:** `<55lmtr$tqc@kettle.magna.com.au>`

```

John De Angelis wrote:
› 
› Hi,
…[5 more quoted lines elided]…
› only from COBOL that it fails.

Hi John. I'd like to help, but I'm afraid I don't have an equivalent setup here
to run your demo program on. Can you tell me how the call fails - bad return
code or something else ? I guess the first thing I'd check is that the typedefs
in dce.cpy are not in error.

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
