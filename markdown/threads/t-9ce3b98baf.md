[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Win95 API Question

_3 messages · 2 participants · 1998-10_

---

### Win95 API Question

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1998-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981016205338.17670.00001784@ng120.aol.com>`

```
Hello,

I am looking for a Win95 API that will allow me to change the "Task Bar
Options" / "Always on Top" selection.  I have looked in the Win32 Software
Development Kit that comes with NetExpress, but i have not been able to locate
the proper API to allow me to modify this selection.  Is anyone aware of the
name of this API ?

Thanks in advance,
Bob Hennessey
```

#### ↳ Re: Win95 API Question

- **From:** "Larry Howe" <larry@comjet.com>
- **Date:** 1998-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckfW1.313$fl.4120007@audrey2.cais.com>`
- **References:** `<19981016205338.17670.00001784@ng120.aol.com>`

```
Bob,

I found where you can retrieve the always on top state. However I could not
find how to set it. HTH.

Larry


SHAppBarMessage


WINSHELLAPI UINT APIENTRY SHAppBarMessage(
    DWORD dwMessage,
    PAPPBARDATA pData
);

Sends an appbar message to the system.

Returns a message-dependent value. For more information, see the Microsoft
Platform SDK documentation for the appbar message sent.
dwMessage
Appbar message value to send. This parameter can be one of the following
values: ABM_ACTIVATE  Notifies the system that an appbar has been activated.
ABM_GETAUTOHIDEBAR  Retrieves the handle to the autohide appbar associated
with a particular edge of the screen.
ABM_GETSTATE  Retrieves the autohide and always-on-top states of the Windows
taskbar.
ABM_GETTASKBARPOS  Retrieves the bounding rectangle of the Windows taskbar.
ABM_NEW  Registers a new appbar and specifies the message identifier that
the system should use to send notification messages to the appbar.
ABM_QUERYPOS  Requests a size and screen position for an appbar.
ABM_REMOVE  Unregisters an appbar, removing the bar from the system's
internal list.
ABM_SETAUTOHIDEBAR  Registers or unregisters an autohide appbar for an edge
of the screen.
ABM_SETPOS  Sets the size and screen position of an appbar.
ABM_WINDOWPOSCHANGED  Notifies the system when an appbar's position has
changed.

pData
Address of an APPBARDATA structure. The content of the structure depends on
the value set in the dwMessage parameter.




Bob7536 wrote in message <19981016205338.17670.00001784@ng120.aol.com>...
>Hello,
>
>I am looking for a Win95 API that will allow me to change the "Task Bar
>Options" / "Always on Top" selection.  I have looked in the Win32 Software
>Development Kit that comes with NetExpress, but i have not been able to
locate
>the proper API to allow me to modify this selection.  Is anyone aware of
the
>name of this API ?
>
>Thanks in advance,
>Bob Hennessey
```

##### ↳ ↳ Re: Win95 API Question

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1998-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981018082113.24661.00002292@ng119.aol.com>`
- **References:** `<ckfW1.313$fl.4120007@audrey2.cais.com>`

```
Hi Larry,

Thanks for the help.  

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
