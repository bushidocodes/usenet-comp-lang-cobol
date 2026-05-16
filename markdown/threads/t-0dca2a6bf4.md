[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# a history question

_74 messages · 13 participants · 2004-09 → 2004-10_

---

### a history question

- **From:** bob_peterson@rediffmail.com (Bob)
- **Date:** 2004-09-27T09:29:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`

```
In the history of C language it is always mentioned that C was the
first platform independent language?
So if this is true then what was the nature of the languages which
were there before C(like Cobol,fortran adn Basic)?
weren't they platform independent?

which platform there were running on?


greetings,
Bob
```

#### ↳ Re: a history question

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-27T22:50:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cja5f301upd@news2.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`

```

In article <e80b0472.0409270829.40a9b8a4@posting.google.com>, bob_peterson@rediffmail.com (Bob) writes:
> In the history of C language it is always mentioned that C was the
> first platform independent language?

Only if that history is written by someone who doesn't know what he's
talking about.

Dennis Ritchie's history of C,[1] for example, makes no such claim.
In fact, he goes into some detail about what was done to make C
available for multiple platforms, implying (correctly) that C is
*not* "platform-independent".

Anyone who actually understands C - who is familiar with the
language's standard, history, and common practice - knows that it is
by no means platform-independent, and never was; and that this was
never one of its goals.

> So if this is true then what was the nature of the languages which
> were there before C(like Cobol,fortran adn Basic)?
> weren't they platform independent?

Many languages were supported on multiple platforms.  That's not the
same thing as "platform-independent" (unless you have a very weak
definition of the latter).

> which platform there were running on?

Various ones; the question is too broad to be answered in a newsgroup
posting.  There's a tremendous amount of information on the history
of programming languages available, on the Internet and otherwise.


1. http://cm.bell-labs.com/cm/cs/who/dmr/chist.html
```

#### ↳ Re: a history question

- **From:** "Charles W. Cribbs II" <charlescribbs@earthlink.net>
- **Date:** 2004-09-27T22:55:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GT06d.2036$ls6.1702@newsread3.news.atl.earthlink.net>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`

```
No they had to be compiled for the various machines they where to run on.


"Bob" <bob_peterson@rediffmail.com> wrote in message
news:e80b0472.0409270829.40a9b8a4@posting.google.com...
> In the history of C language it is always mentioned that C was the
> first platform independent language?
…[8 more quoted lines elided]…
> Bob
```

#### ↳ Re: a history question

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-27T17:07:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409271607.3c01c51b@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`

```
bob_peterson@rediffmail.com (Bob) wrote 

> In the history of C language it is always mentioned that C was the
> first platform independent language?

Can you show a history that does in fact claim this ?  Far from
'always' I have never seen this particular claim.

Unix was a platform indepenent OS, AT&T had a portable C compiler
which could be implemented on different systems.  But I doubt that
anyone with two clues to rub together would make that particular
claim.

In fact, in order to write programs that are 'platform independent' it
is usually necessary to specify the actual code for each platform
within particular #IFDEFs.  In other words the language may be
dependent but has features to cater for this.

> So if this is true then what was the nature of the languages which
> were there before C(like Cobol,fortran adn Basic)?
> weren't they platform independent?

Cobol, Algol, Pascal, Fortran and many others were platform
independent.
```

#### ↳ Re: a history question

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-27T19:43:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bt26d.31986$vl.17062@fe40.usenetserver.com>`
- **In-Reply-To:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com>`

```
Bob wrote:
> In the history of C language it is always mentioned that C was the
> first platform independent language?
> So if this is true then what was the nature of the languages which
> were there before C(like Cobol,fortran adn Basic)?
> weren't they platform independent?

That's an interesting term.  When you speak of "platform independent" 
these days, people think of something like Java, which is compiled once, 
then run anywhere through a platform-dependent runtime environment.

However, COBOL, FORTRAN, BASIC, et. al. were (are) as platform 
independent as C.  This doesn't mean that C is - I'd dispute that claim. 
  C programs (like the aforementioned high-order languages) must be 
compiled on the architecture for which it is destined.

I can't take a PC-based executable programmed in COBOL, FTP it up to the 
Unisys mainframe, and expect it to do run.  Now, if I have the source, 
it is very likely that I may be able to FTP that up, compile it, and 
with a few tweaks, come up with an equivalent executable for that 
environment.  Same for C - especially considering our mainframe's 
36-bit-word architecture.  :)

To the best of my knowledge, Java was the first language to use a 
bytecode interpreter - so, it's still interpreted (like a scripting 
language), but it's faster because it doesn't also have to translate the 
source to machine code at runtime.  If it wasn't the first, it's 
definitely the most popular.
```

##### ↳ ↳ Re: a history question

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-09-27T23:34:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4158E9CC.9CCE6DB4@mb.sympatico.ca>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com>`

```
LX-i wrote:
> 
> Bob wrote:
…[5 more quoted lines elided]…
> 

> 
> To the best of my knowledge, Java was the first language to use a
…[4 more quoted lines elided]…
> 


Didn't Accucobol work this way?

PL
```

##### ↳ ↳ Re: a history question

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-27T22:22:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409272122.4bbc8256@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com>`

```
LX-i <lxi0007@netscape.net> wrote 

> However, COBOL, FORTRAN, BASIC, et. al. were (are) as platform 
> independent as C.  This doesn't mean that C is - I'd dispute that claim. 
…[4 more quoted lines elided]…
> Unisys mainframe, and expect it to do run. 

Actually that it implementation dependent.  With RM and Accu that is
exactly what you _can_ do - given appropriate runtimes.

> To the best of my knowledge, Java was the first language to use a 
> bytecode interpreter - so, it's still interpreted (like a scripting 
> language), but it's faster because it doesn't also have to translate the 
> source to machine code at runtime.  If it wasn't the first, it's 
> definitely the most popular.

Bytecoded languages date from the 60s at least. Many Pascals were byte
coded, (they called it pcode) such as UCSD, where a program compiled
on any machine (eg Apple ][) could run on any other (eg DEC PDP-16) as
long as it had the UCSD runtime system.

Bytecoded Cobol systems include Microsoft, MicroFocus (from CIS Cobol
in 1978 to Server Express .int), RM, Accu.

There is no prohibition for C or C++ to not be bytecoded, versions of
MS VC++ can create pcode modules, though this is only useful for space
saving as there are not many other systems that would run it.
```

###### ↳ ↳ ↳ Re: a history question

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-28T07:57:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dd6d.33118$vl.16643@fe40.usenetserver.com>`
- **In-Reply-To:** `<217e491a.0409272122.4bbc8256@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <217e491a.0409272122.4bbc8256@posting.google.com>`

```
Richard wrote:
> LX-i <lxi0007@netscape.net> wrote 
> 
…[10 more quoted lines elided]…
> exactly what you _can_ do - given appropriate runtimes.

Interesting.

>>To the best of my knowledge, Java was the first language to use a 
>>bytecode interpreter - so, it's still interpreted (like a scripting 
…[8 more quoted lines elided]…
> long as it had the UCSD runtime system.

heh - are you telling me I just gave my age away?  :)

> Bytecoded Cobol systems include Microsoft, MicroFocus (from CIS Cobol
> in 1978 to Server Express .int), RM, Accu.
…[3 more quoted lines elided]…
> saving as there are not many other systems that would run it.

That's good information - thanks.  So you're saying that you could 
compile a program on a Windows PC, and run that same executable on, say, 
a Mac or Linux?  (The runtime environment would be the one to handle the 
environment change?)
```

##### ↳ ↳ Re: a history question

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-28T08:30:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com>`

```
On Mon, 27 Sep 2004 19:43:48 -0500, LX-i <lxi0007@netscape.net> wrote:

>Bob wrote:
>> In the history of C language it is always mentioned that C was the
…[7 more quoted lines elided]…
>then run anywhere through a platform-dependent runtime environment.

Java is not platform independent; Java IS a platform. On Wintel, you
compile to Intel's machine language and execute on Microsoft's
software platform. Both are proprietary, profit-making and rigged to
put the competition at a disadvantage. The JVM is Sun's proprietary
language and software platform.

>To the best of my knowledge, Java was the first language to use a 
>bytecode interpreter - so, it's still interpreted (like a scripting 
>language), but it's faster because it doesn't also have to translate the 
>source to machine code at runtime.  If it wasn't the first, it's 
>definitely the most popular.

Interpreted pseudo-code has been re-invented a hundred times. Users
pay the high price every time they execute a program. 

The JVM is no longer an interpreter; it's now a JIT compiler back-end.
It translates intermediate code into machine language the first time a
program is touched. Dot-NET works the same way.

Micro Focus produces pseudo-code by default, in a file named .int. The
runtime interpreter is cobrun. Cobcrawl would be more accurate.
Programs execute six times slower than native code, which is the
typical ratio for interpreters.
```

###### ↳ ↳ ↳ Re: a history question

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-28T08:03:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%id6d.33140$vl.9276@fe40.usenetserver.com>`
- **In-Reply-To:** `<ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>`

```
Robert Wagner wrote:
> On Mon, 27 Sep 2004 19:43:48 -0500, LX-i <lxi0007@netscape.net> wrote:
> 
…[8 more quoted lines elided]…
> language and software platform.

So this claim is only possible because Sun is willing to provide JVMs 
for every environment possible?

>>To the best of my knowledge, Java was the first language to use a 
>>bytecode interpreter - so, it's still interpreted (like a scripting 
…[9 more quoted lines elided]…
> program is touched. Dot-NET works the same way.

And I can tell the difference - Java stuff today seems much faster than 
it used to, although it's sluggish in the beginning.

> Micro Focus produces pseudo-code by default, in a file named .int. The
> runtime interpreter is cobrun. Cobcrawl would be more accurate.
> Programs execute six times slower than native code, which is the
> typical ratio for interpreters. 

There's always a trade-off.  :)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-28T14:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com>`

```
On Tue, 28 Sep 2004 08:03:52 -0500, LX-i <lxi0007@netscape.net> wrote:

>Robert Wagner wrote:
>> On Mon, 27 Sep 2004 19:43:48 -0500, LX-i <lxi0007@netscape.net> wrote:
…[12 more quoted lines elided]…
>for every environment possible?

Microsoft wrote their own JVM, which included extensions that work
only on a MS platform. MS said they fixed a weakness in the spec,
which was true. The Sun licensing contract says outsiders developing a
JVM are not allowed to hurt portability by adding proprietary
features. Sun sued MS and won. Rather than fix their JVM, Microsoft
got in a snit, removed it from the market and stopped supporting old
copies. XP users must download their JVM from Sun.

Some JVMs, like the one for Unisys MCP, were written by open sourcers
such as JBoss.

>>>To the best of my knowledge, Java was the first language to use a 
>>>bytecode interpreter - so, it's still interpreted (like a scripting 
…[12 more quoted lines elided]…
>it used to, although it's sluggish in the beginning.

There is a Cobol compiler that produces Java bytecode --- PerCobol by
LegacyJ. Micro Focus and Fujitsu have compilers that produce dot-NET
bytecode (MSIL) and use the Common Language Runtime. See .. your
compiled Cobol can be portable after all. In the case of dot-NET, to
every operating system supported by Microsoft.

The greatest advantage of this approach  is having access to the
runtimes and TONS of class libraries developed to serve other
languages .. for free. Want to package a document on another machine
as XML, transport it to your machine via the internet and unpackage
it? No need to write code; a single INVOKE will do it.
Want to send an email to everyone in the client's Outlook address
book? A few INVOKEs will do the job. :)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-28T13:33:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409281233.2740fb29@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 

> Some JVMs, like the one for Unisys MCP, were written by open sourcers
> such as JBoss.

"""While Unisys could have chosen a number of JVMs, or developed its
own, the company has had a partnership with Sun for years to deliver a
native JVM for the OS2200 and MCP versions of the ClearPath
mainframes."""

That seems to say that it is a Sun JVM.

JBoss doesn't develop VMs, it develops sofware written in Java, such
as:

"""Leading Open Source Projects - JBoss Inc. employs the leading
developers and controls the critical mass of knowledge for a number of
Java-based open source Projects including JBoss Application Server,
JBoss AOP, JBoss Cache, Hibernate, Tomcat, Nukes, JGroups, JBoss IDE,
Javassist, and JBossMail."""
 
> Want to send an email to everyone in the client's Outlook address
> book? A few INVOKEs will do the job. :)

Good grief, most Windows machines seem to be doing that all the time
_without_ the user doing anything at all, that is after they had
opened a curious attachment they received in Outlook Express.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T01:34:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <217e491a.0409281233.2740fb29@posting.google.com>`

```
On 28 Sep 2004 13:33:27 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 
>
…[17 more quoted lines elided]…
>Javassist, and JBossMail."""

This seems to contradict both of the above:

A complete and secure Java environment
Unisys will provide a complete Java environment for its ClearPath
mainframes that includes the Java Virtual Machine (JVM) together with
a fully compliant J2EE application server from the preeminent open
source project, JBoss. Unisys will also provide complete worldwide
support for both the JVM and the JBoss application server on its
ClearPath server platforms. Customers can then take advantage of a
low-cost J2EE application server from the world of open sourceï¿½and
with the support and backing of Unisys. So you can gain the economies
of open source without the risk of an open source support model.
Whatï¿½s more, the MCP operating system and ClearPath architecture will
provide a secure, mainframe environment for running your
mission-critical Java-based applications. You really can have it all.

http://www.unisys.com/products/clearpath__servers/clearpath__plus__mcp/features.htm

I hope Chuck Stevens will ring in with the answer.

>> Want to send an email to everyone in the client's Outlook address
>> book? A few INVOKEs will do the job. :)
…[3 more quoted lines elided]…
>opened a curious attachment they received in Outlook Express.

The attachment contained VBScript. It isn't  necessary to open the
attachment if the Preview feature is on .. or if your non-MS
mainreader is allowed to "use MS graphics software."
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-28T23:59:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409282259.577052cc@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <217e491a.0409281233.2740fb29@posting.google.com> <fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 

> >"""Leading Open Source Projects - JBoss Inc. employs the leading
> >developers and controls the critical mass of knowledge for a number of
> >Java-based open source Projects including JBoss Application Server,
                                             ^^^^^^^^^^^^^^^^^^^^^^^^^
> >JBoss AOP, JBoss Cache, Hibernate, Tomcat, Nukes, JGroups, JBoss IDE,
> >Javassist, and JBossMail."""
> 
> This seems to contradict both of the above:

No it does not (parentheses added):
 
> Unisys will provide a complete Java environment for its ClearPath
> mainframes that includes ( the Java Virtual Machine (JVM) ) together with
> ( a fully compliant J2EE application server from the preeminent open
> source project, JBoss. )
   
'JBoss' only applies to 'J2EE Application Server'.

It really is quite easy to read these things correctly.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-09-29T08:16:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Hnf9CleflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <217e491a.0409281233.2740fb29@posting.google.com> <fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com>`

```
.    Am  29.09.04
schrieb  robert@wagner.net.yourmammaharvests (Robert Wagner)
    auf  /COMP/LANG/COBOL
     in  fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com
  ueber  Re: a history question

>> """While Unisys could have chosen a number of JVMs, or developed its
>> own, the company has had a partnership with Sun for years to deliver a
…[6 more quoted lines elided]…
>> as:


RW> This seems to contradict both of the above:
RW>
RW> A complete and secure Java environment
RW> Unisys will provide a complete Java environment for its ClearPath
RW> mainframes that includes the Java Virtual Machine (JVM) together with
RW> a fully compliant J2EE application server from the preeminent open
RW> source project, JBoss. Unisys will also provide complete worldwide
RW> support for both the JVM and the JBoss application server on its
RW> ClearPath server platforms. Customers can then take advantage of

RW> http://www.unisys.com/products/clearpath__servers/clearpath__plus__mc
RW> p/features. htm

   1) when they write that the "provide" something to their customers,  
it does not mean that they have developed it themselves. The sell it  
(or _want_ to sell it), and provide support for it.

   b) the text makes a distinction between 1) the "Java Virtual  
Machine (JVM)" and 2) the "J2EE application server"


   I have learned many years ago not to read into press releases and  
promotion material like the above quoted, things which are not  
expressed explicitely in their text.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Die Arbeit in weiï¿½er Haut kann sich nicht dort emanzipieren, wo sie
in schwarzer Haut gebrandmarkt wird."     - Karl Marx     12.11.1866
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-09-29T12:15:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjf1k2$8fi$1@si05.rsvl.unisys.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <217e491a.0409281233.2740fb29@posting.google.com> <fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:fk1kl0tsfkv5pbv218dqbc080mt5ldfngp@4ax.com...

> This seems to contradict both of the above:

Only if you read it incorrectly and jump to unwarranted conclusions!


> I hope Chuck Stevens will ring in with the answer.

Others already have.  JVM and J2EE are different aspects of the Java
environment.

I don't have much knowledge beyond what's already been expressed by others
about the Unisys MCP Java environment.  My primary duties revolve around
COBOL; others would be far better equipped to weigh in on the subject of
Java.

It'd also be my expectation (I think reasonable) that discussions as to the
details of the Unisys MCP Java environment would likely produce much more
reliable answers on one of the "comp.lang.java" newsgroups, where
discussions about *Java* are the order of the day, than they would on
"comp.lang.cobol", where discussions about *COBOL* are the order of the day.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-28T16:41:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fUk6d.2$uO6.0@fe40.usenetserver.com>`
- **In-Reply-To:** `<h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com>`

```
Robert Wagner wrote:
> 
> Microsoft wrote their own JVM, which included extensions that work
…[5 more quoted lines elided]…
> copies. XP users must download their JVM from Sun.

I remember that.

> There is a Cobol compiler that produces Java bytecode --- PerCobol by
> LegacyJ. Micro Focus and Fujitsu have compilers that produce dot-NET
…[10 more quoted lines elided]…
> book? A few INVOKEs will do the job. :)

Ah - the world's first COBOL virus, coming soon to an Inbox near you! 
;)  Thanks for the info.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T01:34:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fi0kl0pbifmmqagn2tdii4i308qmld0ml1@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <fUk6d.2$uO6.0@fe40.usenetserver.com>`

```
On Tue, 28 Sep 2004 16:41:28 -0500, LX-i <lxi0007@netscape.net> wrote:


>Ah - the world's first COBOL virus, coming soon to an Inbox near you! 

The first Cobol virus was written in the '60s. <polishing fingernails
on lapel>
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-29T07:58:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ncWdnaNU24HqLMfcRVn-tg@giganews.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com>`

```
Robert Wagner wrote:
>
> Microsoft wrote their own JVM, which included extensions that work
…[5 more quoted lines elided]…
> copies. XP users must download their JVM from Sun.

Not so. XP users need not download JVM from Sun.

They can actually they should do the reverse - purge all reference to Java 
from their system.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T16:36:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com>`

```
On Wed, 29 Sep 2004 07:58:39 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>Robert Wagner wrote:
>>
…[11 more quoted lines elided]…
>from their system.

Without Java they won't be able to read many manuals, do electronic
banking and file unemployment claims.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-29T18:24:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WIadnSQu1cmP2cbcRVn-ug@giganews.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com>`

```
Robert Wagner wrote:
> On Wed, 29 Sep 2004 07:58:39 -0500, "JerryMouse" <nospam@bisusa.com>
> wrote:
…[18 more quoted lines elided]…
> banking and file unemployment claims.

* Read many manuals? I suppose. Until they're translated to PDF or Word
* Electronic banking? Quite possibly.
* File unemployment claims? Nah. I remember many years ago when I told my 
new boss we've evidently gotten off on the wrong foot, I suggest we start 
over as the professionals we were, and if he ever talked "that way" to me 
again, I'd drag his droopy ass out to the parking lot and teach him how to 
pick up his teeth with a broken arm that I was quite capable of filling out 
an unemployment claim form with a pencil. Didn't need no stinkin' Java!
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-30T00:10:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com>`

```
On Wed, 29 Sep 2004 18:24:11 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>> Without Java they won't be able to read many manuals, do electronic
>> banking and file unemployment claims.
…[8 more quoted lines elided]…
>an unemployment claim form with a pencil. Didn't need no stinkin' Java! 

You're a Tough Guy. USMC Special Ops had many tough guy wannabes. They
were in the bottom quartile, usually had shaved heads and a lunatic
look in their eyes. The real stars had no egotistical illusions. We
relied on intelligence rather than bravado.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 9)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-29T23:03:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com>`

```
In article <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com>,
 Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

> On Wed, 29 Sep 2004 18:24:11 -0500, "JerryMouse" <nospam@bisusa.com>
> wrote:
…[16 more quoted lines elided]…
> relied on intelligence rather than bravado.


This has to be a first..."USMC" and "intelligence" used in the same 
paragraph.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-30T09:37:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com>`

```
On Wed, 29 Sep 2004 23:03:10 -0400, Joe Zitzelberger
<joe_zitzelberger@nospam.com> wrote:

>In article <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com>,
> Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:
…[23 more quoted lines elided]…
>paragraph.

This is what happens when people's experiental mode is limited to
Hollywood stereotypes rather than real world.

In the computer realm, Hollywood says a ten year-old 'genius' can
crack 128-bit DES encryption. Do you buy into that too? If not, don't
believe Hollywood's charicature of Marines as dumb grunts. 

On the other hand, the History Channel portrays Navy Seals favorably.
I know from first hand experience they ARE dumb asses. They get
themselves killed through sheer stupidity. Special Ops Marines
wouldn't make the mistakes nor take the risks they do.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2004-09-30T08:31:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjgubj$5t5$1@panix5.panix.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com>`

```
In article <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On Wed, 29 Sep 2004 23:03:10 -0400, Joe Zitzelberger
><joe_zitzelberger@nospam.com> wrote:
…[29 more quoted lines elided]…
>Hollywood stereotypes rather than real world.

Gosh, Mr Wagner... who told you the length, depth, breadth, number and 
quality of Mr Zitzelberger's experiences?

DD
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 11)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-30T09:19:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com>`

```
In article <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com>,
 Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

> On Wed, 29 Sep 2004 23:03:10 -0400, Joe Zitzelberger
> <joe_zitzelberger@nospam.com> wrote:
…[41 more quoted lines elided]…
> 

That was intended to be something of a joke...I know that marines are no 
different from other grunts.  However, I also know that institutionally, 
the USMC does some very stupid things that the army would never consider.

I cite as example an experience I had at a staging area, run by the 
USMC, for the invasion of kuwait/iraq.  We were taking some indirect 
fire, so I naturally found the nearest prepared bunker and took some 
cover.  It lacked a proper roof, so an airburst would have been 
troublesome, but it was otherwise functional.

A few months later, home on leave, I mentioned the incident to my 
father, who was with the 31st infantry, the rear guard for the 1st 
marines, as they retreated from Chosin.  Before I even finished the 
story he said something to the effect of "stupid grunts didn't put a 
roof on the foxhole, did they".

The USMC hasn't done anything uniquely 'marine' since the second world 
war, -- it has just fought alongside the army as more infantry.  In all 
that time of association they have not absorbed the simple concept of 
protecting ones head from enemy fire.  in a world where artillery causes 
75% of casualties and where head wounds are triaged last, they still 
have an institutional bias against roofed fighting positions.  IMHO, 
that earns the corps a darwin award.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 12)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-09-30T10:05:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<415C20D0.18D9B20F@mb.sympatico.ca>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com>`

```

> 
> >
…[4 more quoted lines elided]…
>

It's worth remembering that the tediously reported cracking of the code
referred to finding A KNOWN MESSAGE  (to wit, something like "this is
the secret message").  This is light years away from the general
solution to compromising DES.  If you have a known message to begin
with, you hardly need the entire internet to find out what's in it.

PL
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 13)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-10-01T16:25:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjk0do0ipk@news2.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <415C20D0.18D9B20F@mb.sympatico.ca>`

```

In article <415C20D0.18D9B20F@mb.sympatico.ca>, Peter Lacey <lacey@mb.sympatico.ca> writes:
> 
> > > In the computer realm, Hollywood says a ten year-old 'genius' can
…[5 more quoted lines elided]…
> solution to compromising DES.

There's a known-plaintext attack against 3DES that has a signifi-
cantly smaller work factor than brute force?

(I'm not sure what you're referring to with "the tediously reported
cracking" anyway - I thought Robert was talking about one of those
stupid cryptography-thriller movies, ie fiction.  There have been
successful brute-force attacks against straight DES, with a 56-bit
key.  I'm not aware of any successful brute-forcing or other attack
against a DES variant with a key on the order of 128 bits, but this
isn't really my area.)

> If you have a known message to begin
> with, you hardly need the entire internet to find out what's in it.

Yes, but that's not what people are referring to when they talk
about known-plaintext attacks, since that would be pointless.  When
you mount a known-plaintext attack (where the entire plaintext is
known, not just part), you're looking for the *key*.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 14)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-01T19:18:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q87rl01iot1kbi2ernec1q8kffmghad7ai@4ax.com>`
- **References:** `<h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <415C20D0.18D9B20F@mb.sympatico.ca> <cjk0do0ipk@news2.newsguy.com>`

```
On 1 Oct 2004 16:25:28 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>
>In article <415C20D0.18D9B20F@mb.sympatico.ca>, Peter Lacey <lacey@mb.sympatico.ca> writes:
…[10 more quoted lines elided]…
>cantly smaller work factor than brute force?

Mr. Lacey is referring to differental cryptanalysis, which normally
requires _two_  known plaintexts. It looks for differences in the
encrypted version that depart from randomness. DES was designed to
resist this type attack. It works on other algorithms, but not DES.

>(I'm not sure what you're referring to with "the tediously reported
>cracking" anyway - I thought Robert was talking about one of those
>stupid cryptography-thriller movies, ie fiction. 

I was.

> There have been
>successful brute-force attacks against straight DES, with a 56-bit
>key.  I'm not aware of any successful brute-forcing or other attack
>against a DES variant with a key on the order of 128 bits, but this
>isn't really my area.)

One unclassified machine containing thousands of custom gate array
chips can process 90 billion keys per second. It takes, on average,
four days to find a 56-bit key. Using the same machine on a 128-bit
key would take 2^72 = 4722366482869645213696 * 4 days.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 15)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-10-04T15:21:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjrpp10dfb@news4.newsguy.com>`
- **References:** `<h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <415C20D0.18D9B20F@mb.sympatico.ca> <cjk0do0ipk@news2.newsguy.com> <q87rl01iot1kbi2ernec1q8kffmghad7ai@4ax.com>`

```

In article <q87rl01iot1kbi2ernec1q8kffmghad7ai@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 1 Oct 2004 16:25:28 GMT, mwojcik@newsguy.com (Michael Wojcik)
> wrote:
…[14 more quoted lines elided]…
> requires _two_  known plaintexts.

He may have been referring to differential cryptanalysis, but I
would be loathe to assume that.

DC requires *chosen* plaintext.  (That is, it doesn't work for any
arbitrary plaintext.)  And actually, it doesn't require known
plaintext; it requires that plaintext pairs have known characteristics
in their (bitwise exclusive-or) difference.

And a successful DC attack against DES with a 56-bit key requires
on the order of 2**47 plaintext pairs, not a single pair.  (Those
"pairs" could be one very long plaintext, of course, since blocks
are independent prior to the application of the cipher's combining
mode, which can be omitted when testing for characteristics.  But
that doesn't apply to the sort of message Peter was talking about.)

> It looks for differences in the
> encrypted version that depart from randomness.

Not quite.  DC uses the characteristics of the fixed S-boxes to
determine which n-round subkeys are more probable.  Given sufficient
"right pairs" (that is, pairs of plaintexts which satisfy high-
probability characteristics in their difference), you can determine
the subkey with a probability approaching 1.  Then you brute-force
the remaining bits of the full key.

> DES was designed to resist this type attack.
> It works on other algorithms, but not DES.

Oh, it works on DES.  It's just not practical.  The same applies to
many Feistel ciphers invented after 1990, and probably to some
invented before then, since the NSA knew about DC before it was
publically discovered (which is why DES' S-boxes are hardened against
it).

And DC is inapplicable to algorithms that aren't Feistel ciphers with
fixed (or trivially derived) S-boxes.

(Of course you're correct that brute-forcing a 128-bit key has a work
factor of 2**72 times that of brute-forcing 56-bit key.  It seemed
highly unlikely that anyone's brute-forced something of that size,
even with esoteric methods like the analog ones Rivest's been playing
with, but I was too lazy to look it up.)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 12)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-30T15:58:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebaol09ladpv2ko31vqr4qs7ahi9ksa9n5@4ax.com>`
- **References:** `<ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com>`

```
On Thu, 30 Sep 2004 09:19:17 -0400, Joe Zitzelberger
<joe_zitzelberger@nospam.com> wrote:

>The USMC hasn't done anything uniquely 'marine' since the second world 
>war, -- it has just fought alongside the army as more infantry.  In all 
…[4 more quoted lines elided]…
>that earns the corps a darwin award.

This is true. They never mentioned protecting your head in  boot camp
or advanced infantry training. I've seen covered foxholes in movies
but never on a real life Marine foxhole.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-10-01T15:29:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0410011429.3a03598d@posting.google.com>`
- **References:** `<ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <ebaol09ladpv2ko31vqr4qs7ahi9ksa9n5@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 

> This is true. They never mentioned protecting your head in  boot camp
> or advanced infantry training. 

Perhaps that's because they think it is your least important asset.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 12)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-10-01T06:49:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jcmdnXC3_NXU2cDcRVn-qA@giganews.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:
>
> That was intended to be something of a joke...I know that marines are
…[15 more quoted lines elided]…
> roof on the foxhole, did they".

Maybe the Marines knew the enemy did not have air-burst shells? Maybe there 
were not enough trees in the desert to build a roof? Maybe all the "Roof, 
portable foxhole, metal, Model 341" supplies were still on board supply 
ships in the Bering Sea. Maybe all the roofing material was requisitioned to 
build an army rear-area recreation hall?

It may also be part of the psyche: Marines have "camps" - the Army has 
"forts." Marines know that before they get the roof finished, they'll be 
moving out. The army would probably build a roof with rain gutters, lay in 
some carpet, and adjust their satellite TV antenna.

>
> The USMC hasn't done anything uniquely 'marine' since the second world
…[7 more quoted lines elided]…
> that earns the corps a darwin award.

I heard a correspondent commenting on troop morale in Iraq. He said: "Army 
morale is at virtually 100%... and twice that for the Marines."
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-10-01T08:54:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-0E0F9E.08542901102004@knology.usenetserver.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <jcmdnXC3_NXU2cDcRVn-qA@giganews.com>`

```
In article <jcmdnXC3_NXU2cDcRVn-qA@giganews.com>,
 "JerryMouse" <nospam@bisusa.com> wrote:

> Joe Zitzelberger wrote:
> >
…[27 more quoted lines elided]…
> some carpet, and adjust their satellite TV antenna.

You make them sound like the Air Force...
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2004-10-01T09:09:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjjkus$gqo$1@panix5.panix.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-0E0F9E.08542901102004@knology.usenetserver.com>`

```
In article <joe_zitzelberger-0E0F9E.08542901102004@knology.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <jcmdnXC3_NXU2cDcRVn-qA@giganews.com>,
> "JerryMouse" <nospam@bisusa.com> wrote:

[snip]

>> It may also be part of the psyche: Marines have "camps" - the Army has 
>> "forts." Marines know that before they get the roof finished, they'll be 
…[3 more quoted lines elided]…
>You make them sound like the Air Force...

I wasn't going to say anything, but...

... guess which branch issued *my* DD214?

DD
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 13)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-01T14:38:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g0oql0tqva9e629u3ol6aapp4vj6oue0tk@4ax.com>`
- **References:** `<%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <joe_zitzelberger-54FA8E.23031029092004@knology.usenetserver.com> <kainl05km1k9dfppa7auev0csf7sc6p86s@4ax.com> <joe_zitzelberger-C94AB0.09191730092004@knology.usenetserver.com> <jcmdnXC3_NXU2cDcRVn-qA@giganews.com>`

```
On Fri, 1 Oct 2004 06:49:30 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>It may also be part of the psyche: Marines have "camps" - the Army has 
>"forts." Marines know that before they get the roof finished, they'll be 
>moving out. The army would probably build a roof with rain gutters, lay in 
>some carpet, and adjust their satellite TV antenna.

The way it works today, construction would be outsourced (without
competitive bidding) to Halliburton, who'd hire former Special Forces
guys for $80K. They'd build roofs using ISO-9000 methodology, thereby
driving the cost up ten times. This makes everyone happy:
over-the-hill  grunts make twice what their warehouse jobs paid;
Halliburton execs book hundreds of millions in profit; bureaucrats
feel like puppet-masters; voters are pleased because Our Boys aren't
getting  killed; W gets reelected.

There a no monuments listing the names of civilian contractors.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-10-01T06:57:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T5adnQnAj8OK28DcRVn-qQ@giganews.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com>`

```
Robert Wagner wrote:
>
> You're a Tough Guy. USMC Special Ops had many tough guy wannabes. They
> were in the bottom quartile, usually had shaved heads and a lunatic
> look in their eyes. The real stars had no egotistical illusions. We
> relied on intelligence rather than bravado.

In other words, pussies.

Army rules:
1. If it moves, salute it.
2. If it doesn't move, pick it up.
3. If you can't pick it up, paint it.

Marine rules:
1. If it moves, kill it.
2. If it doesn't move, make sure it's dead.
3. If it's not dead, kill it.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-01T14:38:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mnpql098qou94iefpi10jea252uqo35qco@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <ftill01ade85nalb8k7pki31t8l7kkfrt2@4ax.com> <WIadnSQu1cmP2cbcRVn-ug@giganews.com> <0viml0dr04de0d64kopjh64nn8dqikge1u@4ax.com> <T5adnQnAj8OK28DcRVn-qQ@giganews.com>`

```
On Fri, 1 Oct 2004 06:57:12 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>Robert Wagner wrote:
>>
…[15 more quoted lines elided]…
>3. If it's not dead, kill it. 

Those are the infantry rules. The Recon rules are:

1.  If it moves, hide from it.
2.  If it doesn't move, hide behind it.
3.  If they spot you, get the hell out of there. This is why you
practiced running six minute miles all day.
4.  Never carry more than 20 pounds.
5.  Never use paths; always go cross-country.
6.  Stay downwind. Animals will give you away.
7.  If all else fails, intimidate them with firepower.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-29T12:03:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409291103.6e8358b7@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> Not so. XP users need not download JVM from Sun.
> 
> They can actually they should do the reverse - purge all reference to Java 
> from their system.

And, of course, vice versa, Java users should purge all reference to
XP from their machines.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-29T18:18:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N7WdnZozieMi38bcRVn-tA@giganews.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <217e491a.0409291103.6e8358b7@posting.google.com>`

```
Richard wrote:
> "JerryMouse" <nospam@bisusa.com> wrote
>
…[6 more quoted lines elided]…
> XP from their machines.

Couldn't agree more. But tell me, does XP exist on a toaster?
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-29T22:54:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409292154.26ec72a1@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <%id6d.33140$vl.9276@fe40.usenetserver.com> <h8pil096f5m46fvlpar6pldbelso76ceof@4ax.com> <ncWdnaNU24HqLMfcRVn-tg@giganews.com> <217e491a.0409291103.6e8358b7@posting.google.com> <N7WdnZozieMi38bcRVn-tA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 


> Couldn't agree more. But tell me, does XP exist on a toaster?

No, they don't make 2.5GHz, 512MByte 80GB toasters.
```

###### ↳ ↳ ↳ Re: a history question

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-28T17:42:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjc7qg02m2s@news4.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>`

```

In article <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> 
> Interpreted pseudo-code has been re-invented a hundred times. Users
> pay the high price every time they execute a program. 

The height of the price is relative.  Not all applications are
performance-critical, and there are numerous advantages to run-time
interpretation.

Essentially every program not written by IBM for the AS/400 is
interpreted, whether it's an OPM, EPM, or ILE binary.  People are
still buying AS/400s.

> The JVM is no longer an interpreter; it's now a JIT compiler back-end.
> It translates intermediate code into machine language the first time a
> program is touched. Dot-NET works the same way.

JIT schemes differ among JVMs.  The last time I checked, the Sun
HotSpot JIT compiled frequently-visited code blocks (as the name
implies), not entire programs.  That's been a popular technique in
JIT compilation for emulators as well.

> Micro Focus produces pseudo-code by default, in a file named .int. The
> runtime interpreter is cobrun. Cobcrawl would be more accurate.

Yet many of our customers - who could switch to generated code by
adding a single flag to their compilation command lines - continue to
use interpreted code.  Apparently the price isn't high enough to make
them add that one flag.

> Programs execute six times slower than native code, which is the
> typical ratio for interpreters. 

Closer to a factor of ten, on modern processors, in the studies I've
seen.  True code interpreters have to look up each instruction in
some kind of translation table.  Those tables rarely fit in cache, so
if the instruction mix is evenly distributed across the table, you
get a cache miss on every (size of table) / (size of cache line)
instruction, on average.  In practice, tables can be and are arranged
to group pseudo-ops by their expected frequency of use, which reduces
the penalty somewhat, but caching effects still dominate.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-09-28T19:27:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zWi6d.2052$q67.1851@newssvr11.news.prodigy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com>`

```
"Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
news:cjc7qg02m2s@news4.newsguy.com...
[snip]
> Closer to a factor of ten, on modern processors, in the studies I've
> seen.  True code interpreters have to look up each instruction in
…[5 more quoted lines elided]…
> the penalty somewhat, but caching effects still dominate.

Michael,

Don't sell your interpreter (or ours) too short...

In my experience, the 10x factor you mention holds for compute bound 
programs only, which is hardly the normal COBOL program.  Given the frequent 
excursions to library routines, mostly for I/O but also for some of the more 
complex COBOL semantics, the 10x does not hold up.  The 10x also is 
attacked, as you suggest, by careful and creative interpreter design, much 
as the semiconductor designers recognize special performance bottlenecks and 
apply transistors.

I think that your (and our) customers are willing to use interpretive object 
because (1) it meets there needs, and (2) it is *much* more convenient.

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-28T20:44:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjcif00no7@news1.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com>`

```

In article <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com>, "Tom Morrison" <t.morrison@liant.com> writes:
> "Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
> news:cjc7qg02m2s@news4.newsguy.com...
…[7 more quoted lines elided]…
> programs only, which is hardly the normal COBOL program.

Right.  What I meant was "closer to a factor of ten, while actually
executing interpreted code".  Thanks for the clarification.

> Given the frequent 
> excursions to library routines, mostly for I/O but also for some of the more 
> complex COBOL semantics, the 10x does not hold up.

True.  COBOL code that relies heavily on statements that perform
relatively complex processing - eg INSPECT - do relatively more work
per COBOL statement, so they hit the interpretation penalty less
frequently.

> The 10x also is 
> attacked, as you suggest, by careful and creative interpreter design, much 
> as the semiconductor designers recognize special performance bottlenecks and 
> apply transistors.

Well, yes, but ultimately interpreters always run afoul of data-cache
penalties, if the code being interpreted has more symbols than will
fit in a cache line.  There's no way around that.  (On the other hand,
plenty of directly-executed code has caching problems, too.)

> I think that your (and our) customers are willing to use interpretive object 
> because (1) it meets there needs, and (2) it is *much* more convenient.

Yup.  There are certainly COBOL applications which want the performance
advantage of running executable code, but my feeling is that they're a
small minority.  Most COBOL applications are probably I/O-bound, and in
many cases the majority of that is waiting on user input anyway.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-09-29T13:21:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<415AFD11.D931546D@mb.sympatico.ca>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com>`

```
Tom Morrison wrote:
> 
><snip>

> I think that your (and our) customers are willing to use interpretive object
> because (1) it meets there needs, and (2) it is *much* more convenient.
> 
> Tom Morrison
> Liant Software Corporation

I don't get this.  Why is interpreted code more convenient than compiled
code?  In my experience, once people learn how to do something they do
it as routine.  They may have some trouble during the learning phase, to
be sure, but from then on they never think about it.

PL
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-09-29T21:38:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cXF6d.363$d_7.99@newssvr30.news.prodigy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com> <415AFD11.D931546D@mb.sympatico.ca>`

```
"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message 
news:415AFD11.D931546D@mb.sympatico.ca...
> Tom Morrison wrote:
>>
…[12 more quoted lines elided]…
> be sure, but from then on they never think about it.

Peter,

It has to do with the nature of the customer.  RM/COBOL object code (and 
data files, for that matter) is 100% portable across a wide variety of 
machines.

Best regards,
Tom Morrison
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-09-29T19:53:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<415B5918.5C72A298@mb.sympatico.ca>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com> <415AFD11.D931546D@mb.sympatico.ca> <cXF6d.363$d_7.99@newssvr30.news.prodigy.com>`

```
Tom Morrison wrote:
> 
> "Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
…[24 more quoted lines elided]…
> Tom Morrison

Ah.  I didn't realize that you were talking portability.  Case closed. 
(Although of course RM can't claim this as an exclusive IIRC).

PL
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T21:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u15ml0tfg6lkqgu1tiuflv7qto6i7kpcn0@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com> <415AFD11.D931546D@mb.sympatico.ca>`

```
On Wed, 29 Sep 2004 13:21:05 -0500, Peter Lacey
<lacey@mb.sympatico.ca> wrote:

>Tom Morrison wrote:
>> 
…[9 more quoted lines elided]…
>code? 

The convenience is portability. It will run on other platforms without
recompilation.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-29T15:21:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409291421.7f14fdb3@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <zWi6d.2052$q67.1851@newssvr11.news.prodigy.com> <415AFD11.D931546D@mb.sympatico.ca>`

```
Peter Lacey <lacey@mb.sympatico.ca> wrote 

> I don't get this.  Why is interpreted code more convenient than compiled
> code?  In my experience, once people learn how to do something they do
> it as routine.  They may have some trouble during the learning phase, to
> be sure, but from then on they never think about it.

In the case of a software house, or any shop where there is a mixture
of different machine types, the use of .int code is far more
convenient to develop, test and distribute than any other form - there
is only one set of files to distribute no matter what the target
machine is.

With compiled code it is necessary to create a different set for each
machine type, to have a machine available of that type, at least for
testing, and to maintain separate distributions.

You may not see this as a problem, but the clients of Liant take that
route because they have that problem and RM Cobol is the solution (or
at least, one solution).
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T00:23:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com>`

```
On 28 Sep 2004 17:42:40 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>In article <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
>> 
>> Interpreted pseudo-code has been re-invented a hundred times. Users
>> pay the high price every time they execute a program. 

>Essentially every program not written by IBM for the AS/400 is
>interpreted, whether it's an OPM, EPM, or ILE binary.  People are
>still buying AS/400s.

Nearly all modern CISC processors (except Itanium) use microcode to
translate instructions. That's not called  'interpretation'.

>Yet many of our customers - who could switch to generated code by
>adding a single flag to their compilation command lines - continue to
>use interpreted code.  Apparently the price isn't high enough to make
>them add that one flag.

I worked at a place like that. They complained about the daily batch
job taking 8-14 hours. The manager watched me run a timing test (no
I/O) interpreted vs. compiled. The difference was 6x. Their solution,
of course, was to buy a faster machine, which ran the daily batch in
2-3 hours .. still in interpreted mode. 

I 'accidentally' compiled one of the batch programs to .gnt. It did a
lot of I/O, so it didn't run 6x faster, but it did run 2x faster. 

What's the difference between ignorance and indifference?
I don't know and I don't care.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-29T16:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjenan02kn2@news4.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com>`

```

In article <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 28 Sep 2004 17:42:40 GMT, mwojcik@newsguy.com (Michael Wojcik)
> wrote:
…[6 more quoted lines elided]…
> translate instructions. That's not called  'interpretation'.

That's not what I'm talking about, either.  On the AS/400, only IBM
LIC (Licensed Internal Code) is compiled to machine language.  Every-
thing else is compiled to an intermediate form called "MI" ("machine
instructions", though it has nothing to do with the actual CPU
opcodes), and compiled MI is interpreted at runtime.

> >Yet many of our customers - who could switch to generated code by
> >adding a single flag to their compilation command lines - continue to
…[4 more quoted lines elided]…
> job taking 8-14 hours.

Then it wasn't a place like the sort I described, where the
performance cost of using interpreted code isn't important.  If
they're complaining about it taking too long, then it's important.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T21:56:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com>`

```
On 29 Sep 2004 16:19:35 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>In article <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
>> On 28 Sep 2004 17:42:40 GMT, mwojcik@newsguy.com (Michael Wojcik)
…[13 more quoted lines elided]…
>opcodes), and compiled MI is interpreted at runtime.

At program start/load time, MI is 'translated' to PowerPC opcodes. The
process is similar to 'compiling' bytecode to native.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 7)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-10-01T16:32:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjk0q70181p@news1.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com>`

```

In article <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 29 Sep 2004 16:19:35 GMT, mwojcik@newsguy.com (Michael Wojcik)
> wrote:
…[19 more quoted lines elided]…
> process is similar to 'compiling' bytecode to native.

First, that would still be entirely unrelated to CPU microcode
translation.

Second, POWER processors are not CISC, so your comment about CISC
processors and microcode translation is irrelevant.

Third, I am at a loss to find a single AS/400 model with a PowerPC
processor.  Aside from the long-discontinued CISC models, they all
seem to use PowerAS, POWER4, or POWER5.  So translating OS/400
program code to PPC opcodes would be suboptimal.

Fourth, care to provide a reference to support your claim?
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-01T19:18:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com>`

```
On 1 Oct 2004 16:32:07 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>
>In article <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
…[27 more quoted lines elided]…
>processors and microcode translation is irrelevant.

An AS/400 programmer told me translation was done by microcode.
Research showed that's incorrect; it is done by software (SLIC).

>Third, I am at a loss to find a single AS/400 model with a PowerPC
>processor.  Aside from the long-discontinued CISC models, they all
>seem to use PowerAS, POWER4, or POWER5.  So translating OS/400
>program code to PPC opcodes would be suboptimal.

Picky, picky. See below. AS is a PowerPC with about 20 additional
instructions.

>Fourth, care to provide a reference to support your claim?

" The MI instructions are translated by SLIC into PowerPC AS  machine
instructions.  MI objects are likewise translated into underlying
machine data structures and machine instructions."

pages.sbcglobal.net/vleveque/AS400_Arch.doc
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-10-01T12:35:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjkbhj$q85$1@si05.rsvl.unisys.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com...

> An AS/400 programmer told me translation was done by microcode.
> Research showed that's incorrect; it is done by software (SLIC).

Just out of curiosity, why would you categorically exclude "microcode" from
the realm of "software"?   I recognize that sometimes it's encoded in ROM or
some otherwise non-alterable medium once it's been written, but I also
recognize that sometimes it's not.

Heck, I've even worked on systems where the "user-visible" instruction set
was handled by two *layers* of code -- one "microcode", one "nanocode", both
retrieved off disk at system boot into non-user-accessible memory whence it
was run -- above the actual hardware.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-02T01:17:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <cjkbhj$q85$1@si05.rsvl.unisys.com>`

```
On Fri, 1 Oct 2004 12:35:14 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
…[6 more quoted lines elided]…
>the realm of "software"?  

I'm just using common terminology, which distinguishes microcode from
software amenable to system programmer modification.

I've read microcode, but never had occasion to write it.

>Heck, I've even worked on systems where the "user-visible" instruction set
>was handled by two *layers* of code -- one "microcode", one "nanocode", both
>retrieved off disk at system boot into non-user-accessible memory whence it
>was run -- above the actual hardware.

When I was running and publishing benchmarks, someone wrote the Sieve
in microcode. The assembly language program executed a single
instruction. He blew away the competition .. with a low-speed
processor.

It seems to me compilers could 'micro-optimize' by creating custom
instructions for very common functions.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-10-04T09:20:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjrt84$2t0g$1@si05.rsvl.unisys.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <cjkbhj$q85$1@si05.rsvl.unisys.com> <obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com...

> >Just out of curiosity, why would you categorically exclude "microcode"
from
> >the realm of "software"?
>
> I'm just using common terminology, which distinguishes microcode from
> software amenable to system programmer modification.

"Common terminology?"  The 1984-vintage Webster's Eighth Collegiate has
"microcode: code used in microprogramming" and "microprogramming:  the use
of routines stored in memory rather than specialized circuits to control a
device (as a computer)".   "... Distinguish[ed] from software amenable to
system programmer modification" and similar sentiments do not appear in the
definitions in Webster's online, in Brittanica online, or even in Wikipedia
as I see it.

How, by the way, would you define "amenable to system programmer
modification?"  Would the writing of microcode in a language with which most
"system programmers" are unfamiliar qualify as rendering the writing of
microcode "unamenable" to such programmers?  What of implementations that go
quite a distance out of their way to make sure their customers *don't need*
system programmers in the first place?  What is a "system programmer" in
such an environment?

And to carry it one step further:  I know of an implementation in which the
very class of software of which you speak, according to your own definitions
would be considered "microcode" to a commercial customer and "software" to
the university next door -- because the university next door had access to
the Micro Implementation Language compiler that allowed them to write their
own microcode (or modify existing microcode) as part of a Computer Science
curriculum or for purposes of their own internal language research projects,
a privilege not granted to (or particuarly desired by) commercial customers
who were only concerned about making sure their RPG, COBOL and FORTRAN
programs produced the results they desired in a timely manner.

> I've read microcode, but never had occasion to write it.

I've read it, played with it enough to figure out what I needed to know
about the hardware implementation and the way it interacted with the object
code generated by the user-language compilers, but never contributed
anything productive.

> When I was running and publishing benchmarks, someone wrote the Sieve
> in microcode. The assembly language program executed a single
…[4 more quoted lines elided]…
> instructions for very common functions.

Ummm ... yeah ... like ADD and MOVE and even the likes of Function SQRT
should the compiler writers elect to take advantage of the hardware support
provided to other languages ... Is that somehow *news* to any of the
readership of this forum?   ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 12)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-05T01:40:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnp3m0t281ukogsgdo60csop2u9ul3nskg@4ax.com>`
- **References:** `<bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <cjkbhj$q85$1@si05.rsvl.unisys.com> <obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com> <cjrt84$2t0g$1@si05.rsvl.unisys.com>`

```
On Mon, 4 Oct 2004 09:20:20 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
…[15 more quoted lines elided]…
>as I see it.

Webster's definition of microinstruction (syn. microcode)
distinguishes it from machine language:

"a computer instruction that activates the circuits necessary to
perform a single machine operation usually as part of the execution of
a machine-language instruction "

>How, by the way, would you define "amenable to system programmer
>modification?"  Would the writing of microcode in a language with which most
…[4 more quoted lines elided]…
>such an environment?

A system programmer is one who modifies, extends or creates an
operating system and/or general purpose tools such as compilers and
text editors.  A microcode engineer (sometimes firmware engineer) is
one who modifies or creates microcode. Microcode engineers work for
the computer manufacturer. 

If microcode can be modified in the field i.e. is not in ROM, a system
programmer has opportunity to modify it or create custom instructions.
Of course, doing so voids manufacturer support. For this reason,
system programmers working for commercial end-users are reluctant to
mess with microcode. 

>And to carry it one step further:  I know of an implementation in which the
>very class of software of which you speak, according to your own definitions
…[7 more quoted lines elided]…
>programs produced the results they desired in a timely manner.

What about their C++ and Java programs?

>> When I was running and publishing benchmarks, someone wrote the Sieve
>> in microcode. The assembly language program executed a single
…[9 more quoted lines elided]…
>readership of this forum?   ...

I was thinking of looping operations with an expensive Branch/Jump.
For example, measuring the length of a string.

Burroughs Medium Systems generated one machine instruction for nearly
every Cobol statement. ADD a binary number to a display number? One
instruction. MOVE a binary number to a packed number? One instruction.
The size of executables and execution time was one third that of other
machines with comparable clock speed.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 13)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-10-05T09:26:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjuhvd$1kq8$1@si05.rsvl.unisys.com>`
- **References:** `<bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <cjkbhj$q85$1@si05.rsvl.unisys.com> <obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com> <cjrt84$2t0g$1@si05.rsvl.unisys.com> <cnp3m0t281ukogsgdo60csop2u9ul3nskg@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:cnp3m0t281ukogsgdo60csop2u9ul3nskg@4ax.com...

> Webster's definition of microinstruction (syn. microcode) ...

Nope.  The text you cite appears to be from the Merriam-Webster Online
Dictionary at  www.merriamwebster.com, but that entry does *not* list
"microcode" as a synonym for "microinstruction".

Under "microcode", it does have "the microinstructions esp. of a
microprocessor".  That does not make the two terms synonymous, it means that
"microcode" *consists of* microinstructions.


> A system programmer is one who modifies, extends or creates an
> operating system and/or general purpose tools such as compilers and
> text editors.

In environments in which systems programmers are not typically necessary,
it's quite likely that one person will wear many hats!

>A microcode engineer (sometimes firmware engineer) is
> one who modifies or creates microcode. Microcode engineers work for
> the computer manufacturer.

Always and unconditionally?   I remember a DP manager who compiled the I/O
microcode for his Burroughs system, bound the listing and used it as his
bathroom reading material.

> If microcode can be modified in the field i.e. is not in ROM, a system
> programmer has opportunity to modify it or create custom instructions.

So does a computer science professor researching the best way to implement
the constructs of a language.  What's your point?

> Of course, doing so voids manufacturer support.

Always and unconditionally?

>For this reason, system programmers working for commercial end-users are
reluctant to
> mess with microcode.

May be.  Their reluctance is on them, not on the manufacturer, *if* the
manufacturer has made the tools available!

> >And to carry it one step further:  I know of an implementation in which
the
> >very class of software of which you speak, according to your own
definitions
> >would be considered "microcode" to a commercial customer and "software"
to
> >the university next door -- because the university next door had access
to
> >the Micro Implementation Language compiler that allowed them to write
their
> >own microcode (or modify existing microcode) as part of a Computer
Science
> >curriculum or for purposes of their own internal language research
projects,
> >a privilege not granted to (or particuarly desired by) commercial
customers
> >who were only concerned about making sure their RPG, COBOL and FORTRAN
> >programs produced the results they desired in a timely manner.
>
> What about their C++ and Java programs?

What about them?  The particular microcoded system I'm talking about never
had need for either one of these languages (though it did get a nice Pascal
compiler late in its marketing life).  Its manufacturer decided to
discontinue development of future models in the early 1980's, at which point
in history neither C++ nor Java were yet of much general interest in that
particular market.   Had there been any sort of demand for either or both of
these languages back in the 1970's on this class of machines (which was
originally targeted against the System/3), such programs would have been
accommodated  by Burroughs providing compilers, and microcode, supporting
them.  There wasn't.  I don't know of very many preexisting C++ or Java
applications that someone would have wanted to "port" to this particular
system in the 1970's, or even the 1980's.

> I was thinking of looping operations with an expensive Branch/Jump.

What do you think of looping operations with an *inexpensive* Branch/Jump?
Or is that another one of those things that nobody could possibly ever have?

> For example, measuring the length of a string.

Which is why some implementations and some designs of strings prefix them
with their length so that a user can determine immediately how long they are
rather than using a delimiter that requires them to figure that out!

> Burroughs Medium Systems generated one machine instruction for nearly
> every Cobol statement. ADD a binary number to a display number? One
> instruction. MOVE a binary number to a packed number? One instruction.
> The size of executables and execution time was one third that of other
> machines with comparable clock speed.

Of course.  And the Burroughs B1000 COBOL instruction set looked a lot like
the Medium System instruction set.  And the Burroughs B1000 FORTRAN
instruction set looked a lot like the Large System instruction set.  A
full-blown B1000 could give a medium-sized Medium System a run for its money
in COBOL and RPG, could run circles around a B5900 in Fortran, and there
were certain packaged application environments using COBOL74 and DMSII in
which I wouldn't have been afraid to benchmark a fully-configured B1900
against a small-to-medium-sized B7900!   The performance of the high end of
the Burroughs Small System overlapped that of the low end of the Burroughs
Large System.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 14)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-05T23:47:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ia36m0t2r7f4npircicmcnj4hecl58edng@4ax.com>`
- **References:** `<ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <cjkbhj$q85$1@si05.rsvl.unisys.com> <obrrl0piik4vm9k1ic73b3sou4cf0ee5kj@4ax.com> <cjrt84$2t0g$1@si05.rsvl.unisys.com> <cnp3m0t281ukogsgdo60csop2u9ul3nskg@4ax.com> <cjuhvd$1kq8$1@si05.rsvl.unisys.com>`

```
On Tue, 5 Oct 2004 09:26:21 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
>news:cnp3m0t281ukogsgdo60csop2u9ul3nskg@4ax.com...

>> A system programmer is one who modifies, extends or creates an
>> operating system and/or general purpose tools such as compilers and
…[3 more quoted lines elided]…
>it's quite likely that one person will wear many hats!

I have, even on systems where system programmers ARE typically
necessary.  When one is wearing the hat, he IS a system programmer.

>>A microcode engineer (sometimes firmware engineer) is
>> one who modifies or creates microcode. Microcode engineers work for
…[4 more quoted lines elided]…
>bathroom reading material.

Of course not always. 
>
>> If microcode can be modified in the field i.e. is not in ROM, a system
…[3 more quoted lines elided]…
>the constructs of a language.  What's your point?

My point is that a system programmer can wear the hat of microcode
engineer.

>> Of course, doing so voids manufacturer support.
>
>Always and unconditionally?

I assumed it did, without checking. Seems reasonable.

>>For this reason, system programmers working for commercial end-users are
>reluctant to
…[3 more quoted lines elided]…
>manufacturer has made the tools available!

The manufacturer can't support user-developed code.

>> I was thinking of looping operations with an expensive Branch/Jump.
>
…[7 more quoted lines elided]…
>rather than using a delimiter that requires them to figure that out!

The issue is languages. Pascal uses that style. Cobol can (via ODO)
but the practice is discouraged. The basic Cobol string is delimited
by size and padded with spaces. 

Databases use that style, but conversion to Cobol with ODO is usually
not supported. Strings are most often padded with spaces. Does Unisys
DMS convert to ODO?

> the Burroughs B1000 COBOL instruction set looked a lot like
>the Medium System instruction set.  And the Burroughs B1000 FORTRAN
…[7 more quoted lines elided]…
>Large System.

AS/400 proponents say the same vs. low-end S/390. Sun and HP
proponents compare themselves to mid-range S/390. Sounds to me like
envy.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 9)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-10-06T15:34:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ck13ak01cdu@news4.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>`

```

In article <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 1 Oct 2004 16:32:07 GMT, mwojcik@newsguy.com (Michael Wojcik)
> wrote:
…[23 more quoted lines elided]…
> instructions.

I'll grant that was a nit.  However, the differences between PowerPC
and PowerAS are central to AS/400 architecture, including as they do
support for tag bits and single-level store.

> >Fourth, care to provide a reference to support your claim?
> 
…[4 more quoted lines elided]…
> pages.sbcglobal.net/vleveque/AS400_Arch.doc

I remain dubious.  First, note this document also claims:

   The SLIC supports the Machine Interface(MI), an abstract system
   interface.  The SLIC interprets MI commands and executes them on the
   hardware.  The MI is an abstract machine, presenting itself to the
   system user as the lowest level of machine architecture directly
   accessible.

which appears to support my claim.

Second, the passage you cited is vague; "translated" could mean JIT
compilation of MI pseudo-ops into native operations, or it could mean
table-based interpretation.

Third, it's not clear just how reliable LeVeque's sources are.  He
doesn't have any IBM Research pubs to cite, for example - probably
because IBM is relatively close-mouthed about just how the '400
works.  (Contrast the first generation of RS/6000, for example -
IBM published _RISC System/6000 Technology_, SA23-2619, with copies
of papers by Phil Hester and other RS/6000 designers.)

I'll grant that I haven't found any definitive sources for my
position on this matter either, though, so for the moment I'm
considering this unresolved.  MI may be interpreted or it may be JIT-
compiled.  (And the details may have changed between AS/400 genera-
tions, of course; the original AS/400s, particularly the little
B-series machines, sure didn't seem to be doing any compilation to
native code.  Often they didn't seem to be doing anything at all.
Used to kick off a build, then go and work on another platform for
the rest of the day...)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-07T08:31:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s799m0tufhvdb0m2dlbep8j4rv7h7ca11c@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <ck13ak01cdu@news4.newsguy.com>`

```
On 6 Oct 2004 15:34:44 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>
>In article <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
…[68 more quoted lines elided]…
>the rest of the day...)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-07T16:54:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p6pam01it7sjaotvqmf4q6ahmk6hqqnoru@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <ck13ak01cdu@news4.newsguy.com>`

```
On 6 Oct 2004 15:34:44 GMT, mwojcik@newsguy.com (Michael Wojcik)
wrote:

>
>In article <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
…[47 more quoted lines elided]…
>which appears to support my claim.

It could be read either way -- JIT compiler or interpreter. If SLIC
were interpreting MI, performance would be terrible. 

>I'll grant that I haven't found any definitive sources for my
>position on this matter either, though, so for the moment I'm
…[6 more quoted lines elided]…
>the rest of the day...)

The few AS/400s I've worked on ran close to expected speed, just a
little slow. If they had been interpreted, I'd have known right away.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 11)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-10-09T00:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ck7cln0g1p@news2.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com> <lutjl059ngc1i43jthuakhr9oba7s85rm7@4ax.com> <cjenan02kn2@news4.newsguy.com> <3jrll052kop5n7h9vriniaacnr7r01hh2t@4ax.com> <cjk0q70181p@news1.newsguy.com> <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com> <ck13ak01cdu@news4.newsguy.com> <p6pam01it7sjaotvqmf4q6ahmk6hqqnoru@4ax.com>`

```

In article <p6pam01it7sjaotvqmf4q6ahmk6hqqnoru@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 6 Oct 2004 15:34:44 GMT, mwojcik@newsguy.com (Michael Wojcik) wrote:
> >In article <cs9rl0l4ihrarb5amk8lev5e755a47opoc@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
…[20 more quoted lines elided]…
> It could be read either way -- JIT compiler or interpreter.

Reading "interprets MI commands and executes them on the hardware"
as "JIT-compiles them" is quite a gloss.

> If SLIC were interpreting MI, performance would be terrible. 

"terrible" is relative.  Hercules running on a modern PC is faster
than any of the mainframes that would have run the version of MVS
that it uses when it was new, and it's interpreting 370 opcodes.
People use Hercules, and people used the 370s it emulates when they
were slower than it is now.

> The few AS/400s I've worked on ran close to expected speed, just a
> little slow. If they had been interpreted, I'd have known right away.

I hope you'll forgive me if I don't take your claim of oracular
ability to discern interpretation at face value.  I'd need something
just a bit more specific than "expected speed" and "a little slow",
and something rather stronger and more concrete than "known right
away".
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-28T19:03:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409281803.74081b54@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <cjc7qg02m2s@news4.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote

> Yet many of our customers - who could switch to generated code by
> adding a single flag to their compilation command lines - continue to
> use interpreted code.  Apparently the price isn't high enough to make
> them add that one flag.

I recall using Level II Cobol on Concurrent-DOS on an ICL PC2 8088
4MHz with 1 MByte of RAM.  The run-time ran as shared code so only one
copy existed in the machine for the 3 or 4 users that had terminals to
it.  It used .int rather than .gnt because the .gnts were 3 times the
size in the procedure division and that could not be afforded.

There was always spare CPU time, but the uncached 20MByte disks were
rather slow. At least the OS was sophisticated enough to recover CPU
time during async disk access, something that MS didn't do for another
10 years.
```

###### ↳ ↳ ↳ Re: a history question

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-28T12:06:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409281106.5a87c51a@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

> Both are proprietary, profit-making and rigged to
> put the competition at a disadvantage. 

Just as any business does, such as MicroFocus or Fujitsu.

> The JVM is Sun's proprietary language and software platform.

Actually there are several independent implementations including IBMs
and the open source Kaffe.

> Interpreted pseudo-code has been re-invented a hundred times. Users
> pay the high price every time they execute a program. 

On _some_ systems that is true.

BTW, by convention, 'pseudo-code' is a textural way of writing a
program outline without using a specific language.  p-code or
byte-code is used as the term for these intermediate codes.
 
> Micro Focus produces pseudo-code by default, in a file named .int. The
> runtime interpreter is cobrun. Cobcrawl would be more accurate.
> Programs execute six times slower than native code, which is the
> typical ratio for interpreters.

But in typical applications which use disk access and screen i/o or
gui the difference in overall performance is insignificant.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-29T00:23:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ssjl05olvvcfajt6kctk1fncbmdqjj6cp@4ax.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <217e491a.0409281106.5a87c51a@posting.google.com>`

```
On 28 Sep 2004 12:06:19 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

>> The JVM is Sun's proprietary language and software platform.
>
>Actually there are several independent implementations including IBMs
>and the open source Kaffe.

They signed a license agreement requiring them to play by Sun's rules,
as did Microsoft.

>BTW, by convention, 'pseudo-code' is a textural way of writing a
>program outline without using a specific language.  p-code or
>byte-code is used as the term for these intermediate codes.

I stand corrected. Many definitions say P stands for Pascal.
 
>> Micro Focus produces pseudo-code by default, in a file named .int. The
>> runtime interpreter is cobrun. Cobcrawl would be more accurate.
…[4 more quoted lines elided]…
>gui the difference in overall performance is insignificant.

It would be interesting to see TPC-C benchmarks both ways. That's a
respected test of OLTP on 'typical business applications'.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-29T01:50:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409290050.69ae6e94@posting.google.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <217e491a.0409281106.5a87c51a@posting.google.com> <5ssjl05olvvcfajt6kctk1fncbmdqjj6cp@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 

> >Actually there are several independent implementations including IBMs
> >and the open source Kaffe.
> 
> They signed a license agreement requiring them to play by Sun's rules,
> as did Microsoft.

Geez, Robert, do you just make this stuff up ?  Do you think it is
only necessary to check _after_ you have spread misinformation ?  Once
you have formed a conclusion you just make up 'facts' to fit.

"""Kaffe is not an officially licensed version of the Java virtual
machine. In fact, it contains no Sun source code at all, and was
developed without even looking at the Sun source code. It is legal --
but Sun controls the Java trademark, and has never endorsed Kaffe, so
technically, Kaffe is not Java."""

Kaffe, Japhar and GCJ could not be GPLed if they were, in turn,
subject to Sun's licencing.

Nor could IBM's Jikes be put out under IBM's Public Licence.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-29T16:54:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cjepbd0u1m@news2.newsguy.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <ck6il0lj299ho1d0ipniqlaav5ae87gsor@4ax.com> <217e491a.0409281106.5a87c51a@posting.google.com> <5ssjl05olvvcfajt6kctk1fncbmdqjj6cp@4ax.com>`

```

In article <5ssjl05olvvcfajt6kctk1fncbmdqjj6cp@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> On 28 Sep 2004 12:06:19 -0700, riplin@Azonic.co.nz (Richard) wrote:
>
…[4 more quoted lines elided]…
> respected test of OLTP on 'typical business applications'.

Recompiling the TPC-C application from .int to .gnt made only a small
difference in tpm/C.  It did drop average response time somewhat,
indicating there might be more margin for adding more clients, but at
the time we were an order of magnitude under the limit allowed by the
spec, so it's hard to say how much of a difference it really would
have made - comms or something else besides CPU capacity might well
have been the limiting factor.

Profiling typically showed int-code interpretation was less of the
total processor time than processing the user I/O stream - that's
not including the actual I/O time, just the time taken to process
the data from the screen into working storage, and back from working
storage to output.  In one typical run, the worst case for int-code
interpretation among all the COBOL runtime processes was 22% of the
time that process was in run state, but the total run state time for
that process was negligible - less that 0.01% of the profiling
interval.  int-code interpretation didn't even show up on the profile
of the busiest COBOL runtime, which was dominated by calls to the
DBMS interface.

Any information about these specific tests beyond that is proprietary
and confidential, I'm afraid.

TPC-C does not do much computation.  None of the TPC-C modules are
very large.  (In fact, there's probably more computation required in
the TPC-C *client* than there is in the server application itself,
since the client has to generate pseudorandom think times based on
a specific generator mandated by the spec and so forth.)  So for it
interpretation basically comes down to caching effects.

Because TPC-C is inherently a highly-parallel test with lots of
(simulated) users performing the same small set of tasks, there's a
lot of duplicated references to the same code and data, which tends
to reduce adverse cache effects.
```

##### ↳ ↳ Re: a history question

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-28T09:06:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-36A6A2.09063028092004@knology.usenetserver.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com>`

```
In article <bt26d.31986$vl.17062@fe40.usenetserver.com>,
 LX-i <lxi0007@netscape.net> wrote:

> I can't take a PC-based executable programmed in COBOL, FTP it up to the 
> Unisys mainframe, and expect it to do run.  Now, if I have the source, 
…[3 more quoted lines elided]…
> 36-bit-word architecture.  :)

Why not?  You can do that on a Mac.  And you could do that on an Amiga 
(IIRC).  Is Unisys slacking?


> To the best of my knowledge, Java was the first language to use a 
> bytecode interpreter - so, it's still interpreted (like a scripting 
> language), but it's faster because it doesn't also have to translate the 
> source to machine code at runtime.  If it wasn't the first, it's 
> definitely the most popular.

There was the UCSD Pascal system in the late 70's / early 80's that did 
bytecodes and had portable objects -- it it was sooooooooo sloooooooow 
on those machines that it just was not workable.
```

###### ↳ ↳ ↳ Re: a history question

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-28T16:38:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tRk6d.1$uO6.0@fe40.usenetserver.com>`
- **In-Reply-To:** `<joe_zitzelberger-36A6A2.09063028092004@knology.usenetserver.com>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <bt26d.31986$vl.17062@fe40.usenetserver.com> <joe_zitzelberger-36A6A2.09063028092004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:
> In article <bt26d.31986$vl.17062@fe40.usenetserver.com>,
>  LX-i <lxi0007@netscape.net> wrote:
…[11 more quoted lines elided]…
> (IIRC).  Is Unisys slacking?

I'm sure that falls under the realm of "we've never had a requirement 
for it".  :)  There is a JVM, though.
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-09-29T07:56:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Hnf8-UeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <joe_zitzelberger-36A6A2.09063028092004@knology.usenetserver.com> <tRk6d.1$uO6.0@fe40.usenetserver.com>`

```
.    Am  28.09.04
schrieb  lxi0007@netscape.net (LX-i)
    auf  /COMP/LANG/COBOL
     in  tRk6d.1$uO6.0@fe40.usenetserver.com
  ueber  Re: a history question

>> Why not?  You can do that on a Mac.  And you could do that on an Amiga
>> (IIRC).  Is Unisys slacking?

l> I'm sure that falls under the realm of "we've never had a requirement
l> for it".  :)  There is a JVM, though.

   But there were Pascal compilers for the 1100. The one of the UCS  
suite has apparently been withdrawn because of a lack of customer  
demand. Before UCS Pascal, I had a free Pascal compiler which I used  
for some small programs.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Die Interessen der Nation lassen sich nicht anders formulieren als unter
dem Gesichtspunkt der herrschenden Klasse oder der Klasse, die die
Herrschaft anstrebt."            - Leo Trotzki         (27. Januar 1932)
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-29T17:26:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5EG6d.1938$Za.618@fe40.usenetserver.com>`
- **In-Reply-To:** `<9Hnf8-UeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <joe_zitzelberger-36A6A2.09063028092004@knology.usenetserver.com> <tRk6d.1$uO6.0@fe40.usenetserver.com> <9Hnf8-UeflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    Am  28.09.04
> schrieb  lxi0007@netscape.net (LX-i)
…[15 more quoted lines elided]…
> for some small programs.

And you could compile them on your PC, then run the executables on the 
2200 mainframe?  Or was this a Pascal compiler that was on the 2200?
```

###### ↳ ↳ ↳ Re: a history question

_(reply depth: 6)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-09-30T07:25:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9HrmvWCPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<e80b0472.0409270829.40a9b8a4@posting.google.com> <9Hnf8-UeflB@jpberlin-l.willms.jpberlin.de> <5EG6d.1938$Za.618@fe40.usenetserver.com>`

```
.     Am  29.09.04
 schrieb  lxi0007@netscape.net (LX-i)
     bei  /COMP/LANG/COBOL
      in  5EG6d.1938$Za.618@fe40.usenetserver.com
   ueber  Re: a history question

>>    But there were Pascal compilers for the 1100. The one of the UCS
>> suite has apparently been withdrawn because of a lack of customer
>> demand. Before UCS Pascal, I had a free Pascal compiler which I used
>> for some small programs.

l> And you could compile them on your PC, then run the executables on the
l> 2200 mainframe?  Or was this a Pascal compiler that was on the 2200?

   No, both are (were) native OS/1100-Compilers producing REL resp.  
OMN elements. No p-code ï¿½ la UCSD-Pascal.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Ohne Pressefreiheit, Vereins- und Versammlungsrecht ist keine
Arbeiterbewegung mï¿½glich"        - Friedrich Engels      (Februar 1865)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
