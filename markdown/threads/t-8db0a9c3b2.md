[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetCobol - How make auto-clear in Accept numeric field?

_2 messages · 2 participants · 2010-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### NetCobol - How make auto-clear in Accept numeric field?

- **From:** Gilberto Strapazon <gilbertopb@gmail.com>
- **Date:** 2010-10-08T07:07:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d726798e-516f-4be6-9e31-43140174bf4e@w19g2000yqb.googlegroups.com>`

```
Hi

I searched a lot but didn´t find how to solve this.

We are converting from Microfocus Cobol to Fujitsu NetCobol.
The programs will keep the original console character interface. This
means, display/accept for all, using scrren section also.

The problem is Netcobol Accept appears to not have the auto-clear
feature for the field input and the user have to manually clean all
the field. For character field (PIC X) there´s no problem, but for
numeric fields this is a worst and a risk or error.

Just to detail:

In all the fiels I make an ACCEPT, I want to show the contents of that
field and,
  1) if the user just press ENTER, keep that contents,
  2) if the user writes something, i.e, when press first value key,
the field content is cleaned to receive the new input.

In the Microfocus Cobol there´s the ADISCTRL, but we have not find
nothing similar in Fujitsu NetCobol. Appears almost examples we have
found, is people using NetBios for massive batch or as CGI,

Thanks in advance for your sugestions


Gilberto Strapazon
Porto Alegre

http://cwconnect.computerworld.com.br/zenta
http://gilbertostrapazon.blogspot.com
```

#### ↳ Re: NetCobol - How make auto-clear in Accept numeric field?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-09T12:05:44+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h9meaFbreU1@mid.individual.net>`
- **References:** `<d726798e-516f-4be6-9e31-43140174bf4e@w19g2000yqb.googlegroups.com>`

```
Gilberto Strapazon wrote:
> Hi
>
…[30 more quoted lines elided]…
> http://gilbertostrapazon.blogspot.com

Processing using screen sections is an archaic way to do things, but 
sometimes people have no choice. As you are converting from Micro Focus you 
are probably tied to the screen sections in the legacy programs.

For interactive data entry you would be much better off using PowerCOBOL 
(and it gives much more control over the data fields because they are true 
Windows controls, so you have access to all their properties, colours, text 
fonts, etc.).

Given that you really have no option, try adding "FULL" to your numeric 
field definitions in the screen section. This may give somethng closer to 
the behaviour you are seeking.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
