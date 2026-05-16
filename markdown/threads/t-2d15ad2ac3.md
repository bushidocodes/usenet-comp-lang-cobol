[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading COBOL "data files"

_12 messages · 11 participants · 2004-07_

---

### Reading COBOL "data files"

- **From:** shooper@rxworks.com (Scott Hooper)
- **Date:** 2004-07-14T22:38:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
I have read through all the newsgroups I could find and am getting
very confused about what to do with my files. I have a heaps of
FILExxxx.DAT files, some with matching .CTL files, that I need to read
into something like Access, dBase or delimited text. The files were
created using a custom program written in RM/COBOL-85. I have all the
.COB files. What I can't do is spend any money on a one-off tool. I'm
hoping that somebody can offer me a VB, VB.NET or C# code solution for
reading these.

Also, I have this entire COBOL program but can't run it as I get
messages talking about the need for me to install the RM/COBOL
runtime. Is this available free anywhere? I understand the developer
tools would cost, but surely the runtime is free for end users?

Many thanks in advance,
Scott Hooper
```

#### ↳ Re: Reading COBOL "data files"

- **From:** docdwarf@panix.com
- **Date:** 2004-07-15T05:32:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd5ivh$99g$1@panix5.panix.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
In article <a8341757.0407142138.560efc01@posting.google.com>,
Scott Hooper <shooper@rxworks.com> wrote:

[snip]

>What I can't do is spend any money on a one-off tool.

Hmmmmm... so you have all of these 'documents' in 'Italian' and you want 
to be able to translate them into 'German' without learning both languages 
spending any money on interpreting services?

You just might get what you pay for, then.

DD
```

#### ↳ Re: Reading COBOL "data files"

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-15T11:33:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
"Scott Hooper" <shooper@rxworks.com> wrote in message
news:a8341757.0407142138.560efc01@posting.google.com...
> I have read through all the newsgroups I could find and am getting
> very confused about what to do with my files. I have a heaps of
…[5 more quoted lines elided]…
> reading these.

Tutorial: Using COBOL-created data with non-COBOL programs.

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

The price is right (free for use).

Basically that will tell you you MUST have the COBOL FD or other record
layout documentation - but if you have the *.COB files, you have these
descriptions, so you are probably beyond the most frequent barrier to
success.

I have a Win/32 DLL which uses the FD info and then converts the data to
IEEE format; and several "base" conversion programs (BASIC language). Sounds
like that software would probably be exactly what you want.... except the
part where you say, " What I can't do is spend any money on a one-off tool."

But if you change your mind and are interested in a package of BASIC
language source/executable (PowerBASIC/Windows, very usable with Microsoft
Visual BASIC or any "C" for Windows)   - with the understanding it is not
free - please contact my office.
```

##### ↳ ↳ Re: Reading COBOL "data files"

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2004-07-15T15:25:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0407151425.48388bb2@posting.google.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com>...
> "Scott Hooper" <shooper@rxworks.com> wrote in message
> news:a8341757.0407142138.560efc01@posting.google.com...
…[28 more quoted lines elided]…
> free - please contact my office.

In the case of RM Cobol, IIRC, .COB files are *object* (or
intermediate code) files. So the OP may not have the FDs after all.
```

###### ↳ ↳ ↳ Re: Reading COBOL "data files"

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-07-16T08:09:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ljvef0pr0d33q0qj7j7svdn3dh3uf8d9qm@4ax.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com> <7f64e2ff.0407151425.48388bb2@posting.google.com>`

```
On 15 Jul 2004 15:25:11 -0700, epc8@juno.com (E P Chandler) wrote:

>"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com>...
>> "Scott Hooper" <shooper@rxworks.com> wrote in message
…[32 more quoted lines elided]…
>intermediate code) files. So the OP may not have the FDs after all.
Not necessarally. The object name can be whatever you tell the
compiler to be. The default is .COB.

People here are aware of that.
The point here is that the OP is not willing to spend money with this,
but this is just not possible.
If he has the FS's (which he may have even if he does not have the
other sources) or if he can has whoever developed the APP for the file
layout, then it would be easy to do this work, and he might even get
someone to do it really cheap.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Reading COBOL "data files"

- **From:** sfkhooper <sfkhooper.19q11n@mail.codecomments.com>
- **Date:** 2004-07-21T00:42:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78268131db2911489215debcd29c57f0@news.thenewsgroups.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com>`

```
Hi Michael,

Well I've heard just about everyone say that I'm not going to get
anywhere down the
free-coz-someone-else-has-already-done-it-in-your-preferred-language
road, so I would be quite interested in learning more about your suite
of products. Yes, I have a matching FILExxx.COB and COPYxxx.COB for
every one of my DATAxxx.DAT files, but the COB files do appear to be
object files.

Cheers,
Scott Hooper

By the way, reading through this thread, I keep being referred to as
"OP". The mind boggles with possibilities???
```

###### ↳ ↳ ↳ Re: Reading COBOL "data files"

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-07-21T02:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QhkLc.15449$tk3.15083@newssvr23.news.prodigy.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com> <78268131db2911489215debcd29c57f0@news.thenewsgroups.com>`

```
"OP" = Original Poster


"sfkhooper" <sfkhooper.19q11n@mail.codecomments.com> wrote in message
news:78268131db2911489215debcd29c57f0@news.thenewsgroups.com...
> Hi Michael,
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Reading COBOL "data files"

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-21T11:06:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v6sLc.39975$eH1.18992335@newssvr28.news.prodigy.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <zYtJc.36957$eH1.17637907@newssvr28.news.prodigy.com> <78268131db2911489215debcd29c57f0@news.thenewsgroups.com>`

```
"sfkhooper" <sfkhooper.19q11n@mail.codecomments.com> wrote in message
news:78268131db2911489215debcd29c57f0@news.thenewsgroups.com...
> Hi Michael,
>
…[6 more quoted lines elided]…
> object files.

As outlined in previous posts and explained thouroughly in my tutorial, if
you do not have the file descriptions converting this data reduces to taking
the data files, loading them up in some kind of editor and making some
intelligent guesses as to what data is located where in what format.

To call this a 'painstaking' process is understatement. Ed Guy has a product
called 'parserat' (do an internet search, I know you'll find it) which can
make this a bit easier.

But if you want to send me one matched set of FILExxx.COB and COPYxxx.COB
files I will check them to see if they really are object files and/or might
otherwise be usable for conversion purposes. (address below).

Once you have a record layout, conversion can be a bit tedious, but is not
terribly complicated... in my view, figuring out 'what do do with what I
have' and 'where do I get information I don't have'  will take much longer
than "put what I have into a format I can use."
```

#### ↳ Re: Reading COBOL "data files"

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-07-15T08:57:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<693df0h93ihd96ri0fjk5fp7p40bnq4rl4@4ax.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
There is no such thing as a free lunch.  In this situation it looks
like you're going to get what you will pay for, as it usually works
out.

On 14 Jul 2004 22:38:17 -0700, shooper@rxworks.com (Scott Hooper)
wrote:

> What I can't do is spend any money on a one-off tool.

> install the RM/COBOL runtime. Is this available free anywhere? I understand the developer
>tools would cost, but surely the runtime is free for end users?
```

#### ↳ Re: Reading COBOL "data files"

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-15T11:13:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Kednd6kla7eMGvdRVn-sw@giganews.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
Scott Hooper wrote:
> I have read through all the newsgroups I could find and am getting
> very confused about what to do with my files. I have a heaps of
…[5 more quoted lines elided]…
> reading these.

Let's start over. WHY do you need to convert these files into (pick from
list)?

>
> Also, I have this entire COBOL program but can't run it as I get
> messages talking about the need for me to install the RM/COBOL
> runtime. Is this available free anywhere? I understand the developer
> tools would cost, but surely the runtime is free for end users?


It's almost free. A few thousand.
```

##### ↳ ↳ Re: Reading COBOL "data files"

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-07-16T14:10:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AlRJc.2736$fW3.1560@newssvr22.news.prodigy.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com> <5Kednd6kla7eMGvdRVn-sw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:5Kednd6kla7eMGvdRVn-sw@giganews.com...
> Scott Hooper wrote:
[snip]
> > Also, I have this entire COBOL program but can't run it as I get
> > messages talking about the need for me to install the RM/COBOL
…[4 more quoted lines elided]…
> It's almost free. A few thousand.

Just for the record, not true.

As I have communicated to the OP privately, he can probably accomplish his
mission (which I presume to be, but have not had confirmed, moving data from
the COBOL application to the application sold by his company) by the use of
a single-user Windows runtime (his company's application runs on Windows
only).  The retail cost of a single-user runtime is comparable to the price
of the single-user Windows XP Professional runtime on the same box...

Tom Morrison
```

#### ↳ Re: Reading COBOL "data files"

- **From:** james8049 <james8049.19hp1o@mail.codecomments.com>
- **Date:** 2004-07-16T12:43:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e00907a8978fd20d9f8f1505e1c5432@news.thenewsgroups.com>`
- **References:** `<a8341757.0407142138.560efc01@posting.google.com>`

```
If you know perl WELL, then this link could be useful:--

'http://perlmonks.thepen.com/212360.html'
(http://http://perlmonks.thepen.com/212360.html) 

Lots of assembly required and definately not for the faint hearted,
but, its all free and you can tweak the program to do anything you
want!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
