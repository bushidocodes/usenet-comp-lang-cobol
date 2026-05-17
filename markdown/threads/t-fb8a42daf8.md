[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# X"91" function calls in MF

_3 messages · 3 participants · 1995-03_

---

### X"91" function calls in MF

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-03-03T15:50:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3j7vdr$a8n@wrdis02.robins.af.mil>`

```
Is there a complete list of supported function codes for x"91"
available somewhere. My documentation only shows 60/61 and
69.

I just learned that I won't be able to live without 35, which makes
me wonder how many more I don't know about.

Thanks in advance,

Jon Wilson
```

#### ↳ Re: X"91" function calls in MF

- **From:** "7133..." <ua-author-17073934@usenetarchives.gap>
- **Date:** 1995-03-06T16:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb8a42daf8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3j7vdr$a8n@wrdis02.robins.af.mil>`
- **References:** `<3j7vdr$a8n@wrdis02.robins.af.mil>`

```
› Is there a complete list of supported function codes for x"91"
available somewhere. My documentation only shows 60/61 and
69.

I just learned that I won't be able to live without 35, which
makesme wonder how many more I don't know about. <

Which CALL-BY-NUMBER routine is available to you will be
dependent ypon which platform you are on. The X'91' function 35
is documented in the DSO/Windows/OS2 product, but not the UNIX
products. This is because that call causes a DOS Shell to be
created. UNIX doesn't know how to do that. For the UNIX
environment the same type of functionality is provided with the
CALL "SYSTEM" call.

Regards,
```

#### ↳ Re: X"91" function calls in MF

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-03-10T12:15:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb8a42daf8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3j7vdr$a8n@wrdis02.robins.af.mil>`
- **References:** `<3j7vdr$a8n@wrdis02.robins.af.mil>`

```

In article <3j7vdr$a.··.@wrd··f.mil>, jwi··.@b85··f.mil (Jon Wilson) writes:
› Is there a complete list of supported function codes for x"91"
› available somewhere. My documentation only shows 60/61 and
…[3 more quoted lines elided]…
› me wonder how many more I don't know about.

Well, there are a ton. However, I'd strongly (VERY strongly) suggest that you
do not use any of them, but instead find equivalent CBL_ calls (if the function
is of any real worth these days (as 35 is) then one should exist (soon, if not
right now)).

If you want to know my reasons for discouraging the use of x"91", mail me.

Cheers,
Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
