[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help! GO TO and PERFORM THRU!

_96 messages · 19 participants · 2007-02 → 2007-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Help! GO TO and PERFORM THRU!

- **From:** "Impy" <Impy.McFerguson@gmail.com>
- **Date:** 2007-02-24T10:02:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
Okay, so I have been doing the Cobol thing for a couple of months now,
Unisys, DMS2, datasets, batch, BOLTS screens, etc. and quite enjoying
it. However, it appears our S&P manual states we are to use GO TOs,
and my fellow Cobol programmers use them, as well as the PERFORM THRU
statements.

Okay, they use them pretty cleanly I'd say. PERFORM A100-READ-FILE
THRU A100-READ-FILE-EXIT, etc.  and the GO TOs are only used to loop
through reads and writes and such, and to go to the exit paragraphs
upon errors, or maybe in a nested loop to go back to an earlier loop.

It's not exactly spaghetti code (or is it?) , and it's 'the way it's
done' where I work, so I'm just following orders. This is my first
programming job, went back to school in my 30's, been toying with
programming since 7th grade, having lots of fun too.

So, if you are going to use PERFORM THRU and GO TO this seems a
halfway decent way of using them. But I believe I have some choice in
how I proceed in writing my code, S & P manual may be out of date, but
I haven't really discussed this much with anyone.

I have been reading much trashing of PERFORM THRU and GO TO this
morning, and I'm just curious what opinions people have. Obviously, I
will do things the way my company wants them done, but I will have
some flexibility in future programs, so I'd like to start thinking
about it now.

Thanks
Impy
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "Impy" <Impy.McFerguson@gmail.com>
- **Date:** 2007-02-24T13:43:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172353386.297833.287020@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
Okay, I've been reading through old posts, looks like this has been
pretty much thoroughly covered, so that's interesting. I will test the
waters to see if I can NOT use PERFORM THRU and drop the GO TO, but if
not, I'll try to keep it neat.

Thanks
Impy
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "Impy" <Impy.McFerguson@gmail.com>
- **Date:** 2007-02-24T13:45:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172353530.464657.206980@z35g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
--------------------------

Sorry, I replied to myself and the posts got melded together. I think
I've read enough on this subject, but thanks.
--------------------------
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-02-24T16:58:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12u1gp5kdf3ngfb@news.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
Impy wrote:
> Okay, so I have been doing the Cobol thing for a couple of months now,
> Unisys, DMS2, datasets, batch, BOLTS screens, etc. and quite enjoying
…[23 more quoted lines elided]…
> about it now.

Lucky you!

If your shop standard mandates PERFORM THRU and GO TOs, you'll always have a 
job.
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-24T15:00:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172358001.066422.182050@m58g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
On Feb 25, 7:02 am, "Impy" <Impy.McFergu...@gmail.com> wrote:
> Okay, so I have been doing the Cobol thing for a couple of months now,
> Unisys, DMS2, datasets, batch, BOLTS screens, etc. and quite enjoying
> it. However, it appears our S&P manual states we are to use GO TOs,

Is it dated 1967 ?

> and my fellow Cobol programmers use them, as well as the PERFORM THRU
> statements.

> Okay, they use them pretty cleanly I'd say. PERFORM A100-READ-FILE
> THRU A100-READ-FILE-EXIT, etc.  and the GO TOs are only used to loop
…[14 more quoted lines elided]…
> morning, and I'm just curious what opinions people have.

It should be obvious from posts made here over the last couple of
decades. Most have moved on, there isn't much left unsaid on the
subject of GOTO and PERFORM THRU.

I would say, however, that there is nothing wrong at all with a GOTO.
They are clear and precise. When you see one you know exactly what
will happen. The problem lies elsewhere entirely: at the labels that
must exist for them.

> Obviously, I
> will do things the way my company wants them done, but I will have
> some flexibility in future programs, so I'd like to start thinking
> about it now.
```

##### ↳ ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "Impy" <Impy.McFerguson@gmail.com>
- **Date:** 2007-02-25T10:05:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172426711.739083.196360@8g2000cwh.googlegroups.com>`
- **In-Reply-To:** `<1172358001.066422.182050@m58g2000cwm.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <1172358001.066422.182050@m58g2000cwm.googlegroups.com>`

```

> > it. However, it appears our S&P manual states we are to use GO TOs,
>
> Is it dated 1967 ?

** 2002 ** I think the mandate on the GO TO dates from, lol.


>
> It should be obvious from posts made here over the last couple of
…[7 more quoted lines elided]…
>

>
> Lucky you!
>
> If your shop standard mandates PERFORM THRU and GO TOs, you'll always have a
> job.

We can't even find people for our existing openings for Cobol
Programmers, and many of the ones there are very near retirement age.
So my job is pretty secure, I think, lol. It's pretty much my job for
as long as I want it, I think I can handle it, still learning after a
couple of months, but I guess I 'look like a Cobol Programmer'.


http://pag.csail.mit.edu/~adonovan/dilbert/show.php?day=4&month=11&year=1997

I'm not sure they mandate the PERFORM THRU, but it is how I'm being
told how to code it. This is a brand spanking new report I'm writing
for an existing subsystem. And the mandate on the GOTO is from about 5
years ago I think.

Yes, I have been reading about this 'style war' for a couple of days
now, and I realize it's an old can of worms best left alone, or a
sleeping dog or something.

I can see a use for GO TOs in Cobol (if you're careful), and if you
keep the paragraphs neat and structured (and never have to change
things), it might not be too bad, but having been doing this for a
WHOLE 2 months, I might not *quite* have the experience or wisdom to
see the bigger picture.

My employer tends to keep their code pretty neat and tidy,  but I
think the use of GO TO and PERFORM THRU is more of an inertia thing,
just keep doing it that way cause it ain't broken. But I don't know.

It will be interesting to see how it goes, I like it a lot and can't
wait to go to work in the mornings. Hopefully, it will stay that way.

Thanks all!
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-25T23:15:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ert5ar$dm3$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <1172358001.066422.182050@m58g2000cwm.googlegroups.com> <1172426711.739083.196360@8g2000cwh.googlegroups.com>`

```
In article <1172426711.739083.196360@8g2000cwh.googlegroups.com>,
Impy <Impy.McFerguson@gmail.com> wrote:
>
>> > it. However, it appears our S&P manual states we are to use GO TOs,
…[58 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-02T17:13:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A9KdnYC2jeAnIHXYnZ2dnUVZ_hynnZ2d@comcast.com>`
- **In-Reply-To:** `<1172426711.739083.196360@8g2000cwh.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <1172358001.066422.182050@m58g2000cwm.googlegroups.com> <1172426711.739083.196360@8g2000cwh.googlegroups.com>`

```
Impy wrote:
> 
> I'm not sure they mandate the PERFORM THRU, but it is how I'm being
> told how to code it. This is a brand spanking new report I'm writing
> for an existing subsystem. And the mandate on the GOTO is from about 5
> years ago I think.

Just because you have to use PERFORM THRU doesn't mean you have to use 
GO TO to loop through things.  You can specify an exit paragraph without 
ever explicitly "GOing TO" it.  :)

-8<---

     move [value] to [calc-key]
     fetch [owning] record

     if error-num = zeroes
         perform myPara1 thru myParaExit
     end-if
     .
myPara1.

     perform with test after
       until error-num > zeroes

         fetch next [some] record within [useful] set

         if error-num = zeroes
             [do something with it]
         end-if
     end-perform
     .
myParaExit.
     exit.

->8---

Of course, Unisys DMS has the ON ERROR clause on most statements, which 
are really suited to the exit paragraph scenario...

-8<---

     perform myPara1 thru myParaExit
     .
myPara1.

     move [value] to [calc-key]
     fetch [owning] record
       on error go to myParaExit
     .
myPara1cont.

     fetch next [some] record within [useful] set
       at end go to myParaExit

     [do something with it]

     go to myPara1cont
     .
myParaExit.
     exit.

->8---

Something tidy like the above probably wouldn't present that much of a 
maintenance headache, especially if everyone in the shop is familiar 
with that coding style.
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** raul@raul.com
- **Date:** 2007-02-25T23:28:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45e2197b$0$7474$9a6e19ea@news.newshosting.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
I have used COBOL for many years, even now sometimes, and I must say I like
it a lot.

I normally use the PERFORM THRU, especially when doing validations. Then, if
the validation fails
you use a GO TO to get to the, say, 1200-VALIDATION-EXIT procedure, which
has an EXIT statement.

There is nothing wrong with it, I'd say.

Raul Ward
```

##### ↳ ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "ruddy" <iruddock@blueyonder.co.uk>
- **Date:** 2007-02-26T01:37:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172482649.993940.291000@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<45e2197b$0$7474$9a6e19ea@news.newshosting.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com>`

```
On Feb 25, 11:28 pm, r...@raul.com wrote:
> I have used COBOL for many years, even now sometimes, and I must say I like
> it a lot.
…[8 more quoted lines elided]…
> Raul Ward


I don't think its worth getting too bogged down worrying about using
GO TO's or not, or PERFORM THRU's. What is more relevant is what do
the existing programs do? If they are already written in a particular
style then you would be well advised to adopt that, at least until you
are 100% comfortable with it.

I have personally heard many criticisms of the COBOL GO TO statement
over the past 20 years and I think people forget about the history.
Some of the code was written before we had the constructs that we have
now and the only way to split some conditions up was to use some GO
TO's. But again, if they already exist don't touch them, unless you
are being tasked to do exactly that. I like to use the GO TO command
as long as I'm not going far :-). For example.

    MOVE 1 TO WS-SUB.
B100-ADD.
   ADD 1 TO WS-SUB.
   IF WS-SUB < 100
      IF WS-STATUS-ERROR-FLAG(WS-SUB) = 1
         PERFORM PROCESS-ERROR
      END-IF
      GO TO B100-ADD.

Yes, I know, I know. There is at least one easier method just using a
PERFORM VARYING and you don't have to use a GO TO. But please don't
post it. You would be missing the point I'm making. Does it really
matter. As long as its clear and you can see the place its going to as
in this example I feel its as good as anything.

Incidently, am I the last person using SECTIONS. I have heard people
talking about 'falling through' but I don't get this problem. When I
want to exit a section I do just that with the EXIT SECTION statement.

Regards

Razor
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-28T15:46:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54k8niF20o965U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com>`

```

"ruddy" <iruddock@blueyonder.co.uk> wrote in message 
news:1172482649.993940.291000@v33g2000cwv.googlegroups.com...
> On Feb 25, 11:28 pm, r...@raul.com wrote:
>> I have used COBOL for many years, even now sometimes, and I must say I 
…[39 more quoted lines elided]…
> post it. You would be missing the point I'm making.

I think your point fails to be "made"... :-)

The first status flag in the above will never be tested, the mixing of 
scope-delimited COBOL with full-stop-terminated COBOL is ugly and confusing, 
and all of this without even looking at whether GO TO is OK or not... :-)

>Does it really
> matter.

It does if someone else has to maintain it. If you are the only person who 
will ever use or change it, then it doesn't. (Have you met Tony Dilworth... 
?)

>As long as its clear and you can see the place its going to as
> in this example I feel its as good as anything.
>

Well, that's all right then... :-)

(Seriously, there is nothing wrong with GO TO when used carefully and when 
the destination is local;;; Richard already commented that the problem is in 
the labels and I think he has a point. Having said all of that, I prefer NOT 
to use GO TO for my own programs (I'm just not Evangelical about it... :-)))

> Incidently, am I the last person using SECTIONS.

No, you're not. I still use them (have since early 70s, after experimenting 
with PERFORM...THROUGH) and find them very useful, even in OO COBOL. Have a 
look at some code I posted here a few weeks back (something I hardly ever do 
because the style wars generated are just tedious...)  and feel free to 
criticize ... give you a chance to get your own back for my comments 
above... :-)

http://groups.google.com/group/comp.lang.cobol/tree/browse_frm/thread/a5bc256300719882/591df69b54314bc6?rnum=21&hl=en&q=productivity&_done=%2Fgroup%2Fcomp.lang.cobol%2Fbrowse_frm%2Fthread%2Fa5bc256300719882%2F8f64437938861860%3Flnk%3Dgst%26q%3Dproductivity%26rnum%3D25%26hl%3Den%26#doc_e59987cf1370a3fa

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-02-28T13:20:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rkfFh.4783$re4.3001@newssvr12.news.prodigy.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net>`

```
> I don't think its worth getting too bogged down worrying about using
> GO TO's or not, or PERFORM THRU's.

For sure it ain't worth another 400-post monster thread on the topic.

That's why archives are available.

MCM
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-28T07:58:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net>`

```
On Wed, 28 Feb 2007 15:46:07 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>The first status flag in the above will never be tested, the mixing of 
>scope-delimited COBOL with full-stop-terminated COBOL is ugly and confusing, 
>and all of this without even looking at whether GO TO is OK or not... :-)

I couldn't disagree more.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-01T12:15:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54mgoqF20ch7tU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com...
> On Wed, 28 Feb 2007 15:46:07 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> I couldn't disagree more.

About the flag or the style mix :-)?

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-01T08:18:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net>`

```
On Thu, 1 Mar 2007 12:15:37 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> I couldn't disagree more.
>
>About the flag or the style mix :-)?

I like full stop periods within paragraphs - and always use END-IFs
with my IFs.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-02T12:58:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54p7lrF21d53dU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com...
> On Thu, 1 Mar 2007 12:15:37 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> with my IFs.

Fair enough. A personal preference.

As you may have gathered, I disagree. I think periods were a major cause of 
error in "old" COBOL and the fewer you have of them, the better. The only 
requirement now (in the Procedure Division...) seems to be immediately 
preceding a paragraph/section name and I reckon that is great.

Why would I prefer fewer periods (full stops)...?

1. With some of the old impact printers they didn't render properly and were 
easily missed. Sure, that is much less of a problem these days when we print 
listings with laser printers, but I have lingering suspicions of any program 
listing. Fortunately, I never use COBOL listings these days and haven't for 
many years... Still, reducing the periods reduces any real or imagined risk 
and makes me feel better :-).

2. Using an end-of-statement terminator (full stop) (which is small and 
easily missed) rather than a scope delimiter (which is easily visible and 
logically sensible) makes cutting and pasting code much more error prone.

3. Using both scope delimiters and full stops just seems ugly and 
unnecessary to me.

I think using END-IF is a step in the right direction, but why not take a 
few more steps and use ALL of the scope delimiters? Before you know it you 
are thinking in logical scope blocks (just as you would in a modern 
language), and periods are just an ugly irrelevance in the middle of your 
code... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-01T21:46:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172814373.266489.167110@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<54p7lrF21d53dU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net>`

```
On Mar 2, 12:58 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Howard Brazee" <how...@brazee.net> wrote in message
>
…[26 more quoted lines elided]…
> and makes me feel better :-).

Print a program listing ? How 70s.  I haven't done that since I got
Wordstar at the end of that decade.

> 2. Using an end-of-statement terminator (full stop) (which is small and
> easily missed) rather than a scope delimiter (which is easily visible and
> logically sensible) makes cutting and pasting code much more error prone.

My editor highlights full stops as red blocks. They don't get missed.

> 3. Using both scope delimiters and full stops just seems ugly and
> unnecessary to me.
…[7 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-03T04:07:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54qsudF21u7fpU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <1172814373.266489.167110@j27g2000cwj.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172814373.266489.167110@j27g2000cwj.googlegroups.com...
> On Mar 2, 12:58 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[38 more quoted lines elided]…
>
I agree. Nevertheless, you will find green lineflo in many programming 
cubicles around the World, even today. It is being replaced by stacks of A4 
or letter laser printed sheets, but many COBOL programmers use printouts to 
save referring back ot the Data Division on screen. I think it stems from 
not having a decent IDE, historically.

>> 2. Using an end-of-statement terminator (full stop) (which is small and
>> easily missed) rather than a scope delimiter (which is easily visible and
…[3 more quoted lines elided]…
>

Well, that would certainly be better. Unfortunately, I know of no way to do 
this with a 3270 screen....(even a colour one... you would simply get a tiny 
red dot.)

I don't think it is really the size of the dot that offends me; it is just 
using a dot when there is a perfectly good scope delimiter.

Obvbiously, it comes down to personal preference, I was just trying to 
explain WHY I have the preference I have.

>> 3. Using both scope delimiters and full stops just seems ugly and
>> unnecessary to me.
…[10 more quoted lines elided]…
>

Are you advocating the mixing of full stops and scope delimiters, Richard? 
If so, I'd be interested in hearing your reasons.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-02T11:30:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172863854.644008.57150@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<54qsudF21u7fpU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <1172814373.266489.167110@j27g2000cwj.googlegroups.com> <54qsudF21u7fpU1@mid.individual.net>`

```
On Mar 3, 4:07 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Richard" <rip...@Azonic.co.nz> wrote in message
>
…[78 more quoted lines elided]…
> If so, I'd be interested in hearing your reasons.

Not at all, I am entirely indifferent to what others may do with full
stops.  I was just pointing out that the claim they are difficult to
see is not necessarily true for everyone, and so that may be a hollow
claim.

My Cobol programs tend to have hundreds of full stops, especially in
data division. Each one is important so I make sure that they are
visible.

I also have to deal with old code written by others from time to time
so I ensure I have the tools to deal with it easily.

What I would like is a compiler that tells me when I have the scope
terminators wrong, probably as an option, so that I don't have to
bother with counting them.. (this relates to visible logic being
actually what you get).
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-03T10:53:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54rklsF22c22uU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <1172814373.266489.167110@j27g2000cwj.googlegroups.com> <54qsudF21u7fpU1@mid.individual.net> <1172863854.644008.57150@j27g2000cwj.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172863854.644008.57150@j27g2000cwj.googlegroups.com...
> On Mar 3, 4:07 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[101 more quoted lines elided]…
>

I think that if we are required to justify most of our style choices, the 
claims are hollow or can be refuted. :-)

We just THINK it makes sense and so become comfortable with doing it that 
way.

> My Cobol programs tend to have hundreds of full stops, especially in
> data division. Each one is important so I make sure that they are
> visible.
>

I was careful to confine my "full stop objection" to the Procedure Division, 
which just shows the illogicality of what I said. (If they are hard to see, 
they will be just as hard to see in the Data Division...) It is really an 
aesthetic thing, although it may be based on distant memories of times when 
there was a real risk of them not being printed correctly.

> I also have to deal with old code written by others from time to time
> so I ensure I have the tools to deal with it easily.
…[5 more quoted lines elided]…
>

I don't think I have ever counted scope delimiters, although I can see that 
with nesting it might be a useful check.

I DO take care to ensure that COBOL is indented into matching blocks which 
is part of ensuring that visual logic matches actual logic.

If you have one-too-many delimiters the Fujitsu compiler will tell you, but 
it is more cavalier about having too few. It only grumbles if the lack of a 
delimiter means the code is ambiguous or it can't understand what you are 
doing.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-02T08:13:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net>`

```
On Fri, 2 Mar 2007 12:58:50 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>As you may have gathered, I disagree. I think periods were a major cause of 
>error in "old" COBOL and the fewer you have of them, the better. The only 
>requirement now (in the Procedure Division...) seems to be immediately 
>preceding a paragraph/section name and I reckon that is great.

I haven't had that experience, except once where a period was in
column 73.   That must have been 25 years ago.

>Why would I prefer fewer periods (full stops)...?
>
…[5 more quoted lines elided]…
>and makes me feel better :-).

The hard part about impact printers was that commas and periods looked
the same.    But I also don't use CoBOL listings these days, so there
is no risk.

>2. Using an end-of-statement terminator (full stop) (which is small and 
>easily missed) rather than a scope delimiter (which is easily visible and 
>logically sensible) makes cutting and pasting code much more error prone.

It's not an either/or choice, but more of a belts and suspenders
choice.

>3. Using both scope delimiters and full stops just seems ugly and 
>unnecessary to me.

It's not ugly for me.   But even if wearing both belts and suspenders
is not stylish - my pants don't fall down.

>I think using END-IF is a step in the right direction, but why not take a 
>few more steps and use ALL of the scope delimiters? Before you know it you 
>are thinking in logical scope blocks (just as you would in a modern 
>language), and periods are just an ugly irrelevance in the middle of your 
>code... :-)

I've thought about that - but haven't gone that far.   Some of them
"seem ugly and unnecessary to me".

Does anybody here use every possible explicit scope delimiter all the
time?
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-02T10:05:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com>`

```
On Fri, 02 Mar 2007 08:13:31 -0700, Howard Brazee <howard@brazee.net>
wrote:

>Does anybody here use every possible explicit scope delimiter all the
>time?  

I suppose one explicit scope delimiter is the parenthesis.   I use
this more than necessary for the code - to make sure that my
intentions were absolutely clear.

I rarely use END-READ, although I probably have written 90% of the
END-READ lines in my shop.    I did a search through our source code
for END-COMPUTE with zero matches.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-03T10:40:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54rjujF21itbuU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com...
> On Fri, 02 Mar 2007 08:13:31 -0700, Howard Brazee <howard@brazee.net>
> wrote:
…[10 more quoted lines elided]…
> for END-COMPUTE with zero matches.

Yes, I forgot about end-compute. I don't use it normally. But I certainly 
would, IF I had a multi-line complex compute. As those are best avoided, my 
compute statements tend to occupy a single line.

END-READ (and NOT AT END) I use as a matter of course and have for some 
years now.

In fairness, I rarely use files that require READing; relational databases 
do all of the serious data storage and it would only be a text file that I'd 
be likely to READ.

I find it puzzling that INSPECT has no scope delimiter and every so often I 
write END-INSPECT and then have the compiler grizzle and throw it out.

All of the others that I can think of, I use and find useful.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-02T13:51:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172872303.445681.99090@p10g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<54rjujF21itbuU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com> <54rjujF21itbuU1@mid.individual.net>`

```
On Mar 3, 10:40 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Howard Brazee" <how...@brazee.net> wrote in message
>
…[32 more quoted lines elided]…
> Pete.

Scope delimitres are only required for conditional statements and not
for imperitive ones.

COMPUTE X = Y + 1       is imperitive

COMPUTE X = Y + 1
       ON SIZE ERROR
                COMPUTE X = -1
.

is conditional. A _single_ END_COMPUTE is required to make it
equivalent to an imperitive statement.

You do not add scope terminators to statements because it is  "a multi-
line complex compute", you only do so because it is conditional with
an 'ON SIZE ERROR'.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-03T11:08:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54rlj5F229pknU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com> <54rjujF21itbuU1@mid.individual.net> <1172872303.445681.99090@p10g2000cwp.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172872303.445681.99090@p10g2000cwp.googlegroups.com...
> On Mar 3, 10:40 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[56 more quoted lines elided]…
>

No, I do whatever I think is necessary. I can add END-COMPUTE  whether it is 
a conditional or imperative compute. I may do so for readability or to 
ensure that the block is clearly defined.

I was aware of the difference between imperative and conditional COMPUTEs 
(and other arithmertic statements).

I WOULD add END-COMPUTE to "a multi-line complex compute" whether it was 
conditional or imperative.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-02T23:34:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dw2Gh.92687$k82.17368@fe07.news.easynews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <6nlgu2tp0vus89fdo3pl3reimk0ehd3m3a@4ax.com> <54rjujF21itbuU1@mid.individual.net> <1172872303.445681.99090@p10g2000cwp.googlegroups.com>`

```
Richard (I hadn't read your note before responding to Pete's)

You are (of course) correct that scope delimiters are NEVER required for 
imperative statements, but there are times when things get confusing 
with/without them.    For example,

Call "ABC"
    On Exception
           Display field-1
        Not On Exception
           Perform XYZ
               .

Interestingly enough, this is conforming source code in both the '85 and '02 
Standards, but with different logic flow (depending on the "nature" of Field-1).

For the '85 Standard this is equivalent to:

Call "ABC"
    On Exception
         Display field-1
     Not On Exception
         Perform XYZ
 End-Call
      .

For the '02 Standard it is equivalent to:

Call "ABC"
    On Exception
         Display field-1   *> field-1 is a screen name
              Not On Exception
                  Perform XYZ
         End-Display
 End-Call
   .

(There was some debate, I don't remember how it ended whether the code 
would/should get a "syntax error" in the '02 Standard if field-1 were NOT a 
screen-name - or whether the NOT ON EXCEPTION then would go with the CALL. 
However, this statement COULD be made "legal" and equivalent to the original '85 
meaning in the '02 Standard by coding (with a scope terminator for an imperative 
statement),

Call "ABC"
    On Exception
         Display field-1
         End-Display
     Not On Exception
        Perform XYZ
End-Call
  .

To follow-up and give an example using COMPUTE where scope terminator on an 
imperative statement makes a difference, compare:

  Compute A = B + C
    On Size Error
        Compute X = Y + 1
        End-Compute
    Not On Size Error
        Display "Which Compute"
     .

versus

  Compute A = B + C
    On Size Error
        Compute X = Y + 1
             Not On Size Error
                 Display "Which Compute"
     .

This also gets back to the original question/issue about mixing scope 
terminators and periods (full-stops).  This type of confusion ONLY impacts 
"conforming" source code when you have at least one period terminating a 
conditional statement.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-03T10:29:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54rj9eF222pjiU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com...
> On Fri, 2 Mar 2007 12:58:50 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[49 more quoted lines elided]…
>

Fair enough.

A conclusion I'm coming to is that we all use styles that are most 
comfortable for us, without necessarily having any really good reason for 
doing so.

(We probably think we have good reason or will justify what we do, but in 
the final analysis it is just that that's how we do it. I know that is 
certainly the case for me. Much of my own coding style is really based 
around arguable aesthetics; I may think it is beautiful and elegant but 
someone else may not... :-))

Provided what we do is (easily) understandable to others (if we are working 
in environments where others must maintain code we wrote), it probably 
really doesn't matter much.

> Does anybody here use every possible explicit scope delimiter all the
> time?

Yes, I do.

Ironically, now that I've learned to write COBOL "properly", I'm abandoning 
it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-02T23:18:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0h2Gh.82505$_X1.72221@fe05.news.easynews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <54rj9eF222pjiU1@mid.individual.net>`

```
Pete,
  Do you use scope terminators for NON-conditional forms of statements, e.g.

  Compute A = B +1
  End-Compute

or

  Call "ABC"
  End-Call

or do you always add the "conditional phrases" or do something else (well other 
than not use COBOL <G>).

This has always been one of those "odd" situations that I have mixed feelings 
about, especially when it CAN end up changing logic flow
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T00:24:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54t484F22ak7dU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <54rj9eF222pjiU1@mid.individual.net> <0h2Gh.82505$_X1.72221@fe05.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:0h2Gh.82505$_X1.72221@fe05.news.easynews.com...
> Pete,
>  Do you use scope terminators for NON-conditional forms of statements, 
…[15 more quoted lines elided]…
>

I thought I had made it clear... sorry.

I would (probably...) NOT write...
  Compute A = B +1
  End-Compute

... because it is quite clear without the scope terminator, and, no scope 
terminator is required by the language as it is the imperative form. I would 
NOT follow it with a full stop (unless one was required because of an 
immediately following label, and then I would put the full stop in column 12 
on a line by itself.)

I WOULD (possibly...) write...(do not look for significance; it's a coding 
format example...)

compute  x =  (function STORED-CHAR-LENGTH (some-field) + function  ANNUITY 
(lump-sum)) *
                      ((ABC * 17.985461) / function 
INTEGER-OF-DATE(the-cats-birthday)) +
                      1/(5/3 * 8/5 * fuck-all) +
                      XYZ +
                      ABC +
                      DEF +
                      GHI +
                      JKL *  function MAX  (val(ALL)) +
                     MNO * function MIN (Val(ALL))
end-compute

... even though there is no strict requirement for the scope delimiter.


I WOULD (definitely...) write...
>  Call "ABC"
>  End-Call

Seems inconsistent, doesn't it...? (Why not do it for compute? I tried to 
answer that in my response to Richard.)

So, why a scope terminator with CALL/INVOKE but NOT with COMPUTE?

The reason is that in this case there is a chance that the CALL will have 
parameters added to it later, so I consider it needs a "block". In order to 
be consistent as far as CALL/INVOKE are concerned, I therefore ALWAYS code 
these with provision for a block, thus...

call "ABC"
      using  XYZ
      returning PQR
            on exception
                 perform wailing-and-gnashing-of-teeth
end-call

...or, in imperative form...

call
   "ABC"
end-call

BOTTOM LINE:

If the structure is a de facto "block", or could become a block, or looks 
like it needs a block, I use the scope delimiters, whether the language 
requires them or not.

The tail doesn't wag the dog :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-03-03T00:10:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L13Gh.1197020$5R2.586039@pd7urf3no>`
- **In-Reply-To:** `<54rj9eF222pjiU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <54rj9eF222pjiU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Howard Brazee" <howard@brazee.net> wrote in message 
> 
…[7 more quoted lines elided]…
> 
As well as the COMPUTE, I'm willing to bet that you didn't/don't use the 
following as regular usage - I NEVER did :-

		END-INVOKE

Now if I go back to the original INVOKE syntax, listed in Ray Obin's 
1993 M/F paperback :-

---------------------------------------------------------------------
        INVOKE object-identifier-3  {identifier-1 }
                                    {a-n-literal-1}
                USING { [BY REFERENCE] (identifier-2] } ] ]
                      {  BY CONTENT     {identifier-3 } } ]
                [RETURNING identifier-4 ]
                [ON EXCEPTION imperative-statement-1]
                [NOT ON EXCEPTION imperative-statement-2]
        [END-INVOKE]

With reference to the EXCEPTIONS :-

- If the method is not available, imperative statement-1 will be executed

- When the method has completed, imperative statement-2 2ill be executed.

---------------------------------------------------------------------

That's what the sub-committee (OOCTG) dreamed-up before the main J4 
Committee got their sticky hands on the topic.

While Ray's book makes several references to CONFORMANCE and checking, 
there are no entries for REPOSITORY, which obviously was added by J4 
sometime before Fujitsu produced their first OO compiler. REPOSITORY is 
only effective in Net Express from Version 4.0 onwards. Given 
Conformance and Repository, it's fairly apparent why the 'EXCEPTIONS' do 
not form part of the 2002 INVOKE syntax.

As written above, like Richard described for the COMPUTE, include those 
conditionals for ON EXCEPTION/NOT ON EXCEPTION then the END-INVOKE made 
sense. Above of course is different from the final COBOL 2002 INVOKE 
syntax; while the END-INVOKE is now superfluous, you can see the train 
of thought where the SCOPE TERMINATOR was retained.

Jimmy
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T00:43:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54t5b5F1qp4f3U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <0gfgu21l03oju3j42p1uonjjfcge9tsloj@4ax.com> <54rj9eF222pjiU1@mid.individual.net> <L13Gh.1197020$5R2.586039@pd7urf3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:L13Gh.1197020$5R2.586039@pd7urf3no...
> Pete Dashwood wrote:
>> "Howard Brazee" <howard@brazee.net> wrote in message
…[11 more quoted lines elided]…
> END-INVOKE

Sorry Jimmy, you lose...

I ALWAYS write END-INVOKE or END-CALL, (and have done for years now.)

Got into the habit when using CALL in the Microfocus development for the 
Channel Tunnel ticketing (TRIBUTE project)(it was that long ago :-))...long 
before OO, and also coded the ON EXCEPTION clause because, in those days we 
frequently ran out of memory when trying to call dynamic routines.)

It has nothing to do with the electric wet dreams of J4 or MF or any other 
"Authority"; it has to do with making my code readable and clear, and 
preparing it for possible future expansion.

See my response to Bill.

>
> Now if I go back to the original INVOKE syntax, listed in Ray Obin's 1993 
> M/F paperback :-
>

Aw, sorry, my copy seems to be missing... I'm hopeless when it comes to 
hanging onto really important documents... :-)


> ---------------------------------------------------------------------
>        INVOKE object-identifier-3  {identifier-1 }
…[25 more quoted lines elided]…
>

Ok...


> As written above, like Richard described for the COMPUTE, include those 
> conditionals for ON EXCEPTION/NOT ON EXCEPTION then the END-INVOKE made 
…[3 more quoted lines elided]…
>
No, I can't... and I really don't care... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-04T02:24:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:54p7lrF21d53dU1@mid.individual.net...
>
> "Howard Brazee" <howard@brazee.net> wrote in message 
…[41 more quoted lines elided]…
>

There are many ways to write a nested IF statement. Here is one style I have 
seen (with the ending left unfinished):

IF
    stmts
ELSE IF
    stmts
ELSE IF
    stmts
ELSE IF
    stmts
ELSE IF
    stmts

How would you choose to end something like this?

1. You could just put a period at the end of the last statement in the last 
ELSE IF.

2. You could code END-IF with a period.

3. You could code an END-IF for each IF all on one line, with or without a 
period after the last one. The more IFs the more chance of getting it wrong 
and the harder it will be to read.  Of course the IBM mainframe compiler 
shows you a nesting level number to aid in this type of thing.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-03T19:42:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com>`
- **In-Reply-To:** `<i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> There are many ways to write a nested IF statement. Here is one style I have 
> seen (with the ending left unfinished):
…[12 more quoted lines elided]…
> How would you choose to end something like this?

I would end it with "END-EVALUATE" - because I would convert the 
structure to "EVALUATE TRUE", and each of the nested IFs would become 
WHENs.  :)  (Is that cheating?)

> 1. You could just put a period at the end of the last statement in the last 
> ELSE IF.
…[6 more quoted lines elided]…
> shows you a nesting level number to aid in this type of thing.

If I wasn't allowed to change the structure, I'd probably go with #2. 
It matches the if...elseif...elseif...endif structure of some other 
languages.  Plus, with them not indented, it would be (to me) the most 
obvious ending delimiter to a structure like that.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T17:47:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54v1auF221i6sU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com...
> Charles Hottel wrote:
>> There are many ways to write a nested IF statement. Here is one style I 
…[18 more quoted lines elided]…
>

No, it isn't cheating, it is sound good sense. (I read your post after 
posting mine on the same subject...:-))

>> 1. You could just put a period at the end of the last statement in the 
>> last ELSE IF.
…[12 more quoted lines elided]…
>

Not me. I'd rewrite the whole construct to use EVALUATE.

If they kicked up about that or said it was banned by S & P, I'd have a 
programmers workshop and get the standards changed. :-)

If it was a really urgent fix I'd ask them to decide whether their 
restrictive standard and continuing bad coding practice were more important 
than getting it done.  I'd demonstrate that it worked perfectly with the 
EVALUATE in place (fait accompli is often a powerful persuader... :-)).

If that battle was lost, I'd ask them to get someone else to change it, as I 
really feel very strongly about writing crap code.

If they insisted that I do it, and do it the way they wanted, (on the basis 
that they are paying me and I have accepted the contract) I'd use option 3 
without a period at the end, and I'd add a disclaiming note to the code 
stating it was done under extreme duress and denying all responsibility for 
it. I'd also immediately terminate the contract on the grounds that I was 
completely unsuited for working on their site, and it was therefore in the 
interest of all concerned for me to move on.

But if it came to that point, I wouldn't be working there anyway... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-04T13:40:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p%zGh.9073$tD2.6493@newsread1.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com...
> Charles Hottel wrote:
>> There are many ways to write a nested IF statement. Here is one style I 
…[17 more quoted lines elided]…
> (Is that cheating?)

 <snip>

Unfortunately this kind of rewiriting is considered wasted effort by 
management where I work and it is "discouraged".
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T03:25:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<550365F22doa8U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <WqmdnbQDAZfHr3fYnZ2dnUVZ_tfinZ2d@comcast.com> <p%zGh.9073$tD2.6493@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:p%zGh.9073$tD2.6493@newsread1.news.pas.earthlink.net...
>
> "LX-i" <lxi0007@netscape.net> wrote in message 
…[26 more quoted lines elided]…
>
Maybe time to educate the Management... :-)

It is no more effort to replace the structure with EVALUATE than it is to 
put full stops and scope delimiters into it.

It WOULD be wasted effort if the thing didn't need maintaining, but it does.

Perhaps the Management need to understand that "discouraging" better 
practices does not improve morale (read "productivity") and, in very 
practical terms, actually means the cost of maintaining code is increased.

Management who stamp on enthusiasm and encourage bad practice actually 
deserve everything they get...

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T17:25:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54v01nF22mrarU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[73 more quoted lines elided]…
>

I simply wouldn't  use that construct.

For me that is NOT a "pure" nested IF (and those are the only kind I 
use...); it doesn't represent a decision tree with conditions nested in the 
TRUE branches. I discussed this elsewhere in CLC fairly recently...(December 
20th, 1999...7 years is nothing to an old codger like me :-))

http://groups.google.com/group/comp.lang.cobol/browse_frm/thread/6a7ab60484d1f8c8/9330087ea14ea382?lnk=gst&q=nested+IF&rnum=1&hl=en#9330087ea14ea382

The above (Charlie's example, not my nested IF dissertation...) is best 
served by an EVALUATE, with each of the ELSE statements being replaced by 
WHEN.

Leaving the fine points of how to do stuff aside, and coming back to your 
question, this is again a case of letting the format reflect the logic. I 
would structure it as

 IF
    stmts
 ELSE IF
             stmts
           ELSE IF
                      stmts
                     ELSE IF
                                 stmts
                               ELSE IF
                                          stmts
                                         END-IF
                               END-IF
                     END-IF
           END-IF
 END-IF

... with absolutely no sign of a full stop anywhere in the 
neighbourhood...but taking great care to ensure the indentation matched up 
correctly and that the count of END-IFs matches the count of IFs (That's a 
very good idea I picked up from Richard... :-))

This is a perfect example of what Richard was saying about Python... Things 
become clearer when the visual format represents the logical structure.

And I would submit that it bears out my own preference re mixing styles; 
adding periods to the above does nothing to clarify it or make it more 
readable, in fact, it has exactly the opposite effect...

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-03T23:10:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172992248.712776.186760@i80g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<54v01nF22mrarU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net>`

```
On Mar 4, 5:25 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Charles Hottel" <chot...@earthlink.net> wrote in message
>
…[122 more quoted lines elided]…
> readable, in fact, it has exactly the opposite effect...

Well actually Python does not have a case statement and uses elif as
an else if.  The nesting of these does impose a particular indenting,
but it is that of Charles, not that of yours.

    if ( a ):
        do a bits
    elif ( b ):
        do b bits
    ...

Of course you could do:

    if ( a ):
        do a bits
    else:
        if ( b ):
            do b bits

The lack of a case statement id a philosophic decision - in Python
there should only be one way of doing anything.

I don't particularly like EVALUATE TRUE and would do with a series of
IF .. ELSE IF with all the IFs at the same indent, just like Python
requires with a series of elifs.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T23:21:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54vktbF223gu0U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <1172992248.712776.186760@i80g2000cwc.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172992248.712776.186760@i80g2000cwc.googlegroups.com...
> On Mar 4, 5:25 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[153 more quoted lines elided]…
>

I think that's OK... :-) (I can mentally "translate" elif into "case"... 
:-))

> Of course you could do:
>
…[5 more quoted lines elided]…
>

Less keen on that. I think the first option works fine for me.


> The lack of a case statement id a philosophic decision - in Python
> there should only be one way of doing anything.

Sounds a bit Nazi  :-) (but there is efficiency in Dictatorship...)

>
> I don't particularly like EVALUATE TRUE and would do with a series of
> IF .. ELSE IF with all the IFs at the same indent, just like Python
> requires with a series of elifs.

Fair enough.

>
I don't like EVALUATE TRUE either... much prefer to evaluate on something 
that is controlling the logic flow (shades of GO TO...DEPENDING ON :-))

Indentation is definitely a personal preference and I've spent some time 
here recently explaining why I indent the way I do. That is not intended to 
devalue anyone else's way of doing it; rather, people who haven't yet 
decided on the style they will use may find an explanation helpful. I 
remember when I started COBOL and how bewildering the various styles I 
encountered were. Until confidence is gained, it can be a bit intimidating.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-05T12:14:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5538h1F22iggbU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <1172992248.712776.186760@i80g2000cwc.googlegroups.com>`

```
Richard<riplin@Azonic.co.nz> 03/04/07 12:10 AM >>>
>On Mar 4, 5:25 pm, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
>> >> As you may have gathered, I disagree. I think periods were a major
cause
>> >> of error in "old" COBOL and the fewer you have of them, the better.
The
>> >> only requirement now (in the Procedure Division...) seems to be
>> >> immediately preceding a paragraph/section name and I reckon that is
…[4 more quoted lines elided]…
>> >> 1. With some of the old impact printers they didn't render properly
and
>> >> were easily missed. Sure, that is much less of a problem these days
when
>> >> we print listings with laser printers, but I have lingering suspicions
of
>> >> any program listing. Fortunately, I never use COBOL listings these
days
>> >> and haven't for many years... Still, reducing the periods reduces any
>> >> real or imagined risk and makes me feel better :-).
>>
>> >> 2. Using an end-of-statement terminator (full stop) (which is small
and
>> >> easily missed) rather than a scope delimiter (which is easily visible
and
>> >> logically sensible) makes cutting and pasting code much more error
prone.
>>
>> >> 3. Using both scope delimiters and full stops just seems ugly and
>> >> unnecessary to me.
>>
>> >> I think using END-IF is a step in the right direction, but why not
take a
>> >> few more steps and use ALL of the scope delimiters? Before you know
it
>> >> you are thinking in logical scope blocks (just as you would in a
modern
>> >> language), and periods are just an ugly irrelevance in the middle of
your
>> >> code... :-)
>>
>> >> Pete.
>>
>> > There are many ways to write a nested IF statement. Here is one style
I
>> > have seen (with the ending left unfinished):
>>
…[18 more quoted lines elided]…
>> > 3. You could code an END-IF for each IF all on one line, with or
without a
>> > period after the last one. The more IFs the more chance of getting it
>> > wrong and the harder it will be to read.  Of course the IBM mainframe
>> > compiler shows you a nesting level number to aid in this type of
thing.
>>
>> I simply wouldn't  use that construct.
>>
>> For me that is NOT a "pure" nested IF (and those are the only kind I
>> use...); it doesn't represent a decision tree with conditions nested in
the
>> TRUE branches. I discussed this elsewhere in CLC fairly
recently...(December
>> 20th, 1999...7 years is nothing to an old codger like me :-))
>>
…[3 more quoted lines elided]…
>> served by an EVALUATE, with each of the ELSE statements being replaced
by
>> WHEN.
>>
>> Leaving the fine points of how to do stuff aside, and coming back to
your
>> question, this is again a case of letting the format reflect the logic.
I
>> would structure it as
>>
…[17 more quoted lines elided]…
>> neighbourhood...but taking great care to ensure the indentation matched
up
>> correctly and that the count of END-IFs matches the count of IFs (That's
a
>> very good idea I picked up from Richard... :-))
>>
>> This is a perfect example of what Richard was saying about Python...
Things
>> become clearer when the visual format represents the logical structure.
>>
…[27 more quoted lines elided]…
>requires with a series of elifs.

I think one big difference here is that COBOL does not actually have an ELIF
or ELSIF or ELSEIF clause to its IF statement.  If it did you may indeed
see

IF ...
    stmts
ELSEIF
   stmts
ELSEIF
   stmts
ELSE
   stmts
END-IF

But there is no such thing.  Probably because EVALUATE TRUE can be used in
its stead.

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-05T13:29:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bvou25pka3fmiuuqtrr0313n26ifmjrj7@4ax.com>`
- **References:** `<1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <1172992248.712776.186760@i80g2000cwc.googlegroups.com> <5538h1F22iggbU1@mid.individual.net>`

```
On Mon, 5 Mar 2007 12:14:40 -0700, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>I think one big difference here is that COBOL does not actually have an ELIF
>or ELSIF or ELSEIF clause to its IF statement.  If it did you may indeed
…[13 more quoted lines elided]…
>its stead.

Except for a long time ELSE IF was available and EVALUATE TRUE wasn't.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-06T10:11:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<555llaF238ngjU1@mid.individual.net>`
- **References:** `<1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <1172992248.712776.186760@i80g2000cwc.googlegroups.com> <5538h1F22iggbU1@mid.individual.net> <9bvou25pka3fmiuuqtrr0313n26ifmjrj7@4ax.com>`

```
Howard Brazee<howard@brazee.net> 03/05/07 1:29 PM >>>
>On Mon, 5 Mar 2007 12:14:40 -0700, "Frank Swarbrick"
><Frank.Swarbrick@efirstbank.com> wrote:
>
>>I think one big difference here is that COBOL does not actually have an
ELIF
>>or ELSIF or ELSEIF clause to its IF statement.  If it did you may indeed
>>see
…[11 more quoted lines elided]…
>>But there is no such thing.  Probably because EVALUATE TRUE can be used
in
>>its stead.
>
>Except for a long time ELSE IF was available and EVALUATE TRUE wasn't.

True.  But then neither was END-IF for the same period, so certainly the
best (only?) option was:

IF ...
  stmts
ELSE IF ...
  stmts
ELSE IF ...
  stmts
ELSE
  stmts.

Or the similar
IF ...
  stmts
ELSE 
IF ...
  stmts
ELSE 
IF ...
  stmts
ELSE
  stmts.

I'm not fond of them, but they were probably the best option pre-COBOL '85. 
What I don't like is either of the following:

IF ...
  stmts
ELSE IF ...
  stmts
ELSE IF ...
  stmts
ELSE
  stmts
END-IF
END-IF
END-IF

or

IF ...
  stmts
ELSE IF ...
  stmts
ELSE IF ...
  stmts
ELSE
  stmts
END-IF.


I'm sort of OK with this:
IF ...
    stmts
ELSE 
    IF ...
        stmts
    ELSE 
        IF ...
            stmts
        ELSE
            stmts
        END-IF
    END-IF
END-IF

But one tends to run out of room, plus it's hard to tell what 'level' things
are at, especially when there are other conditionals within 'stmts'.

YMMV, as usual.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-04T13:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:54v01nF22mrarU1@mid.individual.net...
>

<snip>

> I simply wouldn't  use that construct.
>
…[7 more quoted lines elided]…
>

<snip>

Well I admit I have not seen it used often in COBOL programs, But it is a 
style I have seen suggested in several books on programming in C.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T03:44:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5504b1F2358jsU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[20 more quoted lines elided]…
>

So if the words for   "out", "outer or otherwise", "by means of", "with", 
"since", "after or in the style of" and "up to"  (aus, ausser, bei, mit, 
nach,  seit, von, and zu) all take the Dative case in German, does that mean 
that they should in English :-)?

Learning other languages is, on the whole, a good thing, but let's not lose 
sight of the case in point... COBOL.

Sometimes (until much later when the finer points are grasped) something can 
seem like something we already know and understand, when in fact, it isn't.

It isn't ITSA, it's ITSLIKE... similar, but not the same, and very often the 
subtle differences are VERY important. C has such a construct probably 
because many people coming to C will expect it, and CASE and SWITCH type 
constructs can be intimidating to people who haven't encountered them 
before; Python has it, as Richard described, because there is no other 
alternative. None of these are good reasons for using it in COBOL which DOES 
have much better alternatives.

The person who writes a book on C might write a quite different book if 
describing COBOL. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-04T10:02:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ulnuqqc58tmc3@corp.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5504b1F2358jsU1@mid.individual.net...
[snip]
> The person who writes a book on C might write a quite different book if
> describing COBOL. :-)

"How to Convert COBOL to C" by Ob Fuscater?
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T10:08:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<550qr0F22n23sU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net> <12ulnuqqc58tmc3@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12ulnuqqc58tmc3@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[7 more quoted lines elided]…
>
Yeah, that's the guy... :-)

He also collaborated on "The Dark Passage" with Hugo First, and "Relational 
Database Migration" with Cantgetta Date.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-04T21:13:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qEGGh.9119$Jl.1466@newsread3.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net> <12ulnuqqc58tmc3@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12ulnuqqc58tmc3@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[8 more quoted lines elided]…
>

How about: "The C Programming Language" 2nd edition page 57 by Brian W. 
Kernighan and Dennis M. Ritchie.

"This construction  ... occurs so often that it is worth a brief separate 
discussion. This sequence of if statements is the most general way of 
writing a multi-way decision. ...".

Now I am not arguing by referencing authority, but these guys have a certain 
reputation and I think it is at least worth listening to what they say.  I 
am not saying they are always right. As Pete said what works in C may not be 
best in COBOL.  I happen to think that COBOL IF statments are superior to C 
as you get the effect of block statements without having to explicitly point 
out the block to the compiler with special delimiters and when you do want 
to use a delimeter  you only need and ending one.  Also COBOL EVALUATE is 
superior to the C case statement. So if I have acces to a better tool then I 
would and should use it, but if I don't,  I use what I have without pissing 
and moaning first about not having the tool I want. And even if the superior 
tool is available I may run into code that does not use it, and I may well 
have to deal with that without rewriting it.

It is not a perfect world., if it were by now the 2002 COBOL standard would 
be more than just a bunch of words on paper .
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-04T21:13:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pEGGh.9118$Jl.1588@newsread3.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5504b1F2358jsU1@mid.individual.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[49 more quoted lines elided]…
>

Well, I am not advocating for or against this style.  I understand your 
position against it, but I personally am ambivalent. I believe it is my best 
interest be flexible because on the whole computers and programming 
languages can be mighty inflexible at times. I am prepared to accept those 
coding practices that I inevitably run into, as long as I can understand 
them well enough and quickly enough, to deal with them and do my job without 
a great increase in the normal amount of errors. I think this is a pragmatic 
approach developed from having to do a lot of maintainence programming.  I 
have no control over what the next assignment may look like, so being 
flexible and familiar with as many coding styles as possible is beneficial. 
On the other hand if I think I have the time I will rewrite code to make it 
better i.e. more readable. By code I mean short stretches and not entire 
programs. I believe I have posted sample code here in the past of IF 
statements that I have disapproved of and usually they run on and on for 
many pages.  I object to them because they are  too complex and take too 
much time to understand, however to date I have managed to deal with such 
well enough to maintain steady employment. I realize that is probably not as 
important to you as it is to me.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T11:23:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<550v64F22nonpU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net> <pEGGh.9118$Jl.1588@newsread3.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:pEGGh.9118$Jl.1588@newsread3.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[71 more quoted lines elided]…
> I realize that is probably not as important to you as it is to me.
On the contrary, Charles, it is very important to me that COBOL guys should 
have employment and I've been trying to assist that here for years. (Even if 
it means advising them to expand their skill sets and look at other 
languages...)  I think what you outlined above is eminently fair and 
reasonable and I would endorse it.

My discussion was never meant to imply that I CAN'T maintain bad code (I 
have done on countless occasions); it was meant to underline that we should 
NOT do so passively. Rolling over to it (for whatever reasons) simply 
perpetuates it.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2007-03-04T14:34:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173047669.972944.149080@c51g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<5504b1F2358jsU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <54v01nF22mrarU1@mid.individual.net> <R2AGh.9074$tD2.4723@newsread1.news.pas.earthlink.net> <5504b1F2358jsU1@mid.individual.net>`

```
On Mar 4, 2:44 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Charles Hottel" <chot...@earthlink.net> wrote in message
>
…[48 more quoted lines elided]…
> Pete.


Without replying to your points specifically, I suspect that some
people can write reasonable readable code in almost any style and some
can't or won't.  I would also say that C was developed before 1971
when I think it was first published and "structured programming"
concepts weren't as well developed, it was also reputed to have a
compiler that used no more than 5K of storage and that many of the
compiled progrmas were of a similar size or smaller, it could also be
used on a wide variety of platforms, which I am sure you and many
others already know.  Several other languages also have similarly
ancient roots.

Robert
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-04T07:52:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esdtra$fb0$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`

```
In article <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>,
Charles Hottel <chottel@earthlink.net> wrote:

[snip]

>There are many ways to write a nested IF statement. Here is one style I have 
>seen (with the ending left unfinished):
…[12 more quoted lines elided]…
>How would you choose to end something like this?

I cannot speak for Mr Dashwood, of course... but based on previous 
experiences I would, most likely, terminate such a structure in a manner 
similar to the one used most frequently at the client's site.

'It might look ugly to *you*, sure, but *we're* used to ugly around here.'

DD
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-04T23:59:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54vn4eF22qc81U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esdtra$fb0$1@reader2.panix.com...
> In article <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>,
> Charles Hottel <chottel@earthlink.net> wrote:
…[27 more quoted lines elided]…
>

Yes, we've discussed this one before.

There is a definite case for:

"They are paying me to do what they ask, so I'll do what they ask."

While I accept it is commercially ethical, to me,  it smacks of a Nuremburg 
defence... Should we follow orders even when we know that the orders are 
stupid or at least based on lack of understanding or "We've always done it 
that way"?

I think my reservation about this arises when they ask me to do something 
which I REALLY wouldn't do. It is one thing being a cyber whore and taking 
money for services, but even whores have limits... For me, (and I accept 
this isn't true for everybody, and I don't think the people it isn't true 
for are "wrong") there is a point where it becomes: "No, sorry, I won't do 
that..." or, OK, but if you want me to do that, I charge extra..." :-)

There is middle ground here, where you can make a case and explain why you 
object, and suggest an alternative that would be better. As they are 
employing you as a "consultant" you have a perfect right to offer them 
advice, in fact, it can be argued that you are morally bound to do so. They 
are buying your expertise; give them some benefit from it other than just 
complying with bad practice.

In the final analysis this will come down to individual personalities, 
backgrounds, environments,  and attitudes and there isn't necessarily a 
"right" or "wrong" approach.

Throughout my programming career (around 25 years of a career that is 
currently in its 42nd year) I have always done my best to change minds where 
there was a chance of improving things, and simply moved on when there 
wasn't. Some sites value this, some sites don't. I think it is not good for 
the growth of a contractor to stay too long in one place. It is easy to get 
into a comfortable rut and just keep on taking the money... Moving exposes 
you to new ideas, new platforms, new ways of doing things and different 
attitudes. All of this is good for growth.

These days, I get paid to have opinions and manage others who are grappling 
with the things I grappled with years ago (the platforms may be different 
but the problems of software development don't change much...). It is fun 
and I like it. I enjoy watching them and myself grow, and I hope I never 
become Doc's "Corner Office Idiot" :-). Invariably, the teams are sorry to 
see me go (although some of the management may breathe a quiet sigh of 
relief :-)) and I am sorry to leave. However, it gives me a chance to take 
some time off and do some of the back-burner projects I set myself (writing 
prose and software for fun and, sometimes, profit... :-)) before I finally 
have to go back to work and get a "real" job.

BOTTOM LINE:

Whether you opt to toe the line and take the money, or challenge what you 
believe is wrong and  (possibly not) take the money, is an individual 
decision that will depend on individual factors and circumstances.  It can 
only be right or wrong for an individual, and not for everyone.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-04T15:06:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esen97$kmm$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <54vn4eF22qc81U1@mid.individual.net>`

```
In article <54vn4eF22qc81U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:esdtra$fb0$1@reader2.panix.com...
…[29 more quoted lines elided]…
>Yes, we've discussed this one before.

Yet Mr Hottel sees a need to revisit it... perhaps something new may be 
learnt from this revisiting.

>
>There is a definite case for:
>
>"They are paying me to do what they ask, so I'll do what they ask."

That is the basis of contractural fulfillment, certainly.

>
>While I accept it is commercially ethical, to me,  it smacks of a Nuremburg 
>defence...

Mr Dashwood, if the arguments you bring forward for structuring a slew of 
IF... ELSE code are so insubstantial that you need to base them in the 
ash-beds of the Auschwitcz crematoria then perhaps you might do well to 
revisit them.

In accordance with Godwin's Law 
http://catb.org/esr/jargon/html/G/Godwins-Law.html) this thread may be 
considered ended... but it might be interesting to see where Mr Dashwood's 
logic takes it.

>Should we follow orders even when we know that the orders are 
>stupid or at least based on lack of understanding or "We've always done it 
>that way"?

No, Mr Dashwood, code should be structured in fashions which are most 
readily apprensible by majority of the maintaining-base of pgrogrammers, 
the 'shop standard', as it were.  No 'Nicht Schuldig!', no 'Befehl is 
Befehl'... you take the King's penny, Mr Dashwood, and you write to the 
King's specs.  Don't like it?  Don't take the job... but if you *do* take 
the job and don't write to the specs then don't be surprised if your work 
doesn't pass Prod review.

[snip]

>There is middle ground here, where you can make a case and explain why you 
>object, and suggest an alternative that would be better. As they are 
…[3 more quoted lines elided]…
>complying with bad practice.

... and when they say 'That's a very pretty argument... but our standards 
are *only* PERFORM... THRU EXIT, every sentence  - and we like 'em *short* 
here! - ends with a period and the precompiler will flag SEARCH as invalid 
syntax' then you decide whether you can deal with this sort of exercise in 
minimalism or whether your delicate, artistic nature is just too... 
*gentle* to survive under such crushing restrictions.

>
>In the final analysis this will come down to individual personalities, 
>backgrounds, environments,  and attitudes and there isn't necessarily a 
>"right" or "wrong" approach.

Of *course* there is a 'right' approach; it has been stated in this forum, 
repeatedly, in the formulation of 'A well-functioning system is one which 
causes the person who has the authority for signing the paychecks related 
to it to smile.'

>Throughout my programming career (around 25 years of a career that is 
>currently in its 42nd year) I have always done my best to change minds where 
>there was a chance of improving things, and simply moved on when there 
>wasn't. Some sites value this, some sites don't.

Hee hee hee... Mr Dashwood, what people say they want and what they 
actually pay for might not be the same thing.  I remember a job that I got 
submitted for, decades on back, at a Major Newspaper that said they were 
offering a three-month contract to help them get over summer vacations.  
My pimp called me with:

P: 'They liked your papers but they didn't like your longevity, you didn't 
get the job.'

M: 'What do they mean?  They're looking for three months, my last contract 
was six, the one before that nine, the one before that another nine... 
what's wrong with the longevity?'

P: 'They say they want someone who shows greater longevity.'

M: '... so they can terminate them after three months?'

P: 'Yep... go figure, it's their nickel.'

M: 'Gotcha... I wonder what the *real* reason was.'

>I think it is not good for 
>the growth of a contractor to stay too long in one place. It is easy to get 
>into a comfortable rut and just keep on taking the money... Moving exposes 
>you to new ideas, new platforms, new ways of doing things and different 
>attitudes. All of this is good for growth.

That's one way to see it, Mr Dashwood... and another way to see it is 
demonstrated in an exchange reported to me by a fellow who used to work in 
a mid-sized, family-run jewelery company:

Executive Vice-President: 'Change is good, new ways are good... anyone 
who's stayed at this joint for more than ten years does so because he just 
can't hack it in the outside world!'

(stunned silence)

Chief of Manufacturing: 'How long have *you* been here, Jimmy?'

EVP: 'Twenty-five years... so I know what I'm talking about!'

DD
```

###### ↳ ↳ ↳ Changeing coding styles was Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-03-04T18:10:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com>`

```
On Sun, 4 Mar 2007 15:06:15 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <54vn4eF22qc81U1@mid.individual.net>,
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[83 more quoted lines elided]…
>*gentle* to survive under such crushing restrictions.

While change of style should not be undertaken frequently or lightly,
when carried to the extreme you have just claimed for one
installation, it becomes a real drag on the company and is the sort of
mentality that makes COBOL less useful in newer situations.  It is an
example of why I claim it is Fortress Management that refuses to
evolve existing tools yet embraces every new fad that has blocked OO
COBOL.  This has been aided and abetted by vendors that are extremely
expensive or in the case of the IBM mainframe have at best only
recently made tools available that even come close to what Pete has
described as being available for C#.  Developing OO code using Endevor
(I can't remember the spelling) and ISPF does not sound straight
forward to me.  The problem is not Fortress COBOL in terms of the
working population.  The problem lies higher up the food chain.  

Yes, I can code to some of the restrictions you mention but do I want
to be at a company that is that brain dead?  Since I am semi-retired,
the money would have to be fantastic or there would have to be other
compensating factors for me to even consider it.
>> rest snipped
```

###### ↳ ↳ ↳ Re: Changeing coding styles was Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T11:14:18+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<550ulrF227nftU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com> <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com>`

```

"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com...
> On Sun, 4 Mar 2007 15:06:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[107 more quoted lines elided]…
>

Obviously, I completely agree. I think that dissent can help these managers 
to understand what is necessary on the shop floor and get that passed on to 
vendors. The same applies to S & P and the use of tools.

There SHOULD be proper tools for COBOL (God knows, it's been around long 
enough) but as long as no-one grizzles, there won't be. (Sadly, it is now 
probably too late; COBOL has lost Management credibility and is unlikely to 
regain it.)

We haven't even considered the effect such management attitude has on morale 
and, consequently, productivity.

> Yes, I can code to some of the restrictions you mention but do I want
> to be at a company that is that brain dead?  Since I am semi-retired,
> the money would have to be fantastic or there would have to be other
> compensating factors for me to even consider it.
>>> rest snipped

Precisely. The important thing is to have a choice.

Pete.
```

###### ↳ ↳ ↳ Re: Changeing coding styles was Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-04T23:03:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esfj7a$d8q$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com> <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com>`

```
In article <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Sun, 4 Mar 2007 15:06:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[30 more quoted lines elided]…
>>>> 'It might look ugly to *you*, sure, but *we're* used to ugly around here.'

[snip]

>The problem is not Fortress COBOL in terms of the
>working population.  The problem lies higher up the food chain.  

*Bingo*, Mr Hottel.  'A fish rots from the head'; what one may be 
attributing to 'Fortress COBOL' may be the fault of nothing more than, 
say, a situation similar to that of the American automobile industry, 
circa 1972, in which Everyone Knew Nobody Wanted No Li'l-Bitty Cars, or 
the Banking Industry in the 3-6-3 days (pay 3% interest on deposits, 
collect 6% interest on loans and be on the golf links at 3:pm), or when 
every newspaper editorial board Knew As Fact that a decent citizen wanted 
a copy of the Daily Muck delivered to his doorstep, right next to the milk 
bottles.

>
>Yes, I can code to some of the restrictions you mention but do I want
>to be at a company that is that brain dead?  Since I am semi-retired,
>the money would have to be fantastic or there would have to be other
>compensating factors for me to even consider it.

In general, Mr Hottel, I find that Work is better than Not... but I recall 
a situation from decades on back when yes, I *needed* the job, I had rent 
to pay and student loans that needed to be attended-to... and the software 
vendor was selling the Corner-Office Idiot I reported to a load of crap, 
their package could not be made to do what they said it could... and 
deadline was slipping and I was getting blamed... and blamed in public.

Only problem is... I addressed the assignment of responsibility as I did 
any other logical difficulty; step up to the whiteboard, fall into Formal 
Logic Mode and show, step by step, where the errors in assumptions were, 
where the shortcomings in product were and what steps I had taken to get 
around them... in short, I demonstrated, in public, that this fellow was 
wrong and that his approach needed to be changed... but at least I was 
gentle about it.

So... they called in my pimp; he listened to what I had to say... glanced 
over the paperwork and said 'Look, I know this vendor, they've done this 
before, their product is crap, you are right and Jones is wrong... and I 
also know that Jones has been with the company for twenty-seven years so 
he can say that the sun rises in the west if he wants to.  Do you want to 
be right or do you want to keep your job?'

My papers were on the streets that afternoon... and I do not blame
'Fortress Cobol' for this, I blame my own seduction by the heroic exploits
of that well-known navigator, Popeye the Sailor-Man who, after receiving
sufficient rebuffs to more reasonable offerings, announces 'That's all I
can stand, I can't stands no more!'... and for youngsters or those who
need a bit of comic escape the results have been called 'amusing' for
decades.

In general... I present my definitions, postulates, common notions and 
propositions as to how I have come to a conclusion.  Sometimes I'll even 
handicap myself a bit - I'm deadly serious about shops where SEARCH gets 
flagged as 'forbidden' by a precompiler and reading PMAPs of ways to get 
around it has, I believe, taught me a thing or three - but after a while 
it is time to hit the old lonesome highway.  Other readers here may have 
been in positions where in the example above Jones gets told 'Do what the 
nice consultant says or start collecting your pension three years 
early'... this has never happened to me... ahhhh, but there's Hope, and it 
is a wonderful world that has new experiences in it!

DD
```

###### ↳ ↳ ↳ Re: Changeing coding styles was Re: Help! GO TO and PERFORM THRU!

_(reply depth: 14)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-03-05T02:20:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I7LGh.9347$tD2.1664@newsread1.news.pas.earthlink.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com> <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com> <esfj7a$d8q$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esfj7a$d8q$1@reader2.panix.com...
> In article <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com>,
> Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
…[101 more quoted lines elided]…
>

Well "decades back"  it was a much different employment situation.  I have 
moved on from jobs that I did not like and sometimes the new one was better 
and sometimes it was not. In the process I have learned the level of poor 
management I can tolerate.
```

###### ↳ ↳ ↳ Re: Changeing coding styles was Re: Help! GO TO and PERFORM THRU!

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-05T06:04:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esgbt6$m0j$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <862mu25a973j9psbv1athkci3j2s7uka9c@4ax.com> <esfj7a$d8q$1@reader2.panix.com> <I7LGh.9347$tD2.1664@newsread1.news.pas.earthlink.net>`

```
In article <I7LGh.9347$tD2.1664@newsread1.news.pas.earthlink.net>,
Charles Hottel <chottel@earthlink.net> wrote:
>
><docdwarf@panix.com> wrote in message news:esfj7a$d8q$1@reader2.panix.com...

[snip]

>> In general, Mr Hottel, I find that Work is better than Not... but I recall
>> a situation from decades on back when yes, I *needed* the job, I had rent
…[39 more quoted lines elided]…
>Well "decades back"  it was a much different employment situation.

That might depend, Mr Hottel, on whom one asks... and there are a few 
folks whom I've met - believe it or not! - who, decades later, still 
*need* the job, have rent to pay and loans that need to be attended-to... 
and Corner-Office Idiots blaming them in public for not being able to make 
software packages do what salesfolk had promised the Corner-Office 
Idiots said packagaes could be made to do.

As the Germans used to say, Mr Mottel: Plus ca change, plus c'est la meme 
chose.

>I have 
>moved on from jobs that I did not like and sometimes the new one was better 
>and sometimes it was not. In the process I have learned the level of poor 
>management I can tolerate. 

Experience can be a wonderful teacher, Mr Hottel... but such rates!

DD
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T11:05:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<550u68F2383p6U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esen97$kmm$1@reader2.panix.com...
> In article <54vn4eF22qc81U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[53 more quoted lines elided]…
> revisit them.

That's a bit harsh, Doc. My discussion has moved on from the IF...ELSE to 
the ethical considerations around contractual obligation. The structuring of 
code has nothing to do with it, and your emotive reference to Auschwitcz is 
unnecessary and inappropriate.

(I expect more from you :-))

>
> In accordance with Godwin's Law
> http://catb.org/esr/jargon/html/G/Godwins-Law.html) this thread may be
> considered ended... but it might be interesting to see where Mr Dashwood's
> logic takes it.

Thank you for your forebearance :-) (I didn't actually mention Hitler or the 
Nazis...)
>
>>Should we follow orders even when we know that the orders are
…[9 more quoted lines elided]…
> doesn't pass Prod review.

(I have NEVER had work NOT pass product review.)

Sometimes, at the time you take the King's shilling, there is 
misrepresentation as to what the King's Service entails. (There are many old 
soldiers who can corrrobate this; actual service was nothing like how it was 
presented at the recruitment office :-))

I have had a number of contracts (certainly, in the days when I was a 
contract programmer) where the actual job was nothing like what was 
presented to me during interview. On one occasion they expected me to do 
Assembler maintenance for the same money they would pay a COBOL programmer, 
on another, a so-called new system development was actually repairing a very 
old existing system, and on yet another occasion I was told there might be 
some PL/1 maintenance required and found that the ONLY language on the site 
was PL/1 :-)

My point is that you can sometimes get into something and find it really 
isn't for you... An agreement is an agreement as long as people agree to it. 
If they don't, then it is necessary to change, renegotiate, or cancel the 
agreement.

(I always advise young contractors to read the contract carefully and DON'T 
agree to things that are restrictive. "Standard contracts" are designed to 
completely shaft the contractor and make you a virtual slave. Some of the 
terms and conditions are SO unfair as to make them laughable.  Like, they 
can terminate you on one month, but you CAN'T terminate the contract, or 
they retain exclusive IP rights to everything you do while employed under 
this contract... Just strike these clauses out. Of course they can own what 
you do for them, but you NEVER relinguish the right to own it too... "unfair 
contracts" is probably worth another thread in itself...)

>
> [snip]
…[15 more quoted lines elided]…
>

Your sarcasm is wasted on me. I don't have a delicate artistic nature which 
is easily crushed, but I do have lines for my own professionalism and there 
are things I won't do, contract or no contract. This is a personal choice 
and I don't advocate that everyone should follow it. My personal integrity 
is important to me and doing the best I can for a client is too. (I realise 
that expressing such things can sound pompous, but that's how it is for me.) 
The ultimate protest is to quit and, fortunately, it very rarely comes to 
that. As I described earlier, there is middle ground and it is possible to 
persuade or make a case. People of goodwill can usually resolve issues; 
autocrats who are not interested in doing this are people who I prefer not 
to work for.

And it isn't "My way or the highway". It is a case of making sure that 
issues are explored so that change is possible. I see that as part of the 
consultant role.

It is also true that as experience, and with it, credibility, are obtained, 
there is more chance of being listened to. I found that on many sites where 
I worked, my opinion was actually sought and valued, so, establishing early 
on that there would be resistance to bad practice actually paid off for all 
concerned. (Renewal of contract was always at a higher rate and on some 
occasions they went to extraordinary lengths to ensure I stayed with them; 
one company paid the rent on my London flat while I went to NZ for 3 months 
at the end of a contract, on the understanding I would return for a year 
with them when I got back... that is quite exceptional for a contractor. The 
point is that there are managers and companies who DO value dissent, 
provided it is presented in an acceptable way and provided alternatives are 
proposed. "Any fool can find fault, but it takes a wise man to find fault 
wisely".

>>
>>In the final analysis this will come down to individual personalities,
…[6 more quoted lines elided]…
> to it to smile.'

Just because you say something over and over does not give it truth or 
validity, Doc, as well you know :-)

Your statement is a personal view just as mine is. Neither is 'right' or 
'wrong' for everyone, they are just possible approaches.

>
>>Throughout my programming career (around 25 years of a career that is
…[6 more quoted lines elided]…
> actually pay for might not be the same thing.

Certainly true. But if you assist them to formulate what they want, you can 
help to ensure that what they get is actually useful.

>I remember a job that I got
> submitted for, decades on back, at a Major Newspaper that said they were
…[17 more quoted lines elided]…
>

Sounds like a lucky escape... :-) Do you think by 'longevity' they could 
possibly mean your age :-)

>>I think it is not good for
>>the growth of a contractor to stay too long in one place. It is easy to 
…[13 more quoted lines elided]…
> (stunned silence)

(I have heard exactly the same words from different executives on different 
continents. And I've also heard the converse that moving too much indicates 
instability... there is truth in both positions, and it depends on the 
specific individual and their circumstances.)
>
> Chief of Manufacturing: 'How long have *you* been here, Jimmy?'
>
> EVP: 'Twenty-five years... so I know what I'm talking about!'

Honesty, especially from senior managers is always refreshing. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-04T23:35:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esfl4m$1u3$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com> <550u68F2383p6U1@mid.individual.net>`

```
In article <550u68F2383p6U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:esen97$kmm$1@reader2.panix.com...
…[56 more quoted lines elided]…
>That's a bit harsh, Doc.

What's harsh, Mr Dashwood... the fact that you Godwin'd yourself or the 
fact that I pointed it out?   Lead with your chin and you might catch 
something unusual.

>My discussion has moved on from the IF...ELSE to 
>the ethical considerations around contractual obligation. The structuring of 
>code has nothing to do with it, and your emotive reference to Auschwitcz is 
>unnecessary and inappropriate.

The structuring of code is the product of time and skill in exchange for 
money in agreement with a predefined contract... and when this was pointed 
out you stated how it reminded you of the Nuremburg Defense.  If you 
expected to be able to invoke that condition, Mr Dashwood, by name and 
*not* drag along the associated horrors of the Third Reich then you might 
want to have a go at referring to a 'Waterloo' and leaving Bonaparte out 
of it.

>
>(I expect more from you :-))

If you expected me to forget my lessons, Mr Dashwood, you've been 
disappointed... but don't worry, I'm sure I'll do it at other times.

>
>>
…[6 more quoted lines elided]…
>Nazis...)

Kind of hard to have a Nuremberg Defense without them, Mr Dashwood.

>>
>>>Should we follow orders even when we know that the orders are
…[11 more quoted lines elided]…
>(I have NEVER had work NOT pass product review.)

Well, if a shop sets standards low enough... sorry, couldn't resist.  I 
have had work turned back, Mr Dashwood, with downcast, apologetic eyes... 
because 'everyone knew that (construct) was not allowed' but I was not 
told because they wanted to see me fail... well, not me, specifically, 
just the manager to whom I was assigned.

(In that situation they made one small mistake... they returned the code 
to me on a Friday at 4:pm.  I was younger in those days and could get a 
*lot* more done before a Tuesday 10:am Status Meeting.)

[snip]

>My point is that you can sometimes get into something and find it really 
>isn't for you... An agreement is an agreement as long as people agree to it. 

Mr Dashwood, that ranks up there on the profundity scale with Batman's 
'Goodness is better than Evil, Robin, because... it's Nicer.'  If some 
people don't agree with a contractual agreement with which they formerly 
agreed then other people may find themselves owning a new company.

>If they don't, then it is necessary to change, renegotiate, or cancel the 
>agreement.

... or sue.

[snip]

>>>They
>>>are buying your expertise; give them some benefit from it other than just
…[10 more quoted lines elided]…
>Your sarcasm is wasted on me.

Not in the least, Mr Dashwood... you recognised it as such, eh?

>I don't have a delicate artistic nature which 
>is easily crushed, but I do have lines for my own professionalism and there 
>are things I won't do, contract or no contract. This is a personal choice 
>and I don't advocate that everyone should follow it.

*Precisely*, Mr Dashwood... but one does not learn one's limits without 
first stretching them a bit.

[snip]

>>>In the final analysis this will come down to individual personalities,
>>>backgrounds, environments,  and attitudes and there isn't necessarily a
…[11 more quoted lines elided]…
>'wrong' for everyone, they are just possible approaches.

... and now this time my sarcasm was lost.  Oh well, doesn't work all the 
time... Mr Dashwood, consider the assertion 'there isn't necessarily a 
'right' or 'wrong' approach' to be on the same logical level as 
''Everything is relative' is *absolutely* true!', a Goedel-stretching 
exercise.

[snip]

>> P: 'They say they want someone who shows greater longevity.'
>>
…[8 more quoted lines elided]…
>possibly mean your age :-)

At the time, Mr Dashwood, the pimp made it very clear that they were 
looking for someone who had been employed on contracts of greater 
duration... so they could take me for an option of three months, 
'possibility of renewal but no rate increase'.

DD
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-05T15:31:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<551doqF22epfvU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esfl4m$1u3$1@reader2.panix.com...
> In article <550u68F2383p6U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
>>>>> [snip]

>>>>
>>>>While I accept it is commercially ethical, to me,  it smacks of a
…[12 more quoted lines elided]…
> something unusual.

Godwin is not universally accepted and, quite frankly, I don't care whether 
something I'm discussing violates Godwin's Law or anyone else's. As I am 
oblivious to this particular consequence, it is hardly "leading with my 
chin"...

>
>>My discussion has moved on from the IF...ELSE to
…[13 more quoted lines elided]…
>

Not at all. The "Nuremburg Defense" is now a generally accepted rhetorical 
device and is NOT necessarily associated with the original War Crime trials, 
although it is named after them.  Everyone who wears a Bikini on the beach 
is not necessarily located at or even thinking about Bikini Atoll.

As for Waterloo, you picked an extremely bad example to support your case. 
Many people who mention a situation that was their downfall use "Waterloo" 
without having any idea who the combatants were,  when the battle occurred, 
or even exactly where Waterloo is located, let alone knowing who the 
opposing commanders were. The term has come to mean a "crushing defeat", 
just as Nuremburg Defence has come to mean "following orders", without any 
direct connection to the eponymous event.
>>
>>(I expect more from you :-))
…[3 more quoted lines elided]…
>
 No doubt ... I look forward to it :-)

>>
>>>
…[11 more quoted lines elided]…
>

No it isn't. See above. Do a search on Nuremberg/Nuremburg and Godwin; I'm 
not the only one who says that reference to a Nuremburg  Defence doesn't 
necessarily constitute a violation of Godwin (not that I care whether it 
does or not...)

However, as this term obviously does have strong emotional connotations for 
some people (not mentioning any names but just follow my eyes... :-)) I 
shall avoid using it in future and replace it with reference to the Milgram 
experiment (which reaches the same conclusion  - "only following orders" is 
NOT a defence - and is much more interesting than a bunch of thugs getting 
their just desserts...)

"Ordinary people, simply doing their jobs, and without any particular 
hostility on their part, can become agents in a terrible destructive 
process. Moreover, even when the destructive effects of their work become 
patently clear, and they are asked to carry out actions incompatible with 
fundamental standards of morality, relatively few people have the resources 
needed to resist authority."

http://en.wikipedia.org/wiki/Milgram_experiment

>>>
>>>>Should we follow orders even when we know that the orders are
…[16 more quoted lines elided]…
> Well, if a shop sets standards low enough... sorry, couldn't resist.

LOL! good one...:-) I like to think I was instrumental in getting the 
standards lowered to a pont where even my code was acceptable :-)

> I
> have had work turned back, Mr Dashwood, with downcast, apologetic eyes...
…[7 more quoted lines elided]…
>
 Ah, happy times... :-)

> [snip]
>
…[5 more quoted lines elided]…
> 'Goodness is better than Evil, Robin, because... it's Nicer.'

Holy Niceness, Doc, you actually watch Batman?!

I take no issue with Batman's profundity (Goodness IS nicer than Evil). That 
you would rank my poor utterings on the same scale is an honour I am 
embarrassed by... :-)


> If some
> people don't agree with a contractual agreement with which they formerly
…[6 more quoted lines elided]…
>

That's the American way, certainly.

Many of us outside the USA (yes, there are people living in Terra 
Incognita... :-)) prefer to try and settle our differences out of court, and 
amicably. (It keeps the lawyers on their toes when there is less work, and 
it means that we are not donating large sums of money unnecessarily, to 
people who really never earn it.)

I think I mentioned somewhere previously that people of goodwill should be 
able to resolve their differences. The acquisition of negotiating skill is 
an important part of growth also.


> [snip]
>
…[19 more quoted lines elided]…
> Not in the least, Mr Dashwood... you recognised it as such, eh?

And I also recognise it as being a weakness... :-) (I won't trot out the old 
chestnut about the "lowest form of wit" because I may want to use sarcasm 
myself sometime... :-))

>
>>I don't have a delicate artistic nature which
…[28 more quoted lines elided]…
> ... and now this time my sarcasm was lost.

(Or maybe I pretended not to see it for the sake of this discussion... we'll 
never know... :-))

Oh well, doesn't work all the
> time... Mr Dashwood, consider the assertion 'there isn't necessarily a
> 'right' or 'wrong' approach' to be on the same logical level as
> ''Everything is relative' is *absolutely* true!', a Goedel-stretching
> exercise.
>

Leave your underwear out of this :-) (nice pun, though...:-))

> [snip]
>
…[16 more quoted lines elided]…
>

Like I said, a lucky escape...

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-05T06:46:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esgebd$57h$1@reader2.panix.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net>`

```
In article <551doqF22epfvU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:esfl4m$1u3$1@reader2.panix.com...
…[34 more quoted lines elided]…
>chin"...

If we limit ourselves to that which is 'universally accepted', Mr 
Dashwood, we might find outselves with scant little to discuss... but 
since you state above that you don't care whether you violate anyone's 
rules then, perhaps, it doesn't matter.  It might take time for the 
concept of 'ignorantia juris non excusat' so I'll do my bit to help speed 
the plow; try http://catb.org/esr/jargon/html/G/Godwins-Law.html ... or 
you might want to check out your own demonstrations regarding the 
consequences of Godwin's Law you might want to check out 
<http://groups.google.com/group/comp.lang.cobol/msg/00e66fc14118cc38?dmode=source>

>
>>
…[17 more quoted lines elided]…
>although it is named after them.

Cite?  According to http://en.wikipedia.org/wiki/Nuremberg_Defense '(t)he 
defense was most famously employed during the Nuremberg Trials, after 
which it is named', from 
http://www.adversity.net/Terms_Definitions/TERMS/Nuremberg_Defense.htm 
'The term "Nuremberg Defense" was originally coined during the Nazi war 
crimes trials at Nuremberg after World War II.  Nazi war criminals who 
were charged with genocide, mass murder, torture and other atrocities used 
the defense "I was only following orders" so frequently that the argument 
became known generically as "The Nuremberg Defense" and 
http://www.urbandictionary.com/define.php?term=Nuremberg+defense holds 
'Used by Nazi Germany's military officers in Nuremberg when they were on 
trial...'

>Everyone who wears a Bikini on the beach 
>is not necessarily located at or even thinking about Bikini Atoll.

There's no need for that, Mr Dashwood; in the case of swinwear it is easy 
to find a source for definition that shows a drift from the originally 
explosive implact that cloth had on the bathing scene and 
http://209.161.33.50/dictionary/bikini agrees with you rather nicely.  
Nowhere have I found a citing which separates the Defense from the horrors 
which made the Trials necessary.

>
>As for Waterloo, you picked an extremely bad example to support your case. 
…[3 more quoted lines elided]…
>opposing commanders were.

Then it should be easy for you to provide cites for these as well, Mr 
Dashwood... I barely know what *I* think, let alone others, but when I 
turn to sources similarly common to the ones I gave above words like 
'Napoleon' and 'defeat' seem to just sort of... be there.


>The term has come to mean a "crushing defeat", 
>just as Nuremburg Defence has come to mean "following orders", without any 
>direct connection to the eponymous event.

Evidence contrary to this assertion has been offered, Mr Dashwood... take 
your time in generating your counterarguments.

[snip]

>>>> In accordance with Godwin's Law
>>>> http://catb.org/esr/jargon/html/G/Godwins-Law.html) this thread may be
…[14 more quoted lines elided]…
>does or not...)

Done and done, Mr Dashwood, and you seem to be the only one.  Cites?

>
>However, as this term obviously does have strong emotional connotations for 
…[13 more quoted lines elided]…
>http://en.wikipedia.org/wiki/Milgram_experiment

The Milgrams!  I was in New Haven when they were being conducted, caused a 
bit of a stir and, I believe, a few jobs... did you know that he designed 
them to test the Nuremberg Defense?  (My favorite response given to a 
participant who wanted to stop 'torturing' was a disembodied, dry voice 
informing 'The conditions of the experiment demand that you continue')

[smip]

>>>> No, Mr Dashwood, code should be structured in fashions which are most
>>>> readily apprensible by majority of the maintaining-base of pgrogrammers,
…[13 more quoted lines elided]…
>standards lowered to a pont where even my code was acceptable :-)

Glad you enjoyed, Mr Dashwood... I believe it was Cicero who asked 'Who is 
it who says we must speak of Truth and not laugh?'

[snip]

>>>My point is that you can sometimes get into something and find it really
>>>isn't for you... An agreement is an agreement as long as people agree to 
…[5 more quoted lines elided]…
>Holy Niceness, Doc, you actually watch Batman?!

Mr Dashwood, my box of miscellaneous trite-n-truisms has had a few odd 
bits tossed into it over the decades from a variety of sources.

>
>I take no issue with Batman's profundity (Goodness IS nicer than Evil). That 
>you would rank my poor utterings on the same scale is an honour I am 
>embarrassed by... :-)

Better that, perhaps, than slipping on Robin's tights... some things *are* 
best left to the young'uns, it seems.

[snip]

>>>>>In the final analysis this will come down to individual personalities,
>>>>>backgrounds, environments,  and attitudes and there isn't necessarily a
…[18 more quoted lines elided]…
>never know... :-))

What is Life without a bit of Uncertainty, aye.

>
>> Oh well, doesn't work all the
…[6 more quoted lines elided]…
>Leave your underwear out of this :-)

Some things left for the younger folks, remember?

> (nice pun, though...:-))

Glad you enjoyed.

DD
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 16)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T08:24:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esggjf$dfo$03$1@news.t-online.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com>`

```
As a complete aside in this thread, I
wonder if it is possible to code Duffs
device using legal Cobol (or maybe
using idiosyncrosies of a particular Cobol compiler)

http://www.lysator.liu.se/c/duffs-device.html

Roger
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-05T11:51:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12uoin9g52rk28e@corp.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:esggjf$dfo$03$1@news.t-online.com...
> As a complete aside in this thread, I
> wonder if it is possible to code Duffs
…[3 more quoted lines elided]…
> http://www.lysator.liu.se/c/duffs-device.html

Yes, it is possible to implement Duff's device in
conforming COBOL by using GO TO for all
transfers of control.

In the following. "p-from" simulates a "pointer to
char" and "p-to" simulates a pointer to the
memory-mapped device. The final call to "p-to"
is not part of Duff's device. The routine may be
adapted to output any one type.

-----
      $set ans85 flag"ans85" flagas"s" nestcall
       identification division.
       program-id. duffstst.
       environment division.
       configuration section.
       special-names.
           symbolic sym-eol is 11.
       data division.
       working-storage section.
       01 cnt binary pic 9(4).
       01 output-text pic x(80).
       procedure division.
       main section.
       begin.
           move 1 to cnt
           string  "a b c d e f g"
                 delimited by size
               into output-text
               with pointer cnt
           subtract 1 from cnt
           call "duffsdev" using cnt output-text
           move 1 to cnt
           string  "abcdefghijklmnpqrstuvwxyz"
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                   "0123456789"
                 delimited by size
               into output-text
               with pointer cnt
           subtract 1 from cnt
           call "duffsdev" using cnt output-text
           stop run.

       identification division.
       program-id. duffsdev is initial.
       data division.
       working-storage section.
       01 terminal-char pic x value sym-eol.
       01 n binary pic 9(4).
       01 case binary pic 9(4).
       01 p-from binary pic 9(4) value 1.
       linkage section.
       01 cnt binary pic 9(4).
       01 txt.
           03 t pic x occurs 1 to 9999 depending on cnt.
       procedure division using cnt txt.
       begin.
           compute n = (cnt + 7) / 8.
           compute case = function mod (cnt 8).
           go to 1 2 3 4 5 6 7 depending on case.
       0.  call "p-to" using t (p-from). add 1 to p-from.
       7.  call "p-to" using t (p-from). add 1 to p-from.
       6.  call "p-to" using t (p-from). add 1 to p-from.
       5.  call "p-to" using t (p-from). add 1 to p-from.
       4.  call "p-to" using t (p-from). add 1 to p-from.
       3.  call "p-to" using t (p-from). add 1 to p-from.
       2.  call "p-to" using t (p-from). add 1 to p-from.
       1.  call "p-to" using t (p-from). add 1 to p-from.
           subtract 1 from n. if n > 0 go to 0.
           call "p-to" using terminal-char.
           exit program.
       end program duffsdev.

       identification division.
       program-id. p-to is common.
       data division.
       linkage section.
       01 c pic x.
       procedure division using c.
       begin.
           if c = sym-eol
               display " "
           else
               display c with no advancing
           end-if
           exit program.
       end program p-to.
       end program duffstst.
-----
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 18)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T18:21:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eshjjj$5kj$01$1@news.t-online.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com>`

```
Well, not quite :-)
That's just normal loop unrolling.

This really was just an info on an interesting aspect of C code.
To do this in Cobol, we would have to
allow an inline perform to span over either paragraphs or
"when" clauses of the evaluate  :-)

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12uoin9g52rk28e@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[99 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 19)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-05T12:59:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12uommhsukcpf17@corp.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com> <eshjjj$5kj$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:eshjjj$5kj$01$1@news.t-online.com...
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
> news:12uoin9g52rk28e@corp.supernews.com...
…[20 more quoted lines elided]…
> "when" clauses of the evaluate  :-)

1. "is it possible to code Duffs (sic) device using
    [conforming] COBOL"

2. "it is possible to implement Duff's device in
    conforming COBOL"

Duff's device is peculiar to C. One may "code" or
"implement" Duff's device in conforming COBOL;
but the result is not Duff's device--only a simulation
of it.

Likewise, a MOVE statement in COBOL when
"code[d]" or "implement[ed]" in C is not a MOVE
statement--only a simulation of it.

I stand by my OCD! <g>
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 20)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T19:31:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eshnmg$ksh$00$1@news.t-online.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com> <eshjjj$5kj$01$1@news.t-online.com> <12uommhsukcpf17@corp.supernews.com>`

```
Yes, indeed, it's quite obvious that you
can not do it in Cobol (or indeed in any other language?) :-)

Just giving the newsgroup readers food for thought :-)

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12uommhsukcpf17@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-06T12:14:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<553mjhF234adsU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com> <eshjjj$5kj$01$1@news.t-online.com> <12uommhsukcpf17@corp.supernews.com> <eshnmg$ksh$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message 
news:eshnmg$ksh$00$1@news.t-online.com...
> Yes, indeed, it's quite obvious that you
> can not do it in Cobol (or indeed in any other language?) :-)
>

Everything I want to do, I can do in COBOL.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 22)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-06T08:12:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j51ru2pmm4s3so9oabldslc5u0arrn0sl0@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com> <eshjjj$5kj$01$1@news.t-online.com> <12uommhsukcpf17@corp.supernews.com> <eshnmg$ksh$00$1@news.t-online.com> <553mjhF234adsU1@mid.individual.net>`

```
On Tue, 6 Mar 2007 12:14:56 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Yes, indeed, it's quite obvious that you
>> can not do it in Cobol (or indeed in any other language?) :-)
>>
>
>Everything I want to do, I can do in COBOL.

But does this satisfy your partner?
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-07T14:45:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<556jqdF22v9srU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <550u68F2383p6U1@mid.individual.net> <esfl4m$1u3$1@reader2.panix.com> <551doqF22epfvU1@mid.individual.net> <esgebd$57h$1@reader2.panix.com> <esggjf$dfo$03$1@news.t-online.com> <12uoin9g52rk28e@corp.supernews.com> <eshjjj$5kj$01$1@news.t-online.com> <12uommhsukcpf17@corp.supernews.com> <eshnmg$ksh$00$1@news.t-online.com> <553mjhF234adsU1@mid.individual.net> <j51ru2pmm4s3so9oabldslc5u0arrn0sl0@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:j51ru2pmm4s3so9oabldslc5u0arrn0sl0@4ax.com...
> On Tue, 6 Mar 2007 12:14:56 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> But does this satisfy your partner?

:-)
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-05T08:39:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3deou2d05ojkpln4o44qjraa6a1ai38lls@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <54vn4eF22qc81U1@mid.individual.net> <esen97$kmm$1@reader2.panix.com>`

```
On Sun, 4 Mar 2007 15:06:15 +0000 (UTC), docdwarf@panix.com () wrote:

>Executive Vice-President: 'Change is good, new ways are good... anyone 
>who's stayed at this joint for more than ten years does so because he just 
…[6 more quoted lines elided]…
>EVP: 'Twenty-five years... so I know what I'm talking about!'

That's Microsoft.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-05T08:36:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r7eou21nb8d1iu9q8hogc7abmhg4pn8tqr@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com>`

```
On Sun, 4 Mar 2007 07:52:10 +0000 (UTC), docdwarf@panix.com () wrote:

>
>'It might look ugly to *you*, sure, but *we're* used to ugly around here.'

New fashions are virtually always ugly - until we get used to them.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-05T18:51:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s5WdnUjv4oCmVHHYnZ2dnUVZ_sninZ2d@comcast.com>`
- **In-Reply-To:** `<r7eou21nb8d1iu9q8hogc7abmhg4pn8tqr@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <esdtra$fb0$1@reader2.panix.com> <r7eou21nb8d1iu9q8hogc7abmhg4pn8tqr@4ax.com>`

```
Howard Brazee wrote:
> On Sun, 4 Mar 2007 07:52:10 +0000 (UTC), docdwarf@panix.com () wrote:
> 
>> 'It might look ugly to *you*, sure, but *we're* used to ugly around here.'
> 
> New fashions are virtually always ugly - until we get used to them.

heh - bell-bottomed code!  :)  I like!  (In fact, I think I *know* some 
code like that...)
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-04T06:46:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ulfsdffu4fkb0@news.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`

```
Charles Hottel wrote:
>>
>
…[14 more quoted lines elided]…
> How would you choose to end something like this?

END-IF(4)?
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-05T10:44:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<553380F236v7tU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net>`

```
Charles Hottel<chottel@earthlink.net> 03/03/07 7:24 PM >>>
>
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[16 more quoted lines elided]…
>> As you may have gathered, I disagree. I think periods were a major cause

>> of error in "old" COBOL and the fewer you have of them, the better. The 
>> only requirement now (in the Procedure Division...) seems to be 
>> immediately preceding a paragraph/section name and I reckon that is
great.
>>
>> Why would I prefer fewer periods (full stops)...?
>>
>> 1. With some of the old impact printers they didn't render properly and 
>> were easily missed. Sure, that is much less of a problem these days when

>> we print listings with laser printers, but I have lingering suspicions of

>> any program listing. Fortunately, I never use COBOL listings these days 
>> and haven't for many years... Still, reducing the periods reduces any
real 
>> or imagined risk and makes me feel better :-).
>>
>> 2. Using an end-of-statement terminator (full stop) (which is small and 
>> easily missed) rather than a scope delimiter (which is easily visible and

>> logically sensible) makes cutting and pasting code much more error
prone.
>>
>> 3. Using both scope delimiters and full stops just seems ugly and 
>> unnecessary to me.
>>
>> I think using END-IF is a step in the right direction, but why not take a

>> few more steps and use ALL of the scope delimiters? Before you know it
you 
>> are thinking in logical scope blocks (just as you would in a modern 
>> language), and periods are just an ugly irrelevance in the middle of your

>> code... :-)
>>
…[3 more quoted lines elided]…
>There are many ways to write a nested IF statement. Here is one style I
have 
>seen (with the ending left unfinished):
>
…[13 more quoted lines elided]…
>1. You could just put a period at the end of the last statement in the last

>ELSE IF.
>
>2. You could code END-IF with a period.
>
>3. You could code an END-IF for each IF all on one line, with or without a

>period after the last one. The more IFs the more chance of getting it wrong

>and the harder it will be to read.  Of course the IBM mainframe compiler 
>shows you a nesting level number to aid in this type of thing.

4. You could use EVALUATE instead.

EVALUATE TRUE
WHEN ...
    stmts
WHEN ...
    stmts
WHEN ...
    stmts
WHEN ...
    stmts
WHEN ...
    stmts
END-EVALUATE

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-06T12:24:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<553n4jF22a2ouU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <553380F236v7tU1@mid.individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:553380F236v7tU1@mid.individual.net...
> Charles Hottel<chottel@earthlink.net> 03/03/07 7:24 PM >>>
>>
…[110 more quoted lines elided]…
>
Gosh! you mean like LX-1 and myself suggested 3 days ago in this thread?

There has been a whole debate sparked by this... We moved from using 
EVALUATE to whether or not you should agree to perpetuate bad practice. You 
really must keep up, Frank... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-05T18:57:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s5WdnUvv4oA_V3HYnZ2dnUVZ_sninZ2d@comcast.com>`
- **In-Reply-To:** `<553n4jF22a2ouU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <553380F236v7tU1@mid.individual.net> <553n4jF22a2ouU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Gosh! you mean like LX-1 and myself suggested 3 days ago in this thread?
> 
> There has been a whole debate sparked by this... We moved from using 
> EVALUATE to whether or not you should agree to perpetuate bad practice. You 
> really must keep up, Frank... :-)

heh - some folks only read from work, Monday thru Friday.  From what I 
can tell, Mr. Brazee and Mr. Swarbrick fall into that classification.  :)
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-06T08:14:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<091ru25hgas1b9paf2nv74jfvthdebm3mf@4ax.com>`
- **References:** `<45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <553380F236v7tU1@mid.individual.net> <553n4jF22a2ouU1@mid.individual.net> <s5WdnUvv4oA_V3HYnZ2dnUVZ_sninZ2d@comcast.com>`

```
On Mon, 05 Mar 2007 18:57:18 -0700, LX-i <lxi0007@netscape.net> wrote:

>heh - some folks only read from work, Monday thru Friday.  From what I 
>can tell, Mr. Brazee and Mr. Swarbrick fall into that classification.  :)

Usually when I am in weekends, I am fixing a problem, and don't have
breaks that fit this newsgroup.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 12)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-06T09:57:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<555ksiF23hnjnU2@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <553380F236v7tU1@mid.individual.net> <553n4jF22a2ouU1@mid.individual.net> <s5WdnUvv4oA_V3HYnZ2dnUVZ_sninZ2d@comcast.com>`

```
>
>
…[5 more quoted lines elided]…
>> EVALUATE to whether or not you should agree to perpetuate bad practice.
You 
>> really must keep up, Frank... :-)
>
>heh - some folks only read from work, Monday thru Friday.  From what I 
>can tell, Mr. Brazee and Mr. Swarbrick fall into that classification.  :)

What he said.
:-)
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-06T09:57:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<555kreF23hnjnU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <d46bu2pmbuh8c7muk07ter4d3o8o0d23bl@4ax.com> <54mgoqF20ch7tU1@mid.individual.net> <qjrdu2172daq1ae22ebqnn7r6uiki905g1@4ax.com> <54p7lrF21d53dU1@mid.individual.net> <i5qGh.6286$PL.2602@newsread4.news.pas.earthlink.net> <553380F236v7tU1@mid.individual.net> <553n4jF22a2ouU1@mid.individual.net>`

```
Pete Dashwood<dashwood@removethis.enternet.co.nz> 03/05/07 4:24 PM >>>
>
>"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
…[23 more quoted lines elided]…
>EVALUATE to whether or not you should agree to perpetuate bad practice. You

>really must keep up, Frank... :-)

Yes, I tend to reply to messages prior to reading other replies.  And I
don't read this group on the weekend.
Ah well.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-02-28T17:53:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GkjFh.2556$M65.85@newssvr21.news.prodigy.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:54k8niF20o965U1@mid.individual.net...
> the mixing of  scope-delimited COBOL with full-stop-terminated COBOL is 
> ugly and confusing..

Amen.

I find the same thing in BASIC.

These mean the same thing...
IF  Condition1 THEN
   DoSomething1
END IF
(called 'block if')

and
IF Condition1 THEN DoSomething1
(called "single-line if")


But you can mix and match and boy, that IS confusing...

IF Condition1 THEN
     IF Condition2 THEN DoSomething2      <<< Executed only when both 
Condition1 and Condition2 are true
     DoSomething1                                   <<< Executed whenever 
condition1 is true regardless of condition2
END IF

Of course in Real Life the distance between "IF Condition1"  and its 
companion END IF is many many lines of source code. Darned near impossible 
to figure out what the logic flow is in that case.

It gets worse when (sadly) the single-line IF includes an EXIT or GOTO 
statement, eg

IF Condition1 THEN
     IF Condition2 THEN DoSomething2: EXIT
     DoSomething1
END IF

BASIC EXIT is similar to COBOL EXIT "structure type" (e.g. PARAGRAPH, 
PERFORM, SECTION)   except 'structure type' is optional; when "structure 
type"  is omitted EXIT exits the current loop structure regardless of its 
type (FOR, DO, IF, TRY, FUNCTION, SUB, SELECT or  WHILE).

I tell others to use block IF or single-line IF - whatever they are comfy 
with - but don't intersperse them like this.

MCM
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-28T11:56:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54m1j1F21mm38U1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net>`

```
Michael Mattias<mmattias@talsystems.com> 02/28/07 10:53 AM >>>
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
>news:54k8niF20o965U1@mid.individual.net...
…[25 more quoted lines elided]…
>END IF

Here's something similar in C (and other C-like languages, I assume):

if (condition1)
{
    if (condition2)
       DoSomething2();
    DoSomething1();
}

I personally don't find that hard to read, though I do understand your
point.


>Of course in Real Life the distance between "IF Condition1"  and its 
>companion END IF is many many lines of source code. Darned near impossible

>to figure out what the logic flow is in that case.
>
…[11 more quoted lines elided]…
>type (FOR, DO, IF, TRY, FUNCTION, SUB, SELECT or  WHILE).

Wow, now that one is, umm, interesting.  :-)

>I tell others to use block IF or single-line IF - whatever they are comfy 
>with - but don't intersperse them like this.

COBOL doesn't really have a 'single line IF' in the same sense as the other
examples.  By that I mean you can't have:

if condition1
    if condition2 perform DoSomething2
    perform DoSomething1
end-if.

(Well, you can have it, but it won't do what you intend!  :-)

Anyway....

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-02-28T20:11:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_llFh.3078$BE2.1819@newssvr27.news.prodigy.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <54m1j1F21mm38U1@mid.individual.net>`

```
"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:54m1j1F21mm38U1@mid.individual.net...

>>BASIC EXIT is similar to COBOL EXIT "structure type" (e.g. PARAGRAPH,
>>PERFORM, SECTION)   except 'structure type' is optional; when "structure
…[3 more quoted lines elided]…
> Wow, now that one is, umm, interesting.  :-)

Yes, the creators and maintainers of BASIC  continue to invent new kinds of 
rope with which the careless, lazy or sloppy may hang themselves!

I've always maintained well-written BASIC looks a lot like well-written 
COBOL, whereas poorly-written BASIC looks like.. well, poorly-written BASIC.

MCM
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-28T11:42:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172691742.535389.36010@z35g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<GkjFh.2556$M65.85@newssvr21.news.prodigy.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net>`

```
On Mar 1, 6:53 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:

> I find the same thing in BASIC.
>
…[10 more quoted lines elided]…
> But you can mix and match and boy, that IS confusing...

In Python the scope of a conditional is entirely controlled by the
indenting. The scope ends when you outdent.  This means the the
compiler follows the same rules that you do with your eyes.

    if ( condition1 ):
        if ( condition2 ):
            action2only
            another actio2
        action1

You must ensure that the editor does not use tab characters, or only
uses tabs otherwise it is impossible to get it to work.

In Python you can't write code that looks confusing.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-28T14:40:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com>`

```
On 28 Feb 2007 11:42:22 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>In Python you can't write code that looks confusing.

I very much doubt that.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-28T19:49:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172720964.193481.153810@k78g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com>`

```
On Mar 1, 10:40 am, Howard Brazee <how...@brazee.net> wrote:
> On 28 Feb 2007 11:42:22 -0800, "Richard" <rip...@Azonic.co.nz> wrote:
>
> >In Python you can't write code that looks confusing.
>
> I very much doubt that.


You can write code that is wrong, but as long as you don't have tab
characters in the file (and my editors will expand tabs and will show
any in the file in colour) then what you see is what you get.  You
won't get confused because the visual structure is not the logic
structure.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 8)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-01T09:05:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<es61g9$s5s$02$1@news.t-online.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com> <1172720964.193481.153810@k78g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> schrieb im Newsbeitrag 
news:1172720964.193481.153810@k78g2000cwa.googlegroups.com...
> On Mar 1, 10:40 am, Howard Brazee <how...@brazee.net> wrote:
>> On 28 Feb 2007 11:42:22 -0800, "Richard" <rip...@Azonic.co.nz> wrote:
…[10 more quoted lines elided]…
> structure.

Untangling that last sentence would mean -
I WILL get confused because the visual structure IS the logic structure.

Hmm.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-01T10:47:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172774822.548078.321990@31g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<es61g9$s5s$02$1@news.t-online.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com> <1172720964.193481.153810@k78g2000cwa.googlegroups.com> <es61g9$s5s$02$1@news.t-online.com>`

```
On Mar 1, 9:05 pm, "Roger While" <s...@sim-basis.de> wrote:
> "Richard" <rip...@Azonic.co.nz> schrieb im Newsbeitragnews:1172720964.193481.153810@k78g2000cwa.googlegroups.com...
>
…[16 more quoted lines elided]…
> Hmm.

But that is because I was using english and not Python to express that
idea. Properly parenthesized it is:

You won't get ( confused because the visual structure is not the logic
structure).
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-02T13:33:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54p9niF20rskjU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com> <1172720964.193481.153810@k78g2000cwa.googlegroups.com> <es61g9$s5s$02$1@news.t-online.com> <1172774822.548078.321990@31g2000cwt.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172774822.548078.321990@31g2000cwt.googlegroups.com...
> On Mar 1, 9:05 pm, "Roger While" <s...@sim-basis.de> wrote:
>> "Richard" <rip...@Azonic.co.nz> schrieb im 
…[25 more quoted lines elided]…
>

I'm not convinced that this is "properly parenthesized"... :-) It still 
contains the extraneous NOT which is causing the problem...
>

Quick Boolean analysis... (condition IMPLIES state)

(visual structure = logical structure) -> NOT confusing
NOT (visual structure = logical stucture)  -> confusing

A -> B'
A' -> B

(You won't get confused ) = B' ...because...(the visual structure is NOT not 
the logic structure). = NOT B' = B

"You won't get confused, because the visual structure is the logical 
structure." (Simplest possible form)

Logically valid alternative, conveying idea of possible risk...

"You won't get confused (as you would if the visual structure was NOT the 
logical structure) because the visual structure IS the logical structure."

Python has visual structure = logical structure
therefore...
Python -> NOT confusing

BTW, I read a couple of articles about Python last night and it looks quite 
exciting. Some American high schools are adopting it because of its 
simplicity and elegance, using it so students can develop useful 
applications for the school and as a "precursor" to learning C++ at 
university.

I intend to get into it as soon as I have the current project finished.

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-01T22:21:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12uf62gr0t9ue4b@corp.supernews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com> <1172720964.193481.153810@k78g2000cwa.googlegroups.com> <es61g9$s5s$02$1@news.t-online.com> <1172774822.548078.321990@31g2000cwt.googlegroups.com> <54p9niF20rskjU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:54p9niF20rskjU1@mid.individual.net...
>
> "Richard" <riplin@Azonic.co.nz> wrote in message
…[3 more quoted lines elided]…
> >>
Newsbeitragnews:1172720964.193481.153810@k78g2000cwa.googlegroups.com...
> >>
> >> > On Mar 1, 10:40 am, Howard Brazee <how...@brazee.net> wrote:
> >> >> On 28 Feb 2007 11:42:22 -0800, "Richard" <rip...@Azonic.co.nz>
wrote:
> >>
> >> >> >In Python you can't write code that looks confusing.
…[10 more quoted lines elided]…
> >> I WILL get confused because the visual structure IS the logic
structure.
> >>
> >> Hmm.
…[20 more quoted lines elided]…
> (You won't get confused ) = B' ...because...(the visual structure is NOT
not
> the logic structure). = NOT B' = B
>
…[10 more quoted lines elided]…
> Python -> NOT confusing

H'm!

A: One will not get confused by the difference between
    the visual and logical structures.

B: One will not get confused by the sameness between
    the visual and logical structures.

A is provably true precisely because there is no difference.

B is not provably true because those used to other
languages may be unaccustomed to the sameness (and
therefore confused by this sameness) in Python.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-01T21:17:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172812651.436086.139340@30g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<54p9niF20rskjU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com> <ultbu2t03k5pplghfbvh7p051lhbp2ni60@4ax.com> <1172720964.193481.153810@k78g2000cwa.googlegroups.com> <es61g9$s5s$02$1@news.t-online.com> <1172774822.548078.321990@31g2000cwt.googlegroups.com> <54p9niF20rskjU1@mid.individual.net>`

```
On Mar 2, 1:33 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Richard" <rip...@Azonic.co.nz> wrote in message
>
…[33 more quoted lines elided]…
> contains the extraneous NOT which is causing the problem...

The not is not a problem.

> Quick Boolean analysis... (condition IMPLIES state)
>
…[10 more quoted lines elided]…
> structure." (Simplest possible form)

If you add a comma then you change the parsing.

The thread was about, and examples were given:

"You will get confused because the visual structure is not the same as
the logical structure".

Python will not do that.  The reverse is made by adding one not:

"You will not get confused ..."

It's english, not a computer language.

> Logically valid alternative, conveying idea of possible risk...
>
…[11 more quoted lines elided]…
> university.

Why bother going to C++ ? (or C# or Java)

Over the years I have looked at replacing Cobol with Pascal, Modula2,
Ada, C++, Java, etc.  None have had sufficient dynamics to replace the
ease with which Cobol modules can be swapped out when using dynamic
loading (call and cancel).

Python works for me. You can drop replacement bits into a running
system.

> I intend to get into it as soon as I have the current project finished.

Good.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-01T12:32:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54mhp7F1v5vveU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net> <1172691742.535389.36010@z35g2000cwz.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172691742.535389.36010@z35g2000cwz.googlegroups.com...
> On Mar 1, 6:53 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>
…[28 more quoted lines elided]…
>

I dunno, maybe it's me, but that example above just looks "unclosed" to my 
somewhat jaundiced eye... :-) I'd like to see a SPECIFIC scope delimiter or 
something to tell me the first condition's range has ended. (I'm guessing it 
is implicit when the next statement is indented to the same level as the 
first "if"? What if there is no further statement (as in the example)... we 
are just left hanging... :-))

Having said that, the idea of using in/out-denting to define natural scope 
is pretty cool.

I'd like to find out more about Python but I just haven't got time at the 
moment.

While I'd like to believe your final statement, I wouldn't mind betting 
there is SOMEONE SOMEWHERE who CAN write code in python that looks 
confusing... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Help! GO TO and PERFORM THRU!

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-01T12:22:22+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54mh5fF20qv7hU1@mid.individual.net>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com> <45e2197b$0$7474$9a6e19ea@news.newshosting.com> <1172482649.993940.291000@v33g2000cwv.googlegroups.com> <54k8niF20o965U1@mid.individual.net> <GkjFh.2556$M65.85@newssvr21.news.prodigy.net>`

```

"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:GkjFh.2556$M65.85@newssvr21.news.prodigy.net...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:54k8niF20o965U1@mid.individual.net...
…[48 more quoted lines elided]…
>
Yes, I found in C# (as in Java) you can follow an IF with a single statement 
or a block. At first I used whatever was most convenient but as I gained 
experience I decided, exactly as you did, to try and be consistent. 
Obviously, the block structure is more flexible and allows things to be 
added easily later, at the cost of typing a couple of braces.

Nowadays, I automatically type a brace on the line following my 
condition...(The C# IDE lets me know if I haven't closed it...)

Mixing styles (in any computer programming language) is usually best 
avoided.

Pete.
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-26T08:33:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6v5u2hb0t7ol17o2pkao0bl7mglnemd0e@4ax.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
With this style, I suspect the primary use of GO TO is as a GO TO
THIS-LOOP-EXIT.   

You may also have them for program exits.

It is possible that you will see GO TO THIS-LOOP-TOP or GO TO
THIS-LOOP-MIDDLE.    If these aren't mandated, you should be able to
avoid writing these.
```

#### ↳ Help! GO TO and PERFORM THRU!

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-26T19:47:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qPGEh.26051$ud2.13807@fe09.news.easynews.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
It has been a while since I posted a summary of "approaches" to the LOOP with 
immediate exist issue - with summary comments on the PHILOSOPHICAL issues with 
"GO TO and PERFORM THRU".

Comments in no particular order.

1) For some (unknown to me) reason, the use of SECTIONS is more common in Europe 
while the use of PARAGRAPHS without SECTIONS is more common in the US.  (This 
may impact the programming style).

2) The '02 Standard introduced "EXIT PERFORM <CYCLE>" syntax which is a good way 
to exit from within an inline loop.  EXIT PARAGRAPH and EXIT SECTION provide 
similar functionality for performed paragraphs and sections.

3) If one is coding in (or maintaining) programs in the "older" pre-85 Standard 
(no scope delimiters or inline performs), a (possibly the most  common in the 
US) way to handle "loops" with immediate "problem" exits was something like.:

 001-MAINLINE.
        PERFORM 100-INITIAL-STUFF THRU 100-IS-EXIT
        PERFORM 200-LOOP THRU 200-LOOP-EXIT
                 UNTIL SOME-CONDITION
        PERFORM 900-FINAL-STUFF THRU 900-FS-EXIT
               .
 ....
200-LOOP.
       PERFORM 800-READ THRU 800-READ-EXIT
       IF NOT-EOF
            IF FIELD-1  GOOD-1
                 IF FIELD-2 GOOD-2
                        IF FIELD....
                                NEXT SENTENCE
                       ELSE
                               PERFORM BAD-FIELD.
                               MOVE "Y' TO SOME-CONDITION-FIELD...
                               GO TO 200-LOOP-EXIT
                 ELSE
                         PERFORM BAD-FIELD-2
                          MOVE "Y' TO SOME-CONDITION-FIELD...
                          GO TO 200-LOOP-EXIT
            ELSE
                      PERFORM BAD-FIELD-1
                       MOVE "Y' TO SOME-CONDITION-FIELD...
                       GO TO 200-LOOP-EXIT
    ELSE
             MOVE "Y" TO SOME-CONDITION-FIELD
    .
    PERFORM  300-PROCESS-REC THRU 300-PROCESS-REC-EXIT
    IF NOTHING-WRONG
           PERFORM 400-SOME-MORE   THRU 400-SM-EXIT
    ELSE
            MOVE "Y' TO SOME-CONDITION-FIELD...
             GO TO 200-LOOP-EXIT
     .
     PERFORM 400-WRITE-GOOD-AUDIT-TRAIL THRU 400-WGAT-EXIT
200-LOOP-EXIT.
       EXIT.
..... AND SO FORTH

Now, there were variations on "naming" standards and whether one did a "read 
first" within the loop or before it with a read at end, but this TYPE of 
structure was VERY common and provided a way to "exit a loop" when there was a 
"problem" or condition that meant one didn't want to perform the rest of the 
routine (loop).  With this "structure" the ONLY allowed "perform thru" was from 
the paragraph to the "exit paragraph" associated with it and NO other paragraphs 
were allowed in the "middle".  The only allowed GO TO was to the "exit 
paragraph" associated with the executing paragraph.     .

4) a medium common variation on this structure (particularly in Europe) was to 
replace


        PERFORM 200-LOOP THRU 200-LOOP-EXIT
                 UNTIL SOME-CONDITION

by

        PERFORM 200-LOOP-SECTION
              UNTIL SOME-CONDITION

and change 200-loop paragraph to a section. There would still be an exit 
(paragraph or section).  If it was an exit paragraph within the 
200-loop-section, then you would NOT need to do a "PERFORM THRU" - but if you 
made it an EXIT SECTION, then the PERFORM would still need to be a "THRU"

5) With the '85 Standard, it was possible (but not always very readable) to 
replace all of the above with nested conditional statements (with their scope 
terminator).   One could use CONTINUE and "switches" to make certain that when a 
"bad situation" occurred, then the logic branch would be either just CONTINUE or 
other minimal code - while the "good branch" contained most of the processing 
logic.

6)  With the '02 Standard, the use of EXIT PERFORM/PARAGRAPH/SECTION would allow 
for a "quick" exist from within any performed logic whenever the "bad" situation 
occurred.  The controversy is/was that this really IS a "hidden" GO TO - but 
that it could NEVER lead to "spaghetti" code with crossing logic paths.  Also 
this feature is not particularly widely implemented.  (It does exist in several 
compilers, but probably NOT most of them)

      ****

Ignoring the controversy on paragraphs and sections (very vocal but never with 
any real resolution), the issue behind all of this is
  - "strict" GO-TO-LESS programming
        vs
  - "semi-" structured coding (with only explicit or implicit GO TO of the 
executing logic block)
        vs
  -  allowing spaghetti code (where GO TO and PERFORM logic paths can cross)

Today, there is GENERAL (not universal) agreement that the latter is a "bad" 
thing to do (and even to allow).  Deciding between the first two approaches is 
an "emotional" issue that never gets resolved based on any "facts" (at least 
that I have ever seen).  Certainly sticking STRICTLY to the first approach 
prevents anyone from EVER falling into the 3rd one.  On the other hand, if one 
has a "strictly enforced" (even software) way of following the 2nd approach, it 
rarely leads to "hard to maintain" code which is the REASON why the 3rd approach 
is viewed (by most) as "bad".
```

#### ↳ Re: Help! GO TO and PERFORM THRU!

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-02-27T21:45:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qOGdnaFdIroJO3nYnZ2dnUVZ8qWhnZ2d@pipex.net>`
- **In-Reply-To:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`
- **References:** `<1172340158.494054.74760@p10g2000cwp.googlegroups.com>`

```
Top Post:

Solving problems in code is an opportunity for elegance & 
simplicity.

These two constructs are inelegant and show lack of 
appreciation of good design.

They're old hat: shabby old hat.

Best avoided unless your job depends on it.

Write code so that some day, perhaps, someone could enjoy 
reading it.

Regards

Michael

Impy wrote:
> Okay, so I have been doing the Cobol thing for a couple of months now,
> Unisys, DMS2, datasets, batch, BOLTS screens, etc. and quite enjoying
…[27 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
