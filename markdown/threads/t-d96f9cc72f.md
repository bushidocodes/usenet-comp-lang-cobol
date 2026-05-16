[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# License Management Service

_5 messages · 3 participants · 2009-12_

---

### License Management Service

- **From:** JC <c.joydeep@gmail.com>
- **Date:** 2009-12-11T15:55:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b22bfee$0$276$14726298@news.sunsite.dk>`

```
Hello,

I have downloaded and installed Net Express Personal Edition on Windows 
Vista. But whenever I try to start the application, it says "License 
Management Service is not running". And then stops. I don't have 
license number or Work Order no. So How do I start that service? Please 
help me.

Thanks,
```

#### ↳ Re: License Management Service

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2009-12-13T05:24:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com>`
- **References:** `<4b22bfee$0$276$14726298@news.sunsite.dk>`

```
On Dec 11, 9:55 pm, JC <c.joyd...@gmail.com> wrote:
> Hello,
>
…[6 more quoted lines elided]…
> Thanks,

If I recall correctly, you have to be online and go to the MF web site
```

##### ↳ ↳ Re: License Management Service

- **From:** "Joydeep Chakrabarty" <c.joydeep@gmail.com>
- **Date:** 2009-12-16T14:33:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b294455$0$273$14726298@news.sunsite.dk>`
- **In-Reply-To:** `<5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com>`
- **References:** `<4b22bfee$0$276$14726298@news.sunsite.dk> <5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com...
> On Dec 11, 9:55 pm, JC <c.joyd...@gmail.com> wrote:
>> Hello,
…[9 more quoted lines elided]…
> If I recall correctly, you have to be online and go to the MF web site

I visit that website and their support and help forum regularly. But nowhere 
did I find any kind of help. I don't know when I'd be able to start the 
application.
```

###### ↳ ↳ ↳ Re: License Management Service

- **From:** "me" <me@home.com>
- **Date:** 2009-12-17T11:48:58
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<872dnanAtccxh7fWnZ2dnUVZ8sCdnZ2d@bt.com>`
- **References:** `<4b22bfee$0$276$14726298@news.sunsite.dk> <5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com> <4b294455$0$273$14726298@news.sunsite.dk>`

```
Article 1594 from the MF Knowledgebase - try their Resolution.

Unable to connect to License Manager
This article explains what to do if the message "Unable to connect to 
License Manager" occurs.

Problem:
When running APPTRACK we encountered the error "Unable to connect to License 
Manager". Does this type of error only occur in the Windows runtime product 
server for COBOL version 5.0 WrapPack 5 onwards?

Resolution:
License Manager runs as a Windows Service. First, check that the Micro Focus 
License Manager has been started. Run the services menu (services.msc) or 
access it via the control panel.  Search for Micro Focus License Manager. If 
it is present, hit the Start option. If not present, from a DOS prompt, 
enter the command mflmwin -i which will install the service and should also 
start it. If it doesn't start automatically, then start it using the 
Services menu.
```

###### ↳ ↳ ↳ Re: License Management Service

_(reply depth: 4)_

- **From:** JC <c.joydeep@gmail.com>
- **Date:** 2009-12-17T10:51:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b2a61b6$0$275$14726298@news.sunsite.dk>`
- **References:** `<4b22bfee$0$276$14726298@news.sunsite.dk> <5e16dbd6-8e04-4c85-8471-d886d750169c@p8g2000yqb.googlegroups.com> <4b294455$0$273$14726298@news.sunsite.dk> <872dnanAtccxh7fWnZ2dnUVZ8sCdnZ2d@bt.com>`

```
me submitted this idea :
> Article 1594 from the MF Knowledgebase - try their Resolution.
>
…[15 more quoted lines elided]…
> it. If it doesn't start automatically, then start it using the Services menu.

Micro focus Net Express Personal Edition does not have any program 
called "mflmwin". I am running on Windows Vista 32. I could not find 
any license manager service in my services.

Thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
