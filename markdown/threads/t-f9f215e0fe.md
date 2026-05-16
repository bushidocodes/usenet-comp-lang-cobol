[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AJAX devtool using Cobol

_5 messages · 3 participants · 2007-11_

---

### AJAX devtool using Cobol

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-11-07T01:19:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com>`

```
Anyone using AJAX devtool, especially TIBCO General Interface?

They have BSD license for AJAX (rich-internet apps) devtool. It is
another head-on technology that uses Javascripting/XML/web service.
Has anyone tried this devtool in Cobol? It is a very impressive way of
maintaining codes. Cobol act as a web service components at the back-
end... and on the front-end, this AJAX devtool.
```

#### ↳ Re: AJAX devtool using Cobol

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2007-11-07T20:07:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgs6eg$16j$1@news-01.bur.connect.com.au>`
- **References:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com>`

```
Hi Rene,

> Anyone using AJAX devtool, especially TIBCO General Interface?

One possibility, and my personal preference, is to deploy a TCP/IP Socket
managed by a Java Applet. As long as you connect back to the same codebase
then no certificate signing is reqd. Server Affinity is completely under
your control, and you can receive any number of rows, or array elements, in
response. Unlike Ajax or a.n.other option, you can achieve a high degree of
parallelism with the client JavaScript enriching and adding value to rows,
and presenting them, while the server is busy filling the queue with the
rest of the result set. Realtime visual status aids such as a Record Count
or a Diminishing Scrollbar can also help the user to feel that the server
hasn't forgotten about them. (I'm also quite excited about the prospect of
dynamic/animated chart building with Flash's "Data Binding" and the
streaming of periodic sales figures down the pipe - but I haven't worked
that part out yet :-) Anybody with opinions/experiences of
JavaScript+FABridge -vs- Native ActionScript Getters and Setters?)

Anyway, here is an example of what I'm talking about: -
http://manson.vistech.net/t3$examples/demo_client_web.html

Username: TIER3_DEMO
Password: QUEUE

I'll post more demo instructions at the end of this but, to see the bit you
want in action, just enter an asterix "*" for the Queue Name and then click
the green "Get Job Info" button. You'll see that the <select> list is
populated from the server, one row/element at a time. I have tested this
with up to 3000 rows and scalability doesn't seem to be an issue! The one
performance problem I experienced was the tear-down of the old/previous
option-collection before populating the results from the next query. Thanks
to RobG, the problem was solved with DOM Node Cloning and Replacing.

All of the client source code can be found at:-
http://manson.vistech.net/t3$examples/

QUEUE_LOOKUP.HTML contains the code you'd be interested in specifically the
jobLookup() and getResponse() functions, although following the selectRef
and selectClone objects through the code could be worthwhile. The driving
Applet is CornuCopiae.java and the object definition can be found in
CornuCopiae.html. (The main Socket stuff being in Tier3Socket.java) NB: All
Applet Java code is application-neutral and completely reusable. No Java
coding "need" be done for applications 2 to N.

If you'd prefer someone to have Mugabe(esque) totalitarian control over your
server interaction then I'd suggest Silverlight. (Or Flash's Data Management
Services - "All client-resident data in sync" - Yeah right. But at least
with Flash (and obviously Java) you get the choice!)

Although my code is, at present, VMS-specific you could achieve similar
results with simple INETd server processes, if you dropped the authorization
and were happy with one server process per user.

Cheers Richard Maher

PS. The code doesn't automatically check for versions, but does work on
recent versions of Mac OS X Safari (1.5 JDK), Firefox, Windows Firefox and
IE 6 and 7, Opera, Linux and Firefox. You must have JavaScript enabled,
Applets enabled and a recent JVM. You also can't be behind a firewall that
bans outgoing connections unless you open up 5255.

Here's some of the functionality-catwalk highlights from the example: -

1) Full, one-time, context-specific, VMS User Authentication. No Cookies,
Session IDs, Password Caching or generic Work-Station or Browser
credentials! When you load the demo_client_web.html page into your browser,
a Java Applet is automatically activated that prompts the user for their VMS
Username and Password via a modal dialogue box. If authorization fails, the
"Access Denied" page will be displayed and VMS Intrusion Detection (in
accordance with the policy set out by your System Manager) will be enforced,
and Login-Failures is incremented in SYSUAF. Alternatively, if authorization
is successful (and you left the "Display Logon Confirmation" box ticked)
then a Welcome dialog box will be displayed detailing last login times and
the number of unsuccessful login attempts (if any). Login-Failures is now
set to zero and last non-interactive login time is set to the current time.

If you refresh this page, or move to a different page, then the server
connection is broken and you must be re-authorised before continuing to
access the Demo Queue Manager application.

2) A Hot-Abort button! After you have pressed the "Get Job Info" button
you'll notice that the "Abort Request" button becomes active and turns red.
(Actually you probably won't notice 'cos this query completes too quickly
:-) You can edit the DEMO_UARS.COB code and change the value of the
DEBUG_DELAY field if you want to see your 3GL Interrupt routine in action.)
In this case the cancel-flag I've set in the AST routine is picked up in the
mainline code, resulting in the graceful termination of the loop that
controls "next queue" (or "next row") retrieval.

Also, if you look at the getResponse() function in query_lookup.html, you
will see how the chan.setTimeout() method has been deployed to provide an
erstwhile "blocking" socket Read with the ability to surrender the
event-thread for things like processing the Abort button and ticking over
the clock. (all of this, and much more, "infrastructure-code" is already
there and doesn't have to be re-invented)

3) Predictive text on the Queue Name field so that all matching VMS queues
are retrieved on-demand as the user types. As is now common-place with many
websites, a drop down select list of matching options is automatically
retrieved from the server and made available for the user to select from.

4) Result-set drill-down. Many database queries return a result-set of rows
for the user to scan through and possibly drill-down into for more detail.
I've provided a reasonably generic example of this, where all matching Job
Entries have been populated into a dynamic HTML select list. Once again the
user was able to see the select-list grow, the scroll-bar diminish, and
"Jobs Found" field tick over in real-time, whilst continually being
empowered (by the Abort button) to curtail the results at any time!

If you click on an entry in the Select List then the <frame> changes and the
entry_details.html page appears. See the parent.entry_details.getReady()
call in queue_lookup.html to see how the handover to the new frame takes
place. (Also see goBack() in entry_details.html to see how simply that
operation is reversed.)

The user is now free to move forward, back, first, last, refresh, and delete
queue entries, or return to the previous frame. (Thanks to the deployment of
the VMS Persona functionality, the user is only permitted to see those queue
entries that the Username they signed in under is permitted to see. They can
also *only* delete those entries that this username is allowed to delete.)

5) Floating <div>s. You'll see that any queue names are highlighted in bold
and italics; if you mouseover any of these fields when they are not blank
then the current status information for that queue will be retrieved from
the server and displayed in a quasi-popup DIV.

6) Local Result-Set Sort. If you click on the "header" or "first" row in the
Select List of queues, you will get a popup prompting you for a sort key. If
you select one, the contents of the Select List are sorted in the chosen
order. (Try enter "*" for the Queue Name and then clicking "Get Job Info" to
get some data worth sorting)

See http://manson.vistech.net/t3$examples/demo_uars.cob for the cobol
source.

Cheers Richard Maher

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message
news:1194427140.232270.136480@z24g2000prh.googlegroups.com...
> Anyone using AJAX devtool, especially TIBCO General Interface?
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: AJAX devtool using Cobol

- **From:** khakman <khakman@tibco.com>
- **Date:** 2007-11-09T10:02:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194631365.341592.15490@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com>`
- **References:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com>`

```
You might also want to ask this question in the TIBCO General
Interface developer forums at http://developer.tibco.com/gi.

I know of several cases where cobol systems were exposed via web
services then extended to the browser via a TIBCO GI Ajax client.
Perhaps you'd get some insight there too.

Also in regard to a desire for real-time data, you might look at
http://ams.tibco.com, and http://www.tibco.com/devnet/gi/dwr.jsp for
DWR's ReverseAjax capabilities (though both of those are Java
centric).

--Kevin (tibco)
```

##### ↳ ↳ Re: AJAX devtool using Cobol

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-11-13T05:27:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194960458.905991.272440@e34g2000pro.googlegroups.com>`
- **In-Reply-To:** `<1194631365.341592.15490@19g2000hsx.googlegroups.com>`
- **References:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com> <1194631365.341592.15490@19g2000hsx.googlegroups.com>`

```
Thanks Kevin.

Im going to try Tibco using Cobol web service and hopefully if time
forbids I'm going to post the link here.
-----------------------------------

Hi Richard,

Tried your link but it seems that your entry fields are disabled... or
because of the browser functionality maybe that I could not make the
"Username" and "Password" entry fields to work.
```

###### ↳ ↳ ↳ Re: AJAX devtool using Cobol

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2007-11-14T06:57:54+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhd6p9$38c$1@news-01.bur.connect.com.au>`
- **References:** `<1194427140.232270.136480@z24g2000prh.googlegroups.com> <1194631365.341592.15490@19g2000hsx.googlegroups.com> <1194960458.905991.272440@e34g2000pro.googlegroups.com>`

```
Hi Rene,

> Tried your link but it seems that your entry fields are disabled... or
> because of the browser functionality maybe that I could not make the
> "Username" and "Password" entry fields to work.

When you say they don't "work" what happens. If the dialogue box has popped
up then the Applet looks to have loaded, but you must be running a recent
JRE. What Browser/OS/JRE?

Cheers Richard Maher

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message
news:1194960458.905991.272440@e34g2000pro.googlegroups.com...
> Thanks Kevin.
>
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
