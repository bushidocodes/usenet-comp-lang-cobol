[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Debug Help

_2 messages · 2 participants · 2003-10_

---

### IBM Debug Help

- **From:** timothyp <member43464@dbforums.com>
- **Date:** 2003-10-09T15:15:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3407868.1065726958@dbforums.com>`

```

How do you set a breakpoint in a called CICS program?



Thanks in advance for your help.



Tim
```

#### ↳ Re: IBM Debug Help

- **From:** George Young <gmyoung@qx.net>
- **Date:** 2003-10-14T19:40:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F8C8964.E24ABA8@qx.net>`
- **References:** `<3407868.1065726958@dbforums.com>`

```
I'm assuming you are stepping through the calling program when you want
to do this?

If so, and the called program is in a load module that hasn't been
loaded yet, I think you'd want to do an

at appearance xxx
go

to get control when the load module it is contained in is loaded.

Then  (or if the subroutine is already known or staticly linked into
what you are already debugging)

at entry xxx
go

to get control when the subroutine is entered. Then you can step / set
breakpoints from there.

For details, the the Reference & Messages book for your version of Debug
Tool here http://www.ibm.com/software/awdtools/debugtool/library/


George

timothyp wrote:
> 
> How do you set a breakpoint in a called CICS program?
…[6 more quoted lines elided]…
> Posted via http://dbforums.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
