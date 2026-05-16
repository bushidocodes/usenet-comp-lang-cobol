[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Demo: OO Cobol

_5 messages · 2 participants · 2004-06_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Demo: OO Cobol

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-12T17:46:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40cb3f8b.70591138@news.optonline.net>`

```
* [Continued from forest.cbl]

* This demo of object oriented Cobol continues the theme of sorts and
* trees. It inserts 50,000 random strings into a structure then does
* 50,000 lookups.
*
* One of the main attractions of OO is reusable Components. So rather
* than writing the code myself, as in previous demos, I chose to use two
* off-the-shelf Collection Classes provided by Micro Focus. One is
* called Sorted Collection and the other Dictionary. Both appear to use
* hashing to file and locate entries. Sorted Collection has a method to
* insert an entire Collection with a single operation; Dictionary does
* not. Compared to inserting entries individually, not shown here,
* inserting a Collection is substantially faster. The test data
* resides in an Ordered Collection, where the order is chronological.
* In other words, random order.
*
* Timer is now an OO Class with two methods: start and stop. Note
* how this small Class is 'nested' within a single source file.
*
* Bottom line: the Components were 42 and 59 times slower than the best
* non-OO single-threaded solution, and more then 20 times slower than
* the worst. They were 125 and 175 times slower than the multi-threading
* demo.

* ---------------------------------------------------------------------
* compile: cob -xg oodemo.cbl

      $set mfoo ooctrl(+n)
      $set sourceformat(free)
      $SET NOBOUND OPT(2) NOTRUNC IBMCOMP
      $SET NOCHECK NOPARAMCOUNTCHECK FASTCALL NOREENTRANT
      $SET NOSERIAL NOFIXOPT FASTLINK

   program-id. oodemo.
   author. Robert Wagner.
*                       Object Oriented demo.

* results: Sun SPARC, 1.8 GHz, 4 CPU, time for 10 runs of 50,000 entries.
*
*   Object Oriented                                     ratio to best
*  15. Sorted Collection      106.0                       59.0
*  16. Dictionary                  75.0                       42.0
*
* -- Results from previous demos ----
*                                     --- ratio ---
*  Sort only                                  2.   3.    4.    5.
*  1. Micro Focus file sort     3.7   1.0  1.5  7.4  9.3
*  2. Micro Focus table sort   3.8         1.5  7.6  9.5
*  3. qsort()                         2.5                5.0  6.3
* 9-7 tree, to list                  1.5                      3.8
*  4. radix-insertion, to table   .5                      1.3
*  5. radix-insertion (list)         .4                    best
*
*  Misc
*  6. build tree time              1.4
*  7. search all time              1.3                     ratio to best
*                                                                      4+7
*  Sort followed by search all or tree lookup
* 2+7 MF table sort, search     5.1                        2.8
* 3+7 qsort()                          3.8                        2.1
*  8. tree, to table, search       3.5                        1.9
*  9. tree, to table faster         2.9                        1.6
* 10. tree, lookup (unbalanced) 2.6                       1.4
* 11. tree, balance, lookup      2.6                        1.4
* 4+7 radix-insertion, table      1.8                        best
*
*  Multithreaded tree build and lookup (similar to 10.) ratio to 4+7
* 12. single-threaded               1.7                          .9
* 13. multithreaded with mutex  5.9                        3.3
* 14. self-synchronized              .6                          .3

   class-control.
       OrderedCollection is class "ordrdcll"
       SortedCollection is class "srtdclln"
       Dictionary is class "dictinry"
       Association is class "associtn"
       CharacterArray is class "chararry"
       Timer is class 'timer'
 . data division
 . working-storage section

* Random string (key) inserted into collections
 . 01  data-area
 .     05  data-key
 .         10  data-key-1                  pic v9(18)
 .         10  data-key-2                  pic v9(12)

 . 01  unqualified-variables.
 .     05  n                        comp    pic s9(09)
 .     05  n-limit                  comp    pic s9(09)
 .     05  c                        comp    pic s9(09)
 .     05  test-id                  comp    pic s9(02)
 .     05  repeat-factor         comp    pic s9(02)
 .     05  a-OrderedCollection              object reference.
 .     05  a-SortedCollection                object reference.
 .     05  a-Dictionary                         object reference.
 .     05  a-null                                  object reference.
 .     05  a-String                               object reference.
 .     05  a-Consequent                       object reference.
 .     05  a-Pair                                  object reference.
 .     05  a-CharacterArray                  object reference.

 . 01  Timer-variables
 .     05  a-Timer                              object reference
 .     05  elapsed-time             comp     pic s9(09)
 .     05  elapsed-time-edited               pic  zzzz.9

 . procedure division.
   perform construct-data

   display '15. Sorted Collection' with no advancing
   move 15 to test-id
   perform Timer-on
   perform repeat-factor times
       perform construct-Collection
       perform lookup-entries
       perform destroy-Collection
   end-perform
   perform Timer-off

   display '16. Dictionary' with no advancing
   move 16 to test-id
   perform Timer-on
   perform repeat-factor times
       perform construct-Collection
       perform lookup-entries
       perform destroy-Collection
   end-perform
   perform Timer-off

   perform destory-data
   goback

 . construct-Collection.
     evaluate test-id
         when 15
            invoke SortedCollection "ofReferences"
                using n-limit
                returning a-SortedCollection
            invoke a-SortedCollection "addall"
                using a-OrderedCollection
         when 16
* A Dictionary contains Associations, an object with
* two parts: antecedent (key) and consequent (result). In this
* test, both are the same object -- a String containing a
* random number. Sub-classing Association with nulls tells
* it both parts will be objects rather than intrinsics.
            invoke Association "newClass"
                using a-null a-null
                returning a-Pair
            invoke Dictionary "ofAssociations"
                using a-Pair n-limit
                returning a-Dictionary
            perform varying n from 1 by 1 until n > n-limit
                invoke a-OrderedCollection "at"
                    using n
                    returning a-string
                invoke a-Dictionary "atPut"
                    using a-string a-string
            end-perform
     end-evaluate

 . lookup-entries.
     perform varying n from 1 by 1 until n greater than n-limit
         invoke a-OrderedCollection "at"
             using n
             returning a-String
         evaluate test-id
             when 15
                 invoke a-SortedCollection "occurrencesOf"
                     using a-String
                     returning c
                 if  c not equal to 1
                     display 'Not found ' with no advancing
                     invoke a-String "display"
                     call 'abort'
                 end-if
             when 16
                 invoke a-Dictionary "at"
                     using a-String
                     returning a-Consequent
                 if  a-Consequent not equal to a-String
                     display 'Not found ' with no advancing
                     invoke a-String "display"
                     call 'abort'
                 end-if
         end-evaluate
     end-perform

 . destroy-Collection.
     evaluate test-id
         when 15
            invoke a-SortedCollection "finalize"
                returning a-SortedCollection
         when 16
            invoke a-Dictionary "finalize"
                returning a-Dictionary
     end-evaluate

 . construct-data.
     move low-values to unqualified-variables
     move 2  to repeat-factor
     move 50000 to n-limit
     invoke OrderedCollection "ofReferences"
         using n-limit
         returning a-OrderedCollection
* Construct 50,000 String objects and put references to
* them into an (un)Ordered Collection.
     perform n-limit times
         compute data-key-1 = function random
         compute data-key-2 = function random
         invoke CharacterArray "withLengthValue"
             using length of data-key data-key
             returning a-String
         invoke a-OrderedCollection "add"
             using a-String
     end-perform
     invoke Timer 'new' returning a-Timer
 . destroy-data.
* This destroys the Collection object but not the 50,000 Strings
     invoke a-OrderedCollection "finalize"
         returning a-OrderedCollection

 . Timer-on.
     invoke a-Timer 'start'
 . Timer-off.
     invoke a-Timer 'stop' returning elapsed-time
     compute elapsed-time-edited rounded =
        (elapsed-time * (10 / repeat-factor) / 100)
     display elapsed-time-edited

 . end program oodemo

 . Class-id. timer inherits from base

 . object section
 . class-control.
       base is class 'base'
       Timer is class 'timer'

*   the following are class methods and data
 . factory
 . end factory

*   the following are instance methods and data
 . object
 . working-storage section
 . 01   value 0       comp-x   pic x.
 .  88 running value 1 false 0
 . 01  start-time     comp     pic s9(09)

 . method-id. 'start'
 . local-storage section
 . 01 temp-time                pic  x(08)

 . procedure division.
     if not running
         accept temp-time from time
         invoke self 'time-to-integer'
             using temp-time returning start-time
         set running to true
     end-if
     exit method
 . end method 'start'

 . method-id. 'stop'
 . local-storage section
 . 01 temp-time                   pic  x(08)
 . 01 end-time        comp     pic s9(09)
 . linkage section
 . 01  elapsed-time   comp     pic s9(09)

 . procedure division returning elapsed-time.
     if running
         accept temp-time from time
         invoke self 'time-to-integer'
             using temp-time returning end-time
         compute elapsed-time rounded = end-time - start-time
         set running to false
     end-if
     exit method
 . end method 'stop'

 . method-id. 'time-to-integer'
 . linkage section
 . 01 input-time
 .    05 hours                    pic 99
 .    05 minutes                 pic 99
 .    05 seconds                pic 99
 .    05 hundredths            pic 99
 . 01 output-time   comp    pic s9(9)

 . procedure division using input-time returning output-time.
     compute output-time =
        ((((((hours * 60) +
           minutes) * 60) +
           seconds) * 100) +
           hundredths)
     exit method
 . end method 'time-to-integer'

 . end object
 . end class timer
 .
```

#### ↳ Re: Demo: OO Cobol

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-13T08:32:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406130732.6b919fe6@posting.google.com>`
- **References:** `<40cb3f8b.70591138@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote in message news:<40cb3f8b.70591138@news.optonline.net>...
> * [Continued from forest.cbl]
> 
<snip>> *
> * Bottom line: the Components were 42 and 59 times slower than the best
> * non-OO single-threaded solution, and more then 20 times slower than
> * the worst. They were 125 and 175 times slower than the multi-threading
> * demo.
> 

There are significant differences between components and OO Classes.

(And no, Robert, I am done debating them here...<G>)

For correctness, you should replace "Components" in the above with:

"...MicroFocus Collection Classes, as implemented in the code
below...".

I leave the MicroFocus people to make their own comments...

I confess to not having seen the previous non-OO code so I don't
really know how fair your benchmark is. However, I would note that
there are times when collections are very useful, and there are times
when they are not so. Certainly, on the occasions when I have used
them, performance has not been a prime consideration. There are other
benefits.

All I can take away from your post is: "If I ever need to load 50,000
random numbers into some place where I can search them, it might be
better not to use MicroFocus OO Collection Classes..."

Hardly a "Revelation" for anyone familiar with the SEARCH verb in
COBOL <G>.

I'm not sure what your purpose is here, but contrived examples seldom
prove anything. If you want to examine the usefulness of OO
Collections why not try a TreeView application or recursive XML
parser?

If your object is to show that OO is not a good programming paradigm,
you are far too late; the World has voted with its feet. (Having said
that, I agree it is possible to make a case against OO programming for
certain applications (Batch Processing, for example)); but I use it as
a springboard to components and am not an OO Evangelist as such. I DO
believe in components, and that is why I'm making this post. (Your
denigration of components in the Bottom Line above reflects your own
lack of understanding, but it may cause others to believe you...).

I could easily make posts here and show code that uses components
(some written by me, some not) that achieves things you would have the
greatest difficulty in doing in COBOL, (OO, multi-threaded, recursive,
re-entrant, or otherwise), (try sending e-mail without calling an
external package or component or using an API, which amounts to the
same thing...), but what is the point?

Minds here will not be changed and, for the most part, there is more
resistance to change amongst programmers than there is in the Senior
Membership of a London Club.

Bottom Line: If you don't like the performance of OO Collections,
don't use 'em. You will miss out on a lot, but not when you're storing
50,000 random numbers...

Pete.




> * ---------------------------------------------------------------------
> * compile: cob -xg oodemo.cbl
…[277 more quoted lines elided]…
>  .
```

##### ↳ ↳ Re: Demo: OO Cobol

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-14T00:11:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40cceb33.180087506@news.optonline.net>`
- **References:** `<40cb3f8b.70591138@news.optonline.net> <b3638c46.0406130732.6b919fe6@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote in message
news:<40cb3f8b.70591138@news.optonline.net>...

>All I can take away from your post is: "If I ever need to load 50,000
>random numbers into some place where I can search them, it might be
…[3 more quoted lines elided]…
>COBOL <G>.

I didn't tell the classes how to manage collections. If the SEARCH verb is such
an obvious choice, why didn't they use it?

>I'm not sure what your purpose is here, but contrived examples seldom
>prove anything. If you want to examine the usefulness of OO
>Collections why not try a TreeView application or recursive XML
>parser?

The only reason was continuing the theme of previous demos, which provide a
basis for comparison. 

>If your object is to show that OO is not a good programming paradigm,
>you are far too late; the World has voted with its feet.

Absolutely not. I support OO principles, but am skeptical about implementations.
As is usually the case, the devil is in the details.

I seriously considered writing my own Classes using techniques from previous
demos .. even multithreaded OO. Timing results would have been predictable --
the old time plus speed of an INVOKation, which I had already measured.

That approach would fly in the face of the 'OO philosophy', which says 'don't
waste time doing it yourself; use an off-the-shelf component.' So I did what a
innocent would -- I used classes that came free with the compiler. The result is
a 'finger in the wind' assessment of the outcome from following that philosophy.
It showed that OO is not the panacea that innocents had been promised. 

Hardly a Revelation to anyone who'd fallen for earlier panaceas. 

>(Having said
>that, I agree it is possible to make a case against OO programming for
…[4 more quoted lines elided]…
>lack of understanding, but it may cause others to believe you...).

I wrote the demo for two reasons:
1. To illustrate the flavor of OO Cobol .. for those contemplating a change.
2. To assess the quality of 'typical' class libraries, and thereby alert
innocents to the dangers of panaceas.  

I didn't denegrate components in the Bottom Line; I reported facts. In the words
of our president Truman "People say I give 'em hell. I don't give 'em hell, I
report the truth and they think it's hell."

>Bottom Line: If you don't like the performance of OO Collections,
>don't use 'em. You will miss out on a lot, but not when you're storing
>50,000 random numbers...

I say think about the dynamics that produced poor-quality solutions and do
something to improve the quality.Defenders of low-quality software feel
threatened and react predictably.
```

###### ↳ ↳ ↳ Re: Demo: OO Cobol

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-15T09:34:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406150834.29c22f91@posting.google.com>`
- **References:** `<40cb3f8b.70591138@news.optonline.net> <b3638c46.0406130732.6b919fe6@posting.google.com> <40cceb33.180087506@news.optonline.net>`

```
Robert,

my only beef with your post is that you used the word "component"
where you should have used "Collection Classes as implemented by
MicroFocus".

A Collection Class is not a component (Neither is any other Class).

Until you understand the difference, it is simply wrong to attribute
the (good or) bad performance of OO Classes to "components".

It's a bit like saying that joining two pieces of wood with screws is
an awful way to do it, when you actually used glue. Such a comment is
bound to upset the people who use screws to join wood every day.
However, if you say it authoritatively enough, a certain percentage of
people who have never joined wood with screws OR glue will believe
you. That is what my objection is and that is why I posted.

(People considering component based design may get a completely wrong
impression.)

I have little more to add. (It's all covered in my previous post which
you selectively edited.)

<snipped all but the nub of the conversation>

> 
> I didn't denegrate components in the Bottom Line; I reported facts. In the words
> of our president Truman "People say I give 'em hell. I don't give 'em hell, I
> report the truth and they think it's hell."
> 

Well, it's a nice quote, however, Harry Truman wasn't MY President so
he wasn't OUR president, and your "Truth" is only Hellish in its
inaccuracy (hence the quotes on "Truth").

Your "reported facts" (and I have neither time nor inclination to
argue how "factual" they are; that's not the issue...) were ascribed
to "Components", when, in fact, you were not talking about components,
you were talking about Collection Classes as implemented by
MicroFocus.

As your conclusion was denigratory, you DID denigrate components.

It is simply a matter of record. 


> >Bottom Line: If you don't like the performance of OO Collections,
> >don't use 'em. You will miss out on a lot, but not when you're storing
…[4 more quoted lines elided]…
> threatened and react predictably.

I am not now, have never been, and am not likely in the future to be
defending low-quality software. MicroFocus have a very good reputation
and, although I don't personally use their products, I know many
satisfied customers who do.

There IS a place for Collection Classes; it just isn't the place you
chose. (think about the screws and the glue again... <G>)

I don't feel threatened. (I don't feel threatened by anything anybody
says here, (except maybe when JerryMouse reckons he can get a contract
on someone for a case of beer...<G> Notice I'm always nice to
JerryMouse? "Hi Jerry...")) Why would I?

I'd simply like you to get it right...

Predictably, I won't be responding further to this thread.

(So you got that bit right <G>)

Pete.

PS This is NOT personal. I read your posts with interest (and
Richard's responses to them, with equal interest) whenever I have
time.
```

###### ↳ ↳ ↳ Re: Demo: OO Cobol

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-06-17T01:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40d0ed81.34689330@news.optonline.net>`
- **References:** `<40cb3f8b.70591138@news.optonline.net> <b3638c46.0406130732.6b919fe6@posting.google.com> <40cceb33.180087506@news.optonline.net> <b3638c46.0406150834.29c22f91@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

>Robert,
>
…[4 more quoted lines elided]…
>A Collection Class is not a component (Neither is any other Class).

I thought they were synonymous.

>Until you understand the difference, it is simply wrong to attribute
>the (good or) bad performance of OO Classes to "components".
…[6 more quoted lines elided]…
>you. That is what my objection is and that is why I posted.

In that case, you should explain the difference.

>> I didn't denegrate components in the Bottom Line; I reported facts. In the
words
>> of our president Truman "People say I give 'em hell. I don't give 'em hell, I
>> report the truth and they think it's hell."
…[4 more quoted lines elided]…
>inaccuracy (hence the quotes on "Truth").

Very good in re OUR. 

>> >Bottom Line: If you don't like the performance of OO Collections,
>> >don't use 'em. You will miss out on a lot, but not when you're storing
…[9 more quoted lines elided]…
>satisfied customers who do.

I agree, generally. But their Class Library sucks.

I could have written it work well, but doing it myself would have violated the
spirit of OO, which says use off-the-shelf components. 

>I'd simply like you to get it right...

I did get it right.

>Predictably, I won't be responding further to this thread.

Of course not. Where's the challenge in that? If people responded to a dialog,
we could counter their errors. If they ducked below the radar, our responses
would fall into the void.

>PS This is NOT personal. I read your posts with interest (and
>Richard's responses to them, with equal interest) whenever I have
>time.

We all have the same time -- 24 hours in a day. The issue is not availability of
time, it is priorities.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
