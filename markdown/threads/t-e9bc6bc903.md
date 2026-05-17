[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COM problem with web based COBOL component String2Num

_2 messages · 1 participant · 2018-07 → 2019-01_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### COM problem with web based COBOL component String2Num

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-07-12T21:53:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fqqf0rFbovuU1@mid.individual.net>`

```
One of the free COBOL components available from:
https://primacomputing.co.nz/PRIMAMetro/FreeComponents.aspx
... has a problem.

The String2Num component gives a server error if you try and run it on
the web page.

The server was recently replaced and a number of components needed to be
re-registered as COM. This one wouldn't do so.

It turns out that it was originally a PowerCOBOL component so it needs
the PowerCOBOL runtime and this is not installed on the server, so it
cannot register itself.

We don't want to install PowerCOBOL on the web server so I'll find
another solution. (It used to run on the old web server because it was
wrapped as C# and used Interop Services, which took care of the .dll
dependencies... I can't remember, but I think we also installed full
COBOL runtimes on the old server...)

However, this does NOT affect the functionality or usefulness of the
component. You can still download it and when you run the setup for it
it will install the necessary PowerCOBOL runtime, so it will run on the
machine you install it to, either on the desktop or on a web page, as
demonstrated in the download package. You can deploy it with your own
COBOL applications and it will run OK.

The main purpose of this free download is to help you get used to OO
COBOL and components and it comes with background concepts and a
comprehensive Help file. The component is free for personal or business
use and around 120 people have downloaded it.

I'm irritated that the web page is no longer running the online test and
as soon as I have some time I'll get it working again.

The download continues to function without problem.

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: COM problem with web based COBOL component String2Num

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2019-01-12T00:49:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e9bc6bc903-p2@usenetarchives.gap>`
- **In-Reply-To:** `<fqqf0rFbovuU1@mid.individual.net>`
- **References:** `<fqqf0rFbovuU1@mid.individual.net>`

```
On 13/07/2018 1:53 pm, pete dashwood wrote:
› One of the free COBOL components available from: 
› https://primacomputing.co.nz/PRIMAMetro/FreeComponents.aspx
…[35 more quoted lines elided]…
› Pete.

After around 6 months, I am pleased to report that this problem is now
solved. (The turnaround on PRIMA incident reports is normally within 24
hours if you are on support, 96 hours if you are not... 6 months is
excessive...)

The delay was because I simply haven't had time to do anything about it;
my entire energy (what's left of it.. :-)) has been focused on getting
our Migration tools completed; for PowerCOBOL Screen Migration -
bringing PowerCOBOL projects into Windows Forms and .NET (SCREEN
Conversion), indexed file to RDBMS (DATA Conversion), and transformation
and re-factoring of the legacy COBOL into objects, that run much better
on the network than monolithic code, via a separate Data Access Layer.
(CODE conversion).

The automation of these conversion tasks is now pretty much complete,
and people are picking it up.

Flat files become an optimized Relational Database in third Normal Form,
loaded with your existing data, the legacy code that used to access them
is transformed so that all of the embedded IO verbs are replaced with
invokes of DAL objects that provide exactly the same service to the
application programs (no logic changes, but the data source is moved
from ISAM to RDBMS automatically and transparently), and a Data Access
Layer is generated that manages the new RDB in a highly efficient way.

I took some time out over the holidays and I was looking at our web site
when I realized the free stuff was not working as it should. (I had
forgotten about the problem...)

Like a few people here, I still have a soft spot for the days of the old
IBM 360 and 370 and it is kind of fun to look at stuff from that era.

Take a look at:

https://primacomputing.co.nz/PRIMAMetro/FreeComponents.aspx

and clicking the STRING2NUM icon will bring you to:

https://primacomputing.co.nz/PRIMAMetro/S2NTestServer.aspx

... which is really a walk down memory lane... :-)

(Try clicking The "Then" and "Now" buttons to see what I mean... :-))

Enjoy!

Pete.

I used to write COBOL; now I can do anything...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
