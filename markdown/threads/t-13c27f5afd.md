[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Cobol - how to distribute .exe file?

_8 messages · 4 participants · 2011-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Fujitsu Cobol - how to distribute .exe file?

- **From:** zalek <zalekbloom@hotmail.com>
- **Date:** 2011-08-03T16:25:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com>`

```
I am using Fujitsu Cobol - when I run a program on my PC - it runs OK.
I found the PATH points to a folder with Fujitsu Cobol .dll files. How
can I build a Fujitsu Cobol .exe object that will include all
required .DLL files, so it can run it on PC where Fujitsu Cobol is not
installed?
I search manual, but did not found solution.

Thanks,

Zalek
```

#### ↳ Re: Fujitsu Cobol - how to distribute .exe file?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-08-04T12:35:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99u7rcF4pmU1@mid.individual.net>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com>`

```
zalek wrote:
> I am using Fujitsu Cobol - when I run a program on my PC - it runs OK.
> I found the PATH points to a folder with Fujitsu Cobol .dll files. How
…[7 more quoted lines elided]…
> Zalek

Generally, you would use the Fujitsu installer to install the Fujitsu run 
time libraries as part of your distribution.

This is a Fujitsu supplied .MSI package. There are several and it depends on 
what facilities you are using which one you would deploy.

The methods for deployment change across versions of Fujitsu COBOL so you 
need to check the documentation for the version you are using.

When you installed the development environment it should also have installed 
the deployment support but it depends on the version.

The Runtime .MSI is designed so that if there is already a Fujitsu runtime 
on the target machine, it wont install again (unless it is an older version 
and then it prompts.)

To do what you asked (building all the called .DLLs into the executable) 
would need a specific linkage editor run and it will be a lot of grief. Some 
of the Libraries are dependent and are called dynamically if/when needed. It 
COULD be done, but life is too short and Fujitsu provide all of these 
libraries packaged for install as a Runtime .MSI.

There are alternatives to the Fujitsu installer (Inno Install is very good 
one which I have found useful in the past) but anything you use will need 
the Fujitsu runtime.

Please state which version of Fujitsu you are using if you need further 
help.

Pete.
```

##### ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

- **From:** ZalekBloom@hotmail.com
- **Date:** 2011-08-04T07:55:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net>`

```
On Thu, 4 Aug 2011 12:35:57 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>zalek wrote:
>> I am using Fujitsu Cobol - when I run a program on my PC - it runs OK.
…[39 more quoted lines elided]…
>Pete.

Thanks Pete for the explanation.
My problem is little unconventional.
We have on our network few PCs. I don't want to install my program on
every PC - every PC have access to a network X: drive. I want to
install myprogram.exe program on X: drive, without changing PCs
configuration and if a PC wants to run my program - on a DOS screen it
will issue command:
X:\myprogram.exe

This is the reason I want to put all .dll in my .exe object.

Zalek
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-08-05T03:02:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99vqjpFccuU1@mid.individual.net>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net> <cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com>`

```
ZalekBloom@hotmail.com wrote:
> On Thu, 4 Aug 2011 12:35:57 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[56 more quoted lines elided]…
> Zalek

I understand. This is a normal shared application running over the LAN. You 
need to have your .EXE program installed on the server (X: drive, shared). 
However, you still need the Fujitsu runtime installed (definitely on the 
server, and also on any machines you want it to run on.). This is because 
the executable gets copied to the machine which is sharing the X: drive. 
(There is no true remote execution in a DOS LAN... it just looks that way. 
You CAN use Remote Procedure Calls via DCOM to execute remote COM 
components, but that is a horse of a different colour...))
As soon as your executable makes a call to one of the runtime .DLLs it will 
fail, unless you provide the runtime .DLLs on the local machine. You should 
see a message saying tha .DLL cannot be found. It will be F3B<whatever> or 
possibly one of the F5 group of libraries, depending on your Fujitsu 
version.

Note that you only need to install the runtime ONCE on each machine. After 
that you can deploy COBOL apps without needing to redeploy the runtime.

I think what you are looking for is something like the old Micro Focus COBOL 
(Workbench - 16 bit) which could be built into an executable and deployed 
without further support. Those days are long gone. Both Micro Focus and 
Fujitsu now use a "runtime" architecture and it must be deployed with any 
executables (.DLL or .EXE) you install. (Micro Focus charge a licence fee 
for the use of their runtime every time you deploy it; Fujitsu do not.).

Given that you pay a lot of money for a full COBOL compiler and support, you 
might reasonably expect to be able to deploy the work you do with it, 
without having to pay a royalty. This point has been raised many times with 
Micro Focus, both here and elsewhere and they are adamant that the royalties 
are an essential part of their revenue stream. Of course, the latest .Net 
COBOL compilers generate CIL  (just as C# and VB.Net do) and this is then 
translated by the Common Language Runtime (CLR) into native code for the 
platform, so they don't need a runtime. (The "runtime" is provided by the 
.Net Framework, which is provided free by those nice people at Microsoft... 
:-)) Some people avoid the whole problem by using VB.Net or C#, which are 
also free.

I'm sure you have the deployableable runtime package, although you may not 
recognise it. As requested earlier, if you state what version of Fujitsu you 
are using, I can tell you what to look for.

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

_(reply depth: 4)_

- **From:** ZalekBloom@hotmail.com
- **Date:** 2011-08-06T21:36:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mfqr37tsf4s0589hh2q6dlp0a7rcstla4s@4ax.com>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net> <cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com> <99vqjpFccuU1@mid.individual.net>`

```
On Fri, 5 Aug 2011 03:02:13 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>ZalekBloom@hotmail.com wrote:
>> On Thu, 4 Aug 2011 12:35:57 +1200, "Pete Dashwood"
…[99 more quoted lines elided]…
>Pete.

Thanks again Pete,

Now I see I cannot use Fujitsu Cobol in my case - the PCs I was
talking do not belong to my group and asking permition to install
anything on PC which is not under my authority is a nightmare.

Which versions of Fujitsu Cobol create CIL? My Fujitsu Cobol is called
Netcobol - does it means it is .Net?
Meantime I am thinking of rewritting my program in C# or VBScript.

Thanks again,

Zalek
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-08-07T16:38:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a6j5hF9gpU1@mid.individual.net>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net> <cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com> <99vqjpFccuU1@mid.individual.net> <mfqr37tsf4s0589hh2q6dlp0a7rcstla4s@4ax.com>`

```
ZalekBloom@hotmail.com wrote:
> On Fri, 5 Aug 2011 03:02:13 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[114 more quoted lines elided]…
> anything on PC which is not under my authority is a nightmare.

I understand what you're saying, but the runtime is really just part of your 
application. If they want the application, they have to let you install 
it... :-)

As you are trying to run it remotely, it looks like they may not want the 
application installed either.

>
> Which versions of Fujitsu Cobol create CIL? My Fujitsu Cobol is called
> Netcobol - does it means it is .Net?

No. "NetCOBOL for .Net" is the stupid and confusing name that Fujitsu chose 
for their their latest CIL generating OO COBOL compiler.

NetCOBOL is the standard, unmanaged code, Fujitsu OO COBOL compiler. It is a 
very good implementation of the language. I believe the current version is 
v10 although I stopped using it after v7. v3 was a free one which did not 
have everything in it. v4, v6, v7, and v9 were all stable and offered more 
facilities and bug fixes. This is why I aske you for a version; deployment 
of apps and runtimes was changed across some of these versions.

From v6 they moved to the CASPER remote server registration which was 
supposed to prevent piracy but is easily circumvented by people who know 
what they're doing (and they are the people MOST likely to sell pirate 
copies). For normal legitimate users and small businesses this just 
increased the risk of using COBOL; transferring your licence to a different 
machine or reloading an image copy became a nightmare and it just wasn't 
worth the trouble. If your business depended on COBOL (as mine did at the 
time) it was a severe worry to find that a server problem with CASPER could 
result in you being unable to use software you had bought and paid for.

(Aside: I recently worked with some clients to develop a software protection 
system that prevents pirate copies of their applications being run. (Remote 
Application Validation - RAV).  Like CASPER, it does use a web service to 
validate that the software is legitimate. BUT, if you buy the software 
outright, it gets validated once and after that you can do whatever you like 
with it. If you copy it, it will still run but not on someone else's site. 
If you need to move it to a different machine you can (and it remains 
running on the old machine) but , it has to be fingerprinted to the new 
machine. (Your vendor does this remotely, and may or may not charge you for 
it.) I used all the things I hated about CASPER as design criteria for what 
to avoid... :-)) RAV (the PRIMA software) is simple for users and is 
currently in its first live implementations. For software houses developing 
packages they plan to lease, this is an ideal tool. It is written entirely 
in C# but can protect software written in any language that supports COM, 
including Fujitsu and Micro Focus COBOL or .Net COBOL)

NetCOBOL for .Net is apparently very good but it costs around $8000 for a 
compiler which does what C# does for free. Alchemy are not disposed to 
refund your money or even give you a credit for other software if you change 
your mind. I know of at least one very angry customer who was told he needed 
the product then found he didn't... no refunds or credits.

> Meantime I am thinking of rewritting my program in C# or VBScript.

Obviously, I would say C# :-)  However, VB.Net may be good if you already 
have VB experience. You can certainly use VBScript (or JavaScript) across 
the LAN; just wrap it in WSH.

It all comes down to exactly what you want to do and how much LAN is 
involved.

Good luck!

Pete.
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-08-10T15:41:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<07c035bf-b0b7-4625-afbd-0b7c99f12248@h25g2000prf.googlegroups.com>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net> <cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com> <99vqjpFccuU1@mid.individual.net> <mfqr37tsf4s0589hh2q6dlp0a7rcstla4s@4ax.com>`

```
On Aug 7, 1:36 pm, ZalekBl...@hotmail.com wrote:

> Now I see I cannot use Fujitsu Cobol in my case - the PCs I was
> talking do not belong to my group and asking permition to install
…[4 more quoted lines elided]…
> Meantime I am thinking of rewritting my program in C# or VBScript.

You may be able to write the application as a CGI (or similar) program
running in a web server (such as Apache) on your machine so that the
user interface is browser based. This way the application and its DLLs
run in just one place while the HTML/JavaScript interface could be
anywhere in the world.
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol - how to distribute .exe file?

_(reply depth: 6)_

- **From:** iNFO_rene <infodynamics_ph@yahoo.com>
- **Date:** 2011-08-15T08:13:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfd9a8ef-0eb0-4c54-806c-44298acecd23@v42g2000pri.googlegroups.com>`
- **References:** `<81510285-a4ca-45fb-a2af-201c21fca0d2@f20g2000yqm.googlegroups.com> <99u7rcF4pmU1@mid.individual.net> <cn1l3797fg8n91b1qmpi0k6goc5eu8rhl5@4ax.com> <99vqjpFccuU1@mid.individual.net> <mfqr37tsf4s0589hh2q6dlp0a7rcstla4s@4ax.com> <07c035bf-b0b7-4625-afbd-0b7c99f12248@h25g2000prf.googlegroups.com>`

```
>
> You may be able to write the application as a CGI (or similar) program
…[3 more quoted lines elided]…
> anywhere in the world.

THIS IS THE REAL-TIME APPLICATION! You might want to implement this.
Two platforms though;

1. Windows >> go to .NET or COM+ Cobol application (alternative if you
want to learn is C#)
2. Unix/Linux >> go to J2EE/EJB Cobol application

Then you can use your Cobol anywhere anytime using a web browser. This
is the way to go now.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
