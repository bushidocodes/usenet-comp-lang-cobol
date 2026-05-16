[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PreProcessor in MF Express (MicroFocus)

_4 messages · 2 participants · 2004-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### PreProcessor in MF Express (MicroFocus)

- **From:** "Topaz" <topaz@osiris.be>
- **Date:** 2004-02-17T19:43:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40326165$0$766$ba620e4c@news.skynet.be>`

```
Does anyone know if it's possible to access a remote (mainframe) database
within a Cobol preprocessor for Mainframe Express

Thanx, Topaz
```

#### ↳ Re: PreProcessor in MF Express (MicroFocus)

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2004-02-20T11:12:28
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c14spb$8nh$1@hyperion.microfocus.com>`
- **References:** `<40326165$0$766$ba620e4c@news.skynet.be>`

```
Hi Topaz

With Mainframe Express you can debug your CICS/IMS or batch application
against our own DB2-like database engine, so that you can work without a
connection to the mainframe. Alternatively you can connect to a mainframe
DB2 region and debug your code against existing mainframe data. This works
either way with the SQL Preprocessor included 'in the box'. Does that answer
your question?

If you have any other questions about Mainframe Express, a good place to
post and share views with other users is in the Micro Focus forums at
http://www.cobolportal.com/microfocusforum.


Best regards,

Brian Crane
Product Director
Micro Focus


"Topaz" <topaz@osiris.be> wrote in message
news:40326165$0$766$ba620e4c@news.skynet.be...
> Does anyone know if it's possible to access a remote (mainframe) database
> within a Cobol preprocessor for Mainframe Express
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: PreProcessor in MF Express (MicroFocus)

- **From:** "Topaz" <topaz@osiris.be>
- **Date:** 2004-02-20T18:38:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40364663$0$775$ba620e4c@news.skynet.be>`
- **References:** `<40326165$0$766$ba620e4c@news.skynet.be> <c14spb$8nh$1@hyperion.microfocus.com>`

```
Thanks for your answer, Brian, but it doesn't answer my question. We are
looking at MicroFocus Mainframe Express to offload some of the workload of
the mainframe. We currently have our own repository and our own preprocessor
on the mainframe. This mainframe preprocessor gets data from the repository
at compile time, in order to insert the necessary cobol statements. Before
we purchase MicroFocus Mainframe Express we want to know if we can rewrite
our preprocessor to use with MicroFocus MainFrame Express, and if it's
necessary to migrate our repository from the mainframe to a LAN.

Hope you can help me on that.

Thanx, Topaz

"Brian Crane" <brian.crane@microfocus.com> wrote in message
news:c14spb$8nh$1@hyperion.microfocus.com...
> Hi Topaz
>
…[4 more quoted lines elided]…
> either way with the SQL Preprocessor included 'in the box'. Does that
answer
> your question?
>
…[14 more quoted lines elided]…
> > Does anyone know if it's possible to access a remote (mainframe)
database
> > within a Cobol preprocessor for Mainframe Express
> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: PreProcessor in MF Express (MicroFocus)

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2004-02-24T12:14:26
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1fi10$dtk$1@hyperion.microfocus.com>`
- **References:** `<40326165$0$766$ba620e4c@news.skynet.be> <c14spb$8nh$1@hyperion.microfocus.com> <40364663$0$775$ba620e4c@news.skynet.be>`

```
Topaz,

It's difficult to say for sure, but I cannot think of any reason why this
shouldn't be possible. Mainframe Express allows customised preprocessors to
be put in place. It would then be necessary to establish a communication
method between the preprocessor and your repository, or to migrate the
repository to the LAN as you suggest.

Without knowing all the details and having a closer look at your
environment, it is hard to be more specific. However, I would say that most
Mainframe Express shops have something 'special' about their mainframe
development/production environment which needs to be reflected in the move
to Mainframe Express. Mainframe Express provides a very flexible toolset,
and we often are required to integrate it with 3rd party or 'home-grown'
tools and utilities. The question of how Mainframe Express would be
implemented at your site to meet your exact needs would be something that is
considered fully by our implementation experts.

Are you in contact with anyone else at Micro Focus? If not, and you require
contact details, please email me direct with your full name, organization
and location and I will see what I can do to help.

Best regards,

Brian Crane
Product Director
Micro Focus




"Topaz" <topaz@osiris.be> wrote in message
news:40364663$0$775$ba620e4c@news.skynet.be...
> Thanks for your answer, Brian, but it doesn't answer my question. We are
> looking at MicroFocus Mainframe Express to offload some of the workload of
> the mainframe. We currently have our own repository and our own
preprocessor
> on the mainframe. This mainframe preprocessor gets data from the
repository
> at compile time, in order to insert the necessary cobol statements. Before
> we purchase MicroFocus Mainframe Express we want to know if we can rewrite
…[13 more quoted lines elided]…
> > connection to the mainframe. Alternatively you can connect to a
mainframe
> > DB2 region and debug your code against existing mainframe data. This
works
> > either way with the SQL Preprocessor included 'in the box'. Does that
> answer
…[26 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
