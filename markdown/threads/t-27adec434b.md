[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMMON Tables in host library

_9 messages · 4 participants · 1998-02_

---

### COMMON Tables in host library

- **From:** "paul deneyer" <ua-author-2633468@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bn79m$3ea$1@news3.Belgium.EU.net>`

```

I'm having a problem with the host-library I'm writing.
The library contains all the variables used in the bound modules,
declared as COMMON to avoid a hughe number of INITPBITS
each time the module is called.

The problem is this:
I need a few tables which are the same in definition, but contain
different values for each module. So: 1 table per module.
I've indexed those tables, each with the same index-name but this
seems to be illegal. I had thought the indexnames would only belong
to the table for which they're applied. This seems to be a wrong
assumption?
03 RECDEF OCCURS 7 INDEXED BY I-RECDEF.

I need those indexnames to be the same, so that the modules can
use a copyfile which contains a lot of functionality that is the same
for all modules.

So how do I go about this, keeping the name of the index the same
for each table?


Thanks a lot in advance!

Paul.
```

#### ↳ Re: COMMON Tables in host library

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6bn79m$3ea$1@news3.Belgium.EU.net>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net>`

```

In article <6bn79m$3ea$1.··.@new··U.net>,
Paul Deneyer wrote:
› I'm having a problem with the host-library I'm writing.
› The library contains all the variables used in the bound modules,
…[17 more quoted lines elided]…
› for each table?


Use a subscript, maybe?

DD
```

##### ↳ ↳ Re: COMMON Tables in host library

- **From:** "paul deneyer" <ua-author-2633468@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p2@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p2@usenetarchives.gap>`

```


doc··.@cl··k.net heeft geschreven in bericht
<6bn8an$5.··.@cla··k.net>...
› In article <6bn79m$3ea$1.··.@new··U.net>,
› Paul Deneyer  wrote:
…[22 more quoted lines elided]…
› Use a subscript, maybe?

If I declare a common variable in the host, will that do?
I mean, will I still be able to use SET-statements? I also used the index
for
speed reasons. So, is this usage index the best (read: most speedy) way
of replacing the indexed by clause?

Thanks again (for the dumb questions, new to libs and binding modules)

Paul
```

###### ↳ ↳ ↳ Re: COMMON Tables in host library

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p3@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p2@usenetarchives.gap> <gap-27adec434b-p3@usenetarchives.gap>`

```

In article <6bn925$54h$1.··.@new··U.net>,
Paul Deneyer wrote:
› 
› doc··.@cl··k.net heeft geschreven in bericht
…[27 more quoted lines elided]…
› If I declare a common variable in the host, will that do?

I am not quite sure what you mean by this; please post a bit of code to
indicate your understanding.

› I mean, will I still be able to use SET-statements?

An index is addressed by a SET; if you are replacing it with a subscript
then the answer is obvious.

› I also used the index for
› speed reasons. So, is this usage index the best (read: most speedy) way
› of replacing the indexed by clause?

That depends on the application and the size of your tables; what is your
anticipated transaction volume through these routines? Knowing this can
help phrase an answer more quickly; *no* single approach is best for all
problems at all times.

›
› Thanks again (for the dumb questions, new to libs and binding modules)

This has nothing to do with either of those, I believe.

DD

›
› Paul
›
›
```

###### ↳ ↳ ↳ Re: COMMON Tables in host library

_(reply depth: 4)_

- **From:** "paul deneyer" <ua-author-2633468@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p4@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p2@usenetarchives.gap> <gap-27adec434b-p3@usenetarchives.gap> <gap-27adec434b-p4@usenetarchives.gap>`

```

Someone told me to use a variable with USAGE IS INDEX.
So I'll go that way.

Thanks for your replies !


Paul
```

##### ↳ ↳ Re: COMMON Tables in host library

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1998-02-10T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p2@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p2@usenetarchives.gap>`

```

› Paul Deneyer  wrote:
› 
…[12 more quoted lines elided]…
› 
I like DD's suggestion of a subscript.
But here's another way which I don't recommend unless shop standards
won't let you use subscripts. I tested this and it worked (as I knew all
along, of course).

For a trick, as long as all the elements of the table are the same
length, you can any table's index for the other one. When 'anyindex' is
used to refer to a table of elements, it's interpreted 'dig down into
the table by this amount of bytes', no matter which table the index was
defined in.
Of course, if one table has different-sized elements than the other,
then the use of an 'alien' index will probably end up in the guts of an
element.
If there's a shop standard that you must use indexes (or the more snooty
'indices'), then this trick will work. Can't imagine that comments would
be needed for this, of course. :)

01 TABLE-1.
05 T-1 OCCURS 10 INDEXED BY I-1 PIC X.
01 TABLE-2.
05 T-2 OCCURS 10 INDEXED BY I-2 PIC X.

MOVE "1234567890" TO TABLE-1.
MOVE "ABCDEFGHIJ" TO TABLE-2.

SET I-1 TO 4.
DISPLAY T-2 (I-1). (DISPLAYS "D").

Here's some fun for 'A students' and old COBOL farts with nothing better
to do:

Define 01 TABLE-3 with 05 T-3 OCCURS 5 INDEXED BY I-3 PIC XX.
MOVE "ZYXWVUTSRQ" TO TABLE-3.
SET I-1 TO 4.
DISPLAY T-3 (I-1).
(You'll get two characters for the answer)

Then SET I-3 TO 4.
DISPLAY T-1 (I-3).
(You may be surprised by the answer - it's not '8'.)

Finally, there is a datatype that can be defined in Working-Storage as
'USAGE IS INDEX'. I have to admit that I've never used that datatype.
Perhaps one of those in each module could serve as an index for its
table and there would be no 'INDEXED BY' clause in the table
definitions.

John
```

###### ↳ ↳ ↳ Re: COMMON Tables in host library

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1998-02-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p6@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p2@usenetarchives.gap> <gap-27adec434b-p6@usenetarchives.gap>`

```

John L. Mindock wrote:
›
›
› For a trick, as long as all the elements of the table are the same
› length,
I meant to say 'as long as all the elements of EACH table are the same
length'.

John
```

#### ↳ Re: COMMON Tables in host library

- **From:** "bill graham" <ua-author-105207@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p8@usenetarchives.gap>`
- **In-Reply-To:** `<6bn79m$3ea$1@news3.Belgium.EU.net>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net>`

```

Paul Deneyer wrote:
< snip>
› The problem is this:
› I need a few tables which are the same in definition, but contain
…[9 more quoted lines elided]…
› for all modules.

Paul,
Would a COPY ... REPLACING work for you? It would allow you to use
different index names.
Something like:
COPY REPLACING I-RECDEF BY I-RECDEF-NEW.
You would have a different "I-RECDEF-NEW" in each module.
Bill
```

##### ↳ ↳ Re: COMMON Tables in host library

- **From:** "paul deneyer" <ua-author-2633468@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27adec434b-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27adec434b-p8@usenetarchives.gap>`
- **References:** `<6bn79m$3ea$1@news3.Belgium.EU.net> <gap-27adec434b-p8@usenetarchives.gap>`

```


Bill Graham heeft geschreven in bericht
<34E··.@hob··c.edu>...

› Paul,
›   Would a COPY ... REPLACING work for you? It would allow you to use
…[4 more quoted lines elided]…
› Bill

The whole library is based on the index having the same name for each
table. The library is used to validate/convert file-layouts.
Each table contains the structural info for a certain layout.
Making the indexnames the same allowed me to write a big part of the
validation modules as 'write once, use for all'.

It's only in the host I'm having those problems. There each table
is copied into the working-storage, so that at runtime, all variables
will be allocated in the memoryspace of the host (is COMMON). That saves a
lot
of runtime-overhead for allocation an deallocation (INITPBITS on
the Unisys A-Series).

So, following your suggestion, I would run into the problem of not
having one single name anymore for all validation-modules.

As someone pointed out to me, but I'm not sure if it'll do what I
need it to do, is create a :
01 WS-IRECDEF PIC 9(02) USAGE INDEX.
That would allow me to use index-statements like they are now present
in the source. Including this declaration in each module as common
declaration
should do the trick I think. Or am I overlooking something?


Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
