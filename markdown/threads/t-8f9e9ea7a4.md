[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Re-read a record

_6 messages · 6 participants · 1997-04_

---

### Re-read a record

- **From:** "kwok-ho" <ua-author-7158421@usenetarchives.gap>
- **Date:** 1997-04-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33451C64.488B@netvigator.com>`

```

Hi,

I have a problem in reading record, I've read
some records from a input file, but how can I
read the first record again. Do I need to close the
file and then open it again?

Thanks
Kwok-ho
=================================
            Kwok-ho
 E-mail: kwo··.@net··r.com
=================================
```

#### ↳ Re: Re-read a record

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-04-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8f9e9ea7a4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33451C64.488B@netvigator.com>`
- **References:** `<33451C64.488B@netvigator.com>`

```

.Kwok-ho wrote:
.>
.> Hi,
.>
.> I have a problem in reading record, I've read
.> some records from a input file, but how can I
.> read the first record again. Do I need to close the
.> file and then open it again?
.>
.> Thanks
.> Kwok-ho
.> --
.> =================================
.> Kwok-ho
.> E-mail: kwo··.@net··r.com
.> =================================


If, for some reason, you have to go through the entire file again, then
the answer is yes--close and re-open the file. However, if you need the
information only from the first record later on, just save an image of
the first record in a Working-Storage item.

Mike Dodas
```

##### ↳ ↳ Re: Re-read a record

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-04-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8f9e9ea7a4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8f9e9ea7a4-p2@usenetarchives.gap>`
- **References:** `<33451C64.488B@netvigator.com> <gap-8f9e9ea7a4-p2@usenetarchives.gap>`

```

On Fri, 04 Apr 1997 20:38:19 -0800, Michael Dodas
wrote:

› .Kwok-ho wrote:
› .> 
…[5 more quoted lines elided]…
› .> file and then open it again?
Another way to do it is to define a second SELECT, FD, etc that
references the same external file as the original set. When the moment
arrives that you need that first record, just open and read the second
file.

George Trudeau, Systems Analyst, Town of Falmouth

"My employer wishes his opinions were as good as mine."
```

#### ↳ Re: Re-read a record

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-04T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8f9e9ea7a4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33451C64.488B@netvigator.com>`
- **References:** `<33451C64.488B@netvigator.com>`

```

Assuming you have a sequential file, and it is on a device where re-positioning is appropriate, you can certainly CLOSE the file and then OPEN the file again.

Probably would not work on some historic devices such as card readers (real or virtual).
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: Re-read a record

- **From:** "snap..." <ua-author-919861@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8f9e9ea7a4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<33451C64.488B@netvigator.com>`
- **References:** `<33451C64.488B@netvigator.com>`

```

I believe another way might be to save the first record in another
file, then when you need it close your existing files and open the files
where the rec is saved and read from it.


Hope this helps....

John
```

#### ↳ Re: Re-read a record

- **From:** "dennis to" <ua-author-15564317@usenetarchives.gap>
- **Date:** 1997-04-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8f9e9ea7a4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<33451C64.488B@netvigator.com>`
- **References:** `<33451C64.488B@netvigator.com>`

```

Kwok-ho wrote:
› 
› Hi,
…[12 more quoted lines elided]…
› =================================

Is it a index file or a sequential file ?
If it is an index file, initialize the record buffer and start again
If it is a sequential file, you must open the file and read again..

regard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
