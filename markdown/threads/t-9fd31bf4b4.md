[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus and "dialects"

_3 messages · 2 participants · 2005-02 → 2005-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus and "dialects"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-26T19:22:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C%3Ud.3190795$B07.504694@news.easynews.com>`

```
When I was a Micro Focus employee (about a decade ago now), it seems to me that 
I spent VAST amounts of my time dealing with customers on the question of "Micro 
Focus compilers and 'dialect' support".  Given a couple of recent threads in 
comp.lang.cobol (Kellie and "standard" and Fred and "EXAMINE"),  I thought I 
would post this note.  As far as I know it is current, but I may be out-of-date 
on some of it (or some of it may vary depending upon exactly WHICH MF 
compiler/product you have).

NOTE: With the more recent compilers the "DIALECT" directive does much of what I 
am going to talk about here - via(semi-hidden) references to certain MF provided 
"*.dir" files.  If you want to "limit" your compile to a emulating a specific 
dialect (or level of the Standard), check your product for this directive - and 
which dialects are available.

NOTE2:  Always consider using the SETTINGS directive "occasionally" to see 
exactly which directives YOU are getting (by default, by directive selection, 
and by *.dir file).

   ***

Micro Focus (historically) has been GREAT in providing a "migration path" FROM 
many other environments and compilers; it has (traditionally) been less strong 
in providing a method of developing source code TARGETED for a specific "other" 
environment.  They have provided (IBM) mainframe development products, but even 
these have (to lesser or greater extents) required programmers to be "careful" 
not to use available (with MF) extensions.

For example, with just a little "effort", it is (and has been for years) 
possible to:

 - Use the EXHIBIT statement in the middle of an OO method
        or
- Use the TRANSFORM statement in the middle of a nested program
        or
- Use a mixture of COMP-2, COMP-5, COMP-X, and COMP-6 data items - with an ON 
statement

***

to understand MF's (from here on, I'll use this for "Micro Focus" - not 
"mainframe") "support", it is important to understand the difference between 
their "reserved word" (mostly) and their "flagging" directives.

For example,
   OSVS - provides support for ALL the reserved words in IBM's OS/VS COBOL 
compiler (and does NOT turn off any from any other dialect)
        while
   FLAG(OSVS) (or FLAG"OSVS") says to flag syntax that is invalid in the OS/VS 
COBOL compiler.

NOTE:  MF does (correctly) indicate that some of the reserved word directives do 
impact a FEW syntax/semantic issues.  These are, however, few and far between 
and can "generally" be ignored.  They only come into play when the syntax that 
is acceptable to two dialects yields different semantics - or if certain VERY 
OBSCURE parsing rules come into play.

In general, MF allows programmers to turn on AS MANY different sets of reserved 
words as they want - all in the same program. (Hence, the ability to have 
TRANSFORM and Local-Storage Section - in the same program.).  On the other hand, 
it is "expected" that you will only have ONE "flagging" directive turned on at a 
time.

As far as '85 Standard conformance goes, MF provides both
   FLAG(ANS85)
        and
  FLAGSTD(x,y,...)

Both of these ACTUALLY provide "flagging" for "FIPS amended third standard 
COBOL" - i.e. they include the intrinsic function as part of the "HIGH" level - 
while the actual ANSI (and ISO) Standards called this "optional".  I can't speak 
for how MF is today, but when I worked for them,

   FLAGSTD  (FIPS flagging) - was a (little) more complete
        but
   FLAG(ANS85) (occasionally) provided more informative messages

Now, once a programmer has decided on which dialect's SYNTAX they want to 
emulate, they then need to decide what level of message they want to receive for 
syntax out of that level or emulation.  This is what the FLAGAS directive does. 
If you want an E-level message for each "flagging" message, then use FLAGAS(E). 
(The CHANGE-MESSAGE directive can impact specific messages - increasing, but not 
decreasing their severity level).

   ***

Bottom-Line:
  If you do NOT have access to the "dialect" directive and want to insure that 
you have JUST '85 Standard (with amendments) source code, you would nee to 
specify (via default, directive or *.dir file)

NOOSVS, NOVSC2,NODOSVS,NOBS2000,NODG,NORM,NOXPOPEN,NOISO2002
   (possibly more - depending upon your release/version of MF COBOL)
           and most importantly
NOMF,ANS85

Plus
  FLAGSTD(H)  *> and if you are using RW, Debugging, or another optional module, 
its support
     or  FLAG(ANS85)
Plus
  FLAGAS(x)  *> depending upon which level of severity you want

     ***

If you want to allow features from the ISO 2002 Standard, you would need to 
change from NOISO2002 to ISO2002 and you would want to change to
   FLAG(ISO2002)
(I don't know how much of ISO2002 this actually ALLOWS and what it flags, but I 
do see it documented in the current MF documentation).

To "emulate" another compiler (e.g. IBM's Enterprise COBOL) you would want to 
change both the "reserved word" directives and the flagging directives.

***

Other directives, e.g

 - FLAGSINEDIT
 - HIDE-MESSAGE
 - WARNING

will impact where and which messages you see.

  ***

I hope this is helpful to some in this forum (and that I haven't mislead or 
missed much <G>)
```

#### ↳ Re: Micro Focus and "dialects"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-27T13:48:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dkUd.3258737$B07.512577@news.easynews.com>`
- **References:** `<C%3Ud.3190795$B07.504694@news.easynews.com>`

```
I should have clarified in my original note that what I am talking about here is 
what will (or will not) COMPILE (check) with or without messages.  There are 
entire OTHER sets of directives that impact "run-time behavior".  There are 
actually two types of these directives,  For example:

Type 1 - Impact compiler "emulation"
  - STICKY-LINKAGE
  - PERFORM-TYPE
  - ODOSLIDE
  - IBMCOMP
  - OLDNEXT-SENTENCE
  - RDW
       etc

Type 2 - impact CHOICES that other compilers (especially IBM mainframe ones) 
also provide
 - DYNAM (with NODYNAM "cancels" are NO-OPs)
 - TRUNC (impacts picture truncation)
 - QUOTE/POST (what does the QUOTE figurative constant "use")
       etc
```

#### ↳ Re: Micro Focus and "dialects"

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2005-03-01T13:11:34
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d01olm$geo$1@hyperion.microfocus.com>`
- **References:** `<C%3Ud.3190795$B07.504694@news.easynews.com>`

```
This following is my response speaking primarily from an IBM mainframe 
perspective. The latest products from Micro Focus make it very easy to 
develop code that is compatible with the target environment. The Micro Focus 
compiler itself is highly flexible, allowing conformance to a great range of 
COBOL dialects and standards through a number of compiler options and 
settings that can be configured as appropriate. In Mainframe Express 
Enterprise Edition (the latest product for development and testing of 
mainframe applications) we have made the configuration very easy. Instead of 
our customers requiring detailed knowledge of our compiler in order to 
fine-tune the settings to match the desired mainframe compiler 
version/level, we have a simple drop-down list that allows you to choose the 
desired mainframe compiler level. Within each choice (eg. Enterprise COBOL 
for z/OS, COBOL for OS/390, COBOL for MVS, VS COBOL II... etc) there are 
further options that allow you to match the compilation and runtime 
behaviour to the specific compiler options that you have set on the 
mainframe. When using mainframe dialects, the use of non-mainframe COBOL 
features in your source code produces a compile error on the PC, which 
therefore makes it very difficult to write code that will not run on z/OS. 
These settings can be easily adopted throughout the development organization 
through the use of  'templates' which define the shop-specific standards for 
the development and testing of your applications.

I hope this helps to clarify things.

Best regards,

Brian Crane
Product Director - Mainframe Application Development Products
http://www.microfocus.com/products/mfeee


 It is true that in older products such as COBOL Workbench, there was a 
range of setting.
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:C%3Ud.3190795$B07.504694@news.easynews.com...
> When I was a Micro Focus employee (about a decade ago now), it seems to me 
> that I spent VAST amounts of my time dealing with customers on the 
…[130 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
