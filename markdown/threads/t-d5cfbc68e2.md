[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to animate cobol programs

_4 messages · 4 participants · 2000-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to animate cobol programs

- **From:** "Johan den Boer" <jj.den.boer@hccnet.nl>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bnrb4$e2o$1@news.hccnet.nl>`

```
Hi,

I have a cobol program and I want to animate it. The program has some
C-functions in it. When I step on a call to a c-function ( call "c-func" ) I
get an error no 173, which means program not found on drive/directory.
I have set the COBPATH and PATH environment to point to my cobol
and C directories, so that should not be the problem.
Does anyone have an idea why I cannot call function when animating ?
I do not have the problem when I call another cobol program, it only
happens when I call a C-function.

regards

Johan den Boer
e-mail : jj.den.boer@hccnet.nl
```

#### ↳ Re: How to animate cobol programs

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bo0hc$b9l$1@hyperion.mfltd.co.uk>`
- **References:** `<8bnrb4$e2o$1@news.hccnet.nl>`

```
Johan,

Whenever possible, can you please indicate the product you are using when
posting a question. It makes it much easier for people with the relevant
knowledge to be able to help.

As the error is a 173, I will assume that you are referring to Micro Focus
COBOL. If so, if you are calling a C program you will need to ensure that
the C function is loaded before you can call it. If it is in a DLL you need
to load the DLL by doing

SET procedure-pointer TO ENTRY 'dll-name'.

unless the DLL has the same name as the C function you are calling, in which
case it should not be necessary.


Johan den Boer <jj.den.boer@hccnet.nl> wrote in message
news:8bnrb4$e2o$1@news.hccnet.nl...
> Hi,
>
> I have a cobol program and I want to animate it. The program has some
> C-functions in it. When I step on a call to a c-function ( call "c-func" )
I
> get an error no 173, which means program not found on drive/directory.
> I have set the COBPATH and PATH environment to point to my cobol
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How to animate cobol programs

- **From:** blossom153@aol.com (Blossom153)
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000327160815.28327.00002665@ng-bk1.aol.com>`
- **References:** `<8bo0hc$b9l$1@hyperion.mfltd.co.uk>`

```
Also note that the entry-point name you are calling is CASE sensitive.  You may
want to experiment using the "CASE" compiler directive.
```

#### ↳ Re: How to animate cobol programs

- **From:** "Stonelion" <M.F.M.Lowenstein@net.HCC.nl>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8boj2h$huc$1@tesla.a2000.nl>`
- **References:** `<8bnrb4$e2o$1@news.hccnet.nl>`

```
If the function 'c-func' is part of a DLL, you need to load this DLL. You
can do this by using the animator DO function. Then type: Call "nameofDLL".

Johan den Boer <jj.den.boer@hccnet.nl> wrote in message
news:8bnrb4$e2o$1@news.hccnet.nl...
> Hi,
>
> I have a cobol program and I want to animate it. The program has some
> C-functions in it. When I step on a call to a c-function ( call "c-func" )
I
> get an error no 173, which means program not found on drive/directory.
> I have set the COBPATH and PATH environment to point to my cobol
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
