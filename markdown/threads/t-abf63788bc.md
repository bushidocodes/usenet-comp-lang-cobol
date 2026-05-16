[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Word list

_7 messages · 6 participants · 1999-04 → 1999-05_

---

### Word list

- **From:** "Garry Dell" <gdell@uswest.net>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZTXO2.10640$cq3.236720@news.uswest.net>`

```
I in need of a swear-word list that I could place into a table.

I have a project that will check names against this table to find faulty
names and swear words used as names.

Your help will be greatly appriciated.
```

#### ↳ Re: Word list

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370CC576.9B9C9B9F@NOSPAMhome.com>`
- **References:** `<ZTXO2.10640$cq3.236720@news.uswest.net>`

```
Garry Dell wrote:
> 
> I in need of a swear-word list that I could place into a table.
…[4 more quoted lines elided]…
> Your help will be greatly appriciated.


My last job had a dirty word list.  It was used in a routine which
checked for valid addresses.  Basically, we made sure that users could
add to it.  Misspelled dirty words had to be in it, but names and
addresses can be awfully close to those excluded.

Have you done a web search?
```

##### ↳ ↳ Re: Word list

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990413194424.16588.00000255@ng-fd1.aol.com>`
- **References:** `<370CC576.9B9C9B9F@NOSPAMhome.com>`

```
>> I in need of a swear-word list that I could place
>> into a table.
>> 
>> I have a project that will check names against this
>>  table to find faulty names and swear words... 
snip

Well, you certainly have my curiousity up.  What is the
application here?  I've been around this stuff for almost
20 years, but I swear that's a new one on me.

JC Jones.
```

###### ↳ ↳ ↳ Re: Word list

- **From:** docdwarf@clark.net ()
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f0lmu$s77$1@callisto.clark.net>`
- **References:** `<370CC576.9B9C9B9F@NOSPAMhome.com> <19990413194424.16588.00000255@ng-fd1.aol.com>`

```
In article <19990413194424.16588.00000255@ng-fd1.aol.com>,
JCJ0347 <jcj0347@aol.com> wrote:
>>> I in need of a swear-word list that I could place
>>> into a table.
…[7 more quoted lines elided]…
>20 years, but I swear that's a new one on me.

I've heard that motor-vehicles departments have something like this so as
to make it more difficult for folks to get 'obscene' license-plates... but
the tables had to be expanded over the years because folks began to slip
in obscenities from other languages.

DD
```

###### ↳ ↳ ↳ Re: Word list

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f13rg$jms$1@news.igs.net>`
- **References:** `<370CC576.9B9C9B9F@NOSPAMhome.com> <19990413194424.16588.00000255@ng-fd1.aol.com> <7f0lmu$s77$1@callisto.clark.net>`

```
docdwarf@clark.net wrote in message <7f0lmu$s77$1@callisto.clark.net>...
>In article <19990413194424.16588.00000255@ng-fd1.aol.com>,
>JCJ0347 <jcj0347@aol.com> wrote:
…[16 more quoted lines elided]…
>DD


I'll bet GOTO and ALTER are still available ...
;<0
```

###### ↳ ↳ ↳ Re: Word list

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371498BD.3F6935C@NOSPAMhome.com>`
- **References:** `<370CC576.9B9C9B9F@NOSPAMhome.com> <19990413194424.16588.00000255@ng-fd1.aol.com>`

```
JCJ0347 wrote:
> 
> >> I in need of a swear-word list that I could place
…[10 more quoted lines elided]…
> JC Jones.

Not for me though.  While I'm curious about his application, I will tell
you mine:

I worked in a place which processed data sent in by the public.  This
included names and addresses.  Part of the address cleansing operation
was checking their names against a dirty-word list.
```

#### ↳ Re: Word list

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3738d59a.1650770@news1.frb.gov>`
- **References:** `<ZTXO2.10640$cq3.236720@news.uswest.net>`

```
On Wed, 7 Apr 1999 23:18:26 -0700, Garry Dell wrote:

>I in need of a swear-word list that I could place into a table.

>I have a project that will check names against this table to find faulty
>names and swear words used as names.

>Your help will be greatly appriciated.


Investigate message <6df2qi$4ob@bgtnsc03.worldnet.att.net>, from about
a year ago, in alt.usenet.offline-reader.forte-agent .  That would be
a place to start.  The message was for spam filtering, but a
significant part of it may be what you are looking for.

Generally, I don't like the idea of such things, but sometimes you
have to do things you don't like.  Just be sure that your checks are
not so overly-restrictive that you reject valid names that happen to
be somewhat close to those you don't want.

Also, for ease of maintenance, you may want to store the word list in
a secured file and read it into your program's table.  That way, you
don't have to make changes to your program every time the word list
changes.  Any person with appropriate access to the secured file could
make such changes, which could then be read into the program's table.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
