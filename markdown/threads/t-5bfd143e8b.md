[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multi Column Display Issue

_2 messages · 2 participants · 1998-11_

---

### Multi Column Display Issue

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364a046e.21648117@news.abraxis.com>`

```
For debugging (and just to watch some output on screen) I put display statements
at two locations in one program:  whenever two different performs are carried
out.  The second group (of displays) executes sometime after the first group is
done.  Without any attempt to format the output on screen they're written in the
same very tall pile starting at column 1 line 1.  

I tried to format the output so that the first display statement was set
explicitly to start at line 1 column 1 and the second to start at line 1 column
40.  The screen variables are set by default to 80 x 24 (in the Fujitsu 3.0, and
unknown on Aix--MF v.3??).  Both compilers choked and didn't finish compiling.
I tried DISPLAY AT and variations.  I think the Fujitsu documentation didn't
really specify syntax to allow this or I couldn't figure it out and there is
some documentation in the class's textbook ('From Micro to Mainframes' which is
essentially dedicated to MicroFocus) but nothing exactly about this sort of
trick.  

Is it possible to do this?  (example follows)
'Preciate your opinions!  TS


output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 
output stuff 1 here first                output sfuff 2 here later 


"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
++++++*******Dontcha*just*hate*this*antispamming*stuff??********++++++
*********No generalization is wholly true, not even this one**********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

#### ↳ Re: Multi Column Display Issue

- **From:** "Hugh Candlin" <hugh.candlin@getridofspam.worldnet.att.net>
- **Date:** 1998-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72e6gr$935@bgtnsc03.worldnet.att.net>`
- **References:** `<364a046e.21648117@news.abraxis.com>`

```

OldUncleMe wrote in message <364a046e.21648117@news.abraxis.com>...
>
>Is it possible to do this?  (example follows)
>
>output stuff 1 here first                output sfuff 2 here later


Simple way would be to replace the first DISPLAY with a MOVE,
saving 'output stuff 1' in working storage,
then display 'output stuff 1' (from the save area), some blanks,
and 'output stuff 2', using one DISPLAY statement.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
