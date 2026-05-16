[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Value of 'old' COBOL source ... does anybody know?

_12 messages · 9 participants · 2003-02_

---

### Value of 'old' COBOL source ... does anybody know?

- **From:** "BPR2" <news1@augursw.com>
- **Date:** 2003-02-16T14:24:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
Years ago, we used to assess the value of COBOL source code for production
systems at approximately $20 (US) per LOC.  This figure was arrived at by
dividing the Lines of Code for production systems by the cost of the
Programmer time required to create and maintain those applications for a
period of 5 years.

Now, with much of this COBOL becoming more static and most new development
focused on 'integrating' new applications with the 'old data' still owned
and effectively managed by the COBOL applications this 'evaluation method'
doesn't seem to be appropriate anymore.

Are there other 'evaluation methods' in use now by IT organizations that
seem more appropriate for today's situation?

The question I'm trying to answer is:

If all my source code (and specs, documentation, etc) were destroyed, and I
need to make an insurance claim for it's replacement value ... how would I
calculate the value of the loss?

All ideas are welcome, particularily those from people that have had to
assess the value of source code in the past few years.

Thanks!
```

#### ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** docdwarf@panix.com
- **Date:** 2003-02-16T11:54:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2ofod$hkk$1@panix1.panix.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
In article <eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>,
BPR2 <news1@augursw.com> wrote:

[snip]

>The question I'm trying to answer is:
>
>If all my source code (and specs, documentation, etc) were destroyed, and I
>need to make an insurance claim for it's replacement value ... how would I
>calculate the value of the loss?

What a fascinating situation... talk about Intellectual Property value!  
For an off-the-cuff answer in this brave, new world I'd say that you look
back to the project on which it was developed - say, n hours - and
multiply that by your currrent rate.  (Since the tool which was used to
develop the sytem at that time - you at that skill-level (for that
original rate) - is no longer available then you have to apply the most
equivalent tool - you at your current level (at your present rate) -
available now.)

Then add to your time a 40% factor for 'environment time', since the folks 
who were there then are not available to you now and you will have to 
provide the input they had (if you can) on your own.

DD
```

#### ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-16T10:59:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302161059.39c37b4b@posting.google.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
"BPR2" <news1@augursw.com> wrote 

> If all my source code (and specs, documentation, etc) were destroyed, and I
> need to make an insurance claim for it's replacement value ... how would I
> calculate the value of the loss?

You probably have a duty to mitigate any losses.

If you haven't been making regular off site backups to protect against
complete loss then they may reasonably refuse your claim.
```

#### ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-16T16:14:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302161614.3950a9e0@posting.google.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
"BPR2" <news1@augursw.com> wrote 

> Years ago, we used to assess the value of COBOL source code ...

> All ideas are welcome, particularily those from people that have had to
> assess the value of source code in the past few years.

Don't forget to put this value on your tax return as an asset of the
business. As the profit of a business in the nett value at the end of
the year less the nett value at the beginning of the year then there
may be an large increase in the value of business, and thus in profit.

This may result in an increase in tax liability.

For an insurance claim to succeed it is possible that the insurance
company would require some evidence of value, such as how it is shown
on the books. If it is shown at zero value, or not shown at all, then
they may reasonably feel that is its actual value for payout purposes.

If the programmers are paid and this is shown as an entire cost in the
books and no corresponding increase in asset (source code) value then
obviously your company is gaining a tax writeoff.  If you now think
that there _is_ a value you may be committing tax fraud.

Which is it ?
```

#### ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-02-16T19:57:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E503379.F113D669@ix.netcom.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
BPR2 wrote:
<snip>
> The question I'm trying to answer is:
> 
…[9 more quoted lines elided]…
> BPR

There are a few ways to get this answer. First let me
diverge.

I once had a car that was almost as old as I was. It cost me
$600 to buy and $400 to repair. It got 30+ MPG, had
rear-wheel drive and a 3 speed manual transmission. You
could not get the sucker stuck in snow (unless the snow was
a foot above the bumper!). The only car that did all the
things that my car did was available, new, at ~$5000. So the
question came down to, what was the utility value of my car?
According to the bean counters with the insurance company my
car was worth, at most, $500 (it was no longer listed in the
NADA or Blue book).

However, we all know that software does not suffer wear and
tear. It does not break down or need an oil change because
it is not a mechanical item.

Given that, here are some items to think about:

1) Since this code has been amortized (theoretically) to
zero, it now becomes a case of what would it cost to replace
it with "an off the shelf product"?

2) What would it take to migrate the system to a new
platform (hardware and/or software)? And would this be so
that there would be someone skilled in that
language/platform...

3) How long would it take for some one skilled in the arts
(to take from the PTO) to recreate the system from scratch?

4) Should the company declare a disaster, how long would it
take to recover this system and its data? (a) The length of
time to re-write, (b) the length of time to build a new
system to replace it

5) What revenue stream is the software responsible for? What
would happen without this software?

Given these kinds of questions, which should put things into
some kind of perspective, one can begin to assign value to
the software in question.
```

##### ↳ ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-02-17T01:52:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afX3a.56398$zF6.3825438@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com> <3E503379.F113D669@ix.netcom.com>`

```

Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com> wrote in message news:3E503379.F113D669@ix.netcom.com...
>
> Given these kinds of questions, which should put things into
> some kind of perspective, one can begin to assign value to
> the software in question.

There is one critical flaw in your analysis.

Before you could make any substantial progress in replacing
all of your lost software, the company would go out of business.
```

###### ↳ ↳ ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2003-02-17T09:53:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hl815vcsnac5ie6chs3il8deoe9rbl4kjg@4ax.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com> <3E503379.F113D669@ix.netcom.com> <afX3a.56398$zF6.3825438@bgtnsc04-news.ops.worldnet.att.net>`

```
Well, a company that looses all its software source -   deserves to be
out of business.  Can you spell BACKUP?  Can you say REMOTE SITE?


On Mon, 17 Feb 2003 01:52:06 GMT, "Hugh Candlin" <no@spam.com> wrote:

>There is one critical flaw in your analysis.
>
>Before you could make any substantial progress in replacing
>all of your lost software, the company would go out of business.
>

      
      
      
      
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Even when opportunity knocks, you still have to get up off your seat and open the door.
      
        (Another Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

#### ↳ Re: Value of 'old' COBOL source ... How do you evaluate yours?

- **From:** "BPR2" <news1@augursw.com>
- **Date:** 2003-02-17T15:06:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_T64a.4585$usP.283@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
I think I may need to re-state the question:

Can anyone share with me (and this group) how they 'evaluate' the worth of
the (COBOL) source code for their production applications?

That's the essence of what I need to know.

re: problems with practises, backups and remote site storage, etc ... all
your points are valid ... my backup plans were not adequate to protect
against the circumstances and events that unfolded and I expect that will
translate into me shouldering a portion of the financial responsibility.
But probably not the major share.

The specific circumstances that lead to this loss were:

A) 3 physical sites, one was only for backup storage ... 2 working sites
sent weekly backups to 3rd (backup only) site.
B) Business issues caused the temporary closure of the 2 working sites ...
all copies now only at backup site ... I know, I know ... I shouldn't have
allowed this even for a short time, but I did.
C) Fire (3rd party liability) in backup site at the time all copies are
stored there ... 3rd party accepts liability, agrees to pay
D) 1 set of source code is destroyed by fire ... 2 copies are 'OK' (suffer
smoke damage, probably recoverable)
E) 1 Backup set is retained along with softcopy of documentation ... other
set is 'scrapped' (everything is very stinky, paper 'crumbles' when touched)
... expectation of using 'data recovery' techniques to read 'dirty tapes' at
a later time ... for next few weeks only 1 viable copy exists ... major
activity is re-construction, data recovery is postponed
F) Lawsuit is filed against the company that caused the fire by Insurance
company (demanding about 10X original liability estimate, that 3rd party
originally agreed to) without my knowledge
G) A few weeks later, all the remaining Source code and documentation is
stolen (during break in) along with a collection of evidence intended to
support the claim of 3rd party liability
H) After the theft ... 3rd party denies liability ... seems to believe that
evidence to prove liability no longer exists ... now only photographs of
original source media and documentation remain.

In summary, I don't believe that having an extra backup set of source would
have changed the outcome ... the set that did survive the fire was stolen
... I suspect by one of the people that was responsible for the fire in an
effort to eliminate evidence.

What I need to do now is to find a good method of calculating and describing
the value of the lost source and documentation that a jury will understand
without difficulty.  The more I can learn about how other people do this
type of evaluation, the better I can do this next task.

I hope this explanation is adequate.
```

##### ↳ ↳ Re: Value of 'old' COBOL source ... How do you evaluate yours?

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-02-17T22:30:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E51A8B9.8060005@ix.netcom.com>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com> <_T64a.4585$usP.283@news01.bloor.is.net.cable.rogers.com>`

```
BPR2 wrote:
> I think I may need to re-state the question:
> 
> Can anyone share with me (and this group) how they 'evaluate' the worth of
> the (COBOL) source code for their production applications?
> <snip>

In your case, do you have any payroll and/or contract records to 
establish the costs of development? Do you have any records 
showing what the software represents in revenue (either sold as 
object code, or what it did for your business)?

Having some way of establishing a worth for the software is 
important. The method of establishing worth may not be obvious to 
you, but it can be one that the opposing attorney(s) may use or 
accept.

Regards,
Steve Thompson
```

##### ↳ ↳ Re: Value of 'old' COBOL source ... How do you evaluate yours?

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-02-18T06:35:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wuk4a.40407$rq4.3253437@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com> <_T64a.4585$usP.283@news01.bloor.is.net.cable.rogers.com>`

```

BPR2 <news1@augursw.com> wrote in message news:_T64a.4585$usP.283@news01.bloor.is.net.cable.rogers.com...

IF all of what you said is true, the only advice that I would give you is twofold

1  Say no more to anyone except your lawyers.
2  Print out this thread and show it to your lawyers.

The sooner the better.
```

##### ↳ ↳ Re: Value of 'old' COBOL source ... How do you evaluate yours?

- **From:** SkippyPB <swiegand@NOSPAM.neo.rr.com>
- **Date:** 2003-02-18T09:34:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C2B002F69E6675C9.AD5C58AA209FC2B3.921CD72B591E14F7@lp.airnews.net>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com> <_T64a.4585$usP.283@news01.bloor.is.net.cable.rogers.com>`

```
On Mon, 17 Feb 2003 15:06:34 GMT, "BPR2" <news1@augursw.com>
enlightened us:

>I think I may need to re-state the question:
>
…[47 more quoted lines elided]…
>I hope this explanation is adequate.

Whew!  Who was running that backup site?  The Mafia?

Anyway as far evaluating the value of the software and documentation,
there are probably two ways to go about it:

1)  Actual project cost:  Was a budget done and followed when the
software and documentation was written, tested and installed?  Is
there a final cost associated with that budget (over/above)?  If so,
that could be used as the means of valuing the software and
documentation.

2)  If there was no formal project budget/cost kept, do you have
access to the payroll records of all who worked on the development of
the software and wrote the documentation?  Do you know the exact
timeline of the project cycle?  If yes, you could use the total cost
of payroll as your means of putting a value on your software and
documentation.  

Finally, you will need to show what the cost would be to recreate
everything in today's economy as opposed to whatever the cost was at
the time it was done.  One would expect that cost to be higher, but
you'll need the baseline cost first.

HTH

Good luck,


          ////
         (o o)
-oOO--(_)--OOo-

Vulcanization: The process whereby rubber grows pointed ears and 
starts saying "Live long and prosper". 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Value of 'old' COBOL source ... does anybody know?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-18T13:42:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2td8f$cdi$1@peabody.colorado.edu>`
- **References:** `<eaN3a.365784$pDv.101629@news04.bloor.is.net.cable.rogers.com>`

```
You can't look at the code to decide what it's worth.  Its worth is what you
would be willing to pay for to have its functionality.  If you lost it, how much
would you be willing to pay to be able to do your accounting, finance, bills, or
whatever your CoBOL code do.

This is also how you decide whether to replace or outsource your system.

The code itself is worthless - except that it enables you to meet current and
future needs.  (Source code is needed for future needs).  What is the value of
meeting those needs?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
