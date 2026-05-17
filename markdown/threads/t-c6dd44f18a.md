[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Google translate

_13 messages · 7 participants · 2018-02 → 2018-05_

---

### Google translate

- **From:** "ronald.s.draper" <ua-author-14501841@usenetarchives.gap>
- **Date:** 2018-02-27T03:30:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com>`

```
Looking for an example of using Google translate api from mf cobol. Thanks. Ron
```

#### ↳ Re: Google translate

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-02-27T08:20:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com>`

```
In article ,
wrote:
› Looking for an example of using Google translate api from mf cobol. Thanks. Ron

Is this before or after you get back from the maintenance shop with a yard
of flight-line?

DD
```

##### ↳ ↳ Re: Google translate

- **From:** "ronald.s.draper" <ua-author-14501841@usenetarchives.gap>
- **Date:** 2018-03-02T11:21:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p2@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap>`

```
I have searched the web for an example but strangele one does not exist for cobol or c for that fact.
```

###### ↳ ↳ ↳ Re: Google translate

- **From:** "doug_at_milmac_dot_com" <ua-author-176133@usenetarchives.gap>
- **Date:** 2018-03-02T16:54:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p3@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap>`

```
ron··r@gm··l.com wrote in
news:3f834c98-37cd-4d55-8719-7c6··1@goo··s.com:

› I have searched the web for an example but strangele one does
› not exist for cobol or c for that fact.
›

Have you found an example in *any* language?
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 4)_

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2018-03-02T17:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p4@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap>`

```
On Fri, 2 Mar 2018 21:54:23 -0000 (UTC), Doug Miller
wrote:

› ron··r@gm··l.com wrote in
› news:3f834c98-37cd-4d55-8719-7c6··1@goo··s.com: 
…[5 more quoted lines elided]…
› Have you found an example in *any* language?


Examples in C#, Go, Java, Node.js, PHP, Python and Ruby:

https://cloud.google.com/translate/docs/reference/libraries

C#:


using Google.Cloud.Translation.V2;
using System;

public class QuickStart
{
public static void Main(string[] args)
{
Console.OutputEncoding = System.Text.Encoding.Unicode;
TranslationClient client = TranslationClient.Create();
var response = client.TranslateText("Hello World.", "ru");
Console.WriteLine(response.TranslatedText);
}
}


While that's using Google's libraries, the functions are also
available to anything that can issue a normal-ish HTTP request and
handle a response:

https://cloud.google.com/translate/docs/reference/translate
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 5)_

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2018-03-02T17:24:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p5@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p5@usenetarchives.gap>`

```
On Fri, 02 Mar 2018 16:11:20 -0600, Robert Wessel
wrote:

› On Fri, 2 Mar 2018 21:54:23 -0000 (UTC), Doug Miller
›  wrote:
…[37 more quoted lines elided]…
› https://cloud.google.com/translate/docs/reference/translate


(Hit send too soon)

So if you can interface to something like libcurl, you're good to go
too. Although I don't know if there's a non-Linux mainframe port of
libcurl.
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 4)_

- **From:** "ronald.s.draper" <ua-author-14501841@usenetarchives.gap>
- **Date:** 2018-03-21T23:02:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p4@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap>`

```
I just want to "call" translate with text and parameters and get back the results like calling a sub program. Ron.
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 5)_

- **From:** "snetxa" <ua-author-7470312@usenetarchives.gap>
- **Date:** 2018-04-08T23:51:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p7@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p7@usenetarchives.gap>`

```
On 3/22/2018 11:02 AM, ron··r@gm··l.com wrote:
› I just want to "call" translate with text and parameters and get back the results like calling a sub program. Ron.
›

This S/O link purports to describe a REST call from GnuCOBOL. I haven't
checked it myself. I'd love to have the time to.

https://stackoverflow.com/questions/26367026/how-to-make-http-requests-from-cobol

Kind regards,
Bruce.

---
This email has been checked for viruses by AVG.
http://www.avg.com
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 5)_

- **From:** "snetxa" <ua-author-7470312@usenetarchives.gap>
- **Date:** 2018-04-08T23:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p7@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p7@usenetarchives.gap>`

```
On 3/22/2018 11:02 AM, ron··r@gm··l.com wrote:
› I just want to "call" translate with text and parameters and get back the results like calling a sub program. Ron.
›

There's also the code associated with this link in the COBOL FAQ:
https://open-cobol.sourceforge.io/faq/index.html#function-id


---
This email has been checked for viruses by AVG.
http://www.avg.com
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-09T02:07:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p7@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p7@usenetarchives.gap>`

```
On 22/03/2018 4:02 PM, ron··r@gm··l.com wrote:
› I just want to "call" translate with text and parameters and get back the results like calling a sub program. Ron.
›
I had a quick look at this and it is really pretty easy, but there are a
couple of things in terms of "infrastructure" you need to be aware of.
You'll need an account code stored as a JSON file to get access to the
GOOGLE cloud client library, for example.

I had no trouble finding C, Python, Java, PHP and C# sample code.

I'd do it in C# (as a COM module (.DLL), so it can be called from ANY
language (including Fujitsu and Micro Focus COBOL), and it can be used
on a web page or the desktop.

I'd set properties in the component for:

1. Source language. (If known... a ? would make it detect the language...)
2. Target language.
3. Path to input document (Maybe read text from the clipboard, if this
says CLIP...)
4. Path to output document (Write to the system clipboard if this says CLIP)
5. Path to the JSON file. It is supposed to be set into an EV before you
run your application...

If you look here, it will explain what needs to be done:

The component would have ONE Method:

1. TranslateTxt (Note that this would invoke the "TranslateText" method
of the API)

Obviously, this could be easily extended later to provide a list of
available languages, (for example).

If your COBOL doesn't support Object Orientation, the module will need a
different interface, but it isn't hard to provide that. If it does, then
you just instantiate an instance of the component, set the Properties,
and invoke the Method.

In effect, this is COBOL calling into an object layer for a specialized
service.

(cf https://primacomputing.co.nz/PRIMAMetro/ObjectsAndLayers.aspx) There
are 3 pages that describe the reasons for my choices above.

Contact me privately if you'd like to have it written for you; there
will be a charge. If you want to have a go yourself, I'll support you
for free... :-)

Cheers,

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 6)_

- **From:** "ronald.s.draper" <ua-author-14501841@usenetarchives.gap>
- **Date:** 2018-04-28T02:19:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p10@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p7@usenetarchives.gap> <gap-c6dd44f18a-p10@usenetarchives.gap>`

```
I will simply use the kiss method. Get a free dictionary, index it, and call a lookup routine. No need to make a mountain out of a mole hill. Then post the code for others to enjoy. Suggestions of where and how to post public domain cobol code? Ron
```

###### ↳ ↳ ↳ Re: Google translate

_(reply depth: 7)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-28T04:07:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6dd44f18a-p11@usenetarchives.gap>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com> <gap-c6dd44f18a-p2@usenetarchives.gap> <gap-c6dd44f18a-p3@usenetarchives.gap> <gap-c6dd44f18a-p4@usenetarchives.gap> <gap-c6dd44f18a-p7@usenetarchives.gap> <gap-c6dd44f18a-p10@usenetarchives.gap> <gap-c6dd44f18a-p11@usenetarchives.gap>`

```
On 28/04/2018 6:19 PM, ron··r@gm··l.com wrote:
› I will simply use the kiss method. Get a free dictionary, index it, and call a lookup routine. No need to make a mountain out of a mole hill. Then post the code for others to enjoy. Suggestions of where and how to post public domain cobol code? Ron
›
You will get a word-for-word translation which is pretty crap when you
see what the API produces...

Never mind, your call.

Good Luck!

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: Google translate

- **From:** "jessica.colman" <ua-author-14501279@usenetarchives.gap>
- **Date:** 2018-05-11T14:48:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6dd44f18a-p13@usenetarchives.gap>`
- **In-Reply-To:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com>`
- **References:** `<d4a4b888-2430-4d6b-842a-893dea828ad5@googlegroups.com>`

```
Am 27.02.2018 um 09:30 schrieb ron··r@gm··l.com:
› Looking for an example of using Google translate api from mf cobol. Thanks. Ron
›
If your shop has z/OS Connect installed you may use is to convert the
contents of a copybook into a REST call and receive the results vice versa.

Jessica
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
