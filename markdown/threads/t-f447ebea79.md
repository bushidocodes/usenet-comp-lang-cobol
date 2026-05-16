[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL COmpilers for Tuxedo8.0 on Windows2000

_3 messages · 3 participants · 2003-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL COmpilers for Tuxedo8.0 on Windows2000

- **From:** Ganeshmuruga <member22105@dbforums.com>
- **Date:** 2003-01-09T11:50:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2366317.1042113015@dbforums.com>`

```

Hi,
    I am using tuxedo8.0 calls wrapped in cobol on windows2000 and the
    recommended cobol compiler for this is Net Express from Micro Focus.
    Is there any other compiler for cobol available as a trial version
    or a free download supporting the above.

I am able to compile the programs using mainframe express but it is not
recognised by tuxedo.

Ganesh
```

#### ↳ Re: COBOL COmpilers for Tuxedo8.0 on Windows2000

- **From:** "Douglas Gallant" <no_dgallan1_spam@nycap.rr.com>
- **Date:** 2003-01-11T02:16:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8LT9.7047$2z1.2050@twister.nyroc.rr.com>`
- **References:** `<2366317.1042113015@dbforums.com>`

```
If I recall the MF samples correctly, the trick was setting the
call-convention for the tux api calls. If another compiler can setup the
call the same way then I dont see why it shouldn't work. Of course, you also
have to find the right pieces of the COBOL support to include as part of the
TUXEDO buildserver process.

"Ganeshmuruga" <member22105@dbforums.com> wrote in message
news:2366317.1042113015@dbforums.com...
>
> Hi,
…[11 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: COBOL COmpilers for Tuxedo8.0 on Windows2000

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2003-01-11T12:21:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0e102vk655i716694aja4ntcntl6ogjl5t@4ax.com>`
- **References:** `<2366317.1042113015@dbforums.com> <b8LT9.7047$2z1.2050@twister.nyroc.rr.com>`

```
On Sat, 11 Jan 2003 02:16:39 GMT, "Douglas Gallant"
<no_dgallan1_spam@nycap.rr.com> wrote:

>If I recall the MF samples correctly, the trick was setting the
>call-convention for the tux api calls. If another compiler can setup the
…[16 more quoted lines elided]…
>> Ganesh

As I do not know anything about Tuxedo, I can only say it may be
possible to use RM/COBOL V7 to do it. It will imply creating a C
interface following a very specific construct. If you can supply the
list of sub-routines (call's), and their parameters, then this is
duable, and may prove less expensive than MF.

FF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
