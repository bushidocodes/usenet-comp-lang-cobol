[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HOW TO PROGRAM A CALCULATOR

_19 messages · 13 participants · 1999-04 → 1999-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HOW TO PROGRAM A CALCULATOR

- **From:** jmatiles@yahoo.com (jojo atlies)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
I am a college student in need of help with a program using the cobol
compiler. Below is the output for the program.


                       ***MENU***

                   A. Addition
                   B. Subtraction
                   C. Multiplication
                   D. Division

                  CHOOSE ONE OPERATION:

                  ENTER FIRST NO.:
                  ENTER SECOND NO.:

                  THE ANSWER IS:

After choosing a letter the program must be able to compute after entering
the two nos.
Will appreciate any info. on how to make this program run. Thanx
You could also E-mail me at jmatiles@yahoo.com or at jmatiles@excite.com




   -**** Posted from RemarQ, http://www.remarq.com/?a ****-
 Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370e8cb5.1036780520@news1.ibm.net>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
On Fri, 09 Apr 1999 06:31:00 -0800, jmatiles@yahoo.com (jojo atlies)
wrote:

>I am a college student in need of help with a program using the cobol
>compiler. Below is the output for the program.

Want to really impress the instructor?  Get my book, Sams Teach
Yourself COBOL in 24 Hours and show him how to parse the formula
entered into a program and perform the associated operation.

Be sure to give credit to the book when you show him, and don't make
it the solution to your homework assignment!
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990409125733.04133.00000886@ng-fi1.aol.com>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
perform initialize-para
perform display-menu-para
accept menu-opt
accept first_no
accept second_no
perform validate-para
if true-numbers
    case menu-opt
         when "A"
             compute third_no = first_no +                                     
                                                            second_no
        when "B"
              compute third_no = first_no -                                    
                                                                          
                                                  second_no
        when "C"
             etc
       end-case
        display third_no
else
   display error-msg
end-if
goback


When working with division make sure second_no <> zeroes

TW
```

##### ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<923785876.798481@woody.hotkey.net.au>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3> <19990409125733.04133.00000886@ng-fi1.aol.com>`

```
Doing someone else's homework is not the right thing. It's both wrong to ask
in the first place, and wrong by people that readily supply the programs. We
should encourage people to code, but not to copy.

If anybody is so interested or willing he can do my lawn once a month. (How
willing are you...?).

Regards

Theo Charalambous
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990411003516.02137.00001328@ng-fr1.aol.com>`
- **References:** `<923785876.798481@woody.hotkey.net.au>`

```
and are we who are practiced in the art not support those who will be taking
our place one day...should we not leave behind a legacy of excellance.  People
who do not assist should not frequent this forum, if not but to give
information freely.  And I might point out that I did not code the program for
him rather gave him a map on which to biuld, and is that not how most of were
taught, by the strivings of those who had gone before.

Tell not if you wish, but I am here to learn and encourage others to do the
same, and to pass on what limited knowledge I have to others.

TW
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3710c291@news3.us.ibm.net>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com>`

```
Twymer <twymer@aol.com> wrote in message
news:19990411003516.02137.00001328@ng-fr1.aol.com...
> and are we who are practiced in the art not support those who will be
taking
> our place one day...should we not leave behind a legacy of excellance.
People
> who do not assist should not frequent this forum, if not but to give
> information freely.  And I might point out that I did not code the program
for
> him rather gave him a map on which to biuld, and is that not how most of
were
> taught, by the strivings of those who had gone before.
>
> Tell not if you wish, but I am here to learn and encourage others to do
the
> same, and to pass on what limited knowledge I have to others.


excellent post.
The best way to learn to write good programs is to READ well-written
programs.
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eA5Q2.723$lq5.63885@dfiatx1-snr1>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net>`

```
No, the best way to learn to write good programs is to be called upon to
maintain your own poorly-written programs!

MCM

Leif Svalgaard wrote in message <3710c291@news3.us.ibm.net>...
>The best way to learn to write good programs is to READ well-written
>programs.
>
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3711002c@news3.us.ibm.net>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net> <eA5Q2.723$lq5.63885@dfiatx1-snr1>`

```
That may be a great motivator, but it is doubtful how much better
you will do if you were lousy before.

Michael Mattias <michael.mattias@gte.net> wrote in message
news:eA5Q2.723$lq5.63885@dfiatx1-snr1...
> No, the best way to learn to write good programs is to be called upon to
> maintain your own poorly-written programs!
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7et4e6$oq1$1@news.cerf.net>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net> <eA5Q2.723$lq5.63885@dfiatx1-snr1>`

```
Michael Mattias wrote in message ...
>No, the best way to learn to write good programs is to be called upon to
>maintain your own poorly-written programs!

Good words!

Cheesle
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 6)_

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3738d5a3.1659558@news1.frb.gov>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net> <eA5Q2.723$lq5.63885@dfiatx1-snr1>`

```
On Sun, 11 Apr 1999 18:10:18 GMT, Michael Mattias wrote:

>No, the best way to learn to write good programs is to be called upon to
>maintain your own poorly-written programs!

...several years later.
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7et4cq$opf$1@news.cerf.net>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net>`

```
>Leif Svalgaard wrote in message <3710c291@news3.us.ibm.net>...
>Twymer <twymer@aol.com> wrote in message
…[6 more quoted lines elided]…
>programs.

Agree, but not to the extend to do someones homework. What kind of evolution
would that bring. If those who are to bring further what we have done knows
nothing but copying existing work, there will be no progress, no capability
of individual work.

Copiers are the simplest of kind, those who are bringing the world forward
they inherit knowledge, evaluates it and bring up new thoughts.

If the idea was to give the student some useful thoughts about how to
accomplish the task, it would have been wiser to give him a code fragment
covering a different topic. Providing a ready to go solution is a poor
solution.

Cheesle
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 6)_

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1999-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371750d6.9849180@usenet.acw.vcu.edu>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com> <3710c291@news3.us.ibm.net> <7et4cq$opf$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.no> wrote:

>Agree, but not to the extend to do someones homework. What kind of evolution
>would that bring. If those who are to bring further what we have done knows
…[11 more quoted lines elided]…
>Cheesle

I lurk all the time in comp.lang.cobol.  The rule of thumb in
assisting a "homework" sounding question is for the poster explain
what he/she knows already and post a small code sample showing that
explaination and the problem.  At least the poster is showing he/she
is trying to learn the material but just got "stuck."  

We all had "brain drains" every now and again and need a new angle to
the material.  If the "student" can't even begin on the problem, give
a brief description of how we professionals would approach it then ask
the "student" to provide a sample code showing how far he/she took the
advice.  Then focus on the solving the immediate situation to help
"unstuck" the student.  A kind word now and again goes a long way.

Just my two cents worth adjusted for inflation,

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

_(reply depth: 4)_

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<924089654.864433@woody.hotkey.net.au>`
- **References:** `<923785876.798481@woody.hotkey.net.au> <19990411003516.02137.00001328@ng-fr1.aol.com>`

```
Point well taken. I concur that your intentions are for "bettering" our
language

Regards

Theo
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370E396A.7C8322CB@NOSPAMhome.com>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
You will find people willing to help you.  But you haven't yet asked for
help.  Do you have code which you can't compile?  If so, tell us what
compiler you're using.  If you haven't any code, and expect us to do
your homework for you, you won't have any sympathy from us.  If you have
errors you can't understand, post the relevant code and error messages
and you should find us helpful.

jojo atlies wrote:
> 
> I am a college student in need of help with a program using the cobol
…[28 more quoted lines elided]…
>  Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7elmql$kr$1@news.igs.net>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
Actually, few students go to the effort of typing in the full assignment
before asking us to do their homework for them.  You are to be commended,
but probably not helped until you at least make an effort.  Then, if you
write the program and cannot get it work, type *that* in.  You will get lots
of help.

jojo atlies wrote in message ...
>I am a college student in need of help with a program using the cobol
>compiler. Below is the output for the program.
…[25 more quoted lines elided]…
> Search and Read Usenet Discussions in your Browser - FREE -
```

##### ↳ ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370E6041.2D153118@NOSPAMhome.com>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3> <7elmql$kr$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Actually, few students go to the effort of typing in the full assignment
…[3 more quoted lines elided]…
> of help.

You have a way with words!
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370effa8@news3.us.ibm.net>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
http://www.etk.com then download then etkpak.
Look at the CALCPK routine to see how to compute an arbitrary expression.

jojo atlies <jmatiles@yahoo.com> wrote in message
news:c5pP2.16176$LX.6103782@WReNphoon3...
> I am a college student in need of help with a program using the cobol
> compiler. Below is the output for the program.
…[25 more quoted lines elided]…
>  Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XVMP2.7091$w6.1893795@news4.mia>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
jojo atlies wrote:
>I am a college student in need of help with a program using the cobol
>compiler. Below is the output for the program.

It may be overkill for your needs, and it isn't in COBOL, but you can
download a full-fledged very high precision calculator program from my
web page below.  Download BIGCALC.ZIP, about 10,000 lines of commented
C.
```

#### ↳ Re: HOW TO PROGRAM A CALCULATOR

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37100364.615F@sprynet.com>`
- **References:** `<c5pP2.16176$LX.6103782@WReNphoon3>`

```
jojo atlies wrote:
> 
> I am a college student in need of help with a program using the cobol
…[23 more quoted lines elided]…
> Will appreciate any info. on how to make this program run. Thanx

Gosh, I wrote a program just like this in seventh grade.  In BASIC.  On a
TRS-80 Model III.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
