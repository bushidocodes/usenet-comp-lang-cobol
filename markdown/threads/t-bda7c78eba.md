[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform "Standards" question

_2 messages · 2 participants · 1999-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Re: Perform "Standards" question

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cc8ef7.74834268@netnews>`
- **References:** `<MPG.112a77f51ef0dd60989682@news.texas.net> <36C34D40.8A8F6343@nospam.ibm.net> <36c38066.9968722@netnews> <7a7j2d$grq$1@fenix.maxitel.pt>`

```
'Twas Sun, 14 Feb 1999 22:21:50 +0100, when "PAULO CRUZ"
<scruz_paulo@mail.teleweb.pt> illuminated comp.lang.cobol thusly:

>1.st - I don't agree neither with a 'perform' performing the same paragraph
>it belongs to, nor the 'go to' the paragraph name.

<English>
"don't ... neither" is a double negative.  I take it you mean to say "I
agree with neither a 'perform' performing the same paragraph it belongs
to, nor the 'go to' the paragraph name."
</English>

>2nd. - I assume the problem here is lock control, isn't it ? 

No.  The cases where I most recently wrote a GO TO like this involved an
inquiry.  Actually there were multiple GOs because there were multiple
reasons for rejecting records.  This paragraph was called from two
different places, and they had each implemented some of this filtering
differently, so I moved more filtering down into the file reading
paragraph.
```

#### ↳ Re: Perform "Standards" question

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7al03q$1iu$1@fenix.maxitel.pt>`
- **References:** `<MPG.112a77f51ef0dd60989682@news.texas.net> <36C34D40.8A8F6343@nospam.ibm.net> <36c38066.9968722@netnews> <7a7j2d$grq$1@fenix.maxitel.pt> <36cc8ef7.74834268@netnews>`

```

Randall Bart wrote<36cc8ef7.74834268@netnews>...
>'Twas Sun, 14 Feb 1999 22:21:50 +0100, when "PAULO CRUZ"
><scruz_paulo@mail.teleweb.pt> illuminated comp.lang.cobol thusly:
>
>>1.st - I don't agree neither with a 'perform' performing the same
paragraph
>>it belongs to, nor the 'go to' the paragraph name.
>
…[4 more quoted lines elided]…
></English>

Hoping not to be betrayed by my english:

A - Yes, you took it correctly and you've just helped me improving
 my english, which not being my native tongue sometimes
corners me into difficult situations like the one you caught me into...
Finding myself very often insisting on the correctness of  the usage
of my mother tongue, I'm really glad to find purists here.
Thanks for your valuable criticism.

B - As for the COBOL (another English dialect among so many ones
in this monotonous world!) which brought us here, I personally would
have handled those record rejecting by means of a condition just
appended to the perform command. Anyway, I'd rather do GOTO the
paragraph name (even against my preferences) than PERFORM the
paragraph name under which I'm cycling (what seems actually awful).

Rgds
P.Cruz

>>2nd. - I assume the problem here is lock control, isn't it ?
>
…[8 more quoted lines elided]…
>R B |\  Randall Bart
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
