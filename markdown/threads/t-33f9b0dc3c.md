[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Off-topic: Rephrasing "employment terminated"?

_2 messages · 2 participants · 2002-04_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### Re: Off-topic: Rephrasing "employment terminated"?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-04-11T09:50:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cb55438_2@Usenet.com>`
- **References:** `<a7o5d1$4jga$1@mercury.vcu.edu> <zu6o8.102194$2q2.8621038@bin4.nnrp.aus1.giganews.com> <n49o8.41046$J53.1272791@typhoon.austin.rr.com> <a7t6kk$3dkq$1@mercury.vcu.edu> <3cab0062_4@Usenet.com> <a91se9$6g14$1@mercury.vcu.edu>`

```
Sadly, some companies place a lot of emphasis on phone interviews as a method of "filtering" prospects.

Don't take it to heart. (If it's any consolation... I worked with CICS, almost from the time it was invented,  up until around 1992 and I don't remember what SCT means either. The EIBCALEN question is easily missed if you are nervous and they have already mentioned "zero" to throw you...and the subtle details of LINK, XCTL and START are also easily confused under the same circumstances. This is why phone interviewing is not a good practice; different individuals react differently on the phone.)

Of course, all they are trying to do is filter out people so they don't really care whether the test is "fair" or not.

Write it down to experience. After a few such interviews you will be less nervous and perform better.

Keep trying to get a face-to-face interview.

Pete.


  <bgwillia@vcu.edu> wrote in message news:a91se9$6g14$1@mercury.vcu.edu...

  Hi all, 

  Give you a quick update:  I screwed up the technical interview made over the phone on my first job opportunity.  I thought I knew my CICS down pat since I coded with it from '88 to '96 when the department began switching to Oracle and MS-Access. 

  The first question "what is meant by SCT?" threw off my game plan because I don't remember that acronym in relation with CICS coding.  Then it went downhill from there: 

  "what does it mean then EIBCALEN is zero" (I said normal condition return, actually it is the length of the COMMAREA when the CICS program is first invoked), 

  "what is the difference between XCTL and START (I said XCTL is transfering control to another program without any return abilities and START is the same thing but with return abilites, actually LINK uses a return back to calling program on a higher level and START acts like a CALL statement) ...   

  Well you get the idea.  Also messed up on JCL IDCAMS statements.  But did failly well on my COBOL - just messed up saying "PIC S9(5) COMP" is three bytes when it's four. ("PIC S9(4) COMP" is two bytes on a fullword boundary). 

  I noted down the questions and my responses and look them up to confirm.  Boy, I must of really looked red-faced when I saw how bad I did!  Made a good dent on the desk after banging my head against it for an hour saying "why! why! why!"  (just kidding about the head-banging part).  But it does y'all an idea what the recruiters are asking. 

  Now I'm getting another interview about an Oracle position at the same company.  So, now it's boning up on the vi editor and UNIX commands (haah, finger managling - let me count the ways). 

  Wish me luck, 
  Boyce Williams
```

#### ↳ Re: Off-topic: Rephrasing "employment terminated"?

- **From:** Liam Devlin <LiamD@dontspam.optonline.net>
- **Date:** 2002-04-13T06:24:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CB7CF11.5F925F48@dontspam.optonline.net>`
- **References:** `<a7o5d1$4jga$1@mercury.vcu.edu> <zu6o8.102194$2q2.8621038@bin4.nnrp.aus1.giganews.com> <n49o8.41046$J53.1272791@typhoon.austin.rr.com> <a7t6kk$3dkq$1@mercury.vcu.edu> <3cab0062_4@Usenet.com> <a91se9$6g14$1@mercury.vcu.edu> <3cb55438_2@Usenet.com>`

```
<bgwillia@vcu.edu> wrote in message
news:a91se9$6g14$1@mercury.vcu.edu...

     Hi all, 

     Give you a quick update:  I screwed up the technical
     interview made over the phone on my first job opportunity.
      I thought I knew my CICS down pat since I coded with it
     from '88 to '96 when the department began switching to
     Oracle and MS-Access. 

     The first question "what is meant by SCT?" threw off my
     game plan because I don't remember that acronym in
     relation with CICS coding.  Then it went downhill from
     there: 

I've been working with CICS since '72 and am still using it. I consider
myself pretty knowledgeable, but I don't recognize "SCT". "System
Control Table" or "Security Control Table" come to mind, but I've never
heard of either of them. The IBM online system I worked with before CICS
did have SCT's. 

     "what does it mean then EIBCALEN is zero" (I said normal
     condition return, actually it is the length of the
     COMMAREA when the CICS program is first invoked), 

What it means when EIBCALEN = 0 is that you have no COMMAREA.

     "what is the difference between XCTL and START (I said
     XCTL is transfering control to another program without any
     return abilities and START is the same thing but with
     return abilites, actually LINK uses a return back to
     calling program on a higher level and START acts like a
     CALL statement) ...   

START invokes a separate task, whereas XCTL, LINK & CALL all invoke
programs within the existing task. In my experience, the idea of a
separate task is what people are usually interested in.

     Well you get the idea.  Also messed up on JCL IDCAMS
     statements.  But did failly well on my COBOL - just messed
     up saying "PIC S9(5) COMP" is three bytes when it's four.
     ("PIC S9(4) COMP" is two bytes on a fullword boundary). 

Not really, if you don't specify "SYNC", COMP (or BINARY) fields are
byte aligned. With "SYNC", Pic S9999 is halfword boundary aligned
(address is a multiple of 2) and S9(8)/S9(9) are fullword boundary
aligned (address is a multiple of 4).

     I noted down the questions and my responses and look them
     up to confirm.  Boy, I must of really looked red-faced
     when I saw how bad I did!  Made a good dent on the desk
     after banging my head against it for an hour saying "why!
     why! why!"  (just kidding about the head-banging part).
      But it does y'all an idea what the recruiters are asking. 

     Now I'm getting another interview about an Oracle position
     at the same company.  So, now it's boning up on the vi
     editor and UNIX commands (haah, finger managling - let me
     count the ways). 

Knock 'em dead, Boyce. 

In general, what's the market like these days (I may have more than an
academic interest in it soon), especially the NYC area?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
