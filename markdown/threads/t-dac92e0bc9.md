[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using the Fujitsu COBOL v 3

_7 messages · 5 participants · 2000-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Using the Fujitsu COBOL v 3

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E41A62.17455980@medecine.unige.ch>`

```
Hello,

I'm evaluate this compiler for an eventual a possible purchase!
I have my source of Cobol in fixed format.
When I try to compile it, I receive an avalanche of error? 
The compiler does not understand obviously the format.
Where I specify the format. I use the Project Manager.

Thanks in advance.

Alain.

Ps: Is there a FAQ for the use of Fujitsu COBOL v 3?
```

#### ↳ Re: Using the Fujitsu COBOL v 3

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s1neb$du9$1@ins21.netins.net>`
- **References:** `<39E41A62.17455980@medecine.unige.ch>`

```
Take a look at Thane Hubbell's Teach Yourself COBOL in 24 hours.  In the
early chapters he goes through the process of editing, compiling, linking, 
and executing a program using Fujitsu v. 3.  Later chapters add more
complexity - including the debugger and multiple compilation units.

Floyd Johnson 

Alain Chappuis (Alain.Chappuis@medecine.unige.ch) wrote:
: Hello,

: I'm evaluate this compiler for an eventual a possible purchase!
: I have my source of Cobol in fixed format.
: When I try to compile it, I receive an avalanche of error? 
: The compiler does not understand obviously the format.
: Where I specify the format. I use the Project Manager.

: Thanks in advance.

: Alain.

: Ps: Is there a FAQ for the use of Fujitsu COBOL v 3?
: --
: +----------------------+-------------------------------------------+
: | Alain Chappuis       | Responsable: E-mail; cmu.unige.ch         |
: | Analyste programmeur | WEB    : www.medecine, ebn, jid, Sifm     |
: | Universite de Geneve | E-mail : Alain.Chappuis@unige.ch          |
: | Centre Medical Univ. | Phone  : +41 (22) [70]25.073              |
: | 1, Rue Michel-Servet | FAX    : +41 (22) 347.33.34 ou 702.58.58  |
: | CH-1211 Geneve 4     | http://cmub.unige.ch/www/si/alain.html    |       
: +----------------------+-------------------------------------------+
```

#### ↳ Re: Using the Fujitsu COBOL v 3

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e4959d.64796378@207.126.101.100>`
- **References:** `<39E41A62.17455980@medecine.unige.ch>`

```
What is the first line of your programs?  If it is not the
IDENTIFICATION DIVISION and not a Fujitsu compiler option (ie if is
SOMEONE ELSE'S compiler option) then this will confuse the compiler.
Could that be your problem?

On Wed, 11 Oct 2000 09:44:34 +0200, Alain Chappuis
<Alain.Chappuis@medecine.unige.ch> wrote:

>Hello,
>
…[19 more quoted lines elided]…
>+----------------------+-------------------------------------------+

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Using the Fujitsu COBOL v 3

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s2sv6$3ro$1@slb3.atl.mindspring.net>`
- **References:** `<39E41A62.17455980@medecine.unige.ch>`

```
Other responses have suggested other problems.  My guess is that you
downloaded/created your source code withOUT "CRLF" characters.  All (???) PC
compilers require source code to be
 A) ASCII (not EBCDIC)
 B) "Line sequential" files (files with CR-LF characters separating lines)

How did you create/get your source code?
```

##### ↳ ↳ Re: Using the Fujitsu COBOL v 3

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E567B1.E1711A9@medecine.unige.ch>`
- **References:** `<39E41A62.17455980@medecine.unige.ch> <8s2sv6$3ro$1@slb3.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> Other responses have suggested other problems.  My guess is that you
> downloaded/created your source code withOUT "CRLF" characters.  All (???) PC
> compilers require source code to be
>  A) ASCII (not EBCDIC)

Yes right, my file is issued from Compac (Alpha) 
I have a program which transposes my format DOS(EBCDIC) in ASCII format
for Compac (Alpha) 

>  B) "Line sequential" files (files with CR-LF characters separating lines)

Maybe yes I dont know, if I read this file with notepad I dont see any
extras lines.
 
> How did you create/get your source code?

Now my first line of my program:
000000 @OPTIONS MAIN,ALPHAL,LINECOUNT(72),MESSAGE,NUMBER
000010 Identification Division.                                         OBSERVE
000020*=======================*                                         OBSERVE
000030 Program-Id.             OBSERVE.                                 OBSERVE

Thank you all for your help me.
Alain.
```

###### ↳ ↳ ↳ Re: Using the Fujitsu COBOL v 3

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-13T04:23:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e68e0d.193912869@207.126.101.100>`
- **References:** `<39E41A62.17455980@medecine.unige.ch> <8s2sv6$3ro$1@slb3.atl.mindspring.net> <39E567B1.E1711A9@medecine.unige.ch>`

```
Bill might just be right.  Go to a DOS prompt and use EDIT on your
file:

EDIT OBSERVE.COB 

Then save it.  Don't just exit - make sure to SAVE.

This will insert the CR LF's where only LF's existed before.  (Or is
it only CR's, I can't recall).


On Thu, 12 Oct 2000 09:26:41 +0200, Alain Chappuis
<Alain.Chappuis@medecine.unige.ch> wrote:

>"William M. Klein" wrote:
>> 
…[32 more quoted lines elided]…
>+----------------------+-------------------------------------------+

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Using the Fujitsu COBOL v 3

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-10-12T01:32:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001011213234.06947.00000314@nso-fl.aol.com>`
- **References:** `<8s2sv6$3ro$1@slb3.atl.mindspring.net>`

```
In article <8s2sv6$3ro$1@slb3.atl.mindspring.net>, 
>"Alain Chappuis" <Alain.Chappuis@medecine.unige.ch> wrote in message
>news:39E41A62.17455980@medecine.unige.ch...
…[9 more quoted lines elided]…
>

I believe that it might be helpful to look at the compile option
SRF to specify the source format.  by default it is SRF=VAR,VAR
and works for most situations.
I have encountered some instances where I use SRF=FIX,FIX
for code downloaded from the mainframe.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
