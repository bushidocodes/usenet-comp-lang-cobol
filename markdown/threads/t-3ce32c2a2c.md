[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Scope of names

_2 messages · 2 participants · 2009-01_

---

### Scope of names

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-08T07:09:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%Vm9l.115675$NN4.73020@en-nntp-08.dc1.easynews.com>`

```
I am certain that there is a clear and obvious <G> answer in the Standard ('85 
or later) for this, but some how my mind is just missing it (or worse, what I 
think it says, is what ir really means).

I have been reading
   "8.4.5.1 Local and global names"
on page 106 of the current draft of the next COBOL revision.  (I think the 
wording there is identical to what it is in earlier Standards).

So my question concerns a structure like the following:

 Program-ID. OuterPGM.
      ...
Working-Storage Section.
 01  SomeGroup.
      05 anElem   Global Pic X.
 ....
 Program-ID.  InnerPGM.
      ....
Working-Storage Section.
   01 AnElem   Pic X.
         ...
Move anElem to anElem of SomeGroup.
   ...
 End Program InnerPGM.
End Program OuterPGM.

so I am wondering if that MOVE is "valid" according to name scoping rules.  It 
seems to me it is (but I am not certain) because:

  anElem (with no qualification) *must* refer to the one and only local 
user-defined word in the nested program by that name.
However
  anElem of SomeGroup (with qualification) is a valid identifier with the global 
attribute and there is only one identifier by that qualified name that is 
"visible" in the contained program.

This seems odd (at best) to me, but it also SEEMS to be what the rules say (and 
what they need to say to make certain that you don't have to qualify a "local" 
data-item if there is an identically names (unqualified) data item in a 
containing program.

Am I right?  Does anyone see some other rule in any current (draft or official) 
or past Standard - or even in any implementation's LRM?
```

#### ↳ Re: Scope of names

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-01-09T17:36:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gk8jqv08us@news6.newsguy.com>`
- **In-Reply-To:** `<%Vm9l.115675$NN4.73020@en-nntp-08.dc1.easynews.com>`
- **References:** `<%Vm9l.115675$NN4.73020@en-nntp-08.dc1.easynews.com>`

```
William M. Klein wrote:
> 
> So my question concerns a structure like the following:
…[5 more quoted lines elided]…
>       05 anElem   Global Pic X.

Per your second post, that Global qualifier is actually on SomeGroup.

>  ....
>  Program-ID.  InnerPGM.
…[22 more quoted lines elided]…
> containing program.

That seems sensible to me. It's how I'd expect the language to be
defined. An name should refer to the matching identifier in the
nearest enclosing scope (in lexically-scoped languages in general, not
just in COBOL). All the qualifier is doing is preventing the qualified
"anElem" from matching the local "anElem", so resolution moves to the
outer scope.

You have a similar situation with ECMAScript (Javascript, JScript,
etc), if you use the "with" operator to simulate the behavior of
COBOL's matching of items within group items. Here's an example, using
the Javascript Shell. Input lines are separated by a blank line, with
the output, if any, below the input.

var Outer = { anElem : 1 }; var Inner = { anElem : 2 };

print(Outer.anElem);
1

with (Inner) { print(anElem); }
2

with (Inner) { Outer.anElem = anElem; }

print(Outer.anElem);
2

The "with" statement lets the unqualified "anElem" refer to the
"anElem" property of "Inner", in much the same way that the
unqualified "anElem" in the COBOL example refers to the anElem of the
inner scope. But even there we can use the qualified "Outer.anElem" to
refer to the "anElem" of the other object.

(In this simple ECMAScript example, there's no actual nested scope -
"Outer" and "Inner" are at the same scope level. The same resolution
process applies with nested scopes, but that would just complicate the
picture here. The point of this example was to show how the "with"
operator can be used to implicitly qualify an identifier.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
