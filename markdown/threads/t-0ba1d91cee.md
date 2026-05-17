[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What does Error 39 - "Input record smaller or larger than FD says it is" mean?

_8 messages · 6 participants · 1998-01 → 1998-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "nospam" <ua-author-9248638@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34cd7206.4421088@news.earthlink.net>`

```

I'm taking a COBOL class and having a problem with the above error
message. This is an IBM ES/9000.

Does anyone have ideas on what I could be doing wrong. I'm really
eager to get this fixed as I won't be able to contact my professor
until he's back in town next week.

Please post to the newgroup or send email to ab··.@ear··k.net

Thanks.
```

#### ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34cd7206.4421088@news.earthlink.net>`
- **References:** `<34cd7206.4421088@news.earthlink.net>`

```


Kill spammers wrote in message <34c··.@new··k.net>...
› I'm taking a COBOL class and having a problem with the above error
› message. This is an IBM ES/9000.
…[7 more quoted lines elided]…
› Thanks.

There are 3 places that the system looks for the size of each record in a
file.

A) the file itself (if it is old (i.e. DISP=SHR), then it looks at the
existing physical file attribute
B) Your JCL (particularly for DISP=NEW files), in the DCB field
C) The record length as determined by the FD in your program (either the
RECORD CONTAINS clause or the size of the 01 under the FD)

What that message means is that the length in "C" above doesn't agree with
one of the first two.

FYI, if your program had a specfic file-status field for this file, you
would be getting a "39" during the OPEN. This is why the error is a "39".
MVS programmers rarely do file status checking for QSAM files (but do for
VSAM), on the other thand, this is the type of thing that you can program
around by checking.
```

#### ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34cd7206.4421088@news.earthlink.net>`
- **References:** `<34cd7206.4421088@news.earthlink.net>`

```

Kill spammers wrote:
› 
› I'm taking a COBOL class and having a problem with the above error
› message. This is an IBM ES/9000.
 
› It is listed in the back of the manual.
 
› 
› Does anyone have ideas on what I could be doing wrong.

Yes, I have ideas... my first one is that you are not looking up File
Status errors in the manual.

› I'm really
› eager to get this fixed as I won't be able to contact my professor
› until he's back in town next week.

So contact your manual.

DD
```

#### ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34cd7206.4421088@news.earthlink.net>`
- **References:** `<34cd7206.4421088@news.earthlink.net>`

```

All of a sudden, nos··m@d··.spammer (Kill spammers) wrote:

› I'm taking a COBOL class and having a problem with the above error
› message. This is an IBM ES/9000.
…[7 more quoted lines elided]…
› Thanks.
It means just what it says. The input record does not match the
description in the FD statement. I would advise that you look up the
RECORD CONTAINS, FD, and possibly the RECORDING MODE clauses to get a
better idea of what may be wrong.

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "vlad..." <ua-author-17075103@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34cd7206.4421088@news.earthlink.net>`
- **References:** `<34cd7206.4421088@news.earthlink.net>`

```

nos··m@d··.spammer (Kill spammers) wrote:

› I'm taking a COBOL class and having a problem with the above error
› message. This is an IBM ES/9000.
 
› Does anyone have ideas on what I could be doing wrong. I'm really
› eager to get this fixed as I won't be able to contact my professor
› until he's back in town next week.
 
› Please post to the newgroup or send email to ab··.@ear··k.net
 
› Thanks.

Any File Status ERROR which i believe you are reffering to is a
permanent error..
a "39" means the KEY is NOT the Defined key of the Record... the File
Key is Smaller than the Actual Key of the Record...
```

##### ↳ ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ba1d91cee-p5@usenetarchives.gap>`
- **References:** `<34cd7206.4421088@news.earthlink.net> <gap-0ba1d91cee-p5@usenetarchives.gap>`

```


Vladimere wrote in message <6bloeq$5.··.@cam··g.com>...
› nos··m@d··.spammer (Kill spammers) wrote:
› 
…[16 more quoted lines elided]…
› 
This is not the definition of a File Status 39. Please check your reference
book (one more time).
```

###### ↳ ↳ ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

- **From:** "a..." <ua-author-17084515@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ba1d91cee-p6@usenetarchives.gap>`
- **References:** `<34cd7206.4421088@news.earthlink.net> <gap-0ba1d91cee-p5@usenetarchives.gap> <gap-0ba1d91cee-p6@usenetarchives.gap>`

```

In article <6bmkvl$g.··.@sjx··m.com>, "William M. Klein"
wrote:

› 
› Vladimere wrote in message <6bloeq$5.··.@cam··g.com>...
…[22 more quoted lines elided]…
› 
Language Reference

IBM COBOL Set for AIX
IBM COBOL for MVS & VM
IBM VisualAge for COBOL for OS/2

Document Number SC26-4769-01
...

File status 39:

Â¦The OPEN statement was unsuccessful because a Â¦
Â¦conflict was detected between the fixed file Â¦
Â¦attributes and the attributes specified for Â¦
Â¦that file in the program. These attributes Â¦
Â¦include the organization of the file Â¦
Â¦(sequential, relative, or indexed), the prime Â¦
Â¦record key, the alternate record keys, the codeÂ¦
Â¦set, the maximum record size, the record type Â¦
Â¦(fixed or variable), and the blocking factor. Â¦
Â¦ Â¦
Â¦Under AIX and OS/2, file status 39 is not Â¦
Â¦supported for line sequential files or Btrieve Â¦
Â¦files. Â¦
```

###### ↳ ↳ ↳ Re: What does Error 39 - "Input record smaller or larger than FD says it is" mean?

_(reply depth: 4)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ba1d91cee-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ba1d91cee-p7@usenetarchives.gap>`
- **References:** `<34cd7206.4421088@news.earthlink.net> <gap-0ba1d91cee-p5@usenetarchives.gap> <gap-0ba1d91cee-p6@usenetarchives.gap> <gap-0ba1d91cee-p7@usenetarchives.gap>`

```


A.··.@NoE··l.org wrote in message <34e··.@new··t.net>...
› In article <6bmkvl$g.··.@sjx··m.com>, "William M. Klein"
› wrote:
…[51 more quoted lines elided]…
› 
Good, as you can see a record key problem is only one of the many things
that an FS=39 can mean (and only applies to one of the organizations that
can get it).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
