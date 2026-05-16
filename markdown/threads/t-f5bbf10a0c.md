[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbe: Creating a Cobol dll. How is it done ??

_3 messages · 2 participants · 1999-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Newbe: Creating a Cobol dll. How is it done ??

- **From:** "Svend" <svendl@enterdata.no>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ko4k3$ntn$1@nntp.newmedia.no>`

```
Hi,

I've got one "simple" question for you guys.
Being a C++ guy, I've been assigned to a project where
we're going to make use of some "old" cobol code in our new C++ GUI.

Since the Cobol-people on the project don't really understand the idead of
Dll's and such, they handed
it over to me (they got stuck in DOS :-) ).

Now, my question:
Do you have a sample program, wich compiles and links into a Dll, wich we
can use from our C++ app ? It's enough if it contains one function, taking 1
parameter, and
returns the same parameter back to the caller, as long as I can include the
file in a project and compile.

See, I really don't now how you would prototype such a function, so I'd
appreciate it if
you could give me an explanation of how it'f done, using MF Net Express 3.

Any help would be _greatly_ appreciated.

Thanks.

-Svend
```

#### ↳ Re: Newbe: Creating a Cobol dll. How is it done ??

- **From:** bpetit4354@my-deja.com
- **Date:** 1999-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7krk88$jbo$1@nnrp1.deja.com>`
- **References:** `<7ko4k3$ntn$1@nntp.newmedia.no>`

```
Hi,

You can write Dll's in any language.
I will send you a sample tomorrow (made with MF Visual Cobol 3.5).

Bernard
Siemens ICP Luxembourg
bernard.petit@sni.lu

In article <7ko4k3$ntn$1@nntp.newmedia.no>,
  "Svend" <svendl@enterdata.no> wrote:
> Hi,
>
…[4 more quoted lines elided]…
> Since the Cobol-people on the project don't really understand the
idead of
> Dll's and such, they handed
> it over to me (they got stuck in DOS :-) ).
>
> Now, my question:
> Do you have a sample program, wich compiles and links into a Dll, wich
we
> can use from our C++ app ? It's enough if it contains one function,
taking 1
> parameter, and
> returns the same parameter back to the caller, as long as I can
include the
> file in a project and compile.
>
> See, I really don't now how you would prototype such a function, so
I'd
> appreciate it if
> you could give me an explanation of how it'f done, using MF Net
Express 3.
>
> Any help would be _greatly_ appreciated.
…[5 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Newbe: Creating a Cobol dll. How is it done ??

- **From:** bpetit4354@my-deja.com
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ku9be$ibd$1@nnrp1.deja.com>`
- **References:** `<7ko4k3$ntn$1@nntp.newmedia.no>`

```
Hi,


Here is a Dll: (Sample tested)

       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTDLL.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
      ****************************************************************
      *
      * Enable the PASCAL calling convention (number 3)
      * and call it WINAPI because it is used for WINAPI
      * functions.
      *
      ****************************************************************
       SPECIAL-NAMES.
	   CALL-CONVENTION 3 IS WINAPI.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       LINKAGE SECTION.
      *
      * Short (Integer)  S9(4) Comp-5
      * Long  (Long)	 S9(8) Comp-5
      *
       01  VB-SHORT	 PIC S9(4) COMP-5.
       01  VB-LONG	 PIC S9(8) COMP-5.
       01  VB-CHAR	 PIC X(5).


       PROCEDURE DIVISION WINAPI.
       PROC-1.

	   ENTRY "testcall" USING BY VALUE VB-SHORT
				  BY VALUE VB-LONG
				  BY REFERENCE VB-CHAR.

	   IF VB-SHORT > VB-LONG
	      MOVE "A > B"  TO VB-CHAR
	      MOVE ZERO     TO RETURN-CODE
	   ELSE
	      MOVE "B > A"  TO VB-CHAR
	      MOVE 1	    TO RETURN-CODE
	   END-IF

	   EXIT PROGRAM.



To compile, link & debug:

       viscob testdll /debug+
       call vclinkxd testdll



Here under find TESTDLL.DEF:

       LIBRARY       testdll
       DESCRIPTION   'Visual COBOL Application'
       EXETYPE       WINDOWS
       CODE	      PRELOAD FIXED
       DATA	      PRELOAD FIXED SINGLE
       SEGMENTS      RTSCODE CLASS 'CODE' FIXED PRELOAD
       HEAPSIZE      8192
       EXPORTS       WEP			  @1 RESIDENTNAME
	             VC_GetFirstProcAddress	  @2
	             testcall			  @3


I hope you will understand.

Bernard




In article <7ko4k3$ntn$1@nntp.newmedia.no>,
  "Svend" <svendl@enterdata.no> wrote:
> Hi,
>
…[4 more quoted lines elided]…
> Since the Cobol-people on the project don't really understand the
idead of
> Dll's and such, they handed
> it over to me (they got stuck in DOS :-) ).
>
> Now, my question:
> Do you have a sample program, wich compiles and links into a Dll, wich
we
> can use from our C++ app ? It's enough if it contains one function,
taking 1
> parameter, and
> returns the same parameter back to the caller, as long as I can
include the
> file in a project and compile.
>
> See, I really don't now how you would prototype such a function, so
I'd
> appreciate it if
> you could give me an explanation of how it'f done, using MF Net
Express 3.
>
> Any help would be _greatly_ appreciated.
…[5 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
