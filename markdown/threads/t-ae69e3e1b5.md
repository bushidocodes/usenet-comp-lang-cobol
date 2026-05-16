[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INDEXED BY question

_9 messages · 5 participants · 2006-06 → 2006-07_

---

### INDEXED BY question

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-06-06T20:02:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64g05$of9$03$1@news.t-online.com>`

```
Just asked this Bill off-list.
Blah-blah OCCURS Blah INDEXED BY MY-INDEX.

What is supposed to be the "intial" value of MY-INDEX ?

Reason I ask, I just got a (mainframe) app that seems to
rely on MY-INDEX being initialized to 1.
(And MF, it seems in SE 2.2/4.0 do this).

Roger
```

#### ↳ Re: INDEXED BY question

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-06T11:34:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64hsh$e28$1@si05.rsvl.unisys.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com>`

```
In the general case, the content of any data item is UNDEFINED unless and 
until it is initialized.  I think that applies here.  The most likely value 
for MY-INDEX is zero, but given a declarationlike
    01  whatsis.
         03  some-data pic x(5).
         03  blah-blah OCCURS a-tablesize INDEXED BY MY-INDEX PIC X(5).

a value of zero would point entirely outside the table.

In fact, *in our implementation*, given say a-tablesize = 3, the physical 
*stored values* I'd expect to be valid in MY-INDEX would be 5, 10 and 15. 
There is no requirement that the *value contained* in an INDEXED BY data 
item *be the same* as the corresponding subscript, only that the index 
*correspond* to a subscript when the data item is referenced.

If I did a SET MY-INDEX TO 2, and a SET SOME-NUMERIC TO MY-INDEX, and then 
took a programdump, I'd expect to see 10 in MY-INDEX and 2 in SOME-NUMERIC 
in that programdump.

    -Chuck Stevens


"Roger While" <simrw@sim-basis.de> wrote in message 
news:e64g05$of9$03$1@news.t-online.com...
> Just asked this Bill off-list.
> Blah-blah OCCURS Blah INDEXED BY MY-INDEX.
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: INDEXED BY question

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-06-06T20:44:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64iet$502$01$1@news.t-online.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com>`

```
Sorry, maybe I was not clear -
Does MY_INDEX at the start of execution of the
program/module/function (or whatever else the standard allows)
a value of 0, 1 or undefined ?

(MF sets it to 1)

Roger

"Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag 
news:e64hsh$e28$1@si05.rsvl.unisys.com...
> In the general case, the content of any data item is UNDEFINED unless and 
> until it is initialized.  I think that applies here.  The most likely 
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INDEXED BY question

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-06-06T21:00:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64jdd$78p$01$1@news.t-online.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com> <e64iet$502$01$1@news.t-online.com>`

```
In other words, what is this expected to do -
01  TOPFIELD.
      03  MY-FLD PIC X OCCURS 10 INDEXED BY MY_INDEX.

PROCEDURE DIVISION.
      MOVE "A" TO MY-FLD (MY-INDEX).

Not that it should make any difference (as indices are local) but
a) In Working-Storage
b) In Linkage

(MF is "initializing" to 1, int/gnt, SE 2.2/4.0)
(Regardless of DEFAULTBYTE)

Roger


"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:e64iet$502$01$1@news.t-online.com...
> Sorry, maybe I was not clear -
> Does MY_INDEX at the start of execution of the
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INDEXED BY question

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-06-06T19:02:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jkhg.39712$4L1.37555@newssvr11.news.prodigy.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com> <e64iet$502$01$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message
news:e64iet$502$01$1@news.t-online.com...
> Sorry, maybe I was not clear -
> Does MY_INDEX at the start of execution of the
> program/module/function (or whatever else the standard allows)
> a value of 0, 1 or undefined ?

It's immaterial what its "value" is at the start of the program, because it
has no meaning outside a SET or SEARCH statement or as a subscript.
"Immaterial" is close to "undefined" so if you have to call it something,
call it undefined..

I never had a problem with it before a search, because I have always used
SET index TO ... before a either a search or a sequential access. Note also
that if you *don't* SET it to something before using it, it may have
retained its value from the last use and give you some genuine wacky
results.

MCM
```

###### ↳ ↳ ↳ Re: INDEXED BY question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-06-06T19:07:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%nkhg.224788$sY5.190561@fe10.news.easynews.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com> <e64iet$502$01$1@news.t-online.com>`

```
The answer is
   - in the Standard, the value is undefined
  - "undefined" means that any implementor MAY set it to any value they want 
(either as a documented feature or as an implementation "it happens to work this 
way")

NOTE:
  Both IBM and Micro Focus have a (documented) extension allowing for an index 
to be allowed to be used with any "like-sized" table.  This may (or may not) 
have something to do with the initial value of "1".

Also, Micro Focus has a directive of "OLDINDEX" that may (or may not) impact 
this initial value.
```

###### ↳ ↳ ↳ Re: INDEXED BY question

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-06T12:16:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64k9v$fn7$1@si05.rsvl.unisys.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com> <e64iet$502$01$1@news.t-online.com>`

```
Undefined, which includes whatever Micro Focus or anybody else decides to 
set it to, including "rutabagas".   What the value actually is at the start 
of execution is undefined, and whether the value that it happens to contain 
at the start of execution corresponds to a valid or even meaningful 
subscript at the start of execution is also undefined.

As Bill has pointed out, the implementor *is permitted* by the standard to 
specify an initial value as an extension to standard COBOL, but is under no 
obligation according to the standard to do so, and furthermore is under no 
obligation according to the standard to provide the same subscript 
correspondence value that any other implementor might provide.

    -Chuck Stevens

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e64iet$502$01$1@news.t-online.com...
> Sorry, maybe I was not clear -
> Does MY_INDEX at the start of execution of the
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INDEXED BY question

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-06-06T21:27:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64kvj$art$01$1@news.t-online.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com> <e64hsh$e28$1@si05.rsvl.unisys.com> <e64iet$502$01$1@news.t-online.com> <e64k9v$fn7$1@si05.rsvl.unisys.com>`

```
OK. Thanks. OC has already been updated to do what MF Does :-)

Roger

"Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag 
news:e64k9v$fn7$1@si05.rsvl.unisys.com...
> Undefined, which includes whatever Micro Focus or anybody else decides to 
> set it to, including "rutabagas".   What the value actually is at the 
…[66 more quoted lines elided]…
>
```

#### ↳ Re: INDEXED BY question

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2006-07-16T11:34:49-05:00
- **Newsgroups:** comp.lang.cobol,alt.COBOL
- **Message-ID:** `<CrqdndJ09Zo09yfZnZ2dnUVZ_rednZ2d@comcast.com>`
- **References:** `<e64g05$of9$03$1@news.t-online.com>`

```
In article <e64g05$of9$03$1@news.t-online.com>, simrw@sim-basis.de 
wrote:

>Just asked this Bill off-list.
>Blah-blah OCCURS Blah INDEXED BY MY-INDEX.
…[4 more quoted lines elided]…
>rely on MY-INDEX being initialized to 1.

I'm a bit rusty on my COBOL but it's been my experience that MY-INDEX
has to be initialized by a SET TO statement, unless, of course, it's
being used in a PERFORM ... VARYING statement or something else that 
handles the values for you, like SEARCH.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
