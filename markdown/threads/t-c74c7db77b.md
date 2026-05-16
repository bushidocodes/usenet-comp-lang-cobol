[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# number to string

_9 messages · 5 participants · 2006-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### number to string

- **From:** "luaks" <luaks@o2.pl>
- **Date:** 2006-12-14T02:45:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`

```
Hello

I'm beginer. I try to add some number to string, output must be string
too. For example:
01 STR1   PIC X(25)
01 NUM1  PIC 999V99
01 STR2   PIC X(30)

if STR1 = "aaaaa" and NUM1 = 123,45 then output: STR2 = "aaaa123,45"
How to di it?
Please help me.

luaks
```

#### ↳ Re: number to string

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-14T12:57:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<elrhn9$nvp$1@reader2.panix.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`

```
In article <1166093112.885280.96530@16g2000cwy.googlegroups.com>,
luaks <luaks@o2.pl> wrote:
>Hello
>
…[8 more quoted lines elided]…
>Please help me.

It would seem that you are not trying to 'add some number to string', you 
are trying to edit a numeric field with an implied decimal to a character 
field and concatenate that with an alphabetic field.

Now please do your own homework.

DD
```

#### ↳ Re: number to string

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-12-14T09:04:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93f80$458159ed$d066318d$4606@FUSE.NET>`
- **In-Reply-To:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`

```
luaks wrote:
> Hello
> 
…[11 more quoted lines elided]…
> 
Hint - Look up documentation for "STRING" verb.
bob.
```

##### ↳ ↳ Re: number to string

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-14T09:42:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<unv2o2db6htued844i98gtccqcoorst6ad@4ax.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com> <93f80$458159ed$d066318d$4606@FUSE.NET>`

```
On Thu, 14 Dec 2006 09:04:33 -0500, Bob Iles <bobi@mikal.com> wrote:

>> I'm beginer. I try to add some number to string, output must be string
>> too. For example:
…[11 more quoted lines elided]…
>bob.

Or possibly 05 levels...
```

###### ↳ ↳ ↳ Re: number to string

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-12-14T12:01:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91021$4581837c$d066318d$1293@FUSE.NET>`
- **In-Reply-To:** `<unv2o2db6htued844i98gtccqcoorst6ad@4ax.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com> <93f80$458159ed$d066318d$4606@FUSE.NET> <unv2o2db6htued844i98gtccqcoorst6ad@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 14 Dec 2006 09:04:33 -0500, Bob Iles <bobi@mikal.com> wrote:
> 
…[15 more quoted lines elided]…
> Or possibly 05 levels...

I know that 05 levels would be fine if you know
the input string is always going to be "aaaa", but
how could you use 05 level (excluding array processing)
to do this task.

just curious.
bob.
```

###### ↳ ↳ ↳ Re: number to string

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-14T11:10:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fi43o2d82amfvsk6i6tfr7a48gqoef00qn@4ax.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com> <93f80$458159ed$d066318d$4606@FUSE.NET> <unv2o2db6htued844i98gtccqcoorst6ad@4ax.com> <91021$4581837c$d066318d$1293@FUSE.NET>`

```
On Thu, 14 Dec 2006 12:01:52 -0500, Bob Iles <bobi@mikal.com> wrote:

>>>> if STR1 = "aaaaa" and NUM1 = 123,45 then output: STR2 = "aaaa123,45"
>>>> How to di it?
…[12 more quoted lines elided]…
>to do this task.

As with any problem - the first thing necessary is to determine what
is wanted.
Changing "aaaaa" to "ab   " could mean changing:
 if STR1 = "ab   " and NUM1 = 123,45 then output: STR2 = "ab   123,45"

Or maybe something else is wanted.    It may be a good idea for the
original poster to come up with a test plan with test data & expected
results before going much further.    If he's not sure about the
expected results, then he should check with his customer.
```

##### ↳ ↳ Re: number to string

- **From:** "luaks" <luaks@o2.pl>
- **Date:** 2006-12-15T02:15:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166177744.223517.296940@j72g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<93f80$458159ed$d066318d$4606@FUSE.NET>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com> <93f80$458159ed$d066318d$4606@FUSE.NET>`

```

Bob Iles napisal(a):

> Hint - Look up documentation for "STRING" verb.

Thank you Bob, this is what I need.

luaks
```

#### ↳ Re: number to string

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-12-14T10:41:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166121681.432604.325690@l12g2000cwl.googlegroups.com>`
- **In-Reply-To:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com>`

```

luaks wrote:

> I'm beginer. I try to add some number to string,

'add' is a mathematical operation. you probably mean 'concatenate'.

> output must be string
> too. For example:
…[5 more quoted lines elided]…
> How to di it?

You should note that NUM1 will not have the value '123,45' it may hold
the characters '12345' the 'V' in the PICTURE is an _implied_ decimal
point, it indicates where the decimal point (or comma to you) will go.
You will need to construct an additional edited numeric field that will
include an actual decimal point if that is an actual requirement.

You could use INSPECT to find the number of characters in STR1 and use
reference notation.
```

##### ↳ ↳ Re: number to string

- **From:** "luaks" <luaks@o2.pl>
- **Date:** 2006-12-15T02:21:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166178096.781617.182870@l12g2000cwl.googlegroups.com>`
- **In-Reply-To:** `<1166121681.432604.325690@l12g2000cwl.googlegroups.com>`
- **References:** `<1166093112.885280.96530@16g2000cwy.googlegroups.com> <1166121681.432604.325690@l12g2000cwl.googlegroups.com>`

```

Richard napisal(a):
> > I'm beginer. I try to add some number to string,
>
> 'add' is a mathematical operation. you probably mean 'concatenate'.

Yes, you are right. My english is weak.

> You should note that NUM1 will not have the value '123,45' it may hold
> the characters '12345' the 'V' in the PICTURE is an _implied_ decimal
…[5 more quoted lines elided]…
> reference notation.

Good hint. I will do that.
Thank you.

luaks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
