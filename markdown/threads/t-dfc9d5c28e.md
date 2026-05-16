[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What statement is executed next?

_29 messages · 14 participants · 2003-05_

---

### What statement is executed next?

- **From:** setar@mindspring.com (STR)
- **Date:** 2003-05-02T11:15:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8623d3bf.0305021015.559061f7@posting.google.com>`

```
A beginner's question.  

Given the following code, what statement is executed after the GO TO
400-EXIT Statement in the 400-END paragraph?  Does control return to
the 400-END paragraph to execute the next statement or since the exit
statement is reached does the control return to the next statement of
the 200-TEST paragraph?

Thanks in advance.
----------------------------------------

200-TEST
02168
02169             PERFORM 400-HISTORY THRU 400-EXIT.
02170             MOVE RAS-TEST TO STR-TEST.

400-HISTORY.
02168
02169              MOVE ZEROS TO STR-KEY.
02170              MOVE RAS-MEMBER TO STR-MEMBER.
02171              IF KJ-YR NOT NUMERIC MOVE ZEROS TO KJ-YR.
02176              IF ARJFILE-STATUS NOT EQUAL "00"
02177                  DISPLAY "BAD START ARJFILE, STATUS= "
ARJFILE-STATUS
02178                           UPON CONSOLE
02179                  GO TO 400-END.

400-END.
02332              GO TO 400-EXIT.
02333
02334
02335              IF KJ-TOTAL-PGS (SUB) NOT = ZEROS
02336                    MOVE KJ-TOTAL-PGS (SUB)         TO
DETAIL4-PGS.
02340              COMPUTE KJ-TRANS (SUBH) =
02341                  KJ-USED (SUBH) + KJ-OTHER (SUBH)
02343              IF KJ-TOTAL-TRANS (SUBH)  NOT = ZEROS
02344                    MOVE KJ-TOTAL-TRANS (SUBH)           TO
DETAIL4-TRANS.

400-EXIT.
02403              EXIT.
```

#### ↳ Re: What statement is executed next?

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-02T11:57:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8uf3k$nf3$1@si05.rsvl.unisys.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com>`

```
I think this is a trick homework question.  "EXIT" is indeed a statement,
but it "serves only to enable the user to assign a procedure-name to a given
point in the program."  Thus, the next *executable statement* that is
executed at the completion of GO TO 400-EXIT is, in my view, MOVE RAS-TEST
TO STR-TEST.

If the teacher is trying to confuse you by implying 'When you do a "GO TO",
where do you land when you "COME BACK"?'  The answer is 'You don't "COME
BACK".  You *never* "COME BACK".  You are lost forever 'neath the streets of
Boston.  "PERFORM" is for coming back.'

    -Chuck Stevens

"STR" <setar@mindspring.com> wrote in message
news:8623d3bf.0305021015.559061f7@posting.google.com...
> A beginner's question.
>
…[39 more quoted lines elided]…
> 02403              EXIT.
```

##### ↳ ↳ Re: What statement is executed next?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T19:21:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8uggd$q37$1@peabody.colorado.edu>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com>`

```

On  2-May-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> I think this is a trick homework question.  "EXIT" is indeed a statement,
> but it "serves only to enable the user to assign a procedure-name to a given
…[7 more quoted lines elided]…
> Boston.  "PERFORM" is for coming back.'

Especially since it is quite possible from looking at the code that after the
perform, the code drops through to that paragraph again.
```

##### ↳ ↳ [OT] 'Neath the streets of Boston

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-02T16:26:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37-dnVzrhOIGfy-jXTWJkQ@giganews.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens"
>
> If the teacher is trying to confuse you by implying 'When you do a "GO
TO",
> where do you land when you "COME BACK"?'  The answer is 'You don't "COME
> BACK".  You *never* "COME BACK".  You are lost forever 'neath the streets
of
> Boston.  "PERFORM" is for coming back.'
>

During the last election, I was telling some of our younger employees about
"Campaign Songs" and mentioned "The MTA." They never heard of it.

So I hie myself down to Borders Music and prowl around looking for it
(urban, folk, etc.). Can't find it.

Finally I screw up my resolve and approach the employee with the least scary
spiked hair (although he did have very many body parts pierced) and asked
where I might find Kingston Trio offerings.

"Cool, man," says he. "Lemme show ya!"

He leads me to the "Classics" section and lays hands on the exact CD I
wanted.

"Classics!" Indeed.

For the children:

Spoken:
These are the times that try men's souls. In the course of our nation's
history, the people of Boston have rallied bravely whenever the rights of
men have been threatened. Today, a new crisis has arisen. The Metropolitan
Transit Authority, better known as the M. T. A., is attempting to levy a
burdensome tax on the population in the form of a subway fare increase.
Citizens, hear me out! This could happen to you!

(Eight bar guitar, banjo introduction)

Well, let me tell you of the story of a man named Charley on a tragic and
fateful day.
He put ten cents in his pocket, kissed his wife and family, went to ride on
the M. T. A.

Chorus:
Well, did he ever return? No, he never returned and his fate is still
unknown.
He may ride forever 'neath the streets of Boston. He's the man who never
returned.

Charlie handed in his dime at the Kendall Square Station and he changed for
Jamaica Plain.
When he got there the conductor told him, "One more nickel." Charlie
couldn't get off of that train.

(Chorus)

Now, all night long Charlie rides through the station, crying, "What will
become of me?!!
How can I afford to see my sister in Chelsea or my cousin in Rocksbury?"

(Chorus)

Charlie's wife goes down to the Sculley Square Station every day at quarter
past two,
And through the open window she hands Charlie a sandwich as the train comes
rumblin' through.

(Chorus)

Now, you citizens of Boston, don't you think it's a scandal how the people
have to pay and pay?
Fight the fare increase! Vote for George O'Brien! Get poor Charlie off the
M. T. A.

(Chorus)
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-02T14:49:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8up5b$ulm$1@si05.rsvl.unisys.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:37-dnVzrhOIGfy-jXTWJkQ@giganews.com...

<lyrics of what I knew as "The Ballad of the MTA">:

I think there are some place-name spelling errors:  Kendel, Roxbury, Scully.
Great job otherwise, though.

As to classics:  Feh.  I'm one of those idiots that thinks Englebert
Humperdinck actually wrote an opera.  And there's a popular melody I know
that, when I hear the chorus, I think "Aura Lee, Aura Lee, ... " instead of
"Love me tender, love me true ...".   Not quite old enough to remember when
"To Anacreon in Heav'n" was popular, though I have heard the melody a time
or two in my day!

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-02T21:05:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8v4k6$h57$1@panix1.panix.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com> <b8up5b$ulm$1@si05.rsvl.unisys.com>`

```
In article <b8up5b$ulm$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
>"JerryMouse" <nospam@bisusa.com> wrote in message
…[10 more quoted lines elided]…
>"Love me tender, love me true ...".

Aura Lee, Ayna Lee... both are perversions, some say!

DD
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T11:46:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b90o84$18a$1@panix1.panix.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com> <b8up5b$ulm$1@si05.rsvl.unisys.com>`

```
In article <b8up5b$ulm$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
>"JerryMouse" <nospam@bisusa.com> wrote in message
…[12 more quoted lines elided]…
>or two in my day!

Matters of perversion aside... you might want to direct a browser towards
http://www.blueridgeinstitute.org/ballads/old97song.html and click on the
'audio clip' link... the strain might be a bit familiar.  It is a 1924
recording using the melody attributed to Henry Clay Work (who also wrote
such favorites as 'My Grandfather's Clock' and 'Marching Through 
Georgia')... more importantly, though, listen to the voice... that 
*voice*, nasally and adenoidal... they don't make 'em like that any more, 
by gum.

DD
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

_(reply depth: 4)_

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2003-05-06T00:47:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gCDta.100623$5f4.16728@twister.nyroc.rr.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com> <b8up5b$ulm$1@si05.rsvl.unisys.com>`

```
I hear the tune of "To Anacreon in Heav'n" often at the start of sporting
events, but, of couse, they've changed the words from the original drinking
song.


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:b8up5b$ulm$1@si05.rsvl.unisys.com...
>
> "JerryMouse" <nospam@bisusa.com> wrote in message
…[4 more quoted lines elided]…
> I think there are some place-name spelling errors:  Kendel, Roxbury,
Scully.
> Great job otherwise, though.
>
> As to classics:  Feh.  I'm one of those idiots that thinks Englebert
> Humperdinck actually wrote an opera.  And there's a popular melody I know
> that, when I hear the chorus, I think "Aura Lee, Aura Lee, ... " instead
of
> "Love me tender, love me true ...".   Not quite old enough to remember
when
> "To Anacreon in Heav'n" was popular, though I have heard the melody a time
> or two in my day!
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-03T11:30:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb2ff9f_2@127.0.0.1>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com>`

```
Thanks Jerry for reproducing the words in full.

I remember the song with affection from my youth and always loved the bit
about his wife handing him a sandwich.

(Yes, even in New Zealand we received this at the time (the Kingston Trio
were very popular here after tthe success of "Tom Dooley", but the political
implications were for the most part lost on us...))

Pete.



"JerryMouse" <nospam@bisusa.com> wrote in message
news:37-dnVzrhOIGfy-jXTWJkQ@giganews.com...
>
> "Chuck Stevens"
…[4 more quoted lines elided]…
> > BACK".  You *never* "COME BACK".  You are lost forever 'neath the
streets
> of
> > Boston.  "PERFORM" is for coming back.'
> >
>
> During the last election, I was telling some of our younger employees
about
> "Campaign Songs" and mentioned "The MTA." They never heard of it.
>
…[3 more quoted lines elided]…
> Finally I screw up my resolve and approach the employee with the least
scary
> spiked hair (although he did have very many body parts pierced) and asked
> where I might find Kingston Trio offerings.
…[22 more quoted lines elided]…
> He put ten cents in his pocket, kissed his wife and family, went to ride
on
> the M. T. A.
>
…[6 more quoted lines elided]…
> Charlie handed in his dime at the Kendall Square Station and he changed
for
> Jamaica Plain.
> When he got there the conductor told him, "One more nickel." Charlie
…[10 more quoted lines elided]…
> Charlie's wife goes down to the Sculley Square Station every day at
quarter
> past two,
> And through the open window she hands Charlie a sandwich as the train
comes
> rumblin' through.
>
…[9 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-03T13:10:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-10C2E4.13104703052003@corp.supernews.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com> <3eb2ff9f_2@127.0.0.1>`

```
In article <3eb2ff9f_2@127.0.0.1>,
 "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> Thanks Jerry for reproducing the words in full.
> 
…[7 more quoted lines elided]…
> Pete.

That's ok.  The political implications were mostly lost on Americans as 
well...
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-03T09:29:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KtPsa.2057$S%.208869@news20.bellglobal.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com>`

```
If you had told me, Jerry, I could have just gone to my old vinyl, and
pulled it out.

Donald

"JerryMouse" <nospam@bisusa.com> wrote in message
news:37-dnVzrhOIGfy-jXTWJkQ@giganews.com...
>
> "Chuck Stevens"
…[4 more quoted lines elided]…
> > BACK".  You *never* "COME BACK".  You are lost forever 'neath the
streets
> of
> > Boston.  "PERFORM" is for coming back.'
> >
>
> During the last election, I was telling some of our younger employees
about
> "Campaign Songs" and mentioned "The MTA." They never heard of it.
>
…[3 more quoted lines elided]…
> Finally I screw up my resolve and approach the employee with the least
scary
> spiked hair (although he did have very many body parts pierced) and asked
> where I might find Kingston Trio offerings.
…[22 more quoted lines elided]…
> He put ten cents in his pocket, kissed his wife and family, went to ride
on
> the M. T. A.
>
…[6 more quoted lines elided]…
> Charlie handed in his dime at the Kendall Square Station and he changed
for
> Jamaica Plain.
> When he got there the conductor told him, "One more nickel." Charlie
…[10 more quoted lines elided]…
> Charlie's wife goes down to the Sculley Square Station every day at
quarter
> past two,
> And through the open window she hands Charlie a sandwich as the train
comes
> rumblin' through.
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] 'Neath the streets of Boston

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-03T19:46:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB418C9.7CBB65A1@shaw.ca>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <b8uf3k$nf3$1@si05.rsvl.unisys.com> <37-dnVzrhOIGfy-jXTWJkQ@giganews.com> <KtPsa.2057$S%.208869@news20.bellglobal.com>`

```


Donald Tees wrote:

> If you had told me, Jerry, I could have just gone to my old vinyl, and
> pulled it out.

Well - we still have our old LPs, 'King and I", "Carousel", a whole daffy of
musicals, plus light classics. Now if you are meaning old 78's, (scratch,
scratch, scratch......),  - well they got put into the stove(oven) to melt ever
so slightly - and they make beautiful flower pots <G>

Jimmy
```

#### ↳ Re: What statement is executed next?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-03T11:26:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb2fe81$1_2@127.0.0.1>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com>`

```

"STR" <setar@mindspring.com> wrote in message
news:8623d3bf.0305021015.559061f7@posting.google.com...
> A beginner's question.
>
…[5 more quoted lines elided]…
>

Control returns to statement 02170, where it drops into the 400-HISTORY para
and goes insane (results after that are  (technically)
unpredictable...However, you can bet they won't be what you want...<G> )

Pete.


> Thanks in advance.
> ----------------------------------------
…[31 more quoted lines elided]…
> 02403              EXIT.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

##### ↳ ↳ Re: What statement is executed next?

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-03T20:08:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305031908.c72712b@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3eb2fe81$1_2@127.0.0.1>...
> "STR" <setar@mindspring.com> wrote in message
> news:8623d3bf.0305021015.559061f7@posting.google.com...
…[15 more quoted lines elided]…
> 

Pete,

You're correct only if 200-TEST wasn't PERFORMed.

Regards, Jack.
> > Thanks in advance.
> > ----------------------------------------
…[38 more quoted lines elided]…
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What statement is executed next?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-05T03:40:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb53461_2@127.0.0.1>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com>`

```
Excellent Jack.

My response was based on what he posted, yours went further.

I stand "corrected" <G>

Pete.

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0305031908.c72712b@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:<3eb2fe81$1_2@127.0.0.1>...
> > "STR" <setar@mindspring.com> wrote in message
> > news:8623d3bf.0305021015.559061f7@posting.google.com...
…[9 more quoted lines elided]…
> > Control returns to statement 02170, where it drops into the 400-HISTORY
para
> > and goes insane (results after that are  (technically)
> > unpredictable...However, you can bet they won't be what you want...<G> )
…[48 more quoted lines elided]…
> > ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> > http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> > ---= 19 East/West-Coast Specialized Servers - Total Privacy via
Encryption =---




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-04T16:01:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305041417.69bb9fb8@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com> <3eb53461_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> My response was based on what he posted, yours went further.

> > You're correct only if 200-TEST wasn't PERFORMed.

> > > > 400-EXIT.
> > > > 02403              EXIT.


It also depends on what follows line 02403.  One may expect that it is
another paragraph name or perhaps the end of the source file.  In fact
the EXIT is a no-op (and is thus not 'executed') and any further code
in the 403-Exit paragraph will be executed next.  Of course 'further
code' may give a compile error or warning, depending on the usual
constraints.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-04T16:01:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305041417.73172433@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com> <3eb53461_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> My response was based on what he posted, yours went further.

> > You're correct only if 200-TEST wasn't PERFORMed.

> > > > 400-EXIT.
> > > > 02403              EXIT.


It also depends on what follows line 02403.  One may expect that it is
another paragraph name or perhaps the end of the source file.  In fact
the EXIT is a no-op (and is thus not 'executed') and any further code
in the 403-Exit paragraph will be executed next.  Of course 'further
code' may give a compile error or warning, depending on the usual
constraints.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-04T16:01:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305041418.3fe255cb@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com> <3eb53461_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> My response was based on what he posted, yours went further.

> > You're correct only if 200-TEST wasn't PERFORMed.

> > > > 400-EXIT.
> > > > 02403              EXIT.


It also depends on what follows line 02403.  One may expect that it is
another paragraph name or perhaps the end of the source file.  In fact
the EXIT is a no-op (and is thus not 'executed') and any further code
in the 403-Exit paragraph will be executed next.  Of course 'further
code' may give a compile error or warning, depending on the usual
constraints.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 5)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-04T19:00:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305041800.7f833aa5@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0305041418.3fe255cb@posting.google.com>...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
> 
…[11 more quoted lines elided]…
> in the 403-Exit paragraph will be executed next.  

Hi Richard,

From what I remember, how EXIT performs depends on how the associated
pgraph(s) was (were) entered. If via a PERFORM stmt EXIT will behave
as a branch back to the NSI following the PERFORM. If entered via a GO
TO or a "fall through", it behaves as a "noop". I haven't looked at
the code generated (if any) by an EXIT stmt, but I do know the
behavior in an MVS/mainframe environment is as I've outlined above. In
this case the pgraphs were entered via a PERFORM, so control should
return to the stmt following the PERFORM, n'est-ce pas?
  
Of course 'further
> code' may give a compile error or warning, depending on the usual
> constraints.

In an MVS level mainframe environment, allowing "further code" was
introduced in COBOLII. Prior to that an "exit pgraph" was allowed to
contain only 1 stmt, the EXIT stmt.

I've always assumed the "further code" had to precede the EXIT stmt.
I'll have to check that out.

Regards, Jack.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-06T14:52:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b94jnr$jp1$1@aklobs.kc.net.nz>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com> <8a2d426e.0305041800.7f833aa5@posting.google.com>`

```
Jack Sleight wrote:

> From what I remember, how EXIT performs depends on how the associated
> pgraph(s) was (were) entered. If via a PERFORM stmt EXIT will behave
…[8 more quoted lines elided]…
> I'll have to check that out.

"""An EXIT statement serves only to enable the user to assign a 
procedure-name to a given point in the program. Such an EXIT statement has 
no other effect on the compilation or execution of the program."""

The return to the PERFORM is done because the end of the PERFORM range has 
been reached, in other words the next label after the range specified in 
the PERFORM (or THRU).  Paragraphs are not supposed to be empty so, in 
order to have a pargraph label as the last point in a PERFORM range there 
must be a statement in it.  The EXIT statement is a no-op 'noise word'.  
Because it must have been in its own paragraph it _appeared_ to be 
actioning the return to the PERFORM.

       PERFORM A THRU B
       ...


     A.
        ...
     B.
        EXIT.
        DISPLAY "This will display".
     C.

Should 1) give a compile error (if enforced).  2) execute the DISPLAY 
statement (if not enforced).

However, as allowing other statements in a paragraph with an EXIT is 
non-standard ('85 and '74, maybe other) then the implementation may do 
anything, including, as you say, acting as a return to the PERFORM and 
skipping anything following.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 7)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-05T21:03:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305052003.4d841a8b@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com> <8a2d426e.0305041800.7f833aa5@posting.google.com> <b94jnr$jp1$1@aklobs.kc.net.nz>`

```
Hi Richard,

Sorry, I misread your previous post. I stand beside Pete, corrected. <G>

Regards, Jack.

Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<b94jnr$jp1$1@aklobs.kc.net.nz>...
> Jack Sleight wrote:
> 
…[41 more quoted lines elided]…
> skipping anything following.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 8)_

- **From:** "Werner Spreeuwenberg" <wspreeuw@wanadoo.nl>
- **Date:** 2003-05-06T21:10:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7xVta.390679$gl2.13987889@castor.casema.net>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com> <8a2d426e.0305041800.7f833aa5@posting.google.com> <b94jnr$jp1$1@aklobs.kc.net.nz> <8a2d426e.0305052003.4d841a8b@posting.google.com>`

```
Have you guys ever tried reading the Assembler listing of your pgm ??? See
my other mail.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 9)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-07T11:50:40+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fshhbvc5qhh3nb1am2rm2gb711jtvsl1kp@4ax.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com> <8a2d426e.0305041800.7f833aa5@posting.google.com> <b94jnr$jp1$1@aklobs.kc.net.nz> <8a2d426e.0305052003.4d841a8b@posting.google.com> <7xVta.390679$gl2.13987889@castor.casema.net>`

```
On Tue, 06 May 2003 21:10:27 GMT "Werner Spreeuwenberg" <wspreeuw@wanadoo.nl>
wrote:

:>Have you guys ever tried reading the Assembler listing of your pgm ??? 

Yes.

I did it more frequently after I discovered a compiler bug.

I do it when I am not sure that the compiler will process a statement
correctly.

You just can't completely trust the compilers.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-07T12:58:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305071158.ff26b9e@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb53461_2@127.0.0.1> <217e491a.0305041418.3fe255cb@posting.google.com> <8a2d426e.0305041800.7f833aa5@posting.google.com> <b94jnr$jp1$1@aklobs.kc.net.nz> <8a2d426e.0305052003.4d841a8b@posting.google.com> <7xVta.390679$gl2.13987889@castor.casema.net>`

```
"Werner Spreeuwenberg" <wspreeuw@wanadoo.nl> wrote 

> Have you guys ever tried reading the Assembler listing of your pgm ??? See
> my other mail.

Yes I have thank you.  What I haven't done is look at the assembler
listing for your program from your compiler.

When I looked at mainframe compilers 30 years ago I found that an EXIT
statement in its own paragraph was replaced by a place holder that was
overwritten by a return address.  However I also noticed that an empty
paragraph was replaced by the same place holder, and a paragraph with
statements had a place holder at its end without an EXIT being there.

I drew the conclusion that the EXIT statement actually had no
relationship to the creation of the place holder at all - at least on
the compilers that I used.

Later (25 years ago) we moved to compilers on systems that prevented
self modification of code.

Now, what did you want to show me ?
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-04T18:08:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305041708.56f34c4f@posting.google.com>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <3eb2fe81$1_2@127.0.0.1> <8a2d426e.0305031908.c72712b@posting.google.com> <3eb53461_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3eb53461_2@127.0.0.1>...
> Excellent Jack.
> 
…[5 more quoted lines elided]…
> 
No, no, Pete, sit, sit. <G>

Jack
> "Jack Sleight" <jacksleight@hotmail.com> wrote in message
> news:8a2d426e.0305031908.c72712b@posting.google.com...
…[77 more quoted lines elided]…
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: What statement is executed next?

- **From:** "Werner Spreeuwenberg" <wspreeuw@wanadoo.nl>
- **Date:** 2003-05-03T21:38:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oFWsa.374358$gl2.13327171@castor.casema.net>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com>`

```
Firstly, It's bad programming to make use of a GO TO in Cobol. In most
companies it's NOT allowed. Your code should therefor read:
> 02176              IF ARJFILE-STATUS = "00"
> 02177                  DISPLAY "BAD START ARJFILE, STATUS= "
…[3 more quoted lines elided]…
>                         etc, etc


But, to answer your question : The GO TO paragraph-name statement translates
to a Branch in machine language. The 400-EXIT paragraph name is in fact a
full-word carrying the address of the instruction following that point. The
next statement to be executed will be the EXIT statement. The EXIT statement
will also execute a branche statement according to a return-adress it saved
whilst doing the original PERFORM statement at line number 02169.


"STR" <setar@mindspring.com> schreef in bericht
news:8623d3bf.0305021015.559061f7@posting.google.com...
> A beginner's question.
>
…[39 more quoted lines elided]…
> 02403              EXIT.
```

##### ↳ ↳ Re: What statement is executed next?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-04T15:02:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb482e5$1_2@127.0.0.1>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <oFWsa.374358$gl2.13327171@castor.casema.net>`

```

"Werner Spreeuwenberg" <wspreeuw@wanadoo.nl> wrote in message
news:oFWsa.374358$gl2.13327171@castor.casema.net...
> Firstly, It's bad programming to make use of a GO TO in Cobol. In most
> companies it's NOT allowed. Your code should therefor read:

I submit that you are, in fact, Robert Wagner, posting in disguise from the
Netherlands, and I claim $500 for recognizing you...

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What statement is executed next?

- **From:** "Werner Spreeuwenberg" <wspreeuw@wanadoo.nl>
- **Date:** 2003-05-06T21:08:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZuVta.431032$dW6.15191127@pollux.casema.net>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <oFWsa.374358$gl2.13327171@castor.casema.net> <3eb482e5$1_2@127.0.0.1>`

```
Wrong !!! I'm Werner, a South African living in Holland. Sorry.
```

###### ↳ ↳ ↳ Re: What statement is executed next?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-06T22:39:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB835F4.CBCAE3CF@shaw.ca>`
- **References:** `<8623d3bf.0305021015.559061f7@posting.google.com> <oFWsa.374358$gl2.13327171@castor.casema.net> <3eb482e5$1_2@127.0.0.1> <ZuVta.431032$dW6.15191127@pollux.casema.net>`

```


Werner Spreeuwenberg wrote:

> Wrong !!! I'm Werner, a South African living in Holland. Sorry.

I guess that makes you kinda Double Dutch <G>

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
