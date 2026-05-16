[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Where is the holy grail...(Part 1)

_15 messages · 10 participants · 2003-09_

---

### Where is the holy grail...(Part 1)

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2003-09-16T07:41:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```
Hello everyone,

can you please read this article on the listed below link and post
what do you really think about this topic? Regards, Kellie.

http://www.embedded.com/story/OEG20011214S0098
```

#### ↳ Re: Where is the holy grail...(Part 1)

- **From:** docdwarf@panix.com
- **Date:** 2003-09-16T11:34:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bk7ail$f08$1@panix5.panix.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```
In article <41758a6b.0309160641.2f053885@posting.google.com>,
KELLIE FITTON <KELLIEFITTON@YAHOO.COM> wrote:
>Hello everyone,
>
…[3 more quoted lines elided]…
>http://www.embedded.com/story/OEG20011214S0098

Nothing new there... reuse requires a kind of familiarity with 
that-which-is-available I've not seen in many shops.  Simple case: years 
on back the client I was consulting with decided that error messages 
should be coded in a central file and referred to by numbers; instead of 
coding a dupe-key message in the program you were supposed to move 99999 
(some number) to the file-key, read and use the text you got.

Centralising and standardising the entries was boring, unglamorous work, 
though... and the mechanism was dropped after a month, when folks realised 
that there were seven different entries for this one condition alone.

DD
```

#### ↳ Re: Where is the holy grail...(Part 1)

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-16T18:28:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmf74frekq6cf7@corp.supernews.com>`
- **In-Reply-To:** `<41758a6b.0309160641.2f053885@posting.google.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```
KELLIE FITTON wrote:

> Hello everyone,
> 
…[3 more quoted lines elided]…
> http://www.embedded.com/story/OEG20011214S0098

This is true.  Reuse dovetails with component-based design quite nicely, 
but I agree that there are growing pains.  And, once a repository grows 
to a certain size, it becomes a full-time job to manage the repository. 
  However, like the guy said, it's dividends are not reaped in the short 
term, but in the long - without some vision for the future, reuse is 
just something you read about, not something you ever see happen.
```

##### ↳ ↳ Re: Where is the holy grail...(Part 1)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-18T02:21:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030917222157.22784.00000911@mb-m23.aol.com>`
- **References:** `<vmf74frekq6cf7@corp.supernews.com>`

```

The ever redoubtable puppet-not, KELLIE FITTON, encourages us to visit

 http://www.embedded.com/story/OEG20011214S0098

and to let everyone know
 > what do you really think about this topic? 

I enjoyed the comments there by Jack G. Ganssle concerning re-use of code in
embedded systems.

I, for one, would like to take issue with a portion of what that good author
said; 

<<
Sure, we all know the long-term outweighs today's concerns, but I'll 
betcha most bosses won't agree. They'll usually buy into the idea of the 
benefits of reuse, without being willing to stand the pain of creating 
the reuseable components
>>

I have snipped here, so visit the site to get his exact view. 

In big time business data processing this is not always true.  I have seen
major commitments to re-usability. Allowance for more time in design, and more
time in detailed development to get systems better abstracted. Experienced
managers know that they will face the future with typically smaller staffs then
the group present at development time. Experienced managers know that they
_need_ the design to be generalized.

Re-use is one of the religions of DP, as is structured code, and now
increasingly object orientation. Re-use is practiced faith, not just lip
service; and a lot is spent on it in big business. It pays off, too.  I have
definitely seen maintenance and enhancement efforts that reuse major functions
that would have been cost prohibitive to re-invent.  

Re-use lives, and it not only saves money it makes some enhancement projects
possible that would not otherwise be possible.

I admire the author's point of view. Jack G. Ganssle works in an area that
makes some of us green with envy, Embedded Systems.  A challenging area that is
inherently interesting because of the proximity to the hardware, and always
challenging because the underlying technology from that perspective never
ceases to change.

If re-use is religion, then changing specs are the devil herself. No one can
anticipate the future, and experienced business managers will moderate the
support for abstraction and blue sky design with an admonition that we can
never really know what we will need in the future until  we actually get the
future spec.  But practical business folks do understand that abstraction does
save money.

It is especially important to note that abstraction not only improves our
chances of creating code that will atleast be partially re-usable in the
future, but abstraction improves the fit of the initial code to actual current
business requirements in the initial deployment of a system.

There are related cultural features in modern business data processing that
reflect this 'faith' in abstraction.  There has been a dominant theme to
parameterize business systems, to control them externally with tables, for
several decades.  This is like a denomination in the holy church of modern data
processing.

In effect we re-use executable code by modifying the table entries that control
the code.
This stuff is ubiquitous.  Re-use is alive and well in modern business data
processing.

There is some chance that we succeed more with re-use in business apps because
we make the whole system huge, and it succeeds less in embedded system because
the theme is to make it small.  But another issue must be that managers in
technology (particularly hardware technology) projects have a different set of
concerns than do managers in the less glamorous business contexts.

From the get-go we might even conceive of the embedded system as one that will
be pitched not too long from now; even if we succeed. Whereas, in some business
shops code accumulates always, ... like it never gets pitched.

Embedded systems deal with product market placed that are fleeting (largely).
Common business apps deal with requirements that mostly remain the same,
growing slowly, dropping few features as they go.

So, back to COBOL. Practical applications need re-use to even come close to
acceptable cost containment. It is common practice, not just faith. In some
folks' view OOP tools further automate the generation of code from an
abstracted perspective. 

The initial thrust has been and remains to make basic COBOL interoperable with
the succeeding product OOP code actually installed from shop internal
development or as off the shelf applications.

Later, if any institutions start to mass produce coders educated in COBOL OOP
syntax, that stuff could be used too. (this later seems unlikely, IMHO).



Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Where is the holy grail...(Part 1)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-09-16T23:13:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8E1329.23131116092003@corp.supernews.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```
In article <41758a6b.0309160641.2f053885@posting.google.com>,
 KELLIEFITTON@YAHOO.COM (KELLIE FITTON) wrote:

> Hello everyone,
> 
…[3 more quoted lines elided]…
> http://www.embedded.com/story/OEG20011214S0098

I think reuse is a failure in the authors mind because the author is too 
lazy to design and write for reuse.

It only seems like a pain.  

Once you get the hang of it, and you start really writing your code with 
an eye for reuse, you build up a critical mass that makes your future 
development much quicker.
```

##### ↳ ↳ Critical mass...

- **From:** Colin Campbell <cmcampb@attgloabl.net>
- **Date:** 2003-09-17T11:25:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F68A703.F1DF4C51@attgloabl.net>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <joe_zitzelberger-8E1329.23131116092003@corp.supernews.com>`

```
If your statement is true, why isn't there some software maker that is
beating the socks off everyone else?  You individually may be having success
with code reuse, but are there any large organizations which are doing as
well?

I worked with a brilliant COBOL compiler guy some years ago.  He had
designed a COBOL compiler that ran on a "pseudo machine".  For us to
implement COBOL for customer X, we had to implement only the "pseudo
machine" on top of their actual machine.  I believe approximately 70% of our
code was reusable.  We did pretty well for awhile....


Joe Zitzelberger wrote:

> In article <41758a6b.0309160641.2f053885@posting.google.com>,
>  KELLIEFITTON@YAHOO.COM (KELLIE FITTON) wrote:
…[15 more quoted lines elided]…
> development much quicker.
```

#### ↳ Re: Where is the holy grail...(Part 1)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-18T04:08:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pcaab.1823$Od.117942@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309160641.2f053885@posting.google.com...
> Hello everyone,
>
…[4 more quoted lines elided]…
>

http://www.reusability.com/papers5.html

One of the pitfalls of reuse is the term "generic" and the linear approach
to problems that people often take.

Take the following iterative requirements.

Person A: I need a way to send a message to B.
Person B: I need a way to send a message to A, I want a receipt.
Person C: I need a way to send a message to B, I want a receipt, and it to
take less than 5 seconds.
Person D: I need a way to send a message to A, I want a dated receipt, and
it to take less than 5 seconds.
Person E: I need a way to send a message to A, I want a dated receipt,
signed.
Person F: I need a way to send an encrypted message to A.
Person G: I need a way to send a message to A and B and C.
Person H: I need a way to send a message to A and B and C and D privately.

Typically what you would see:
A)You would create a components to send a message.
B)You update the component to get a receipt
C)You update the component to work in real time.
D)You update the component to work in real time and create the dated.
E) You include the notion of a signature.
F) You update the component to encrypt the message.

Now you have reuse in terms of one component being usable by multiple
people.  You have created an overly complex interface to make a single
"generic" reusable component.

Now....what you should see is something that is reuse at a much lower
level - I'm picking one or two just because I'm lazy.

For A)You would create a components to send a message.
..
For F) You would create a component that performs encryption.

You could then combine (reuse) component (A) with (F) to create an encrypted
message sender.

For G) You would create a component that makes multiple calls to the basic
send component.

You could then combine (reuse) components (A) with (G) to create an
broadcast sender.

You could then combine (reuse) components (A) (G) (F) to create an encrypted
broadcast sender.

Now you have reuse at a much improved level; however, the price here is
repository management.

There are some that argue that a component not change; however, I personally
believe that is a little ambitious and that on occasion changes are
necessary and profitable.  At this point it becomes a question of how well
you defined your interfaces to allow you to change the internals without
affecting the already existing user base - adding new input parameters that
default to "no new" action....for example adding a
"sendReceiptTo(myaddress)" should be ok if the default action is not to send
a receipt.

The difficulty is in the identification of the problem domain.....it changes
constantly.    You need to manage reuse with adaptability and not get stuck
either way.

My personal belief is that the mistake is made when people design for the
specifics of the future instead of designing for the specifics of the
present.  In other words (and this is confusing)- pretend like you have a
base and you have to add the present functionality to it...in this way you
will approach your design with the thought for future adaptation (a good
movie btw)

JCE
```

##### ↳ ↳ Re: Where is the holy grail...(Part 1)

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-18T02:03:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmim5pp2h80ea1@corp.supernews.com>`
- **In-Reply-To:** `<Pcaab.1823$Od.117942@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <Pcaab.1823$Od.117942@twister.tampabay.rr.com>`

```
jce wrote:

> Take the following iterative requirements.
> 
…[41 more quoted lines elided]…
> broadcast sender.

Well said...  Just thought it bore repeating.  :)
```

#### ↳ Re: Where is the holy grail...(Part 1)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-18T04:24:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qsaab.1838$Od.105431@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com>`

```

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0309160641.2f053885@posting.google.com...
> Hello everyone,
>
…[4 more quoted lines elided]…
>
" What is the air speed velocity of an unladen swallow "


JCE (Eagerly awaiting Part II)
```

##### ↳ ↳ Re: Where is the holy grail...(Part 1)

- **From:** Gus <GusPod@XXX.optonline.net>
- **Date:** 2003-09-18T09:01:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<qsaab.1838$Od.105431@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com>`

```
jce wrote:

> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> news:41758a6b.0309160641.2f053885@posting.google.com...
…[9 more quoted lines elided]…
> " What is the air speed velocity of an unladen swallow "

What do you mean - an African swallow or a European swallow?
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part 1)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-09-18T09:06:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com> <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net>`

```
In article <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net>,
 Gus <GusPod@XXX.optonline.net> wrote:

> jce wrote:
> 
…[14 more quoted lines elided]…
> 

Aren't you answering a question with a question...

;-)
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part 1)

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-18T10:50:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkcgmu$e82$1@panix1.panix.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com> <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net> <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com>`

```
In article <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net>,
> Gus <GusPod@XXX.optonline.net> wrote:
…[19 more quoted lines elided]…
>Aren't you answering a question with a question...

Despite the substitution of an ellipsis for a question mark the above 
seems to be the third question in a series.

DD
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part 1)

_(reply depth: 5)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-09-18T18:38:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0309181738.c5eed4e@posting.google.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com> <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net> <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com> <bkcgmu$e82$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<bkcgmu$e82$1@panix1.panix.com>...
> In article <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[26 more quoted lines elided]…
> DD

To continue in this artery, is the swallow migrating from Africa to
Europe or vice-versa? (oops - a real question mark)
```

###### ↳ ↳ ↳ Re: Where is the holy grail...(Part 1)

_(reply depth: 6)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-19T03:22:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QDuab.8672$Od.306617@twister.tampabay.rr.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com> <bweab.29673$BS1.11118495@news4.srv.hcvlny.cv.net> <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com> <bkcgmu$e82$1@panix1.panix.com> <fcd09c56.0309181738.c5eed4e@posting.google.com>`

```

"Robert Jones" <robert@jones0086.freeserve.co.uk> wrote in message
news:fcd09c56.0309181738.c5eed4e@posting.google.com...
> docdwarf@panix.com wrote in message
news:<bkcgmu$e82$1@panix1.panix.com>...
> > In article <joe_zitzelberger-6D5D51.09064718092003@corp.supernews.com>,
> > Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[30 more quoted lines elided]…
>
...African swallows are non-migratory.

JCE
```

##### ↳ ↳ Re: Where is the holy grail...(Part 1)

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-21T17:38:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f6d3a88_3@news.athenanews.com>`
- **References:** `<41758a6b.0309160641.2f053885@posting.google.com> <qsaab.1838$Od.105431@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:qsaab.1838$Od.105431@twister.tampabay.rr.com...
>
> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
…[9 more quoted lines elided]…
>

African or European...?

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
