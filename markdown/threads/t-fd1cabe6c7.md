[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ambiguous data name

_11 messages · 5 participants · 2006-07_

---

### ambiguous data name

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-07T15:28:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4h81vkF1pjtvvU1@individual.net>`

```
Something I've never run in to before...

WORKING-STORAGE SECTION.              
01  X                           PIC X.
01  Y.                                
    05  X                       PIC X.
PROCEDURE DIVISION.
    MOVE 'Y' TO X OF Y.  *> This works
    MOVE 'X' TO X.         *> This does not

Since the first X is a top-level elementary item there's no way (that I know
of) to further qualify it.  Is there any way around this (other than,
obviously, renaming one of the fields)?

Just wondering.

Frank



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: ambiguous data name

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-07-07T17:35:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<439c3$44aed502$d0665194$19243@FUSE.NET>`
- **In-Reply-To:** `<4h81vkF1pjtvvU1@individual.net>`
- **References:** `<4h81vkF1pjtvvU1@individual.net>`

```
Frank Swarbrick wrote:
> Something I've never run in to before...
> 
…[16 more quoted lines elided]…
> 
move x to another level.
01  X-main.
    03  X         pic x.

>     MOVE 'Y' TO X OF Y.  *> This works

and now >     MOVE 'X' TO X or x-main

> 
> --- 
> Frank Swarbrick
> Senior Developer/Analyst - Mainframe Applications
> FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: ambiguous data name

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-10T09:23:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hf9moF1r4rhhU2@individual.net>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <439c3$44aed502$d0665194$19243@FUSE.NET>`

```
Bob Iles<bobi@mikal.com> 07/07/06 3:35 PM >>>
>Frank Swarbrick wrote:
>> Something I've never run in to before...
…[9 more quoted lines elided]…
>> Since the first X is a top-level elementary item there's no way (that I
know
>> of) to further qualify it.  Is there any way around this (other than,
>> obviously, renaming one of the fields)?
…[12 more quoted lines elided]…
>and now >     MOVE 'X' TO X or x-main

Hmm, I should have mentioned "without moving X to another level"!

Honestly, I have no need to do this.  I was just curious if it is possible.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: ambiguous data name

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-07T19:06:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12attn61up0gj8b@news.supernews.com>`
- **References:** `<4h81vkF1pjtvvU1@individual.net>`

```
Frank Swarbrick wrote:
> Something I've never run in to before...
>
…[14 more quoted lines elided]…
> Frank


MOVE -1 TO Z.
MOVE 'X' TO X(Z:1) OF Y.      ???

Of course this is the equivalent of leaving a flaming paper bag of dog poop 
on the door-step of the maintenance programmer that comes after. But the 
original programmer did it to you...
```

##### ↳ ↳ Re: ambiguous data name

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-07-07T19:29:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jpGdna5KYN4dhTLZnZ2dnUVZ_sidnZ2d@adelphia.com>`
- **In-Reply-To:** `<12attn61up0gj8b@news.supernews.com>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com>`

```
HeyBub wrote:
> Frank Swarbrick wrote:
>   
…[28 more quoted lines elided]…
>   
If this program runs on an IBM mainframe, your solution won't work, 
because each 01-level item starts on a doubleword boundary.  Thus, the 
"01 X" is eight bytes from the "01 Y".  Your code would not change the 
contents of "01 X", but it probably wouldn't break the program, either.

Probably better to "solve" the data-name problem, rather than further 
mucking up the program.

Of course, I wonder what the compiler says about the MOVE statement, and 
I would guess that no one ever tried to reference the "01 X" before, so 
why does it need to be given a value now?
```

###### ↳ ↳ ↳ Re: ambiguous data name

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-08T10:36:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12avk7nlu6gjp3b@news.supernews.com>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com> <jpGdna5KYN4dhTLZnZ2dnUVZ_sidnZ2d@adelphia.com>`

```
Colin Campbell wrote:
> HeyBub wrote:
>> Frank Swarbrick wrote:
…[36 more quoted lines elided]…
> mucking up the program.

That would be solving the wrong problem, wouldn't it? Heck, this might be a 
question on a pre-employment test!

So, let's make the code, um, less parochial:

IF IBM-MACHINE
    MOVE -8 TO Z
ELSE
   MOVE -1 TO Z.
MOVE 'X' TO X(Z:1) OF Y.

There, now. Isn't that swell?
```

###### ↳ ↳ ↳ Re: ambiguous data name

_(reply depth: 4)_

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-07-08T14:25:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2L-dnSP7rZ5Fvy3ZnZ2dnUVZ_rSdnZ2d@adelphia.com>`
- **In-Reply-To:** `<12avk7nlu6gjp3b@news.supernews.com>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com> <jpGdna5KYN4dhTLZnZ2dnUVZ_sidnZ2d@adelphia.com> <12avk7nlu6gjp3b@news.supernews.com>`

```
HeyBub wrote:
> Colin Campbell wrote:
>   
…[57 more quoted lines elided]…
>   
I'm sure the employment offers will be flowing in!  Your solution is one 
any programmer could be proud of!  Swell is hardly a strong enough word 
to describe the solution.
```

###### ↳ ↳ ↳ Re: ambiguous data name

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-10T09:27:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hf9ufF1r4rhhU4@individual.net>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com> <jpGdna5KYN4dhTLZnZ2dnUVZ_sidnZ2d@adelphia.com>`

```
Colin Campbell<cmcampb@adelphia.net> 07/07/06 8:29 PM >>>
>HeyBub wrote:
>> Frank Swarbrick wrote:
…[20 more quoted lines elided]…
>> Of course this is the equivalent of leaving a flaming paper bag of dog
poop 
>> on the door-step of the maintenance programmer that comes after. But the

>> original programmer did it to you... 
>>
…[12 more quoted lines elided]…
>why does it need to be given a value now?

It appears I need to learn how to phrase my 'straw man' questions a bit more
obviously!  :-)

This is not real code or even anything like any real code I have seen.  It
was a "just wondering" question.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: ambiguous data name

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-10T16:29:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gfvsg.105271$LI3.48162@fe12.news.easynews.com>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com> <jpGdna5KYN4dhTLZnZ2dnUVZ_sidnZ2d@adelphia.com> <4hf9ufF1r4rhhU4@individual.net>`

```
The answer is that there is no "intended by the language" to do it.  (There are 
only tricks and code changes)
```

##### ↳ ↳ Re: ambiguous data name

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-10T09:24:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hf9pqF1r4rhhU3@individual.net>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com>`

```
HeyBub<heybubNOSPAM@gmail.com> 07/07/06 6:06 PM >>>
>Frank Swarbrick wrote:
>> Something I've never run in to before...
…[17 more quoted lines elided]…
>Of course this is the equivalent of leaving a flaming paper bag of dog poop

>on the door-step of the maintenance programmer that comes after. But the 
>original programmer did it to you... 

There is no "original programmer".  This is not real code, and I have never
run in to the problem in "real life".  It was simply something that occured
to me, so I wondered if there was any way to make the 01 level X
unambiguous.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: ambiguous data name

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-07-11T09:48:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35d06$44b3af3b$d0665194$25955@FUSE.NET>`
- **In-Reply-To:** `<4hf9pqF1r4rhhU3@individual.net>`
- **References:** `<4h81vkF1pjtvvU1@individual.net> <12attn61up0gj8b@news.supernews.com> <4hf9pqF1r4rhhU3@individual.net>`

```
Frank Swarbrick wrote:
> HeyBub<heybubNOSPAM@gmail.com> 07/07/06 6:06 PM >>>
>> Frank Swarbrick wrote:
…[27 more quoted lines elided]…
> Frank

So to recap Frank,

When I was first exposed to Cobol I though the move corresponding
feature Cobol was "neat", but unless you are reformatting a record
with the same fields, it has little value and that is the only
time I have ever found a need to have the same field names
defined, and in many cases would probably prefer the compile to
give me and error or warning (as it will on the level 01 items).
When developing new code, it's just much easier in my mind to
give unique names.

IMO of course.

Sincerely,
Bob.

> 
> 
…[3 more quoted lines elided]…
> FirstBank Data Corporation - Lakewood, CO  USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
