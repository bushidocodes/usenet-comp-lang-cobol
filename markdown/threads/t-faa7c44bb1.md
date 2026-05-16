[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing String from java to object oreinted cobol.

_5 messages · 4 participants · 2005-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Passing String from java to object oreinted cobol.

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-12-23T18:50:18+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<KFXqf.12556$m05.9540@clgrps12>`
- **References:** `<doga69$a7am$1@news.boulder.ibm.com>`

```
"Rajiv Guliani" <rguliani@in.ibm.com> wrote in message 
news:doga69$a7am$1@news.boulder.ibm.com...
> I am trying to pass a string from Java to cobol module.
>
…[16 more quoted lines elided]…
> Now, how can i populate String1 by the value present in String2.

    I don't know the answer to your question, but I know someone in 
comp.lang.cobol (to which I've crossposted) is also working with OO COBOL, 
and I believe he is also working with COBOL code that occasionally talks to 
Java code.

    Hopefully he'll see this message, know the answer, and post it for you.

    - Oliver
```

#### ↳ Re: Passing String from java to object oreinted cobol.

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-12-23T21:09:15+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<%HZqf.54924$2k.10432@pd7tw1no>`
- **In-Reply-To:** `<KFXqf.12556$m05.9540@clgrps12>`
- **References:** `<doga69$a7am$1@news.boulder.ibm.com> <KFXqf.12556$m05.9540@clgrps12>`

```
Oliver Wong wrote:
> "Rajiv Guliani" <rguliani@in.ibm.com> wrote in message 
> news:doga69$a7am$1@news.boulder.ibm.com...
…[29 more quoted lines elided]…
>     - Oliver 

I for one don't do any linkage to or from Java, but as you posted to 
ibm.software originally, I'm assuming you are using the IBM Enterprise 
OO COBOL ?

There is no *working* standard for this in the three OO compilers from 
IBM, Fujitsu or Micro Focus (Net Express), unless you are using dot.Net 
with the last two.

Assuming this is IBM, then you will need to check IBM references. I 
would have thought they would have this detailed either in on-line 
manuals or a series of examples.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Passing String from java to object oreinted cobol.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-12-27T18:24:12+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<gFfsf.201297$xV6.187876@fe02.news.easynews.com>`
- **References:** `<doga69$a7am$1@news.boulder.ibm.com> <KFXqf.12556$m05.9540@clgrps12> <%HZqf.54924$2k.10432@pd7tw1no>`

```
To add to what Jimmy has stated (and again, assuming a CURRENT IBM COBOL 
compiler),  start at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg30/6.2.2.1

and look at some of the other pages around it.


P.S. For those who care (and those who don't) IBM's COBOL does "data conversion" 
on certain type of arguments, e.g. floating-point (from IBM-hex-FP to IEEE) and 
to/from Unicode in certain cases.
```

###### ↳ ↳ ↳ Re: Passing String from java to object oreinted cobol.

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-12-27T23:59:53+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<Zzksf.200705$ki.193558@pd7tw2no>`
- **In-Reply-To:** `<gFfsf.201297$xV6.187876@fe02.news.easynews.com>`
- **References:** `<doga69$a7am$1@news.boulder.ibm.com> <KFXqf.12556$m05.9540@clgrps12> <%HZqf.54924$2k.10432@pd7tw1no> <gFfsf.201297$xV6.187876@fe02.news.easynews.com>`

```
William M. Klein wrote:
> To add to what Jimmy has stated (and again, assuming a CURRENT IBM COBOL 
> compiler),  start at:
…[9 more quoted lines elided]…
> 
Bill,

To follow up on this one, some thoughts I had.

Firstly the page reference you gave - I think if he studies the other 
topics indicated by the "book-mark" showing at the bottom left of the 
page, he will get what he wants. Without back-tracking, I recall his 
example had something like following :-

01 Mystring	object reference.java-string.    ??????

Well for starters that ain't any COBOL Standard other than IBM. 
Presumably IBM provides a set of support classes for java string 
handling whether or not the values are pic x or pic 9.

To the original enquirer, who is in charge COBOL or Java, i.e. which is 
the first to call the other ? Is it COBOL doing decision processing and 
DB handling (whether COBOL files or SQL) and calling Java for support on 
'utilities' - or vice versa.

There's no indication yet how efficient you are at using Java - so 
following may be along the lines of teaching grandmother how to suck eggs.

Firstly there's the Component approach loudly proclaimed by Pete 
Dashwood using Java. He has a routine for string handling. If interested 
contact him via comp.lang.cobol - I'm sure he will be more than willing 
to help.

Secondly, my approach. It's my word, so I sometimes feel like I'm 
'proclaiming in the wilderness' :-) I see no point in adapting to 
anything new, (OO in COBOL for example), if it doesn't give you an 
'edge' for development. To me of prime importance is to arrive at 
methods which are flogged to death until they are as bullet proof as you 
can make them. I use the term R-E-U-S-E.

An easy example; any of the COBOL date function routines I use are in a 
separate class called DateAndTime. I don't have to remember what the 
routines/methods do, or that internally within the class they call 
'private' methods - not a word used in the COBOL Standard, but 
nevertheless they exist.

Same goes for string handling that you are querying. As COBOL is my base 
unit (i.e. pic x or pic 9) I strictly only require objects when I want 
to put them into Windows for display. So if I want to use a Customer 
Name pic x(?) to display, that has to be converted to an object for 
dialogging; similarly if the user keys into a dialog a new name that 
object has to be translated into a pic x for storage in a COBOL file/DB 
Table.

I keep COBOL 'clean' and do my 'translations' in a template class I use 
to build my dialogs. Your situation will be different with IBM, but just 
as background (Note all the 'missing stuff' - Micro Focus have an 
'ignore red-tape' feature ). Where I reference collections these are 
your Java lists/Maps :-

1. Converting to object :

1a. COBOL Business procedural or class :-

        *>-------------------------------------------------------------
        Method-id. "passEntryfield".
        *>-------------------------------------------------------------
        Local-storage section.
        01 ls-display                        pic zz9 blank when zero.
        01 ls-length                         pic x(4) comp-5.
        Procedure Division.

         Evaluate true
           when field-PrimeKey
                move length of Materials-MatID to ls-length
                move Materials-MatID to Dialog-text

           when field-SpecNo
                move length of Materials-SpecNo to ls-length
                move Materials-SpecNo to Dialog-text

           when field-Grade
                move length of ls-display to ls-length
                move Materials-GradeNo to ls-display
                move ls-display        to Dialog-text

         End-evaluate

         invoke os-Dialog "setEntryfield"
                using Dialog-Field, ls-length, Dialog-Text

        End Method "passEntryfield".
        *>-------------------------------------------------------------


1b. Dialog template

        *>--------------------------------------------------------------
        Method-id. "setEntryField".
        *>--------------------------------------------------------------

        *> This method is used for passing pic x and pic 9 fields

        Local-storage section.
        01 ls-Length                         pic x(4) comp-5.
        01 ls-string                         object reference.
        Linkage section.
        01 lnk-Field                         pic x(4) comp-5.
        01 lnk-Length                        pic 9(03).
        01 lnk-Text                          pic x(50).

        Procedure Division using lnk-Field, lnk-Length, lnk-Text.

          move lnk-length to ls-Length
          invoke CharacterArray "withLengthValue"
                 using ls-length, lnk-text returning ls-string
          invoke os-DialogCollection(1) "at"
                 using lnk-field returning Dialog-Object
          invoke Dialog-Object "setText" using ls-string
          invoke Dialog-Object "show"
          invoke ls-string "finalize" returning ls-string

        End Method "setEntryField".
        *>--------------------------------------------------------------

2. Converting to string :

2a. Dialog template

        *>--------------------------------------------------------------
        Method-id. "ReturnEntryField".
        *>--------------------------------------------------------------
        Local-storage section.
        copy "\copylib\dlgreturn.cpy" replacing ==(tag)== by ==ls==.

**** see the above copyfile expanded under 2b

        01 ls-string                     object reference.

        Linkage section.
        01 lnk-Field                     pic x(4) comp-5.

        Procedure Division using lnk-Field.

         initialize ls-ReturnValues
         invoke os-DialogCollection(1) "at"
                using lnk-field returning Dialog-Object
         invoke os-DialogCollection(2) "at"
                using lnk-field returning ws-MethodRec

        if ElementChanged
           move   ws-Row     to ls-Line
           move   ws-Column  to ls-Column
           invoke Dialog-Object "Getlength" returning ls-length
           move lnk-Field to Ls-FieldID

           invoke Dialog-Object "getText" returning ls-string
           invoke ls-string "trimblanks" returning ls-string
           invoke ls-string "getValueWithSize"
               using ls-Length returning ls-text
           invoke ls-string "finalize" returning ls-string
           invoke os-Caller ws-MethodName using ls-ReturnValues
        End-if

        End Method "ReturnEntryField".
        *>--------------------------------------------------------------

2b. COBOL Business procedural or class :-

*      *>--------------------------------------------------------------
        Method-id. "EF-Grade".
        *>--------------------------------------------------------------
        Linkage section.
        copy "\copylib\dlgReturn.cpy" replacing ==(tag)== by ==lnk==.

        *>----------------dilgreturn.cpy ------------------------------

        01 (tag)-ReturnValues.

           *> Column and Line used to identify the 'cell' from a
           *> two-dimensional table

           05 (tag)-Column                  pic x(4) comp-5.
           05 (tag)-Line                    pic x(4) comp-5.
           05 (tag)-length                  pic x(4) comp-5.

           *> Field-ID used where necessary to return a specific
           *> selection, such as the choice from a Radio Button Group

           05 (tag)-FieldID                 pic x(4) comp-5.

           05 (tag)-text.
              10 occurs 1 to ws-MaxLength
                 depending on (tag)-length  pic x(01).

        *>--------------------------------------------------------------

        Procedure Division using lnk-ReturnValues.

        set RecordChanged to true
        compute Materials-GradeNo = function numval (lnk-text)

        End Method "EF-Grade".
        *>--------------------------------------------------------------

So two different approaches, and there are obviously many more. But it 
sure makes it easier for you if you think in terms of generalised 
routines, prove throughly once, and they can be used over and over 
again. As sure as eggs is eggs, apparent one-off routines show they can 
be used again, perhaps six months down the road before you twig.

Doesn't matter which end you do it Java or COBOL - but if COBOL then get 
a handle on the data types that IBM sends/receives and build a general 
purpose routine into a separate class. The alternative of course, send 
Java strings that represent either pic x or pic 9.

Need any help on Java/COBOL - sing out - I'm sure Pete will help and 
Oiver will give you the necessary backup for Java.

Jimmy, Calgary AB
```

#### ↳ Re: Passing String from java to object oreinted cobol.

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-12-29T13:56:32+13:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<41gqi8F1e64s1U1@individual.net>`
- **References:** `<doga69$a7am$1@news.boulder.ibm.com> <KFXqf.12556$m05.9540@clgrps12>`

```
 
Sorry,
I missed this earlier...

Solution below, although he's probably solved it by now :-).

"Oliver Wong" <owong@castortech.com> wrote in message 
news:KFXqf.12556$m05.9540@clgrps12...
>
> "Rajiv Guliani" <rguliani@in.ibm.com> wrote in message 
…[20 more quoted lines elided]…
>

java.lang.String inherits from java.lang.Object

It SHOULD therefore be possible to use the object methods of the Java String 
class to populate String1...

invoke String2 "getChars"  using
                                         by value 0                   *> 
start of string in Java object
                                         by value 4                   *> end 
of string in Java object
                                         by reference String1    *> 
destination string array
                                         by value 0                   *> 
start position in destination array
end-invoke

The Fujitsu environment supports this indirectly... (the code above would 
not work, but somethng very similar can be used if the Java object is 
converted to a COBOL object first).

I believe that future releases of OO COBOL will support Java 
interoperability much better than current ones do.

In YOUR environment you are required to interface through the Java Native 
Interface and this provides a layer around the underlying Java Class.

COBOL represents Java String data in Unicode. To represent a Java String in 
a COBOL program, declare the string as an object reference of the jstring 
class. Then use JNI services to set or extract COBOL alphanumeric or 
national (Unicode) data from the object.

If string1 is defined as USAGE NATIONAL, you will need a different JNI 
Method ("GetStringChars"). I have assumed you are using EBCDIC.

IBM have provided methods in this environment and the one you need is as 
follows:

call "GetStringPlatform"
      using by value JNIEnvPtr
               address of string2
               address of string1
               5
               0
       returning rc     *> rc is a binary fullword integer
end-call

evaluate rc
    when  0
          *> Hooray! the string is in string1...
    when -1
          *> an illegal character was encountered in the input string...
    when -2
          *> The last parameter above defines the output encoding and it has 
been found to be illegal. The string in string1 is set to null.
    when -3
         *> The string filled the target (may have overflowed...)
    when other
         *> something is screwed in your environment...
end-evaluate
...

These EBCDIC services are packaged as a DLL that is part of your IBM Java 2 
Software Development Kit. Use CALL literal statements to call these 
services. The calls are resolved through the libjvm.x DLL side file, which 
you must include in the link step of any COBOL program that uses 
object-oriented language.

Note that you use CALL, rather than INVOKE.

Hope this helps :-)

Pete.


>    I don't know the answer to your question, but I know someone in 
> comp.lang.cobol (to which I've crossposted) is also working with OO COBOL, 
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
