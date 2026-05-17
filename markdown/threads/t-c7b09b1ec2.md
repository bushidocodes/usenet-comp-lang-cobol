[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Returning ERRORLEVEL to DOS?

_4 messages · 4 participants · 1996-11_

---

### Returning ERRORLEVEL to DOS?

- **From:** "ro..." <ua-author-3399655@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55t8fo$50f@skipper.netrail.net>`

```

Hey,

Trying to write a util that needs to return different ERRORLEVELs to a
calling DOS Batch file...

I cant figure out how to get the value I want to return to the DOS level
ERRORLEVEL variable...

Im using Realia V4.1

Any help greatly appreciated!
RonO
                                     ,,,
                                    (o o)
 +------------------------------oOO--(_)--OOo--------------------------------+
 |  Ron Olshavsky - ro··.@net··l.net  |  It's a Mr. Death or something,      |
 |  ftp.netrail.net/pub/users/rono    |  He's come about the reaping?        |
 |  http://www.netrail.net/â€¾rono      |  I dont think we need any...  MP:MOL |
 +---------------------------------------------------------------------------+
```

#### ↳ Re: Returning ERRORLEVEL to DOS?

- **From:** "js..." <ua-author-8923249@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7b09b1ec2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<55t8fo$50f@skipper.netrail.net>`
- **References:** `<55t8fo$50f@skipper.netrail.net>`

```

In message <55t8fo$5.··.@ski··l.net> - ro··.@net··l.net (Ron
Olshavsky) writes:
:>
:>Hey,
:>
:> Trying to write a util that needs to return different ERRORLEVELs to a
:>calling DOS Batch file...
:>
:> I cant figure out how to get the value I want to return to the DOS level
:>ERRORLEVEL variable...
:>
:> Im using Realia V4.1
:>
:>Any help greatly appreciated!
:>RonO
:>--
:> ,,,
:> (o o)
:> +------------------------------oOO--(_)--OOo--------------------------------+
:> | Ron Olshavsky - ro··.@net··l.net | It's a Mr. Death or something, |
:> | ftp.netrail.net/pub/users/rono | He's come about the reaping? |
:> | http://www.netrail.net/~rono | I dont think we need any... MP:MOL |
:> +---------------------------------------------------------------------------+
:>


You should just be able to move the value to RETURN-CODE. I use
Micro-Focus
not Realia, but it should be the same. The below example is what I have
used
in the past.

IF SUCCESS
MOVE 0 TO RETURN-CODE
ELSE
MOVE 1 TO RETURN-CODE.

Hope it works.
Jon

/-----------------------------------------------/
/ Jon Santarelli | If there is a /
/ js··.@int··s.com | better way to do /
/ | it...Find it! /
/ Team OS/2 | Thomas A Edison /
/ See Spike the supercomputing hedgehog, and /
/ stay tuned to see some 'misadventures' of - /
/ Hettie the acoustically minded hedgehog. /
/ http://homepage.interaccess.com/~jsant /
/-----------------------------------------------/
```

#### ↳ Re: Returning ERRORLEVEL to DOS?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-11-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7b09b1ec2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<55t8fo$50f@skipper.netrail.net>`
- **References:** `<55t8fo$50f@skipper.netrail.net>`

```

Move whatever number you want to return-code and then end the program.
return-code is a reserved word that is the DOS error level. I use in in
one of my Realia applications.


Ron Olshavsky wrote in article
<55t8fo$5.··.@ski··l.net>...
› Hey,
› 
…[14 more quoted lines elided]…
› 
+------------------------------oOO--(_)--OOo--------------------------------
+
›  |  Ron Olshavsky - ro··.@net··l.net  |  It's a Mr. Death or something,  
›    |
…[4 more quoted lines elided]…
› 
+---------------------------------------------------------------------------
+
›
›
```

#### ↳ Re: Returning ERRORLEVEL to DOS?

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-11-07T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7b09b1ec2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<55t8fo$50f@skipper.netrail.net>`
- **References:** `<55t8fo$50f@skipper.netrail.net>`

```

*In article <55t8fo$5.··.@ski··l.net>, ro··.@net··l.net says...
*>
*>Hey,
*>
*> Trying to write a util that needs to return different ERRORLEVELs to
*> a
*>calling DOS Batch file...
*>
*> I cant figure out how to get the value I want to return to the DOS l
*>evel
*>ERRORLEVEL variable...
*>
*> Im using Realia V4.1
*>
*>Any help greatly appreciated!
*>RonO
*>--


Ron:

With Realia, simply move a value to RETURN-CODE before exiting your
program. It will be passed to ERRORLEVEL. For example, if you move 16
to RETURN-CODE then in the .bat file:

IF Errorlevel 16 GOTO error

mike dodas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
