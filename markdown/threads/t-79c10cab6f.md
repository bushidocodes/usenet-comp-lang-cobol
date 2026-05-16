[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TRUNC(BIN) and COMP-5

_8 messages · 5 participants · 2007-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### TRUNC(BIN) and COMP-5

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-27T22:18:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com>`

```
I realized that I made one mistake in my reply to RW.

COMP-5 and COMP with TRUNC(BIN) perform identically.  The advantage of COMP-5 is 
that you can use the TRUNC(OPT) compiler option which will impact all "normal" 
COMP and BINARY fields.  You only need to use COMP-5 for fields that MAY contain 
data larger than the picture clause.  (All of this applies to IBM Enterprise 
COBOL - any release and NOT to COMP-5 in other implementations).

To summarize,
  For IBM Enterprise COBOL, COMP-5 is a "content of field" USAGE and is not 
documented as a "performance" USAGE.  It is documented as SLOWER than using 
COMP/BINARY with TRUNC(OPT) in most cases. See:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/2.4.54

which states,

"USAGE COMP-5 has the effect of applying TRUNC(BIN) behavior to individual data 
items. Therefore, you can avoid the performance overhead of using TRUNC(BIN) for 
every binary data item by specifying COMP-5 on only some of the binary data 
items, such as those data items that are passed to non-COBOL programs or other 
products and subsystems. The use of COMP-5 is not affected by the TRUNC 
suboption in effect. "
```

#### ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-10-28T13:12:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SU%Ui.17492$JD.3736@newssvr21.news.prodigy.net>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:mPOUi.263404$zt4.170346@fe08.news.easynews.com...
>I realized that I made one mistake in my reply to RW.
>
> COMP-5 and COMP with TRUNC(BIN) perform identically.  The advantage of 
> COMP-5 is ....

If I may introduce an observation here...

If one is relying on the specific performance of TRUNC(), does that not 
suggest one is catering to overflow, which further suggests the offending 
code should be reworked to avoid overflowing both primary and intermediate 
results or at the very least be handled with an ON SIZE ERROR clause?

Inquiring Minds Want to Know!
```

##### ↳ ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-28T11:31:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uP2Vi.10888$ho4.1898@bignews9.bellsouth.net>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com> <SU%Ui.17492$JD.3736@newssvr21.news.prodigy.net>`

```
"Michael Mattias" <mmattias@talsystems.com> wrote:
>
> If one is relying on the specific performance of TRUNC(), does that not suggest one is catering to overflow, which further 
> suggests the offending code should be reworked to avoid overflowing both primary and intermediate results or at the very least be 
> handled with an ON SIZE ERROR clause?

I have written algorithms that specifically depended on truncation. When you
choose the receiving data type correctly, it can be 'cheaper' than division with
a remainder. Example: stripping off the units digit of a number.
```

##### ↳ ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-28T22:09:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CM7Vi.15616$g82.1477@fe07.news.easynews.com>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com> <SU%Ui.17492$JD.3736@newssvr21.news.prodigy.net>`

```
It is (sort-of) this issue that explains why TRUNC(OPT) is the best performing 
setting.  With this setting, when you have "valid" (fits PICTURE) data *and* 
your operations either produce "valid" data or use ON SIZE ERROR phrases, then 
the compiler can create the "best" code.  TRUNC(STD) and TRUNC(BIN) both require 
the compile to produce code that DOES deal with "over-sized" contents and take 
"appropriate" action.
```

#### ↳ Re: TRUNC(BIN) and COMP-5

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-28T15:43:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com>`

```
On Sat, 27 Oct 2007 22:18:58 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>I realized that I made one mistake in my reply to RW.
>
…[20 more quoted lines elided]…
>suboption in effect. "

I naively thought THE MACHINE would be used to truncate a value to word size. For example,
I thought ADD A B GIVING C would generate

L   R5,A
A  R5,B
ST R5,C

Evidently, IBM has to call a function to insure a 32 bit register doesn't contain more
than 32 bits of data. :)  They COULD have done it with an inline

N   R5,=X'FFFFFFFF'     Do nothing instruction

Further adding to the mystery, this example says TRUNC(OPT) turns the mainframe into a
little-endian machine.

http://tinyurl.com/yt62pa
```

##### ↳ ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-28T22:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AM7Vi.15615$g82.6976@fe07.news.easynews.com>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com> <ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com>`

```
As I have said before, anyone (RW especially <G>) who ASSUMES that they know 
what code is generated by a compiler is likely to make mistakes about the 
performance of specific (COBOL) code sequences and features.

There is a "relatively" long history behind the types of code generated for 
COMP, BINARY, and various TRUNC options.  Certainly IBM's customers are QUITE 
happy with the fact that TRUNCIOPT) with COMP fields is the "best performing" 
combination - as this DOES allow for the majority of "legacy" code to perform 
well.
```

##### ↳ ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-10-29T15:39:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FFqVi.39$7i.49201@news.sisna.com>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com> <ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com>`

```
> Further adding to the mystery, this example says TRUNC(OPT) turns the 
> mainframe into a
> little-endian machine.

:-))

They are simply wrong.



"Robert" <no@e.mail> wrote in message 
news:ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com...
> On Sat, 27 Oct 2007 22:18:58 GMT, "William M. Klein" 
> <wmklein@nospam.netcom.com> wrote:
…[53 more quoted lines elided]…
> http://tinyurl.com/yt62pa
```

##### ↳ ↳ Re: TRUNC(BIN) and COMP-5

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-29T21:58:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RHsVi.373908$TR1.30730@fe06.news.easynews.com>`
- **References:** `<mPOUi.263404$zt4.170346@fe08.news.easynews.com> <ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:ghd9i31ouuucrujojivbmm8e24bo7cgee4@4ax.com...
> On Sat, 27 Oct 2007 22:18:58 GMT, "William M. Klein" 
> <wmklein@nospam.netcom.com> wrote:
>
<snip>
> Further adding to the mystery, this example says TRUNC(OPT) turns the 
> mainframe into a
> little-endian machine.
>
> http://tinyurl.com/yt62pa

Correction now sent to the IBM dox folks.  Thanks for pointing it out.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
