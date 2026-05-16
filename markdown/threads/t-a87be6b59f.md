[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Cobol Install ?

_9 messages · 7 participants · 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Cobol Install ?

- **From:** tippcity_1999@yahoo.com (billman)
- **Date:** 2003-10-27T10:33:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4961a3da.0310271033.7b5e26e8@posting.google.com>`

```
Hi,

How difficult is it to install Microfocus Cobol ? 

We have about 40 batch mainframe (IBM/MVS) cobol programs used for a
data conversion process that we want to run on Windows.  Only one
programmer works on, or even runs, these programs.

Microfocus says we should buy a week of consulting services from them
to cmoe out and install the product(s).  Is it really that difficult ?
 I would have thought it would be more like Microsoft's Visual suite,
which is fairly straightforward.

Thanks for your thoughts...
```

#### ↳ Re: Microfocus Cobol Install ?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-10-27T21:08:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F9CE023.40C87784@shaw.ca>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com>`

```


billman wrote:

> Hi,
>
…[5 more quoted lines elided]…
>

What happens when he leaves, or is he planning on hanging around until he
is 84 ?

>
> Microfocus says we should buy a week of consulting services from them
…[4 more quoted lines elided]…
> Thanks for your thoughts...

Can't blame Micro Focus for trying to make a buck <G>. But you have
probably told them a lot more about the problem than you have told us.
Presumably it is Server Express you want to install ?

The actual install - probably no big deal - BUT - (a) One week of M/F
assistance at $x as opposed to (b) Your one guy at $x per hour for 'y'
weeks - and of course this is probably just an absorbed cost not
specifically posted to a Cost Centre ?

Your man - is he a 'hot shot' COBOL programmer or has the task been
delegated to a 'junior'. No doubt on the re-compiles there will be some
syntax errors which an experienced man can fathom - a junior might
flounder around a bit but eventually get there. The 40 programs - one
conversion suite or a series of separate conversions ?  M/F might have in
mind they can be re-designed, (without affecting the business logic),  to
be more easily automated in a Windows environment.

Possible plus if M/F get involved - with them on site your guy can throw a
host of questions at them about the product - which will give him tips and
quick shortcuts to features. (As he is the only COBOL developer - make
*sure* he documents what he finds out !).

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Microfocus Cobol Install ?

- **From:** Kevin Hansen <khansen@screenio.com>
- **Date:** 2003-10-27T22:01:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9j4rpv8gbbsckgvj72omt0piequrbd2aff@4ax.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com> <3F9CE023.40C87784@shaw.ca>`

```
On Mon, 27 Oct 2003 21:08:48 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

>Can't blame Micro Focus for trying to make a buck <G>. But you have
>probably told them a lot more about the problem than you have told us.
…[20 more quoted lines elided]…
>Jimmy, Calgary AB
---------
All true, and I concur that paying for a little consulting time would
be a good investment.

We've seen lots of people move from mainframes to PCs.  The COBOL
isn't usually much of an issue, but if the developer in question has
never worked in a PC-based development environment, there are a lot of
other issues to get your arms around.

How do your organize your subdirectories and files?  How about (good)
backup procedures?  Setting up a rational testing environment?
Version control?  Linking?  Object libraries?

In the mainframe environment, this is all usually done for you by the
technical services department, but on the PC, it's your problem.  This
is -good- because you can now control your environment, but -bad-
because you need to learn and take care of a lot more stuff.

Once you've had a taste of how productive you can be on a PC COBOL
platform, you'll never look back.  I still remember what a revelation
it was back in 1985 when we discovered interactive debugging on a PC
COBOL.  Fabulous!  

Kevin
Develop Windows(tm) Applications - in COBOL!
http://www.ScreenIO.com
```

#### ↳ Re: Microfocus Cobol Install ?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-10-27T23:41:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364rpvcl5gpqkrda4n3g2b7lthfa0c98h8@4ax.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com>`

```
On 27 Oct 2003 10:33:48 -0800 tippcity_1999@yahoo.com (billman) wrote:

:>How difficult is it to install Microfocus Cobol ? 

:>We have about 40 batch mainframe (IBM/MVS) cobol programs used for a
:>data conversion process that we want to run on Windows.  Only one
:>programmer works on, or even runs, these programs.

:>Microfocus says we should buy a week of consulting services from them
:>to cmoe out and install the product(s).  Is it really that difficult ?
:> I would have thought it would be more like Microsoft's Visual suite,
:>which is fairly straightforward.

:>Thanks for your thoughts...

Well, if it includes converting your existing programs, and it comes with a
guarantee ......
```

#### ↳ Re: Microfocus Cobol Install ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-27T22:58:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mqhnb.4550$RQ1.3942@newsread3.news.pas.earthlink.net>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com>`

```
Well, ....

Are you looking at getting Net Express or Mainframe Express?

From you description of how it will be used, I would GUESS that it would be
Mainframe Express.  If so, the answer is it is EASY to install (most of its
parts) but medium-difficult to "configure" to get working as you want.

Some of the issues:

 - Do you want to "directly" access your mainframe data files or FTP them to
the PC?
 - How do you plan on keeping your mainframe and PC source files "in sync"
 - Have you looked at EBCDIC/ ASCII issues?
 - Have you looked at "compiler compatibility" issues?
 - Do you expect ISPF or "PC" type "look and feel" on the PC?

Now, if from your description, you actually expect to PORT your applications
from the mainframe to the PC and *never* use them again on the mainframe,
then I would expect you to be getting Net Express and not Mainframe Express.
This would be easier to "configure" but harder to actually get working (as a
production environment).

Bottom-Line:
  I would ask Micro Focus (not Microfocus) to provide you with a couple of
"customer references" that you can talk to about how their install went
(either with or without the one week training).
```

##### ↳ ↳ Re: Microfocus Cobol Install ?

- **From:** tippcity_1999@yahoo.com (billman)
- **Date:** 2003-10-27T18:37:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4961a3da.0310271837.5ae1d244@posting.google.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com> <mqhnb.4550$RQ1.3942@newsread3.news.pas.earthlink.net>`

```
Greetings again !  Thank you VERY MUCH for the replies.  This passle
of programs will be used to move two client off the mainframe and then
they will never be run again.

Answering the questions in order - 

What happens when he leaves - we have other people who are familiar
with the whole process and know cobol very well.

Presumably it is Server Express you want to install - wow, don't know
for sure.  We seek to take COBOL programs as text files from the
mainframe, compiling them on Windows, and running them on Windows. 
Also take data from one UNIX system and an MVS mainframe system and
put it on Windows.  There is no GUI when the program runs, no database
access, no cross-platform access of data.  All self contained at
runtime.

cost not specifically posted to a Cost Centre ? - It is, yes.

The 40 programs - one conversion suite or a series of separate
conversions ? - All are "batch", reading one to four flat files,
output one flat file.

How do your organize your subdirectories and files?  How about (good)
backup procedures?  Setting up a rational testing environment?
Version control?  Linking?  Object libraries? - All very good points,
this is where we thought more of the time would be spent (vs. product
installation).

Do you want to "directly" access your mainframe data files or FTP them
to the PC? - "FTP"
How do you plan on keeping your mainframe and PC source files "in
sync" ? - not necessary, we can start anew as it were.
Have you looked at EBCDIC/ ASCII issues? - Just started, this is the
biggest area of peril.
Have you looked at "compiler compatibility" issues? - I assume you
mean the comp/comp-3 etc. and other different interpretations of ANSI
- just started.
Do you expect ISPF or "PC" type "look and feel" on the PC? - A nicety
but not important.  Could be command line for all we care.

Thanks again, it would seem that your thoughts collectively indicate
that a straightforward install is not that big a deal, it's the other
million things that can go wrong.


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<mqhnb.4550$RQ1.3942@newsread3.news.pas.earthlink.net>...
> Well, ....
> 
…[44 more quoted lines elided]…
> > Thanks for your thoughts...
```

###### ↳ ↳ ↳ Re: Microfocus Cobol Install ?

- **From:** mossjm@wideopenwest.com (QCBLSRC)
- **Date:** 2003-10-27T23:58:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3473e5fa.0310272358.240e277a@posting.google.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com> <mqhnb.4550$RQ1.3942@newsread3.news.pas.earthlink.net> <4961a3da.0310271837.5ae1d244@posting.google.com>`

```
tippcity_1999@yahoo.com (billman) wrote in message news:<4961a3da.0310271837.5ae1d244@posting.google.com>...

Uh....why would you want to move your batch processes from a mainframe
to a PC?.
What are the reasons for wanting to do that?
Are you moving all of your other applications off of the mainframe?
Are these batch processes all that is left running on the machine??

Think about this....

What happens if your PC/Windows gets a virus?
How are you going to backup/protect your data?
Will you have to export the data back to the mainframe? (I surely hope
not).

The biggest question to ponders is...why did you buy the mainframe in
the first place?.  Why didn't you just buy a x386 running Windows 3.1?

QCBLSRC
```

###### ↳ ↳ ↳ Re: Microfocus Cobol Install ?

_(reply depth: 4)_

- **From:** tippcity_1999@yahoo.com (billman)
- **Date:** 2003-10-28T06:30:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4961a3da.0310280630.35b516bf@posting.google.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com> <mqhnb.4550$RQ1.3942@newsread3.news.pas.earthlink.net> <4961a3da.0310271837.5ae1d244@posting.google.com> <3473e5fa.0310272358.240e277a@posting.google.com>`

```
QCBLSRC,

the mainframe is being retired.  these programs that run on the
mainframe have to be moved elsewhere as it is cost prohibitive to keep
the mainframe running just for this.  one might wonder why we created
a process on the maniframe, that didn't really have to be on the
mainframe, but what are ya gonna do...

the programs et al on the PC would actually be stored on a win2k
server w/ backup and a-v.

mossjm@wideopenwest.com (QCBLSRC) wrote in message news:<3473e5fa.0310272358.240e277a@posting.google.com>...
> tippcity_1999@yahoo.com (billman) wrote in message news:<4961a3da.0310271837.5ae1d244@posting.google.com>...
> 
…[16 more quoted lines elided]…
> QCBLSRC
```

#### ↳ Re: Microfocus Cobol Install ?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-10-28T11:42:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0310281142.4e45cb5a@posting.google.com>`
- **References:** `<4961a3da.0310271033.7b5e26e8@posting.google.com>`

```
Please email me privately NOT at this address but at 
t h a n e @ s o f t w a r e s i m p l e . c o m

I tried to use your email address from this message but you are over quota.

I think I can help you out. 

tippcity_1999@yahoo.com (billman) wrote in message news:<4961a3da.0310271033.7b5e26e8@posting.google.com>...
> Hi,
> 
…[11 more quoted lines elided]…
> Thanks for your thoughts...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
