[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SYNCSORT returns negative numbers BEFORE positive?

_3 messages · 3 participants · 2002-04_

---

### SYNCSORT returns negative numbers BEFORE positive?

- **From:** hlngus@hotmail.com (Yvonne G)
- **Date:** 2002-04-01T09:29:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d999b872.0204010929.59911a42@posting.google.com>`

```
Hi,
I'm getting negative numbers at the beginning of a descending sort,
instead of at the end. The columns 576 - 579 are PIC S9(09) COMP .

I'm sure it's a basic error on my part, but can someone enlighten me
as to what can be modified?

* STEP 020 SORT HLDHIST FILE BY YTD-DLY-DRAW    
// DLBL HLDHIST,'HLDHIST.FILE',7                
// EXTENT ,POOL01,1,0,1,100                     
// DLBL HLDOUT1,'HLDHIST.SORTED',7              
// EXTENT ,POOL01,1,0,1,100                     
// EXEC SORT,SIZE=256K                          
 OPTION PRINT=CRITICAL,FILNM=(HLDOUT1,HLDHIST)  
 SORT FIELDS=(576,4,D),FORMAT=BI,FILES=1,WORK=1 
 RECORD TYPE=F,LENGTH=(600)                     
 INPFIL BLKSIZE=30000                           
 OUTFIL BLKSIZE=30000                           
 MODS PH1=(SORTMOD,L500,E15)

Thanks in advance.
```

#### ↳ Re: SYNCSORT returns negative numbers BEFORE positive?

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2002-04-02T10:17:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gty54i0.pminews@News.CIS.DFN.DE>`
- **References:** `<d999b872.0204010929.59911a42@posting.google.com>`

```
On 1 Apr 2002 09:29:07 -0800, Yvonne G wrote:

>Hi,
>I'm getting negative numbers at the beginning of a descending sort,
…[18 more quoted lines elided]…
>Thanks in advance.

Hi,

Negative numers have their first bit on, so sorting binary descending will
order them first.
To get around this, specify AQ as fieldtype and add ALTSEQ control cards to
specify the correct order.

SyncSort used to have an option to specify bits in the sort fileds card. If
your version allows this, sort ascending on the first bit and descending on
the rest

Hope this helps




Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

#### ↳ Re: SYNCSORT returns negative numbers BEFORE positive?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-04-02T16:37:14+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vcjaugrqr064egqjf562uc8p0f8rkp9c3@4ax.com>`
- **References:** `<d999b872.0204010929.59911a42@posting.google.com>`

```
On 1 Apr 2002 09:29:07 -0800 hlngus@hotmail.com (Yvonne G) wrote:

:>I'm getting negative numbers at the beginning of a descending sort,
:>instead of at the end. The columns 576 - 579 are PIC S9(09) COMP .

:>I'm sure it's a basic error on my part, but can someone enlighten me
:>as to what can be modified?

:>* STEP 020 SORT HLDHIST FILE BY YTD-DLY-DRAW    
:>// DLBL HLDHIST,'HLDHIST.FILE',7                
:>// EXTENT ,POOL01,1,0,1,100                     
:>// DLBL HLDOUT1,'HLDHIST.SORTED',7              
:>// EXTENT ,POOL01,1,0,1,100                     
:>// EXEC SORT,SIZE=256K                          
:> OPTION PRINT=CRITICAL,FILNM=(HLDOUT1,HLDHIST)  
:> SORT FIELDS=(576,4,D),FORMAT=BI,FILES=1,WORK=1 
:> RECORD TYPE=F,LENGTH=(600)                     
:> INPFIL BLKSIZE=30000                           
:> OUTFIL BLKSIZE=30000                           
:> MODS PH1=(SORTMOD,L500,E15)

Perhaps FI instead of BI?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
