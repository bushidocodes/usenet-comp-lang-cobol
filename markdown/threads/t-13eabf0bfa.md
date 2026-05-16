[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# open nfs file

_3 messages · 2 participants · 1999-11_

---

### open nfs file

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38344745.5E384642@eii.fr>`

```
Hello

When I tried to open an NFS imported
file, I receive a RT 213 (too many locks
!!). I have tried with animator (MF).

The right of the file are ok.

What can be the problem ? (the prog did
work properly when the file was not nfs
imported but directly on the server at
the same path).

THanks

Christophe
```

#### ↳ Re: open nfs file

- **From:** "Ian Marshall" <Ian.Marshall@merant.com>
- **Date:** 1999-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8126pr$eu2$1@hyperion.mfltd.co.uk>`
- **References:** `<38344745.5E384642@eii.fr>`

```
File / record locking is an optional feature on NFS and many implementations
do not have this enabled by default. The NFS process'es that control locking
are lockd and statd (these names may be prefixed by in. or rpc. depending on
your operating system e.g. in.lockd or rpc.statd, etc.)

If these processes are not running the will give undefined results when you
attempt to perform a locking operation.

Make sure these processes are running on *both* the NFS client and NFS
server. If they're not, you'll need to get your sysadmin to enable them.
(Usually just commenting out a couple of lines in the NFS startup script).

If you're on a PC based NFS client, I assume these will have configurable
locking as well, although I haven't used a PC NFS program for years. ( Long
live Samba!!! :-) ).
```

##### ↳ ↳ Re: open nfs file

- **From:** webmaster <webmaster@eii.fr>
- **Date:** 1999-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38351394.912ACC2F@eii.fr>`
- **References:** `<38344745.5E384642@eii.fr> <8126pr$eu2$1@hyperion.mfltd.co.uk>`

```


Ian Marshall wrote:

> File / record locking is an optional feature on NFS and many implementations
> do not have this enabled by default. The NFS process'es that control locking
…[7 more quoted lines elided]…
> server. If they're not, ...

I am sorry to say that they are runing on both systems... maybe they are some
parameters for these ?

>
> > Hello
…[17 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
