[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Net Express Printing

_3 messages · 3 participants · 2002-12 → 2003-01_

---

### Re: Net Express Printing

- **From:** "Stan_A" <Stan_nospam_Archer@hotmail.com>
- **Date:** 2002-12-31T16:08:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ijQ9.575576$QZ.82361@sccrnsc02>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <RaRP9.556469$QZ.80190@sccrnsc02> <3E10923F.5C3D1587@shaw.ca> <0r931v8v2ied7la824gbc35pqmjvmj6r2i@4ax.com>`

```
Ron,

Simply elegant. It begs one small question to make really magnificent
though. What Windows file holds the path to the network printer ?  Then the
user would not have to be prompted for the path at all.


Stan

"Ron" <ron@address.below> wrote in message
news:0r931v8v2ied7la824gbc35pqmjvmj6r2i@4ax.com...
> "James J. Gavan" <jjgavan@shaw.ca> wrote:
> >As an extension to Lorne's suggestion there are three alternatives for
you.
>
>   Why all this fuss?  The easiest way to print to a network printer is
…[10 more quoted lines elided]…
> in domain spamblocked.com)
```

#### ↳ Re: Net Express Printing

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-31T14:39:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E121CB0.1060902@Sympatico.ca>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <RaRP9.556469$QZ.80190@sccrnsc02> <3E10923F.5C3D1587@shaw.ca> <0r931v8v2ied7la824gbc35pqmjvmj6r2i@4ax.com> <7ijQ9.575576$QZ.82361@sccrnsc02>`

```
Stan_A wrote:

>Ron,
>
…[33 more quoted lines elided]…
>>
Stan, if the above works, then so does the below.

        SELECT out-file
            ORGANIZATION IS LINE-SEQUENTIAL
            ASSIGN TO MY-COBOL-DATA-NAME.

    WORKING-STORAGE SECTION.
    77 MY-COBOL-DATA-NAME        PICTURE X(80) VALUE 
"\\machinename\printername".

as will the following:

    PROCEDURE DIVISION.
      ***
            PERFORM LOOKUP-MY-COBOL-DATA-NAME-IN-MY-USER-SETUP-DATABASE.

course you would have to top down that particulat paragraph name with 
your run time.

Donald
```

#### ↳ Re: Net Express Printing

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-01-01T18:27:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vic61voariulvjrped4pcchfeelaf6ff92@4ax.com>`
- **References:** `<MeQP9.161038$qF3.11704@sccrnsc04> <ZpzG4UNLyRNq-pn2-NeUZrZmDY3Qg@h24-82-204-17.wp.shawcable.net> <RaRP9.556469$QZ.80190@sccrnsc02> <3E10923F.5C3D1587@shaw.ca> <0r931v8v2ied7la824gbc35pqmjvmj6r2i@4ax.com> <7ijQ9.575576$QZ.82361@sccrnsc02>`

```
Stan, et. al.

<unabashed commercialism>

I noted that FormPrint has not been mentioned as a possible
alternative.

FormPrint supports Windows printing using NetExpress and allows for
Network printing and printing across the Internet (when combined with
the Flexus Thin Client product.)

FormPrint also has a great print preview feature as well.

For more information, please visit http://www.flexus.com or send a
private e-mail message to me.

"Stan_A" <Stan_nospam_Archer@hotmail.com> wrote:

>Ron,
>
…[25 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
