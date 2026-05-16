[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL delegates and .NET Action<string>

_2 messages · 2 participants · 2009-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: COBOL delegates and .NET Action<string>

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-02-11T17:06:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<499305A2.6F0F.0085.0@efirstbank.com>`

```
>>> On 2/10/2009 at 9:23 PM, in message
<cdc05216-bd17-48af-9c77-50c70d08bdb6@q9g2000yqc.googlegroups.com>,
<biblepolyglotte@gmail.com> wrote:
> Micro Focus COBOL.NET does have the TRY...CATCH...FINALLY...END-TRY
> structure. I realize that not everyone will want to go there.
…[14 more quoted lines elided]…
> C# uses the += operator. Anyone know how that works in COBOL.NET?

Once upon a time I believe I had the answer to this, but I can't recall what
it is.  I think I used .NET Reflector to translate the C# .EXE from bytecode
back to C# and it showed that the actual method used by +=.

.NET Reflector is very fun anyway, so take a look:
http://www.red-gate.com/products/reflector/.
 
Frank
```

#### ↳ Re: COBOL delegates and .NET Action<string>

- **From:** biblepolyglotte@gmail.com
- **Date:** 2009-02-12T08:32:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1684ef7-fff8-417d-b7d5-d70814409693@i38g2000yqd.googlegroups.com>`
- **References:** `<499305A2.6F0F.0085.0@efirstbank.com>`

```
On Feb 11, 7:06 pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> Once upon a time I believe I had the answer to this, but I can't recall what
> it is.  I think I used .NET Reflector to translate the C# .EXE from bytecode
…[3 more quoted lines elided]…
> - Show quoted text -

I hadn't thought of using Reflector here, but the Snippy add-in for
Reflector is the next project I'd like to port from C# to COBOL. Then
I'd like to see if a Reflector add-in to disassemble from MSIL to
COBOL is feasible. :-)

I realized overnight that RoutedEventHandlers are automatically wired
up in generated COBOL files, when event handler attributes are added
to XAML elements in the designer. So I'll have a look at generated
COBOL first, but will keep Reflector in mind.

FxCop demanded a strong name for the AddOneSnippy assembly, so the
snippet compiler is now called COBOL the Barbarian:

http://www.codeplex.com/barbarian

The Reflector add-in to compile from C#, VB, C++, and COBOL -- and
browse the resulting MSIL -- will be COBOL the Conqueror. Now if only
there were a strong name for snippet.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
