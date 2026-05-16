[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Lowercase equivalent to uppercase, or vice versa

_11 messages · 5 participants · 2006-03_

---

### Lowercase equivalent to uppercase, or vice versa

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-23T12:07:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1225lhe6r38lj5f@corp.supernews.com>`

```
The COPY statement, for 2002, 7.1.2.3 General rules,
10, c), 3, states, in part, "... each lowercase letter is
equivalent to its corresponding uppercase letter, as
specified for the COBOL character repertoire in 8.1.2,
COBOL character repertoire.", and, the REPLACE
statement, 7.1.3.3 General rules, 8, c), 3, states, in part,
"... each lowercase letter is equivalent to its corresponding
uppercase letter, as specified for the COBOL character
repertoire in 8.1.2, COBOL character repertoire.".

However, COBOL character repertoire, 8.1.2.1 General
rules, 3, states, in part, "Equivalence of uppercase and
lowercase basic letters is achieved by folding from
uppercase to lowercase in accordance with the case
mapping described in Annex D."

Thus, it seems to me, that the wording in both the COPY
and REPLACE statements should be reversed to say
"each uppercase letter is equivalent to its corresponding
lowercase letter, ...", since folding is from uppercase to
lowercase, then equivalence should be from uppercase
to lowercase.

The same references apply to WD 1.5, except Annex C
instead of Annex D.
```

#### ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-23T17:12:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fGAUf.2907$K11.1151@clgrps12>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1225lhe6r38lj5f@corp.supernews.com...
> The COPY statement, for 2002, 7.1.2.3 General rules,
> 10, c), 3, states, in part, "... each lowercase letter is
…[22 more quoted lines elided]…
> instead of Annex D.

    Not sure if "equivalence" has some special meaning in COBOL, but in 
math, equivalence is a symmetric relationship. So if A is equivalent to B, 
then it is always true that B is equivalent to A.

    - Oliver
```

##### ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-23T10:45:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ikn52212c4t7nc6j7ot9ldc56pu70vs0e4@4ax.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12>`

```
On Thu, 23 Mar 2006 17:12:43 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>
>    Not sure if "equivalence" has some special meaning in COBOL, but in 
>math, equivalence is a symmetric relationship. So if A is equivalent to B, 
>then it is always true that B is equivalent to A.

But does that apply to the King James version of CoBOL?
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-03-23T09:53:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvunbb$tom$1@si05.rsvl.unisys.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <ikn52212c4t7nc6j7ot9ldc56pu70vs0e4@4ax.com>`

```
I'd say that depends on whether you're referring to the original 1960 
recension, or its 1968, 1974, 1985 or 2002 revisions!     ;-)

    -Chuck Stevens

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ikn52212c4t7nc6j7ot9ldc56pu70vs0e4@4ax.com...
> On Thu, 23 Mar 2006 17:12:43 GMT, "Oliver Wong" <owong@castortech.com>
> wrote:
…[6 more quoted lines elided]…
> But does that apply to the King James version of CoBOL?
```

##### ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-23T13:28:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1225q86q8fh8528@corp.supernews.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12>`

```

"Oliver Wong" <owong@castortech.com> wrote in message
news:fGAUf.2907$K11.1151@clgrps12...
[snip]
>     Not sure if "equivalence" has some special meaning in COBOL, but in
> math, equivalence is a symmetric relationship. So if A is equivalent to B,
> then it is always true that B is equivalent to A.

My dictionary, RHCD, provides the special definition
for "equivalent", when used for Mathematics, as
"capable of being set into one-to-one correspondence"
and, for "one-to-one", "associating with each element
in one set a unique element in a second set".

Consider that age 28 is equivalent to adult, but not the
reverse; that is, associating the set of ages with the set
of {baby, child, teenager, adult, senior}.

As to letter case in COBOL, there are some lowercase
letters that may translate to either of two uppercase
letters, depending on context; while uppercase letters
only map to one lowercase letter, that provided in an
annex in the COBOL standard.
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-23T19:58:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S5DUf.3240$K11.1107@clgrps12>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1225q86q8fh8528@corp.supernews.com...
>
> "Oliver Wong" <owong@castortech.com> wrote in message
…[11 more quoted lines elided]…
> in one set a unique element in a second set".

    I believe this is consistent with the definition I was using above. For 
there to exist a one-to-one correspondence between two sets, those two sets 
must be of equal size. (This sometimes leads to surprising results, such as 
the set of even positive numbers is of the same size as the set of all 
integers, including the odd and negative ones).

>
> Consider that age 28 is equivalent to adult, but not the
> reverse; that is, associating the set of ages with the set
> of {baby, child, teenager, adult, senior}.

    The set of natural numbers is NOT in a one to one correspondance with 
the set {baby, child, teen, adult, senior}, so the term "equivalent" here is 
not being used in the mathematical sense.

>
> As to letter case in COBOL, there are some lowercase
…[3 more quoted lines elided]…
> annex in the COBOL standard.

    If that's the case (and I wouldn't be too surprised if it were), then 
"equivalence" is probably the wrong term to describe the mapping.

    - Oliver
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-23T17:54:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12269slsgnij05d@corp.supernews.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com> <S5DUf.3240$K11.1107@clgrps12>`

```

"Oliver Wong" <owong@castortech.com> wrote in message
news:S5DUf.3240$K11.1107@clgrps12...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[16 more quoted lines elided]…
>     I believe this is consistent with the definition I was using above.
For
> there to exist a one-to-one correspondence between two sets, those two
sets
> must be of equal size. (This sometimes leads to surprising results, such
as
> the set of even positive numbers is of the same size as the set of all
> integers, including the odd and negative ones).
…[7 more quoted lines elided]…
> the set {baby, child, teen, adult, senior}, so the term "equivalent" here
is
> not being used in the mathematical sense.

Maybe. The clearest description I have found so far
is "asymmetric relation". An asymmetric relation seems
not to be an "equivalence relation", so 'not mathematical
sense' seems about right. Perhaps, logically equivalent then.
(Though Russell is said to have claimed that mathematics
is a branch of logic!)

> > As to letter case in COBOL, there are some lowercase
> > letters that may translate to either of two uppercase
…[5 more quoted lines elided]…
> "equivalence" is probably the wrong term to describe the mapping.

I am going to do myself a big favor and let WG4/J4
decide that question.
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

_(reply depth: 5)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-24T14:48:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aFTUf.6966$%H.6904@clgrps13>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com> <S5DUf.3240$K11.1107@clgrps12> <12269slsgnij05d@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12269slsgnij05d@corp.supernews.com...
>
> The clearest description I have found so far
…[4 more quoted lines elided]…
> is a branch of logic!)

    Yeah, I know of 4 main properties that a "relationship" (in the 
mathematical sense) can hold (though probably, there exists other 
interesting properties one could discuss as well):

If we use "A -> B" as a short hand for "A is related to B",

Symmetric: (A -> B) implies (B -> A)
Anti-symmetric: (A -> B) implies NOT(B -> A)
Reflexive: (A -> A)
Transitive: ((A -> B) AND (B -> C)) implies (A -> C)

It's possible for a relation to be not be symmetric and not be 
anti-symmetric at the same time (e.g. if A -> B and "sometimes" B -> A, as 
opposed to "always" and "never")

"Equivalence", in the way that I understand it, is symmetric, reflexive and 
transitive.

    - Oliver
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-23T21:16:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NeEUf.94344$NN1.83760@fe12.news.easynews.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1225q86q8fh8528@corp.supernews.com...
<snip>
> As to letter case in COBOL, there are some lowercase
> letters that may translate to either of two uppercase
…[3 more quoted lines elided]…
>

Rick,
  Didn't you say this backwards (or am I misunderstanding your intent)?

The "lower-case" letters
   �
   �
   �
   �
and e

are all treated as "equivalent" (via folding) to
   E
at least for some (most) alphabets - as used in COBOL.

I can't think of any examples where an individual lower-case letter corresponds 
to two different upper-case letters.  There *are* cases where there isn't any 
correspondence OR the correspondence is from a single symbol to multiple 
letters, e.g.
   � and "SS"

and some diagraphs also do odd mapping.
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-23T16:52:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<122668tndn7um50@corp.supernews.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com> <NeEUf.94344$NN1.83760@fe12.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:NeEUf.94344$NN1.83760@fe12.news.easynews.com...
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:1225q86q8fh8528@corp.supernews.com...
…[9 more quoted lines elided]…
>   Didn't you say this backwards (or am I misunderstanding your intent)?

No, but I may be mistaken, (and maybe).

> The "lower-case" letters
>    �
…[7 more quoted lines elided]…
> at least for some (most) alphabets - as used in COBOL.

That may be true for implementations prior to 2002; but
such letters, except for "e", were not COBOL Characters,
hence vendors could do, fairly much, what they wanted.
For 2002, COBOL words may have letters other that
A-Z and a-z, at least, as far as I understand such things.

The translation of the mapping shown in Annex D, for 2002 is:
<�,�>, <�,�>, <�,�>, <�,�>; that is, the first letter is
mapped to the second letter.

There is no mapping of �, �, �, �, or e to E, in COBOL 2002,
referring to Annex D.

> I can't think of any examples where an individual lower-case letter
corresponds
> to two different upper-case letters.  There *are* cases where there isn't
any
> correspondence OR the correspondence is from a single symbol to multiple
> letters, e.g.
>    � and "SS"
>
> and some diagraphs also do odd mapping.

I may be mistaken on that point; but I do note that there
is no mapping of � to any other character, in Annex D,
so it remains unchanged in COBOL words.
```

###### ↳ ↳ ↳ Re: Lowercase equivalent to uppercase, or vice versa

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-23T23:25:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7GUf.139073$fe6.116783@fe01.news.easynews.com>`
- **References:** `<1225lhe6r38lj5f@corp.supernews.com> <fGAUf.2907$K11.1151@clgrps12> <1225q86q8fh8528@corp.supernews.com> <NeEUf.94344$NN1.83760@fe12.news.easynews.com> <122668tndn7um50@corp.supernews.com>`

```
You're right and I was wrong (working from memory).  Folding is defined from 
Upper to Lower in the '02 Standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
