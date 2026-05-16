[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Recursion in Cobol

_1 message · 1 participant · 1999-09_

---

### Re: Recursion in Cobol

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sak0l$6ht$1@nnrp1.deja.com>`
- **References:** `<37dc677b.259238160@news1.ibm.net> <19990914031833.29168.00006225@ng-ff1.aol.com> <37def9de.158071504@news1.ibm.net>`

```
In article <37def9de.158071504@news1.ibm.net>,
  redsky@ibm.net (Thane Hubbell) wrote:
> On 14 Sep 1999 07:18:33 GMT, frlsfly@aol.com (FRLSFLY) wrote:
>
…[6 more quoted lines elided]…
> > I don't track you.  It sounds like you return control upwards first
it's not a
> >recursive call by the Realia program; or is it indirect recursion?
> >
…[15 more quoted lines elided]…
>

Thane,

When we added full support for UPS's new communications capabilities
(UPSLink) to our product, we had to use the "is recursive" clause on a
Ca-Realia program to support a callback function for displaying
communication progress while our program was waiting for an API
function call to complete.

Using a supplied API call, we first passed a memory pointer for the
callback entry point in our program to UPSLink and told it to send us
progress status updates.

Then we called the API function to transmit a file via dial-up tcp/ip.
This function would not return control to our program until the file
transfer was completed.

UPSLink then began the file transfer and periodically called our entry
point to report progress.

CA-Realia runtime created another instance of our program to handle the
callback processing. We displayed an SP2 popup window showing the
current status of the file transfer.

When we received a completion status via the callback, we exited the
callback process and CA-Realia runtime cancelled the second instance of
our program and returned to the API call statement that was waiting for
completion in the original instance of our program.

I thought this was a very effective approach for providing callback
functionality in a COBOL program.

John Chafin

P.S. We had a serious problem when we first tried to implement this
and, to make a long story short, CA-Realia support was absolutely
fantastic.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
