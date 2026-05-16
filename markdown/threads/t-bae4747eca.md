[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PCO and CBL programs called from an executable

_5 messages · 5 participants · 2005-03_

---

### PCO and CBL programs called from an executable

- **From:** Phillip.Small@gmail.com
- **Date:** 2005-03-09T13:52:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com>`

```
I have a oits.exe file that calls the oits.cbl program and oidriver.pco
program.  I am working on a web report and the when ran both in Unix
and in the browser, it hangs.  After making some changes and trying to
fix it, then I started getting this illegal name error.  The output
error is

I/O error : file ''
error code: 9/004 (ANS74), pc=2FA, call=1, seg=0
  4     Illegal file name

Without putting the code in this email, what type of statement would
generate this error?  ie, a CALL or MOVE.  What section?  I put in
several DISPLAY statements before the error to verify if they were
running and at which point in the Procedure Division section.  Any help
or guidance in the right direction is greatly appreciated.
```

#### ↳ Re: PCO and CBL programs called from an executable

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-09T22:51:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R5LXd.4603527$f47.822927@news.easynews.com>`
- **References:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com>`

```
The error is almost certainly on a COBOL "OPEN" statement.

My *guess* is that the specific run-time is set up to (or only can) handle 
"traditional" 8.3 file names (with no special characters) and the file name that 
was "fed" to it (don't ask me how) didn't conform to this - or the path length 
was too long for this system to handle.
```

#### ↳ Re: PCO and CBL programs called from an executable

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2005-03-09T23:22:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0o0gj$7p7$1@hercules.btinternet.com>`
- **In-Reply-To:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com>`
- **References:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com>`

```
Hi.

You've not said which COBOL product you're using here. Regardless of 
which product is involved debugging the application would highlight 
exactly which statement is showing up the problem, and, indeed, the 
filename which is causing the error to occur.

*If* you're using a Micro Focus product, then you can access the product 
documentation via the SupportLine site at 
http://supportline.microfocus.com -- you require a valid maintenance 
contract to get access to this site --  under Self Service, click 
Documentation, and follow the links. For reference, the description for 
RTS004 is :

"A file-name contains an illegal character. This could be any character 
that is not part of the permitted character set or it could be the 
system-dependent delimiter, which on most systems is the space."

(apologies if you're not using a Micro Focus product!).

Hope this helps.

SimonT.
```

##### ↳ ↳ Re: PCO and CBL programs called from an executable

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-03-10T00:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pvMXd.623660$8l.194114@pd7tw1no>`
- **In-Reply-To:** `<d0o0gj$7p7$1@hercules.btinternet.com>`
- **References:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com> <d0o0gj$7p7$1@hercules.btinternet.com>`

```
Wiggy wrote:
> Hi.
> 
…[19 more quoted lines elided]…
> 


Hello Wiggy, (I like that moniker :-) )

I didn't jump in because I think he was using Unix. And assuming M/F I'm 
guessing he would be getting a 9/xx and translating, using your 
extensions to ANSI, giving him the 004. As a thought, and you would 
know. Can you have trouble with 'spacey' pathnames/filenames with Unix ?

Example "\Corrosion-Testing\Data\Myfilename.dat"

I've deliberately got the joining hyphen in there to avoid what I knew 
could be a potential problem some years back. (I think the 
obliques/slashes are right-leaning, rather than left-leaning for Unix 
systems ?)

OK, so you've got to sell product Simon, but if he uses this one, can't 
he get in for free :-)

http://www.cobolportal.com/microfocusforum/agreement.asp

Jimmy
```

###### ↳ ↳ ↳ Re: PCO and CBL programs called from an executable

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2005-03-11T11:16:03
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0rthk$aj2$1@hyperion.microfocus.com>`
- **References:** `<1110405148.479058.193180@z14g2000cwz.googlegroups.com> <d0o0gj$7p7$1@hercules.btinternet.com> <pvMXd.623660$8l.194114@pd7tw1no>`

```
> Hello Wiggy, (I like that moniker :-) )

That stems from my days with long hair...

> I didn't jump in because I think he was using Unix. And assuming M/F I'm 
> guessing he would be getting a 9/xx and translating, using your extensions 
…[8 more quoted lines elided]…
> systems ?)

No, we don't support spacey filenames within our Server Express product,
and yes, on UNIX, directory delimiters are forward slashes.

> OK, so you've got to sell product Simon, but if he uses this one, can't he 
> get in for free :-)
>
> http://www.cobolportal.com/microfocusforum/agreement.asp

I wasn't trying to sell anything actually, though posting on the forum is
always good advice on Micro Focus-related issues.

That and a post from you wouldn't be the same without mentioning it. :-) .

SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
