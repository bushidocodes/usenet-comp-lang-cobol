[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Are you looking for (ISO) COBOL Revision Work?

_5 messages · 3 participants · 2010-05 → 2010-06_

---

### Are you looking for (ISO) COBOL Revision Work?

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-05-30T05:23:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B0rMn.141242$vX7.131234@en-nntp-11.dc1.easynews.com>`

```
Just in case anyone is looking for the current ISO COBOL Revision work, it 
has gone (mostly) from the PL22.4 (ANSI or INCITS) Task Group to "OWG-1" 
which is a "sort-of" working group under and derrived from the old WG4 ISO 
Committee.

You can see what they are doing at:

 http://www.cobolstandard.info/wg4-owg1/
```

#### ↳ Re: Are you looking for (ISO) COBOL Revision Work?

- **From:** Emerson <emersonlopes@gmail.com>
- **Date:** 2010-05-31T09:52:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4669c68-c836-49ce-921c-e2e81e25057b@d12g2000vbr.googlegroups.com>`
- **References:** `<B0rMn.141242$vX7.131234@en-nntp-11.dc1.easynews.com>`

```
On May 30, 7:23 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
wrote:
> Just in case anyone is looking for the current ISO COBOL Revision work, it
> has gone (mostly) from the PL22.4 (ANSI or INCITS) Task Group to "OWG-1"
…[5 more quoted lines elided]…
>  http://www.cobolstandard.info/wg4-owg1/

Thanks Bill for the update.

I got a concern regarding the necessity of type declaration in the
next standard. The logic part (procedure/methods) of an OO Cobol code
barely has the same level of expressiveness as C# or Java (I can prove
it through my website examples - www.100coolthings.net). Nonetheless,
the type declaration and lack of scoped variables really drives me
crazy. The code verbosity simply explode because we need to define
everything twice (Repository and then Working/local/linkage/based
etc).

Micro Focus has a very interesting, but not standard, solution with a
very nice type inference capability. This is so obvious that the ISO
revision should pay attention to that. I don't get it. We have this
wonderful language to write OO and it is still attached to obscure
justification for lousy compilers (no offense) that has to be told
about everything in order to produce code? For instance, don't the
compiler know that a string type is expected in the sentence below ?


       set    aStr   to  System::String::New()

No, it does not. It needs to be told:

environment division.
configuration section.
Repository.
       class ClassString as "System.String".

data division.
working-storage section.
01 aStr  object reference ClassString.

procedure division.
invoke ClassString "NEW" returning aStr


8 useless extra lines to declare something that is pretty clear
already in the "set"  command line.


I'm not advocating the end of repository. It's just it could be a lot
clever, for instance:


repository.
      import namespace "System.Xml".

 set xmlDoc to XmlDocument::"NEW"("my.xml") *> set xmlDoc as a new
instance of System.Xml.XmlDocument class

 set aNode to xmlDoc::SelectSingleNode("//Node-Name")   *> set aNode
to System.Xml.XmlNode type returned by SelectSingleNode method


Regards,

Emerson
```

##### ↳ ↳ Re: Are you looking for (ISO) COBOL Revision Work?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-06-01T11:50:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86j0afF6g4U1@mid.individual.net>`
- **References:** `<B0rMn.141242$vX7.131234@en-nntp-11.dc1.easynews.com> <f4669c68-c836-49ce-921c-e2e81e25057b@d12g2000vbr.googlegroups.com>`

```
Emerson wrote:
> On May 30, 7:23 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
> wrote:
…[66 more quoted lines elided]…
> Emerson

Just wanted to express my support for what Emerson has raised. It is a very 
good example.

I don't thnk the repository can be eradicated because it is used for 
validation at compile time of early bound references and method signatures 
(as well as other things) but it would certainly be an enhancement to OO 
COBOL if it could reference system libraries via an IMPORT.

Being realistic, I don't see this happening at either a standards or 
implementor level and that is a major reason why programmers move away from 
COBOL once they have grasped the concepts of OOP. It is just easier and 
clearer to do it in Java or C#.

For myself, I don't write early bound OO COBOL and have never needed the 
repository for compliance checking. But I still need it for its other uses 
when referencing my own and other Classes in COBOL.

The inescapable fact is that, when it comes to OO Programming, COBOL is just 
too verbose, compared to other OO languages. I don't think we are going to 
change that. The fact that it supports OO at all is pretty fantastic and 
provides a useful bridge for programmers who are learning the new paradigm. 
But once they have learned it, they are unlikely to stay with COBOL.

From a vendor's point of view, you can hardly blame them for not wanting to 
make a large investment in OO COBOL when they are well aware of its 
difficulties in competing with other OO languages.

Pete.
```

##### ↳ ↳ Re: Are you looking for (ISO) COBOL Revision Work?

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-05-31T20:56:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yNZMn.686501$FK3.402285@en-nntp-06.dc1.easynews.com>`
- **References:** `<B0rMn.141242$vX7.131234@en-nntp-11.dc1.easynews.com> <f4669c68-c836-49ce-921c-e2e81e25057b@d12g2000vbr.googlegroups.com>`

```
Actually, I don't think that there are any "new" features related to OO, 
Type declarations, or conformance checking in the revision.  All of this was 
introduced in the 2002 Standard (and Micro Focus has an option to conform to 
that stpecification).

The OO "stuff" was in the 2002 Standard and has been available as a 
specification for 8 years or so.   I am not certain, but I think that Micro 
Focus and Hitachi (but not Fujitsu) have "conforming" implementations 
(available - whegther they are used or not).

Can you point me to something in the revisions work that has changed since 
the 2002 Standard that you think "could be better"?

NOTE:
   There is still an oustanding work assignment to make "method overloading" 
OPTIONAL (and/or mplementor defined) in the next Standard.

"Emerson" <emersonlopes@gmail.com> wrote in message 
news:f4669c68-c836-49ce-921c-e2e81e25057b@d12g2000vbr.googlegroups.com...
On May 30, 7:23 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
wrote:
> Just in case anyone is looking for the current ISO COBOL Revision work, it
> has gone (mostly) from the PL22.4 (ANSI or INCITS) Task Group to "OWG-1"
…[5 more quoted lines elided]…
> http://www.cobolstandard.info/wg4-owg1/

Thanks Bill for the update.

I got a concern regarding the necessity of type declaration in the
next standard. The logic part (procedure/methods) of an OO Cobol code
barely has the same level of expressiveness as C# or Java (I can prove
it through my website examples - www.100coolthings.net). Nonetheless,
the type declaration and lack of scoped variables really drives me
crazy. The code verbosity simply explode because we need to define
everything twice (Repository and then Working/local/linkage/based
etc).

Micro Focus has a very interesting, but not standard, solution with a
very nice type inference capability. This is so obvious that the ISO
revision should pay attention to that. I don't get it. We have this
wonderful language to write OO and it is still attached to obscure
justification for lousy compilers (no offense) that has to be told
about everything in order to produce code? For instance, don't the
compiler know that a string type is expected in the sentence below ?


       set    aStr   to  System::String::New()

No, it does not. It needs to be told:

environment division.
configuration section.
Repository.
       class ClassString as "System.String".

data division.
working-storage section.
01 aStr  object reference ClassString.

procedure division.
invoke ClassString "NEW" returning aStr


8 useless extra lines to declare something that is pretty clear
already in the "set"  command line.


I'm not advocating the end of repository. It's just it could be a lot
clever, for instance:


repository.
      import namespace "System.Xml".

 set xmlDoc to XmlDocument::"NEW"("my.xml") *> set xmlDoc as a new
instance of System.Xml.XmlDocument class

 set aNode to xmlDoc::SelectSingleNode("//Node-Name")   *> set aNode
to System.Xml.XmlNode type returned by SelectSingleNode method


Regards,

Emerson
```

###### ↳ ↳ ↳ Re: Are you looking for (ISO) COBOL Revision Work?

- **From:** Emerson <emersonlopes@gmail.com>
- **Date:** 2010-06-01T13:06:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb4946d6-b9f5-4206-af27-3caae6fdbb84@o1g2000vbe.googlegroups.com>`
- **References:** `<B0rMn.141242$vX7.131234@en-nntp-11.dc1.easynews.com> <f4669c68-c836-49ce-921c-e2e81e25057b@d12g2000vbr.googlegroups.com> <yNZMn.686501$FK3.402285@en-nntp-06.dc1.easynews.com>`

```
Hi Bill,

blame it on my english :)

What I tried to say is that the necessity of type declaration should
be reviewed in the next standard. Repository concept make sense, but
today it is implemented in a way that requires a lot of code since we
need to declare class by class and then define the variable in the
working-storage referring the class declared in the repository...too
much code to say too little...

If we could say the following then the repository would be a very
handy concept:

repository.
     import namespace System.

This change would drive efforts into namespace support addition. This
is something that should be reviewed, too. There is no such thing as
package/namespace support in the 2002 standard, but it should.

If we could get rid of predeclared variables necessity we could also
consider the possibility to define scoped variables, e.g.

    if   sales::getSales(aVendor) > 0
         set     aValue as System.Double
         compute aValue = (avendor::getBaseSalary() +
sales::CalcComissionFor(aVendor)) - aVendor::getAdvances()
         display aValue
    end-if

aValue would exist only in the IF / END-IF block scope. Today we would
need to define it first in the working-storage, even if we are going
to use it only one time in the entire class. I think the MF Visual
Cobol 2010 does it, but it should go to the Cobol Standard.

Regards, Emerson









On May 31, 10:56 pm, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
wrote:
> Actually, I don't think that there are any "new" features related to OO,
> Type declarations, or conformance checking in the revision.  All of this was
…[82 more quoted lines elided]…
> Emerson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
