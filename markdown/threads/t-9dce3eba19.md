[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Start & Read Next

_4 messages · 4 participants · 1997-09_

---

### Start & Read Next

- **From:** "ez..." <ua-author-653628@usenetarchives.gap>
- **Date:** 1997-09-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970923235501.TAA27316@ladder02.news.aol.com>`

```

Are there any words of wisdom about using these two verbs on a VSAM
indexed file? Any Examples for using a partial key?

Thanks -- Ed Mitchell

Ez··.@a··.com
```

#### ↳ Re: Start & Read Next

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-09-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9dce3eba19-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970923235501.TAA27316@ladder02.news.aol.com>`
- **References:** `<19970923235501.TAA27316@ladder02.news.aol.com>`

```

EzEdM wrote:
› 
› Are there any words of wisdom about using these two verbs on a VSAM
…[4 more quoted lines elided]…
› Ez··.@a··.com

They work and are, I believe, the only way to retrieve data on partial.

move half-a-key to rec-key.
start filename key not > rec-key.
read filename next at end etc.

DD
```

##### ↳ ↳ Re: Start & Read Next

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-09-24T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9dce3eba19-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9dce3eba19-p2@usenetarchives.gap>`
- **References:** `<19970923235501.TAA27316@ladder02.news.aol.com> <gap-9dce3eba19-p2@usenetarchives.gap>`

```

The Goobers wrote in article
<342··.@er··s.com>...
› EzEdM wrote:
›› 
…[13 more quoted lines elided]…
› DD

It is usually a good idea to ---
01 RECORD.
05 KEY.
10 PARTIAL KEY PIC X(XX).
10 FILLER PIC X(YY).
05 REMAINING-ATA.....

MOVE LOW-VALUES TO KEY.
MOVE DESIRED-VALUE TO PARTIAL-KEY.
START.....

The point being to make sure that the remaining portion of the key is
initialized to low-values before your START.

"There's a big difference between mostly dead, and all dead.  Please, open
his mouth."
    Miracle Max, "The Princess Bride"
```

###### ↳ ↳ ↳ Re: Start & Read Next

- **From:** "curtis cheuk" <ua-author-17072213@usenetarchives.gap>
- **Date:** 1997-09-27T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9dce3eba19-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9dce3eba19-p3@usenetarchives.gap>`
- **References:** `<19970923235501.TAA27316@ladder02.news.aol.com> <gap-9dce3eba19-p2@usenetarchives.gap> <gap-9dce3eba19-p3@usenetarchives.gap>`

```

Gary Lee 嚙踝蕭嚙篇嚙皚嚙踝蕭D嚙瘩
<01bcc956$d34f6ee0$218··.@gle··l.com>...
› The Goobers  wrote in article
› <342··.@er··s.com>...
…[36 more quoted lines elided]…
› 

Remember to handle the START .. INVALID KEY condition before READ NEXT.
That INVALID KEY condition will occur if PARTIAL-KEY is greater than any
existing keys in the file, or if the file is empty.

After READ NEXT, you also need to check if the READed key value matches
desired-value.

In fact, the following codes will be more efficient...

MOVE LOW-VALUES TO key.
MOVE desired-value TO partial-key.
START filename KEY = partial-key
INVALID KEY
MOVE 'N' TO WS-FOUND
NOT INVALID KEY
READ filename NEXT
(this READed record will have your desired-value)
END-START.

...because READ NEXT is unnecessary if the partial key value is not found,
i.e. partial-key = desired-value
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
