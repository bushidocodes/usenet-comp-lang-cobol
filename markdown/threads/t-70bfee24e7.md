[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to read 10th record of TSQ directly? and how to delete the 10th record of the TSQ?

_4 messages · 4 participants · 2004-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to read 10th record of TSQ directly? and how to delete the 10th record of the TSQ?

- **From:** johnchittazhath@yahoo.com (John Varughese)
- **Date:** 2004-11-09T11:01:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4c71f2.0411091101.61104fd2@posting.google.com>`

```
How to read 10th record of TSQ directly? and how to delete the 10th
record of the TSQ?
```

#### ↳ Re: How to read 10th record of TSQ directly? and how to delete the 10th record of the TSQ?

- **From:** docdwarf@panix.com
- **Date:** 2004-11-09T14:14:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmr4uv$74f$1@panix5.panix.com>`
- **References:** `<f4c71f2.0411091101.61104fd2@posting.google.com>`

```
In article <f4c71f2.0411091101.61104fd2@posting.google.com>,
John Varughese <johnchittazhath@yahoo.com> wrote:
>How to read 10th record of TSQ directly? and how to delete the 10th
>record of the TSQ?

Please do your own homework.

DD
```

##### ↳ ↳ Re: How to read 10th record of TSQ directly? and how to delete the 10th record of the TSQ?

- **From:** "Ron" <NoMoSpam@Spamstopper.org>
- **Date:** 2004-11-09T17:31:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xoqdnbebRrqizgzcRVn_vA@giganews.com>`
- **References:** `<f4c71f2.0411091101.61104fd2@posting.google.com> <cmr4uv$74f$1@panix5.panix.com>`

```
> John Varughese <johnchittazhath@yahoo.com> wrote:
>>How to read 10th record of TSQ directly? and how to delete the 10th
>>record of the TSQ?

Again... RTFM.  (Read the Freakin Manual)
```

#### ↳ Re: How to read 10th record of TSQ directly? and how to delete the 10th record of the TSQ?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-11-10T06:04:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kbikd.874764$Gx4.32415@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<f4c71f2.0411091101.61104fd2@posting.google.com>`
- **References:** `<f4c71f2.0411091101.61104fd2@posting.google.com>`

```


John Varughese wrote:
> How to read 10th record of TSQ directly? and how to delete the 10th
> record of the TSQ?

IBM manuals are available on the web at http://mvshelp.com/ and also 
other places.

EXEC CICS READQ TS
     QUEUE (name)
     INTO  (data-area)
     LENGTH(data-area)
     ITEM  (data-value)
     NOHANDLE
END-EXEC

The trick is using ITEM to specify the tenth record in the queue.

Unfortunately, it would appear that you cannot delete an item in a 
Temp Storage queue.  EXEC CICS DELETEQ deletes the entire named Queue, 
and ALL its items.

Why do you need to delete just one item in a temp storage queue?  What 
are you using a temp storage queue for?

With kindest regards,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
