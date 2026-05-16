[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cpp migration MicroFocus Workbench 2 NetExpress

_1 message · 1 participant · 1999-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### cpp migration MicroFocus Workbench 2 NetExpress

- **From:** Juergen@bop99.ping.de (Juergen Vetter)
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7VdaZpDGOtB@bop99.ping.de>`

```

Hello i have i great problem with netexpress from merant.
the merant german support told me my problem is out of range from the  
hotline.

This is my environment:
=======================
Microsoft windows nt 4.0 service pack 3.0
Merant    netexpress 3.0 service pack 1.0
Microsoft visual c++ 5.x
IBM       universal database 5.2

In the past we use cobol workbench 4.0.26 with no problems.

But now i get this error-code:
173 program not found "checkfil"

a little bit closer:
--------------------
A cpp executable is started, maybe in the netexpress dosbox or direct by
clicking the icon (it dosen't matter).

This cpp executable starts some more dlls (system dlls and some own cpp  
dlls).

I can follow the loadlist by using the c++ debugger and catch the process.

A cobol dll (not static) will be loaded, the runtime cblrtss.dll will be  
loaded.

A few more cpp dlls will be loaded.
The last cpp dll loads a cobol dll (not static).
This cobol dll should load one more cobol dll (not static).
This step fails with the error "173 ... CHECKFIL"

This are the steps i done with no solution:
-------------------------------------------
Start the application from the netexpress dos prompt.
Check the path-environment is less than 256 characters.
Include the netexpress\base\bin and application-path in the path
environment.
Check cobdir and include also the application-path.
Only using must-have directives like CASE and MAKESYN.
Naming the second dll with fullpath does also not solute the problem.

So i think the problem must be between the calling and called program.

I think it's an environment-problem. But what ist the problem?
We build all our cobolsources (more then 750 dlls) as a massmake from the  
commandline.

I didn't understand following results:
--------------------------------------
If i link externl.obj to my cobol-dlls the error 173 changes to 119, which  
means that checkfil is not unique.

So what? CHECKFIL not found or CHECKFIL not unique?

If i use a cobol executable instead of the cpp appication all works fine.

I think it must be my environment, but where is the error or what can i do?

Some more informations:
-----------------------
We do not prefer to build one big dll.
We can't use the CANCEL-Command after calling a dynamic cobol-subprogram,  
because our programs should also run in a mainframe environment.

What can i do?
Our problem is the Y2K-problem. The cobol workbench 4.0.26 is imho not Y2K  
compatible

At Last:
--------
I'm sorry about my terrible english - i hope you can understand this text.
This posting is my last hope
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
