[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HP Microfocus Licencing

_3 messages · 3 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### HP Microfocus Licencing

- **From:** "Ian" <i.patterson@virgin.net>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.hp.apps,comp.sys.hp.hpux,comp.sys.hp.misc
- **Message-ID:** `<7ie9gg$e3r$1@nclient5-gui.server.virgin.net>`

```
We're in the process of upgrading a large system (~5 million lines of code)
built mostly in HP Microfocus COBOL v3.2 running on HP UX 10.01 to HP
Microfocus COBOL v4.1 running on HPUX 11.0. The transition from a technical
point of view has been fine, with a simple recompilation being for the most
part all thats been required.

We're less impressed from a commercial point of view. Reading the terms of
HP's licence in this case, for v3.2 it clearly states that it was a server
based licence whilst for 4.1 it is user based, and operates with a pool of
available licenes.Our HP account manager is claiming that, even though we've
fully supported on v3.2 under our maintenance contract, that only entitles
us to upgrades to the n licenes we have in place, which is nowhere near
enough to support the development team we have in place. As this is
expensive, we're not particularly impressed by his viewpoint.

Has anyone else had this experience? Has anyone had an outcome other than
'buy more licences'?

Thanks in advance for any help you're able to give

Ian

================
i.patterson @ virgin.net
```

#### ↳ Re: HP Microfocus Licencing

- **From:** "pmjones" <pmjones@netcomuk.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.hp.apps,comp.sys.hp.hpux,comp.sys.hp.misc
- **Message-ID:** `<7iev3b$18p$1@taliesin.netcom.net.uk>`
- **References:** `<7ie9gg$e3r$1@nclient5-gui.server.virgin.net>`

```
I'm not sure I have an exact answer to your query. I'm a contractor
currently working for an outsourcing company. We have recently moved from
4.0 to 4.1, but now sourcing Cobol directly from Merant (Micro Focus' new
id, for those who don't know). I believe that we are on a user licence as
well, where previously it was server based. I guess the change is down to
Merant, and not HP - they would have to licence in the same way, or HP
wouldn't be able to account to Merant.

This will help even less, but we only have a few licences, as we have a
batch system, with all development done using NetExpress (was Workbench) on
NT. The productivity gain is tremendous, as it is a gui editor and animator,
so no Unix editor (ie. vi or the like) needed - nor the cumbersone toolbox
Unix editor. We get new staff in and they are coding within days! The code
(using Oracle SQL via the Oracle pre-compiler and cobsql - if that means
anything) is 100% compatible.

See - I told you I wasn't going to help you much. Oh, and just to prove I
don't work for Merant, and am not selling here - the licences are VERY
expensive.

Pete Jones
```

#### ↳ Re: HP Microfocus Licencing

- **From:** mtsuji@pacificnet.net (Mark Tsuji)
- **Date:** 1999-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.hp.apps,comp.sys.hp.hpux,comp.sys.hp.misc
- **Message-ID:** `<374e3276.1880009@news.pacificnet.net>`
- **References:** `<7ie9gg$e3r$1@nclient5-gui.server.virgin.net>`

```
We ran into this problem several months ago.  Under 11.0 HP has
changed their licensing usage to user based.  We found that when our
licenses ran out when  programmers invoked the compiler. The
programmer locks the use count for 1 hour.  We were told that if you
had 10 programmers, you might need 30 licenses, since one programmer
can lock up more than one license if invoked several times per hour.
This was preposterous and unacceptable.   We dropped HP cobol and
licensed directly with Microfocus.  MF licenses by server, not by use
count.  HP called their method "a business decision".  We told them
that large account will not accept it.  It's starting to happen..Don't
get it from HP.  We have the HP runtime for 10.01 compatibility on
11.0 and MF cobol for all conversion/future development.

On Tue, 25 May 1999 14:43:35 +0100, "Ian" <i.patterson@virgin.net>
wrote:

>We're in the process of upgrading a large system (~5 million lines of code)
>built mostly in HP Microfocus COBOL v3.2 running on HP UX 10.01 to HP
…[25 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
