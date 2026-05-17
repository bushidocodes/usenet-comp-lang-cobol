[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 'Advanced' Move statements

_9 messages · 7 participants · 1998-02 → 1998-03_

---

### 'Advanced' Move statements

- **From:** "$appvar2$" <ua-author-16631164@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

Can anyone tell me if it is possible to move a field1 to a field2, when
field2 is variable and I want to code only one move statement. In cobol II
for MVS.
And the declaration of the variables can not be in Linkage Section.

Lars
```

#### ↳ Re: 'Advanced' Move statements

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd42b5$82e0db50$ae881eac@nw105005>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

Lars,
I think your're saying when field2 isn't always field2 but can be some
other receiving field. And, you want to use just one move statement to move
field1 to fieldx. Is this what you mean by "variable"? If I'm
understanding you correctly, then what your looking for is done quite often
in C/C++ with pointer dereferences or indirection, but is not done in
COBOL85. Their may be an extension for this by some COBOL compilers, but
I'm not aware of any. I beleive the next COBOL ANSI standard will make use
of pointer dereferencing/indirection and intrinsic functions.

Dan Maltes
Applied Systmes Technology

$AppVar1$ <$AppVar2$@storebrand.no> wrote in message
<01bd42b5$82e0db50$ae881eac@nw105005>...
› Can anyone tell me if it is possible to move a field1 to a field2, when
› field2 is variable and I want to code only one move statement. In cobol II
…[3 more quoted lines elided]…
› Lars
```

#### ↳ Re: 'Advanced' Move statements

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd42b5$82e0db50$ae881eac@nw105005>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

In article <01bd42b5$82e0db50$ae881eac@nw105005>,
$AppVar1$ <$AppVar2$@storebrand.no> wrote:
› Can anyone tell me if it is possible to move a field1 to a field2, when
› field2 is variable and I want to code only one move statement. In cobol II
› for MVS.
› And the declaration of the variables can not be in Linkage Section.

Not sure what you mean here... could you include some code to demonstrate?

DD
```

#### ↳ Re: 'Advanced' Move statements

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bd42b5$82e0db50$ae881eac@nw105005>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

$AppVar1$ wrote:
› 
› Can anyone tell me if it is possible to move a field1 to a field2, when
…[4 more quoted lines elided]…
› Lars

Lars, we need a little more information. Can you post the definitions
of the fields involved and some examples of what you want to move?
```

#### ↳ Re: 'Advanced' Move statements

- **From:** "huib cobol frog klink" <ua-author-17074505@usenetarchives.gap>
- **Date:** 1998-02-26T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd42b5$82e0db50$ae881eac@nw105005>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

Lars,

Two options. With variable you mean
1) field2 is not always the same field
2) field2 is varying in length

1) It can be done in Cobol II for MVS if you use one of the (IBM) language
extensions and drop your requirement that field2 can not be in Linkage:

LINKAGE SECTION.
01 FIELD2...

PROCEDURE DIVISION.
...
SET ADDRESS OF FIELD2 TO what you like.
...
MOVE FIELD1 TO FIELD2.

2)
DATA DIVISION.
WHATEVER SECTION.
01 FIELD2.
03 ONEBYTE PIC X OCCURS 1 TO max DEPENDING ON F2LEN.

01 F2LEN PIC S9999 USAGE BINARY.
- the level numbers may vary
- usage bin is for efficiency.
- f2len could be IN field2, but before the varying part.

Now in the PROCEDURE DIVISION
upon a MOVE whatever TO FIELD2
the length will be set correctly to the length of whatever (wich may be
varying in length too, in that case the "current" length is used).

This you wanted to know?

Success,
Huib

$AppVar1$ wrote:

› Can anyone tell me if it is possible to move a field1 to a field2, when
› field2 is variable and I want to code only one move statement. In cobol II
…[3 more quoted lines elided]…
› Lars
```

##### ↳ ↳ Re: 'Advanced' Move statements

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f6253d8ebd-p5@usenetarchives.gap>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005> <gap-f6253d8ebd-p5@usenetarchives.gap>`

```

Huib Cobol Frog Klink wrote:
(snip)


› Lars,
› 
…[44 more quoted lines elided]…
›› Lars

Not really clear to me what Lars circumstances are / what problem he's trying to
solve. Does anyone else think this might be a case for reference modification?
You'd need some setup to control the lengths, but you'd have just one MOVE
statement. Is he thinking about copied Procedure Division code?

Bill lynch
```

###### ↳ ↳ ↳ Re: 'Advanced' Move statements

- **From:** "huib cobol frog klink" <ua-author-17074505@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f6253d8ebd-p6@usenetarchives.gap>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005> <gap-f6253d8ebd-p5@usenetarchives.gap> <gap-f6253d8ebd-p6@usenetarchives.gap>`

```

Bill,

Not sure how you see ref.mod. in this case. Neither do I understand what you mean
with "copied PD code". But then you are right: the question is not clear. Let Lars
himself tell what he is after.

LARS, WHERE ARE YOU? WHAT DO YOU REALY WANT?
(Please keep the subject COBOL related :))) )

Bill Lynch wrote:

› 8< snipped my original post
› 
…[5 more quoted lines elided]…
› Bill lynch
```

###### ↳ ↳ ↳ Re: 'Advanced' Move statements

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f6253d8ebd-p7@usenetarchives.gap>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005> <gap-f6253d8ebd-p5@usenetarchives.gap> <gap-f6253d8ebd-p6@usenetarchives.gap> <gap-f6253d8ebd-p7@usenetarchives.gap>`

```

Huib Cobol Frog Klink wrote:

› Bill,
› 
…[16 more quoted lines elided]…
›› Bill lynch

I was speculating that Lars *might* be working on some code to be copied into the
Procedure Division, which would manipulate some standard W-S data names. The data
names wouldn't always have the same length. So the copied P code could use the LENGTH
OF special register to prime a subscript and use the subscript in a MOVE with
reference modification. Sounds pretty farfetched to me:-)

Outside chance it's something like:

WORKING-STORAGE SECTION.
01 FIELD-1 PIC X(22).
01 FIELD-2 PIC X(44).
01 WS-BINARY-FIELDS BINARY SYNC.
05 SUB-1 PIC S9(4).
05 SUB-2 PIC S9(4).
.
.
.
PROCEDURE DIVISION.

.
.
.
.
COPY something.
c MOVE LENGTH OF FIELD-1 TO SUB-1
c MOVE FIELD-1 (1:SUB-1) TO somewhere-else

I'm trying to come up with a situation like Lars' and this is the best I could do.

Doubting it's helpful, but hoping it's clearer,
Bill Lynch
```

#### ↳ Re: 'Advanced' Move statements

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-02-26T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f6253d8ebd-p9@usenetarchives.gap>`
- **In-Reply-To:** `<01bd42b5$82e0db50$ae881eac@nw105005>`
- **References:** `<01bd42b5$82e0db50$ae881eac@nw105005>`

```

All of a sudden, "$AppVar1$" <$AppVar2$@storebrand.no> wrote:

› Can anyone tell me if it is possible to move a field1 to a field2, when
› field2 is variable and I want to code only one move statement. In cobol II
…[3 more quoted lines elided]…
› Lars    

I'm not sure what you are trying to achieve. Can you give some more
detail? Maybe the field definitions, etc....

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
