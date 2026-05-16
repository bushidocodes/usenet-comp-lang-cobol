[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# socket interface

_4 messages · 2 participants · 2008-02_

---

### socket interface

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-02-29T09:11:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<325b3aab-d6a2-4697-9df6-71fc71770907@s8g2000prg.googlegroups.com>`

```
Hi,
I'm using an old version of ACUCOBOL (4,3) and would like to open an
IP port to read data.
The idea is to write an IP Interface.
Is anybody aware of some samples to do this?
Thanks for your help.
```

#### ↳ Re: socket interface

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-02-29T12:56:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<119eef3f-010f-4960-b8dd-47bc53f22e96@n75g2000hsh.googlegroups.com>`
- **References:** `<325b3aab-d6a2-4697-9df6-71fc71770907@s8g2000prg.googlegroups.com>`

```
On Feb 29, 9:11 am, Gio <giovanni_dim...@virgilio.it> wrote:
> Hi,
> I'm using an old version of ACUCOBOL (4,3) and would like to open an
…[3 more quoted lines elided]…
> Thanks for your help.


Hi,

You can use the following APIs to allocate/create/handle Windows
sockets and interface with IP ports:

	WSASocket()

	WSAStartup()

	bind()

	listen()

	WSAConnect()

	WSASend()

	WSARecv()

	WSARecvEx()

	WSAAccept()

	DisconnectEx()

	shutdown()

	closesocket()

	WSACleanup()

	WSAGetLastError()

http://tangentsoft.net/wskfaq/

http://msdn2.microsoft.com/en-us/library/ms742212(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms742213(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms737550(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms739168(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741559(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms742203(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741688(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741684(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741513(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms737757(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms740481(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms737582(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741549(VS.85).aspx

http://msdn2.microsoft.com/en-us/library/ms741580(VS.85).aspx

Kellie.
```

##### ↳ ↳ Re: socket interface

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2008-02-29T13:58:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a29b385b-2cdb-48e4-b12e-aa2962cc8e24@d62g2000hsf.googlegroups.com>`
- **References:** `<325b3aab-d6a2-4697-9df6-71fc71770907@s8g2000prg.googlegroups.com> <119eef3f-010f-4960-b8dd-47bc53f22e96@n75g2000hsh.googlegroups.com>`

```
On 29 Feb, 21:56, Kellie Fitton <KELLIEFIT...@yahoo.com> wrote:
> On Feb 29, 9:11 am, Gio <giovanni_dim...@virgilio.it> wrote:
>
…[70 more quoted lines elided]…
> Kellie.

Thank you Kellie,
once again you are a star.

Giovanni
```

###### ↳ ↳ ↳ Re: socket interface

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-02-29T15:33:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7f37814-bbd8-454b-a8d2-0afb07bc0733@d4g2000prg.googlegroups.com>`
- **References:** `<325b3aab-d6a2-4697-9df6-71fc71770907@s8g2000prg.googlegroups.com> <119eef3f-010f-4960-b8dd-47bc53f22e96@n75g2000hsh.googlegroups.com> <a29b385b-2cdb-48e4-b12e-aa2962cc8e24@d62g2000hsf.googlegroups.com>`

```
On Feb 29, 1:58 pm, Gio <giovanni_dim...@virgilio.it> wrote:
>
> Thank you Kellie,
> once again you are a star.
>

Siete molto benvenuti...

Kellie.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
