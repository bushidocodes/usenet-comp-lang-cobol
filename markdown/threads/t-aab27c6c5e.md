[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# xml schema (xsd) in cobol

_23 messages · 7 participants · 2006-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### xml schema (xsd) in cobol

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-01T19:54:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it>`

```
I need a tool to convert an xml schema definition (.xsd) into Cobol code.
Did anyone already write something like this?

Thanks in advance,
Fabio
```

#### ↳ Re: xml schema (xsd) in cobol

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-01T20:20:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43e109fa$0$22087$4fafbaef@reader1.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it>`

```
I'm looking for an open source project, better if written in Java, but even 
C#, C++, VB are good .

>I need a tool to convert an xml schema definition (.xsd) into Cobol code.
> Did anyone already write something like this?
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: xml schema (xsd) in cobol

- **From:** Doug Robinson <fdr@nolinks.adelphia.net>
- **Date:** 2006-02-04T03:58:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.02.04.16.00.35.888895@nolinks.adelphia.net>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <43e109fa$0$22087$4fafbaef@reader1.news.tin.it>`

```
On Wed, 01 Feb 2006 20:20:23 +0100, Fabio Fabbri wrote:

> I'm looking for an open source project, better if written in Java, but
> even C#, C++, VB are good .
> 
>> [quoted text muted]

AcuCobol has the capability in their newest releases, but alas they are
not open source.                            fdr

(their documentation is however online, so you could go take a look and
maybe get some ideas.)
```

#### ↳ Re: xml schema (xsd) in cobol

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-02T18:32:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YesEf.161258$AP5.149625@edtnps84>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it>`

```
"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43e103eb$0$22093$4fafbaef@reader1.news.tin.it...
>I need a tool to convert an xml schema definition (.xsd) into Cobol code.
> Did anyone already write something like this?

    To me, this is like saying you want to convert arbitrary text into COBOL 
code. For example, converting one of Shakespear's plays into COBOL, or 
converting a haiku into COBOL.

    COBOL source code specifies the behaviour of a computer program. XSD 
specifies the structure of an XML document. I'm not sure how you could get 
an XSD file to specify the behaviour of a computer program, nor could you 
get COBOL to specify the structure of an XML document (you could write a 
COBOL source code which, when compiled, produces a program which CHECKs the 
structure of an XML document, but this COBOL code again specifies the 
behaviour of a program; not the structure of a document).

    - Oliver
```

##### ↳ ↳ Re: xml schema (xsd) in cobol

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-10T00:26:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84>`

```
XSD is not "an arbitrary text" and does not only contain datas. It also 
contains "relations" between members, as parent-children relation, required 
attributes, and so on.
So, XSD doesn't only mean a working-storage record, but it also mean to 
generate most of procedure division statements in an xml-message-handlying 
routine.
The tool I'm trying to build can avoid user from managing these relations, 
focusing on data manipulation.
Fabio

"Oliver Wong" <owong@castortech.com> ha scritto nel messaggio 
news:YesEf.161258$AP5.149625@edtnps84...
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
> news:43e103eb$0$22093$4fafbaef@reader1.news.tin.it...
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T14:40:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J3HIf.3048$_62.1127@edtnps90>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it>`

```

"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it...
> XSD is not "an arbitrary text" and does not only contain datas. It also 
> contains "relations" between members, as parent-children relation, 
…[6 more quoted lines elided]…
> Fabio

    It sounds like what you want is a tool that will generate the template 
for an XML parser in COBOL, given an XSD document.

    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 4)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-15T17:40:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43f3599a$0$28062$4fafbaef@reader1.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90>`

```
That's it... but I already have the template builder, I just need the XSD 
parsing component.

"Oliver Wong" <owong@castortech.com> ha scritto nel messaggio 
news:J3HIf.3048$_62.1127@edtnps90...
>
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
…[14 more quoted lines elided]…
>    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 5)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T19:33:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FmLIf.3098$_62.2606@edtnps90>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it>`

```
"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43f3599a$0$28062$4fafbaef@reader1.news.tin.it...
>
> "Oliver Wong" <owong@castortech.com> ha scritto nel messaggio 
…[7 more quoted lines elided]…
> parsing component.

    Oh, okay. So what you *really* want is an XSD parser, to load the XSD 
into some tree-like representation in memory, which you would then analyze 
and instruct your template builder on how to generate COBOL code...

    Does the XSD parser have to be in COBOL?

    Do you have an XML parser already avaible? XSD is a subset of XML, so if 
you have an XML parser, you can use it to parse the XSD file.

    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 6)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-16T21:41:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43f4e381$0$12603$4fafbaef@reader3.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90>`

```
Nope.
XSD output should not be a memory structure, but Cobol CODE. I don't mind 
the language of the code generator (I usually use java to generate cobol 
code).
This is a simple schema:
[XSD] -->
-->[Code Generator (written for example in Java, Cobol) ] -->
-->[Cobol Code: working storage as in xsd, read and write template for xsd 
data with xml parser]
Then user can complete the template generated with this tool to build the 
final cobol code program.

I'm not much experienced with Cobol and Cobol-code-generators so I was 
asking if something like this is available for free, or I should write the 
whole code myself.


"Oliver Wong" <owong@castortech.com> ha scritto nel messaggio 
news:FmLIf.3098$_62.2606@edtnps90...
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
> news:43f3599a$0$28062$4fafbaef@reader1.news.tin.it...
…[20 more quoted lines elided]…
>    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 7)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-16T22:19:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qT6Jf.1446$Y22.874@clgrps12>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it>`

```

"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43f4e381$0$12603$4fafbaef@reader3.news.tin.it...
> Nope.
> XSD output should not be a memory structure, but Cobol CODE. I don't mind 
> the language of the code generator (I usually use java to generate cobol 
> code).

    I'm getting more and more confused. When you say "XSD output", I'm 
assuming you mean "the output from my tool", because XSD is not executable 
code and cannot actually ouput anything.

    And it sounds like you now want to emit COBOL code, whereas previously 
you said you wanted to emit Java code. What is this COBOL code supposed to 
do?

> This is a simple schema:
> [XSD] -->
> -->[Code Generator (written for example in Java, Cobol) ] -->
> -->[Cobol Code: working storage as in xsd, read and write template for xsd 
> data with xml parser]

    What do the arrows "-->" mean in each of the case? The XSD file is being 
passed to a code generator, I'm guessing. And this code generator is the 
tool you want to download for free. So this first-second arrow combination 
represents "reading from file", I guess. What about the third-fourth arrow 
combination? Does this represent "writing to file" or "passing information 
to another program"? That is, is your code generator emit COBOL code, and 
that's it, or is your code generatoe emitting COBOL code which is being 
passed to another program written in COBOL which does further processing on 
it?

    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 8)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-16T23:21:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yN7Jf.22055$H%4.7316@pd7tw2no>`
- **In-Reply-To:** `<qT6Jf.1446$Y22.874@clgrps12>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12>`

```
Oliver Wong wrote:
> 
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
…[14 more quoted lines elided]…
> code supposed to do?

Fabio,

Very often the person posing the question knows *exactly* what they are 
asking about. Then again sometimes they don't :-).

Try and give Oliver some code snippets that he can latch onto.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 9)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-17T01:24:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43f517cb$0$12595$4fafbaef@reader3.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no>`

```
I know exactly what I'm asking for, but it's a while I don't write in 
English and I'm not explaining myself.
So, let's try with a simple code sample...
My input is a simple xsd element:
<xsd:element name="Date" type="xsd:dateTime" />

I'm writing a tool (using Java lang, but that's not necessary) which writes 
an output like this cobol program:

program id. try.
....
...
working storage.
01 date  X(10)
...

procedure division.
   read-element.
       perform xml-read-date
       move xml-parser-result-date to ws-date
 ***  user-managed-code (not generated)
   exit.
   write-element.
     move ws-date to  xml-parser-result-date
 ***  user-managed-code (not generated)
    perform xml-write-date
    exit.




"James J. Gavan" <jgavandeletethis@shaw.ca> ha scritto nel messaggio 
news:yN7Jf.22055$H%4.7316@pd7tw2no...
> Oliver Wong wrote:
>>
…[24 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 10)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-17T16:37:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ZmJf.3884$_62.2976@edtnps90>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no> <43f517cb$0$12595$4fafbaef@reader3.news.tin.it>`

```

"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43f517cb$0$12595$4fafbaef@reader3.news.tin.it...
>I know exactly what I'm asking for, but it's a while I don't write in 
>English and I'm not explaining myself.
…[24 more quoted lines elided]…
>    exit.

    So you're writing this tool in Java, and you've already got the template 
generator, but you just need an XSD parsing component, right?

    How about Xerces? It's a component that plugs into Java, C or Perl, for 
parsing XML documents in general, but it can handle XSD documents too.

    http://xerces.apache.org/xerces2-j/

    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 11)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-17T22:22:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43f63ea8$0$6000$4fafbaef@reader2.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no> <43f517cb$0$12595$4fafbaef@reader3.news.tin.it> <8ZmJf.3884$_62.2976@edtnps90>`

```
>So you're writing this tool in Java, and you've already got the template 
>generator.
Not exactly. I just have a Java application which can quickly write a cobol 
program from few java instructions.
If I'll use components like Xerces or Castor, I should also write on my own 
the java-class to cobol-program logic, even if my code generator will make 
this step easier.
For now the better suggestion I got in this thread was to use Xml Thunder, 
but it is only for evaluation and I can't use it for business purposes.
However really thanks for listening and trying to help!

Fabio


"Oliver Wong" <owong@castortech.com> ha scritto nel messaggio 
news:8ZmJf.3884$_62.2976@edtnps90...
>
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
…[37 more quoted lines elided]…
>    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 12)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-18T00:46:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7uJf.35601$H%4.27262@pd7tw2no>`
- **In-Reply-To:** `<43f63ea8$0$6000$4fafbaef@reader2.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no> <43f517cb$0$12595$4fafbaef@reader3.news.tin.it> <8ZmJf.3884$_62.2976@edtnps90> <43f63ea8$0$6000$4fafbaef@reader2.news.tin.it>`

```
Fabio Fabbri wrote:
>>So you're writing this tool in Java, and you've already got the template 
>>generator.
…[8 more quoted lines elided]…
> However really thanks for listening and trying to help!

Still not quite there even after Oliver's reply :-) I can understand you 
not wanting to buy additional software - who does ?

It might be a dumb suggestion, but why not do it in COBOL - the 
implication is that you are already familiar with COBOL. I'm sure there 
must be some specific COBOL code generators, but again they would come 
with a price tag.

In brief, edit to create a COBOL template program, which of course is a 
text file (Line Sequential) - and using what you had below :-

        *>----------------- MyTemplate -----------------

***ID  program id.

***WS  working storage.

***PD  procedure division.

***EP  End-program.
        *>----------------------------------------------

Above is a very crude template and obviously you can add other fixed 
features as you wish. (Note you can use the area 1-6 as markers so that
you know what you are reading from the input template).

So, open MyTemplate above as input Line Sequential, (pic x(80)) and open 
as output Line Sequential MyProgram. You read the template in, 
line-by-line writing output records to MyProgram adding additional code 
as necessary. For example the input line above :-

***ID  program id.

is written as output :-

***ID  program id. MyProgram.      (delete the 'marker' if you like)

The following lines are triggered and generated when you identify 
"Procedure Division".

          read-element.
              perform xml-read-date
              move xml-parser-result-date to ws-date
        ***  user-managed-code (not generated)
          exit.
          write-element.
            move ws-date to  xml-parser-result-date
        ***  user-managed-code (not generated)
           perform xml-write-date
           exit.

It is not a difficult exercise for COBOL. I use Net Express with their 
Dialog Editor and GUI classes. I could laboriously cut and paste, but 
prefer to send a record per control to a Dialog Template containing the 
properties pertaining to a particular control *plus* the Method-Name I 
eventually want control objects returned to in my Business class.

That Method-Name above, while I don't generate the whole controlling 
program, (Business Class), I can write the receiving methods just as you 
want your paragraphs above. The following is a selective list each 
method identifying the type of control :-

        *>-----------------------------------------------------------

        *> ++++ Returned events from Dialog ++++

        *>       CB(Checkbox)
        *>       EF(Entryfield)
        *>       DL(DropList)
        *>       LB(Listbox)
        *>       PB(Pushbutton)
        *>       RB(RadioButton)

        *>-----------------------------------------------------------
        Method-id. "DL-Mat-Main".
        *>-----------------------------------------------------------

        Linkage section.
        copy "\copylib\dlgreturn.cpy" replacing ==(tag)== by ==lnk==.

        Procedure Division using lnk-ReturnValues.
        *> user code goes in here
        End Method "DL-Mat-Main".
        *>-----------------------------------------------------------
        Method-id. "EF-Grade".
        *>-----------------------------------------------------------
        Linkage section.
        copy "\copylib\dlgReturn.cpy" replacing ==(tag)== by ==lnk==.

        Procedure Division using lnk-ReturnValues.
        *> user code goes in here
        End Method "EF-Grade".
        *>-----------------------------------------------------------
        Method-id. "EF-PrimeKey".
        *>-----------------------------------------------------------
        Linkage section.
        copy "\copylib\dlgReturn.cpy" replacing ==(tag)== by ==lnk==.

        Procedure Division using lnk-ReturnValues.
        *> user code goes in here
        End Method "EF-PrimeKey".

        *>Note that the next methods coming up are my own fairly
        *>standardized approach - I don't currently, but with a bit
        *>of thought could generate them in full with appropriate
        *>picture sizes and substituting the names of the DBI and
        *>SQL Tables I'm using

        *>-----------------------------------------------------------
        Method-id. "LB-index".
        *>-----------------------------------------------------------
        Local-storage section.
        01 ls-Primekey                   pic 9(04).
        01 ls-Index                      pic x(4) comp-5.
        Linkage section.
        01 lnk-Index                     pic x(4) comp-5.

        Procedure Division using lnk-Index.

          move lnk-Index to ws-CurrentIndex
          invoke os-MaterialsDBI "getKeyFromIndex"
             using ws-CurrentIndex returning ls-PrimeKey

          if   ls-PrimeKey <> zeroes
               invoke self "checkRecordExists" using ls-PrimeKey
          End-if

        End Method "LB-index".
        *>-----------------------------------------------------------
        Method-id. "PB-cancel".
        *>-----------------------------------------------------------
        Procedure Division.
           invoke self "displayEmptyScreen"
        End Method "PB-cancel".
        *>-----------------------------------------------------------
        Method-id. "PB-delete".
        *>-----------------------------------------------------------
        Local-storage section.
        01 ls-collection                   object reference.
        01 ls-response                     pic x(4) comp-5.

        Procedure Division.

         if  RecordFound
             set OKtoDelete to true
             invoke self "ErrorMessages" returning ls-response

             if ls-response = mb-return-ok
                invoke os-MatTable "deleteRecord"
                       using     Materials-MatID
                       returning ws-SqlResult

                Evaluate true
                  when ResultOK
                    invoke os-MaterialsDBI "deleteFromCollection"
                           using ws-CurrentIndex

                    if ws-CurrentIndex > 1
                       subtract 1 from ws-CurrentIndex
                    End-if

                  when TableError
                       invoke self "PB-Exit"
                End-evaluate

             End-if
         End-if

         invoke self "displayEmptyScreen"

        End Method "PB-delete".
        *>-----------------------------------------------------------
        Method-id. "PB-Exit".
        *>-----------------------------------------------------------
         set CancelProgram to true
         invoke os-Dialog "hide"
         invoke self "finalizeobjects"
        End Method "PB-Exit".
        *>-----------------------------------------------------------
        Method-id. "PB-help".
        *>-----------------------------------------------------------
        Procedure Division.
           invoke self "HelpFile"
        End Method "PB-help".
        *>-----------------------------------------------------------
        Method-id. "PB-ok".
        *>-----------------------------------------------------------
        Linkage section.
        01 lnk-Flag                         pic x(4) comp-5.
        Procedure Division using lnk-Flag.

        if     Materials-MatID = spaces
               EXIT METHOD

        else   set RecordChanged to true
        End-if

        if     RecordNotChanged
               move lnk-Flag to RecordChangedFlag
        End-if

        if     RecordChanged
               perform VALIDATE-RECORD

        else   invoke self "displayEmptyScreen"
        End-if

        EXIT METHOD.

        VALIDATE-RECORD.

         set ValidationOK to true
         invoke self "validationRoutine"

         If ValidationOK

             if     RecordFound
                    invoke self "rewriteRecord"

             else   invoke self "writeRecord"
             End-if

             invoke self "displayEmptyScreen"

         End-if
         .
        End Method "PB-ok".
        *>-----------------------------------------------------------

If you already have a COBOL compiler - doesn't cost you a penny and you 
can code to exactly your own design specification.

Jimmy
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 13)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-22T00:03:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43fb9c3d$0$28070$4fafbaef@reader1.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no> <43f517cb$0$12595$4fafbaef@reader3.news.tin.it> <8ZmJf.3884$_62.2976@edtnps90> <43f63ea8$0$6000$4fafbaef@reader2.news.tin.it> <j7uJf.35601$H%4.27262@pd7tw2no>`

```
The template you are writing is really a part of what I'm looking for.
In fact I've almost finished writing my own Java code generator to read a 
cobol text file and parse in to a java data structure and viceversa (maybe 
at a later time I will add a GUI too), so I can create template like yours, 
but using java instructions.
For example writing something like:

    new PerformStatement(new ThroughPhrase("label1","label2"))
    new MoveStatement(2,new Var(destVar,'X',4))
    new EndPerformStatement()

I can obtain, a text file with this cobol program:

identification div...
data div...
working storage.
      destVar       pic X(4)
procedure div...
    perform label1 through label2;
        move 2 to destVar
   end-perform
end file.

I can also do the opposite translation, that is "Cobol code to My Java 
structure", but I was looking for something to help me to build a component 
like "XSD to Cobol code template" or "XSD to my java structure" (for me it's 
the same), writing as least code as possible.

Thanks, Fabio


"James J. Gavan" <jgavandeletethis@shaw.ca> ha scritto nel messaggio 
news:j7uJf.35601$H%4.27262@pd7tw2no...
> Fabio Fabbri wrote:
>>>So you're writing this tool in Java, and you've already got the template 
…[244 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 14)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-22T14:28:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dy_Kf.7403$Nr5.6856@clgrps13>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <YesEf.161258$AP5.149625@edtnps84> <43ebcf8b$0$12604$4fafbaef@reader3.news.tin.it> <J3HIf.3048$_62.1127@edtnps90> <43f3599a$0$28062$4fafbaef@reader1.news.tin.it> <FmLIf.3098$_62.2606@edtnps90> <43f4e381$0$12603$4fafbaef@reader3.news.tin.it> <qT6Jf.1446$Y22.874@clgrps12> <yN7Jf.22055$H%4.7316@pd7tw2no> <43f517cb$0$12595$4fafbaef@reader3.news.tin.it> <8ZmJf.3884$_62.2976@edtnps90> <43f63ea8$0$6000$4fafbaef@reader2.news.tin.it> <j7uJf.35601$H%4.27262@pd7tw2no> <43fb9c3d$0$28070$4fafbaef@reader1.news.tin.it>`

```

"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43fb9c3d$0$28070$4fafbaef@reader1.news.tin.it...
> The template you are writing is really a part of what I'm looking for.
> In fact I've almost finished writing my own Java code generator to read a 
…[24 more quoted lines elided]…
> (for me it's the same), writing as least code as possible.

    You could use a parser-generator like JavaCC or SableCC to generate the 
Java code which can parse COBOL code and create an in-memory representation 
of it. That would give you what you've got right now.

    Then you could use an XML parser like Saxon or Castor which could parse 
an XSD file and create an in-memory representation of it.

    Then you would write a translator which could convert in-memory 
structures describing XML to in-memory structures describing COBOL.

    - Oliver
```

#### ↳ Re: xml schema (xsd) in cobol

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2006-02-03T00:42:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GFxEf.2455$5Q3.2057@twister.nyroc.rr.com>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it>`

```
I'm assuming you mean you want to convert an xsd into a COBOL record layout. 
I don't know of a tool that exactly meets what you're looking for, 
especially the open source part.  I do know of two products that will do 
what you want somewhat as a side-effect of what they. They are XMLBooster 
(www.xmlbooster.com) and XML Thunder (www.canamsoftware.com). Both are COBOL 
code generators to convert data between an XML document and a COBOL record 
and vice versa. They can read/produce an xsd as part of their capabilities.


"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43e103eb$0$22093$4fafbaef@reader1.news.tin.it...
>I need a tool to convert an xml schema definition (.xsd) into Cobol code.
> Did anyone already write something like this?
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: xml schema (xsd) in cobol

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-10T00:19:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43ebce1b$0$12593$4fafbaef@reader3.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <GFxEf.2455$5Q3.2057@twister.nyroc.rr.com>`

```
Thanks for the links and sorry for replaying only after a week. I'll try Xml 
booster. I think maybe it can really help.
I'll try to explain briefly what I'm doing.
I'm developing an application to convert a Cobol program (read as a text 
file) into a Java structured data and viceversa. I already have a cobol xml 
DOM reader/writer.
I was thinking a way to integrate an xsd-to-cobol , which can be very 
helpful to me. If I would find an open source component which already had 
the same purpose, I will save time.
For xsd-to-cobol I mean a program which:
- writes the working storage area as in the xsd
- writes the procedure division statements to read/write the xml message, 
making the user completing the code inserting the data-manipulation 
instructions.

Fabio


"Douglas Gallant" <no@spam.net> ha scritto nel messaggio 
news:GFxEf.2455$5Q3.2057@twister.nyroc.rr.com...
> I'm assuming you mean you want to convert an xsd into a COBOL record 
> layout. I don't know of a tool that exactly meets what you're looking for, 
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T19:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pLIf.3099$_62.1959@edtnps90>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <GFxEf.2455$5Q3.2057@twister.nyroc.rr.com> <43ebce1b$0$12593$4fafbaef@reader3.news.tin.it>`

```

"Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message 
news:43ebce1b$0$12593$4fafbaef@reader3.news.tin.it...
> Thanks for the links and sorry for replaying only after a week. I'll try 
> Xml booster. I think maybe it can really help.
…[11 more quoted lines elided]…
> instructions.

    If you want to translate a COBOL working storage section into an 
equivalent Java data structure, wouldn't you need a COBOL parser, rather 
than an XML/XSD parser?

    In fact, there's almost no reason to use XML as a middle-man in this 
situation; it just adds unnescessary extra complexity.

    - Oliver
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 4)_

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2006-02-15T18:17:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt0fs501050@enews2.newsguy.com>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <GFxEf.2455$5Q3.2057@twister.nyroc.rr.com> <43ebce1b$0$12593$4fafbaef@reader3.news.tin.it> <9pLIf.3099$_62.1959@edtnps90>`

```

"Oliver Wong" <owong@castortech.com> wrote in message
news:9pLIf.3099$_62.1959@edtnps90...
>
> "Fabio Fabbri" <spammeplenty@virgilio.it> wrote in message
…[8 more quoted lines elided]…
> > helpful to me. If I would find an open source component which already
had
> > the same purpose, I will save time.
> > For xsd-to-cobol I mean a program which:
> > - writes the working storage area as in the xsd
> > - writes the procedure division statements to read/write the xml
message,
> > making the user completing the code inserting the data-manipulation
> > instructions.
…[6 more quoted lines elided]…
> situation; it just adds unnescessary extra complexity.

Agreed.   We've done class extraction of COBOL working storage
into XMI with our COBOL front end.   Not terribly hard when
you have a full parser and full name type resolution.  Generating
Java class definitions directly instead of XMI would actually be
easier; XMI is a mess.

See http://www.semanticdesigns.com/Products/FrontEnds/COBOLFrontEnd.html
```

###### ↳ ↳ ↳ Re: xml schema (xsd) in cobol

_(reply depth: 5)_

- **From:** "Fabio Fabbri" <spammeplenty@virgilio.it>
- **Date:** 2006-02-22T00:31:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43fba2c5$0$28060$4fafbaef@reader1.news.tin.it>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it> <GFxEf.2455$5Q3.2057@twister.nyroc.rr.com> <43ebce1b$0$12593$4fafbaef@reader3.news.tin.it> <9pLIf.3099$_62.1959@edtnps90> <dt0fs501050@enews2.newsguy.com>`

```
It's a misunderstanding. I'm not using XSD as a middle-man: I agree with you 
that this is a nonsense.
My problem is to simplify the activity of developers who write xml-message 
readers and writers, starting from XSD schemas. The middle-man can be java; 
XSD is the source, and a cobol program is the output.
I introduced cobol parsing, formatting, indenting and so on inside my java 
code, which can be helpful for output code building, but won't help 
developers with XSD input management.
Simplify XSD input management is now my -real- problem.

Fabio


"Ira Baxter" <idbaxter@semdesigns.com> ha scritto nel messaggio 
news:dt0fs501050@enews2.newsguy.com...
>
> "Oliver Wong" <owong@castortech.com> wrote in message
…[42 more quoted lines elided]…
>
```

#### ↳ Re: xml schema (xsd) in cobol

- **From:** "Roy Bouwmeester" <r.bouwmeester@wanadoo.nl>
- **Date:** 2006-02-04T15:50:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43e4bf32$0$85364$dbd45001@news.wanadoo.nl>`
- **References:** `<43e103eb$0$22093$4fafbaef@reader1.news.tin.it>`

```
Hello Fabio,

I 've been working on a cobol-application which can parse an xml-document 
and even validate it. I made the choice to store the xsd into a 
db2-database. The reason for that decision is the fact that the xsd contains 
about 3000 records. You are also more flexible in appending a new xsd.

Maybe you can take this into consideration.

Regards,
Roy


"Fabio Fabbri" <spammeplenty@virgilio.it> schreef in bericht 
news:43e103eb$0$22093$4fafbaef@reader1.news.tin.it...
>I need a tool to convert an xml schema definition (.xsd) into Cobol code.
> Did anyone already write something like this?
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
