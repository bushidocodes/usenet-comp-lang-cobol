[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Performance Delta - Dynamic vs Static calls

_5 messages · 3 participants · 2002-03_

---

### Performance Delta - Dynamic vs Static calls

- **From:** Johnboy <member@mainframeforum.com>
- **Date:** 2002-03-20T04:14:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9852e9$2_3@news.teranews.com>`

```
Greetings!

Has anybody compiled any statistics on the differences in resource
consumption and performance between dynamic and static COBOL calls in an
LE environment? Especially interested in statistics for the CICS
environment.

Thanks in advance,

John Chase United Stationers, Inc. Des Plaines, IL USA
```

#### ↳ Re: Performance Delta - Dynamic vs Static calls

- **From:** george_proost <proost@spagirik.com>
- **Date:** 2002-03-20T04:15:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c985333$1_3@news.teranews.com>`
- **References:** `<3c9852e9$2_3@news.teranews.com>`

```
 wrote:
  > Use of the EXEC CICS LINK command in an LE runtime environment can mean
  > an increase in CPU cycles. Programs that issue many LINK commands seem
…[28 more quoted lines elided]…
  > supports read-only program storage.

Hi John,

I found some interesting info, short and concise on performance. No
real figures but good guidelines on how to accomplish acceptable usage
of cycles.



http://www.its.state.ut.us/contents/services/cics/programmerhints.shtml-
UTAH State -- Full text

Below is a small extract.
```

#### ↳ Re: Performance Delta - Dynamic vs Static calls

- **From:** JimMoore <member@mainframeforum.com>
- **Date:** 2002-03-20T04:15:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c985334$1_3@news.teranews.com>`
- **References:** `<3c9852e9$2_3@news.teranews.com>`

```
Just one quibble with the text in the previous post. It is not the CALL
'literal' format itself that makes the call static.

This is under the control of the DYNAM/NODYNAM compiler option.

If a progam is compiled with DYNAM, the CALL 'literal' form of the call
will be just as "dynamic" as the CALL identifier-1 format.

When the DYNAM option is used, the COBOL compiler will generate the
equivalent of a LOAD (SVC 06) followed by a BALR to the entry point (a
"dynamic" call) for all user-coded CALLs.

When the NODYNAM option is used, the compiler generates V-Type constants
in the ESD of the object deck for all coded CALLs. The binder (linkage
editor) must then resolve these addresses.

When the CALL identifier-1 format is used, the call is ALWAYS dynamic,
regardless of the DYNAM/NODYNAM compiler option.

Related topics: The "Is Initial" clause of the Program-ID, the Reentrant
(RENT) compile option
```

##### ↳ ↳ Re: Performance Delta - Dynamic vs Static calls

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-20T05:34:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a79s8v$mfl$1@slb5.atl.mindspring.net>`
- **References:** `<3c9852e9$2_3@news.teranews.com> <3c985334$1_3@news.teranews.com>`

```
Although the distinction between DYNAM/NODYNAM is *usually* true in
determining whether CALL "literal" is or is not dynamic/static, the
environment (in this context) was CICS and the use of the DYNAM compiler
option is prohibited there.
```

#### ↳ Re: Performance Delta - Dynamic vs Static calls

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-20T05:41:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a79shp$kbq$1@slb0.atl.mindspring.net>`
- **References:** `<3c9852e9$2_3@news.teranews.com>`

```
If you are interested in all aspects of performance (Including CALL
information), see:

   http://www-4.ibm.com/software/ad/cobol/library/

and select the "compiler" that is most appropriate.  (I believe that they
all address CALLs vs EXEC LINKs)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
