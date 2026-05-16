[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inspect & differing lengths

_15 messages · 11 participants · 2003-08 → 2003-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Inspect & differing lengths

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-08-15T17:21:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
Good afternoon.

I ran into a problem today, and I'm curious to hear from some of the J4 
folks around here if I'm doing something wrong, and if so, why it is wrong.

I have a fixed set of characters (41 of 'em) that I'm trying to 
eliminate in a string.  I want to replace them with a single space, 
thereby shrinking up the original string.  With the following...

77  My-Tag  Pic X(41) Value '[stuff]'.
...
Inspect My-String Replacing All My-Tag by " "

... I get a syntax error telling me that the targets have to be the same 
size.  Checking the 2002 standard, it said that if literal-1 and 
literal-3 were both specified, they must be of the same length. 
However, I'm mixing a literal and an identifier.

Could I do what I'm wanting by making a data item as "Pic X(01) Value 
Space", and use it on the right side of the replacing clause?

If not, why will Inspect not vary lengths like that, using rules similar 
to Move (truncation / space filling)?

Thanks....
```

#### ↳ Re: Inspect & differing lengths

- **From:** "Hugh Candlin" <hugh.candlin@worldnet.att.net>
- **Date:** 2003-08-15T23:20:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rVd%a.102052$0v4.7049047@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```

LX-i <LXi0007@Netscape.net> wrote in message
news:vjqn6s2vjn7c8b@corp.supernews.com...
> Good afternoon.
>
> I ran into a problem today, and I'm curious to hear from some of the J4
> folks around here if I'm doing something wrong, and if so, why it is
wrong.
>
> I have a fixed set of characters (41 of 'em) that I'm trying to
…[5 more quoted lines elided]…
> Inspect My-String Replacing All My-Tag by " "

What you need to do is to successively compare
each 41-byte portion of My-String to My-Tag.

I.E. My-String (1 thru 41) My-String (2 thru 42)
My-String (3 thru 43) etc, until you reach the last
41-byte portion of My-String.

As you do so, if the comparison fails,
move the subscripted starting position character
from My-String to the subscripted output string field,
increment the output string subscript by 1,
increment the My-String start position subscript by 1,
and continue the search.

If you get a hit,
move a space to  the subscripted output string field,
increment the output string subscript by 1,
increment the My-String start position subscript by 41,
and continue the search.
```

#### ↳ Re: Inspect & differing lengths

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-16T11:57:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhjs5c$1nn$1@aklobs.kc.net.nz>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
LX-i wrote:

> I have a fixed set of characters (41 of 'em) that I'm trying to
> eliminate in a string.  I want to replace them with a single space,
…[15 more quoted lines elided]…
> to Move (truncation / space filling)?

INSPECT will only replace character strings of the _same_ length because it 
does it in-situ and never moves stuff aroound.

You need:

      MOVE SPACES TO Work-1 Work-2
      UNSTRING My-String DELIMITED BY My-Tag
          INTO Work-1 Work-2
      MOVE SPACES TO My-String
      STRING Work-1 " " Work-2 DELIMITED BY SPACES
          INTO My-String

Actually you probably need to do more than this such as getting UNSTRING to 
supply the sizes so that you can put, say, a HIGH-VALUE into Work-1 and 
Work-2 to act as a delimiter for the STRING.  Also if you can have more 
than one My-Tag in My-String you need to cater for this.

Or Use INSPECT TALYING My-Count FOR CHARACTERS BEFORE My-Tag and use 
referenece notaion to extract the two parts for reassembly.
```

#### ↳ Re: Inspect & differing lengths

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-08-15T20:41:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y5f%a.8777$kp4.1174494@news20.bellglobal.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
"LX-i" <LXi0007@Netscape.net> wrote in message
news:vjqn6s2vjn7c8b@corp.supernews.com...
> Good afternoon.
>
> I ran into a problem today, and I'm curious to hear from some of the J4
> folks around here if I'm doing something wrong, and if so, why it is
wrong.
>
> I have a fixed set of characters (41 of 'em) that I'm trying to
…[11 more quoted lines elided]…
>

I think you want:  (actually, it is not what you want, but is the way
inspect works)

Inspect My-String Replacing All My-Tag by "a literal of 41 spaces here"

You have to have a literal in the second string the same size as the
original string because they correspond ... ie the first character in the
first literal is replaced by the first character in the second literal, the
second by the second, the third by the third, etc.  The example below, which
changes upper case to lower, illustrates what I mean.

Inspect my-string replacing all "ABCDEFGHJKLMNOPQRSTUVWXYZ" by
"abcdfeghijklmnopqrstuvwxyz".

That gets rid of the bad characters, but does *not* compress the string.  To
do that, you need to unstring delimited by ALL " ", then string delimited by
a single " ".

The inspect cannot move data within the string ... it only replaces, counts,
etc.

Donald
```

##### ↳ ↳ Re: Inspect & differing lengths

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-16T11:31:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hCo%a.100970$3o3.7028803@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com> <y5f%a.8777$kp4.1174494@news20.bellglobal.com>`

```

"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:y5f%a.8777$kp4.1174494@news20.bellglobal.com...
| "LX-i" <LXi0007@Netscape.net> wrote in message
| news:vjqn6s2vjn7c8b@corp.supernews.com...
…[27 more quoted lines elided]…
| first literal is replaced by the first character in the second literal,
the
| second by the second, the third by the third, etc.  The example below,
which
| changes upper case to lower, illustrates what I mean.
|
| Inspect my-string replacing all "ABCDEFGHJKLMNOPQRSTUVWXYZ" by
| "abcdfeghijklmnopqrstuvwxyz".

CONVERTING will work.
The example is a string replacement, not a character replacement.

|
| That gets rid of the bad characters, but does *not* compress the string.
To
| do that, you need to unstring delimited by ALL " ", then string delimited
by
| a single " ".
|
| The inspect cannot move data within the string ... it only replaces,
counts,
| etc.
|
| Donald
|
|
```

###### ↳ ↳ ↳ Re: Inspect & differing lengths

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-08-16T08:01:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H3p%a.9792$kp4.1370913@news20.bellglobal.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com> <y5f%a.8777$kp4.1174494@news20.bellglobal.com> <hCo%a.100970$3o3.7028803@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:hCo%a.100970

> CONVERTING will work.
> The example is a string replacement, not a character replacement.
>
yes, you are right ...

Donald
```

#### ↳ Re: Inspect & differing lengths

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-08-16T09:10:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f3df463.17707852@news.central.cox.net>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote:


>I have a fixed set of characters (41 of 'em) that I'm trying to 
>eliminate in a string.  I want to replace them with a single space, 
…[12 more quoted lines elided]…
>Space", and use it on the right side of the replacing clause?

The right side should be Pic x(41) value spaces or a literal with exactly 41
spaces.
```

#### ↳ Re: Inspect & differing lengths

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-08-16T02:27:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0308160127.2fa975bc@posting.google.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
Bottom posting below (where else would it be!)

LX-i <LXi0007@Netscape.net> wrote in message news:<vjqn6s2vjn7c8b@corp.supernews.com>...
> Good afternoon.
> 
…[22 more quoted lines elided]…
> Thanks....

Having read your question and the other responses, it seems to me that
your question is ambiguous.

Do you mean that you want to replace one or more strings containing
all the 41 characters in the same sequence as a group together?  If
so, then the other answers are appropriate.

Or do you mean that you have a set of 41 different characters each
individual one of which is to be replaced by a space and that you also
want to replace any multiple adjacent spaces by single spaces?

If the latter then your INSPECT statement should contain a space
literal that is 41 characters in length and you should follow up with
a PERFORM statement to removed the adjacent multiple spaces.  A small
twist to this, is whether you would also want to convert any
pre-existing multiple adjacent spaces to single spaces or leave those
as they were before.  My solution would also compress any pre-existing
multiple spaces, but if that isn't what you want, then a much more
complex solution would be required, which I don't want to solve unless
you say it is necessary.

Robert
```

##### ↳ ↳ Re: Inspect & differing lengths

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-08-16T07:55:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vjsadgh0l9rrd8@corp.supernews.com>`
- **In-Reply-To:** `<fcd09c56.0308160127.2fa975bc@posting.google.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com> <fcd09c56.0308160127.2fa975bc@posting.google.com>`

```
Thanks for all the replies - looks like I'll be writing some extra code. 
  (What I was really wanting Inspect Replacing to do was the same thing 
as the VB command Replace - oh well...)  I'm especially intrigued by 
RP's Unstring-then-String idea...   Anyway, more details about the 
problem are below.

Robert Jones wrote:
> Bottom posting below (where else would it be!)
> 
…[34 more quoted lines elided]…
> so, then the other answers are appropriate.

Yes, this is what I'm trying to do.  Our system runs on a Unisys 
ClearPath IX mainframe, and we have a standard ("green screen") 
interface and a GUI.  When we output message traffic to the green 
screen, we can put out start-of-entry (SOE) and tab characters, and 
users can tab to places in the output and transmit, which submits a new 
transaction with the parameters between the SOE and where the cursor was.

The GUI folks had a JavaScript function that would go through each line 
of output (which is written in HTML for them), and replace these 
SOE-to-Tab combinations with a link that the users could click to submit 
the same transaction they would on the green screen.  This function has 
to read every line of every output, and our performance guys said that 
it was really being a drain on systems, especially older ones.

The solution was to modify the mainframe process to insert these links 
as the traffic is being written.  This way, all the GUI has to do is 
display (or redisplay, which is an option) what's already there.  The 
anchor tag that creates the link is 41 characters, and the closing 
anchor tag is 4 (</a>).

Another option that the GUI folks have is "exporting" their HTML output 
to a file with a .txt or .doc extension.  This export process reverses 
any HTML encoding that was done when the traffic was generated.  Now 
that we're putting these tags in, we need to pull them out, and replace 
the starting tag by a single space - this will preserve the columnar 
formatting of the original output.

I think the unstring-then-string solution may be the most 
straightforward, although I had considered others (which went into a 
continuous loop!), and I may try two or three of them.

> A small
> twist to this, is whether you would also want to convert any
…[4 more quoted lines elided]…
> you say it is necessary.

No, we need all the embedded spaces.  :)  Thanks again to everyone for 
the great help...
```

#### ↳ Re: Inspect & differing lengths

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-08-16T11:29:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OAo%a.8382$Ih1.2770824@newssrv26.news.prodigy.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
> I have a fixed set of characters (41 of 'em) that I'm trying to
> eliminate in a string.  I want to replace them with a single space,
> thereby shrinking up the original string.

'Shrinking'  an INSPECTed string is impossible. That's asking for a change
in the PICTURE clause at run time.. except the PICTURE clause only has
meaning at compile time.

If an INSPECTed string has a PICTURE clause of X(41) or X(123), it will
always be 41 or 123 characters in length regardless of its contents.

I think you are actually looking for the REARRANGE verb. (But don't look too
hard, because that doesn't exist).

MCM
```

##### ↳ ↳ Re: Inspect & differing lengths

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-16T11:35:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Go%a.100975$3o3.7028657@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com> <OAo%a.8382$Ih1.2770824@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:OAo%a.8382$Ih1.2770824@newssrv26.news.prodigy.com...
| > I have a fixed set of characters (41 of 'em) that I'm trying to
| > eliminate in a string.  I want to replace them with a single space,
…[9 more quoted lines elided]…
| I think you are actually looking for the REARRANGE verb. (But don't look
too
| hard, because that doesn't exist).

No he's looking for the INSPECT COMPRESSING.

INSPECT MY-STRING
 COMPRESSING ALL SPACES TO SPACE
END-INSPECT
```

#### ↳ Re: Inspect & differing lengths

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-16T11:31:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gCo%a.100969$3o3.7028917@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```

"LX-i" <LXi0007@Netscape.net> wrote in message
news:vjqn6s2vjn7c8b@corp.supernews.com...
| Good afternoon.
|
| I ran into a problem today, and I'm curious to hear from some of the J4
| folks around here if I'm doing something wrong, and if so, why it is
wrong.
|
| I have a fixed set of characters (41 of 'em) that I'm trying to
…[16 more quoted lines elided]…
| to Move (truncation / space filling)?

1. Inspect will not compress the string.
2. Are you removing characters, or a phrase?

What you may want to do is:
Convert the characters or string to spaces.
Have a general purpose string compression routine (re-use) to remove
multiple spaces.

Be careful:

01  MSG.
    05  PIC X(60)  VALUE    'VERB IS THE VERBIAGE'.

INSPECT MESSAGE-AREA  REPLACING ALL 'VERB'  BY 'MOVE'.
Produces:
"MOVE IS THE MOVEIAGE"
```

#### ↳ Re: Inspect & differing lengths

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-08-17T11:10:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zoJ%a.135327$cF.35247@rwcrnsc53>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
You could have 41 statemants of
 Inspect My-String Replacing All "v" by " ".
 Inspect My-String Replacing All "l" by " ". ETC:
You could have one
  Inspect My-String converting
      'abcdefghijk' to 'ABCDEFGHIJK'.
This would be a lower to UPPER case conversion.
In your case the the first string would be your 41 characters
and the second string woud be all spaces 41 of them.
Enjoy Bob (kobolkid)


"LX-i" <LXi0007@Netscape.net> wrote in message
news:vjqn6s2vjn7c8b@corp.supernews.com...
> Good afternoon.
>
> I ran into a problem today, and I'm curious to hear from some of the J4
> folks around here if I'm doing something wrong, and if so, why it is
wrong.
>
> I have a fixed set of characters (41 of 'em) that I'm trying to
…[31 more quoted lines elided]…
>
```

#### ↳ Re: Inspect & differing lengths

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-10-02T16:32:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362dnbTCVvMUBOGiU-KYjA@comcast.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com>`

```
In article <vjqn6s2vjn7c8b@corp.supernews.com>, LXi0007@Netscape.net wrote:

>I have a fixed set of characters (41 of 'em) that I'm trying to 
>eliminate in a string.  I want to replace them with a single space, 
>thereby shrinking up the original string.  With the following...

How about using two indexed strings and manually transversing the one
and copying the characters to the second, skipping duplicate spaces?
```

##### ↳ ↳ Re: Inspect & differing lengths

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-10-02T21:54:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0310022054.62ecc11d@posting.google.com>`
- **References:** `<vjqn6s2vjn7c8b@corp.supernews.com> <362dnbTCVvMUBOGiU-KYjA@comcast.com>`

```
If the unstring/string approach leads to unexpected problems, you may
want to try a ref/mod move of the data portion(s) of the data along
with the space delimeters to the destination field. It's a little more
wordy but it s/b more efficient.

Find the begin tag and the end tag [</a>] adjusting and saving the pos
ptrs and use them to calc the start pos of the data and its length.

Move a begin space, the ref/moded data and an end space to the
destination field using ref/mod. Repeat the process until input EOR.


Regards, Jack.


weberm@polaris.net (Ubiquitous) wrote in message news:<362dnbTCVvMUBOGiU-KYjA@comcast.com>...
> In article <vjqn6s2vjn7c8b@corp.supernews.com>, LXi0007@Netscape.net wrote:
> 
…[5 more quoted lines elided]…
> and copying the characters to the second, skipping duplicate spaces?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
