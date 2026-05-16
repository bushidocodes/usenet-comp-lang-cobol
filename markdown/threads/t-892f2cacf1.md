[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Limit on Arrays on Enterpresie Cobol in Z sereis

_12 messages · 6 participants · 2006-11_

---

### Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** "ravi" <vze8q51f@verizon.net>
- **Date:** 2006-11-11T05:52:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fyd5h.121$5F2.98@trnddc04>`

```
In one of our Cobol program trying load arrays (Cobol memory table). The record length of the array was 85. Based on the requirement we have to load atleast 350,000 records into that. Unfortunately It is not allowing more than 60000 recs. While compiling itself we are getting this error.    

Cobol Version is 

PP 5655-G53 IBM Enterprise COBOL for z/OS  3.3.1       
IGYDS1155-S   A data item exceeded the maximum supported length 16777215 for an item in the "WORKING-STORAGE SECTION", 
              "LOCAL-STORAGE SECTION" or "LINKAGE SECTION".  The item was truncated to 16777215 characters. 

I thought in  IBM Enterprise COBOL for z/OS  3.3.1 we can load upto 128mb. But still not allowing more than 60000 recs. Can anyone tell me what I'm missing like any compiler option etc. Is there any workaround for that?

Thanks 
 
Ravi
sankarravi6@yahoo.com
```

#### ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-11-11T03:32:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1163244774.658824.239380@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<fyd5h.121$5F2.98@trnddc04>`
- **References:** `<fyd5h.121$5F2.98@trnddc04>`

```

ravi wrote:
> In one of our Cobol program trying load arrays (Cobol memory table). The record length of the array was 85. Based on the requirement we have to load atleast 350,000 records into that. Unfortunately It is not allowing more than 60000 recs. While compiling itself we are getting this error.
>
…[10 more quoted lines elided]…
> Ravi


Hello Ravi

I think you will find that 16777215 is the table size  limit for this
compiler.  I looked at the language reference manuals that I downloaded
from the IBM website, the one for version 3 release 3 has this limit,
while that for version 3 release 4 has a table size limit of
134,217,727 bytes.

The place to look in the manual is Appendix B Compiler limits.

It looks as though you will have to find another way of achieving your
requirement.  You could perhaps load the data as a VSAM KSDS or RRDS
and ensure that your dataset definition (control intervals, control
areas, etc) and program buffering permits you to load it into memory in
its entirety, so that the file i/o turns into a form of system managed
table access.

Obviously you could consider upgrading your compiler, it might even be
that your maintenance agreement with IBM already permits that, but that
will presumably take some time to get through your system admin.

with regards

Robert
```

##### ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** docdwarf@panix.com ()
- **Date:** 2006-11-11T13:16:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ej4ifl$hs7$1@reader2.panix.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com>`

```
In article <1163244774.658824.239380@e3g2000cwe.googlegroups.com>,
Robert Jones <rjones0@hotmail.com> wrote:
>
>ravi wrote:
…[15 more quoted lines elided]…
>128mb.

[snip]

>I think you will find that 16777215 is the table size  limit for this
>compiler.  I looked at the language reference manuals that I downloaded
>from the IBM website, the one for version 3 release 3 has this limit,
>while that for version 3 release 4 has a table size limit of
>134,217,727 bytes.

Greatly appreciated, Mr Jones... I believe this might have been touched on 
a while back but your presentation, here and now, causes me to reconsider 
what I learned about 'size' when it comes to system design, where repeated 
lookups on 'small' amounts of data are 'hardcoded' (eg, a copybook 
containing valid USA state/territory codes), 'medium' amounts are loaded 
into a WS table and 'large' quantities are VSAM files.

My first thought, on reading the original posting, was '350,000 recs for a 
lookup?  Even the 60,000 achieved is too much for WS, time to use a 
VSAM... unless it's a Must Be *Really* Fast application, in which case 
maybe he can code aligned tables and refer to them using an 'out of range' 
subscript'... and then I realised that these techniques might be 
Acceptable-But-Extreme Practise for a compiler with a table-size limit of 
32K... and then I realised that 'modern compilers' have a habit of 
re-arranging WS so that the oh-so-carefully-aligned Tables of Yore might 
not be where one thinks they were...

... and then I realised, as you've pointed out, that how much is permitted 
to be loaded into WS has changed a *wee* bit since the days of IKFCBL00's 
earlier incarnations.

Thanks much.

DD
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-11-11T07:35:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12lbkcs3meq875a@news.supernews.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com>`

```

<docdwarf@panix.com>
>
> Greatly appreciated, Mr Jones... I believe this might have been touched on
…[22 more quoted lines elided]…
> DD

I'd think a couple of tests would be in order.

It's possible that it takes longer to search 350,000 records in memory than 
to find the target in an ISAM file.
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 4)_

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 2006-11-11T16:54:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fn5h.5292$L6.1771@newsread3.news.pas.earthlink.net>`
- **In-Reply-To:** `<12lbkcs3meq875a@news.supernews.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <12lbkcs3meq875a@news.supernews.com>`

```
HeyBub wrote:
> <docdwarf@panix.com>
>> Greatly appreciated, Mr Jones... I believe this might have been touched on
…[27 more quoted lines elided]…
> 
Hopefully you meant VSAM KSDS, not ISAM.  VSAM with Batch LSR (BLSR is 
invoked by just making appropriate changes to JCL) and a large number of 
hiperspace buffers could definitely be faster for keyed record access if 
the application is not using efficient search methods for a large 
internal table.  VSAM with BLSR uses very efficient (hashing) techniques 
to locate in-memory VSAM CIs.  With enough BLSR buffers, once you have 
accessed enough records to load all CIs, you in effect have a in-memory 
table but with the storage managed externally to the application 
program.  Could be a very simple solution, without having to upgrade the 
COBOL compiler. (unless things have changed, you have to use BLSR with 
VSAM to get the more efficient buffer management techniques for dealing 
with very large numbers of buffers).
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-11-12T07:26:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12le88gph73nj42@news.supernews.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <12lbkcs3meq875a@news.supernews.com> <4fn5h.5292$L6.1771@newsread3.news.pas.earthlink.net>`

```

"Joel C. Ewing" <
>>
>> I'd think a couple of tests would be in order.
…[3 more quoted lines elided]…
> Hopefully you meant VSAM KSDS, not ISAM.
[...]

Uh, no.

I don't have VSAM. I barely have '0s' and '1s'.

Nevertheless, whether you're looking something up in ISAM, VSAM, or a filing 
cabinet, there's often a faster technique.

Normally, I don't give a fig about micro-efficiency. That said....

I recently reworked a bit of code done by a programmer whose training was 
initially in VB. The object was to sort the contents in a Windows ListView 
Box.

He moved "1" to the SortOrder property of the box.

SIX MINUTES later, the operation completed (it was a large list) [Only 1 
instruction - high marks for macro efficiency]

I read the box contents, wrote an ISAM file (remember, I have only '0s' and 
'1s') then used the resulting file to re-fill the box. [Two loops, 14 
instructions - not as macro efficient]

FIVE SECONDS.

There are, no doubt, other techniques and mine probably would not be as 
efficient on a different compiler. And maybe he was doing something else 
that caused the horrendous execution speed. I dunno.

Point is, there's often another technique.
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-11-11T21:59:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vpacl2pchl4pr0ksc3b9htt1bgjrklls64@4ax.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <12lbkcs3meq875a@news.supernews.com>`

```
On Sat, 11 Nov 2006 07:35:26 -0600 "HeyBub" <heybubNOSPAM@gmail.com> wrote:

:>I'd think a couple of tests would be in order.

:>It's possible that it takes longer to search 350,000 records in memory than 
:>to find the target in an ISAM file. 

Depends on how it is used.

It is clearly faster to do a binary search of 350K records in memory than to
run down an index to find the record.

On the other hand, if one will only be matching 20 records it would clearly be
faster to run the index than to read the 350K records.
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-11-13T13:43:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ej9sqs$22f$1@reader2.panix.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <12lbkcs3meq875a@news.supernews.com>`

```
In article <12lbkcs3meq875a@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>
><docdwarf@panix.com>

[snip]

>> My first thought, on reading the original posting, was '350,000 recs for a
>> lookup?  Even the 60,000 achieved is too much for WS, time to use a
…[10 more quoted lines elided]…
>> earlier incarnations.

[snip]

>I'd think a couple of tests would be in order.
>
>It's possible that it takes longer to search 350,000 records in memory than 
>to find the target in an ISAM file. 

I would agree... but I'd say that more than a couple, or even a 
couple-three tests, might prove to be of interest and/or value.  The 
Operating System and compiler start to figure in here - actual 
disk-resident files versus buffered/'virtual IO files', where the data and 
index components reside (same disk vs. different disks), key size and 
type, how the compiler deals with a SEARCH versus a SEARCH ALL... a 
variety of combinations and permutations begin to become apparent.

DD
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-11-11T14:21:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1163283702.073134.260810@k70g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<ej4ifl$hs7$1@reader2.panix.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com>`

```

message snipped

Thanks for your kind words Doc.  As an afterthought, an additional
benefit from using a VSAM KSDS or RRDS is that one can also have one or
more alternate indexes that can also be loaded up into memory buffers,
so not only is the keyed searching much faster for the primary index,
but you can also do fast key searches on the alternate indexes.

Robert
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-11-12T01:29:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76ncl29vp0tk3cjgm6trt9dh8qf2bkmpqq@4ax.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <1163283702.073134.260810@k70g2000cwa.googlegroups.com>`

```
On 11 Nov 2006 14:21:42 -0800 "Robert Jones" <rjones0@hotmail.com> wrote:

:>Thanks for your kind words Doc.  As an afterthought, an additional
:>benefit from using a VSAM KSDS or RRDS is that one can also have one or
:>more alternate indexes that can also be loaded up into memory buffers,
:>so not only is the keyed searching much faster for the primary index,
:>but you can also do fast key searches on the alternate indexes.

All that is certainly available in an instorage copy.
```

###### ↳ ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-11-13T13:52:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ej9tas$2a1$1@reader2.panix.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com> <ej4ifl$hs7$1@reader2.panix.com> <1163283702.073134.260810@k70g2000cwa.googlegroups.com>`

```
In article <1163283702.073134.260810@k70g2000cwa.googlegroups.com>,
Robert Jones <rjones0@hotmail.com> wrote:
>
>message snipped
>
>Thanks for your kind words Doc.

Shucks, you'se jes' easily gratified, that's all.

DD
```

##### ↳ ↳ Re: Limit on Arrays on Enterpresie Cobol in Z sereis

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-11-13T11:54:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1163447684.776596.283400@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<1163244774.658824.239380@e3g2000cwe.googlegroups.com>`
- **References:** `<fyd5h.121$5F2.98@trnddc04> <1163244774.658824.239380@e3g2000cwe.googlegroups.com>`

```

Robert Jones wrote:
> ravi wrote:
> > In one of our Cobol program trying load arrays (Cobol memory table). The record length of the array was 85. Based on the requirement we have to load atleast 350,000 records into that. Unfortunately It is not allowing more than 60000 recs. While compiling itself we are getting this error.
…[15 more quoted lines elided]…
>
In addition to what I wrote before

I have since thought some more and calculate that 60,000 x 85 bytes is
5,100,000 bytes, which is still well within the 16,777,215 byte limit,
350,000 x 85 bytes would be 29,750,000 bytes which would break that
limit, so the problem would still apply even if you got quite a bit
further loading the table.  Are you sure that your table elements are
really 85 bytes?

Another way of tackling the problem, for tables that are not much (a
few times) larger than the compiler limit, could be to divide the
tables up by fields so that one has corresponding elements in each
table that can be accessed with the same subscript, though
unfortunately not the same index.

e.g.

01  table-a.
     03  element-a occurs 500,000.
           05  key-field         pic x(25).
01  table-b
     03  element-b occurs 500,000.
           05  datafield-1      pic x(10).
           05  datafield-2      pic x(20).
01  table-c
     03  element-c occurs 500,000.
           05  datafield-3      pic x(30).
> 
> with regards
> 
> Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
