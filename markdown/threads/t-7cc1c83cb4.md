[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

_5 messages · 4 participants · 1998-05_

---

### Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-05-28T13:55:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kk8fa$otn$1@nnrp1.dejanews.com>`

```

I am trying to build a COBOL DLL (Built with NetExpress 2.0) that can be
called from a Visual C++ 5.0 C program (not C++). Let us say that the
name/entry point of the DLL is myfunc and this is the procedure division
statement.

01 myvara pic x(10).
01 myvarb pic x(10).

procedure division using myvara, myvarb.


This is on Windows NT 4.0 do I need a special names calling Convention of 74
for winapi on the procedure division. What should the prototype look like for
the C program?

I now use

void __stdcall myfunc (void *, void *) or something like that.

Gene Webb
Project Manager, LABs
Sterling Commerce, Banking Systems Division
15301 Dallas Parkway,
Suite 400, LB 23
Dallas, Texas, 75248
Phone: (972)788-2580
Fax: (972)788-1049

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

- **From:** "jean-michel bain-cornu" <ua-author-6589093@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cc1c83cb4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6kk8fa$otn$1@nnrp1.dejanews.com>`
- **References:** `<6kk8fa$otn$1@nnrp1.dejanews.com>`

```

Thane Hubbell wrote:

› On Thu, 28 May 1998 17:55:54, gen··.@ste··m.com wrote:
› 
…[5 more quoted lines elided]…
› I know I sound like a commercial - but I was just reading the Manual
 
› It's normal, you are from IBM
 
› from Fujitsu 4.0 (Getting started) - (Now in PDF format!!!) - and they
› make the call from visual basic to the cobol program virtually
…[3 more quoted lines elided]…
› might want to look at Fujitsu.  They are STRONG competition with MF
 
› This is completely out of the problem
 
› for GUI and Internet based development, and I've never had a project
› corrupted using it! .
```

##### ↳ ↳ Re: Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cc1c83cb4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7cc1c83cb4-p2@usenetarchives.gap>`
- **References:** `<6kk8fa$otn$1@nnrp1.dejanews.com> <gap-7cc1c83cb4-p2@usenetarchives.gap>`

```

›› It's normal, you are from IBM
 
 
› Just to Clarify. IBM serves as my ISP - I have no other association
› with them.

Whew. For a minute there I thought the neighbourhood was going
down the tubes.
```

#### ↳ Re: Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

- **From:** "jean-michel bain-cornu" <ua-author-6589093@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cc1c83cb4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6kk8fa$otn$1@nnrp1.dejanews.com>`
- **References:** `<6kk8fa$otn$1@nnrp1.dejanews.com>`

```

You need "char*, char*" and you have to take care than the cobol will try to use
10 characters.

gen··.@ste··m.com wrote:

› I am trying to build a COBOL DLL (Built with NetExpress 2.0) that can be
› called from a Visual C++ 5.0 C program (not C++). Let us say that the
…[26 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: Calling a NT COBOL DLL (NetExpress) from Visual C++ 5.0

- **From:** "gael wilson" <ua-author-6589191@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cc1c83cb4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7cc1c83cb4-p4@usenetarchives.gap>`
- **References:** `<6kk8fa$otn$1@nnrp1.dejanews.com> <gap-7cc1c83cb4-p4@usenetarchives.gap>`

```



jean-michel bain-cornu wrote in article
<356··.@pra··e.fr>...
› You need "char*, char*" and you have to take care than the cobol will try
› to use
…[24 more quoted lines elided]…
›› void __stdcall myfunc (void *, void *) or something like that.

Gene, if you use the __stdcall on the function prototype then, yes, you
will need to specify call-convention 74 on the procedure division of your
COBOL program. However, if you specify __cdecl instead (which is the
default) the procedure division statement should be okay as it is.

If you create your COBOL DLL from a NetExpress project you will need to
select the option on the build settings to keep the temporary files when
the DLL is created in order to get the .LIB you will need when creating
your C EXE. Alternatively, if you use the command-line tools use the /K
option on CBLLINK.

Then, all you need to do is use the .LIB when linking the C program

cl /MD cprog.c /link myfunc.lib

The /MD option was specified because the COBOL support uses the shared C
run-time library.

›› 
›› Gene Webb
…[13 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
