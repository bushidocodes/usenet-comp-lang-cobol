[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress Ver 2.0 to 3.0 upgrade problem

_1 message · 1 participant · 1999-01_

---

### NetExpress Ver 2.0 to 3.0 upgrade problem

- **From:** vgibson@westga.edu (Vince Gibson)
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a89308.10015221@news.westga.edu>`

```
I have received and installed NetExpress V3.0 on my development
machine (In addition to V2.0. )

I opened and recompiled all of my GUI application programs developed
with 2.0, in version 3.0.

I then installed the ver 3.0 runtime on a client machine.

I moved copies of my (newly recompiled under 3.0) applications to the
server.

I created a shortcut to my main program on the client and called it�It
would not work.

I then copied all of the runtime files from the client machine into
the application directory on the server where the called .EXE's and
GS's are located. I then tried it again.

My initial login program comes up and runs OK. Once the user id and
password are validated, the program then does a call as follows to the
main menu program:

CALL-MENU SECTION.
          MOVE "J:\FPO\fpomenu.exe" to Command-Line
          MOVE 128 TO Command-Line-Len
          MOVE 0 TO Status-Code
          CALL "CBL_EXEC_RUN_UNIT" USING
               BY REFERENCE Command-Line
               BY VALUE Command-Line-Len
               BY REFERENCE Run-Unit-ID
               BY VALUE Stack-size
               RETURNING Status-code
          END-CALL
          .

It then returns the following message:

 


Question: What exactly do I have to do to get the programs compiled in
V3.0 to work?


I then attempted to call the v2.0 version of the application and it
won't work either. Now the client machine with the new runtime will
not run either version of the application.

I looked in the "readme" file which came with the software, which
states that all code is compatible and that all I had to do was to
recompile any applications developed in 2.0 NetExpress, in NetExpress
3.0.

I recompiled the program under 3.0 and installed the new runtime on
the client. If this stuff is "backward compatible" as advertised, the
old version should still work, as well as the new.

The setup under the v2.0 is this:

The .EXE, .GS, and v2.0 runtime files are located on a network server
in an application directory. The client PC's have the v2.0 runtime
installed on them. I have a shortcut on the client PC which points to
the .EXE on the server. The user clicks on the shortcut, and the
program runs.

I setup is the same under v3.0 except that the 3.0 runtime on the
client is calling a 2.0 developed, 3.0 recompiled program located on
the server.

What am I missing?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
