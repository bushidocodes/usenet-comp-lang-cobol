[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Object Model problems - NetExpress

_2 messages · 2 participants · 2001-01_

---

### Object Model problems - NetExpress

- **From:** "Neil Hayes" <NeilH@syspro.co.za>
- **Date:** 2001-01-09T07:04:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a5a9b80$0$234@helios.is.co.za>`

```
I think I'm just looking for 1 or 2 lines of code to answer this frustrating
problem which I don't seem to find any ole examples anywhere.

I originally attached a zip file containing the project, but I was unable to
post it. So parts of the code appear at the end.

Object.

To create one dll that contains multiple classes which contain methods and
properties

In my example vb project I want to be able to define one root class and
access the rest.or the classes in the manor below.

    Dim myobj as TestClass1.TestClass1    'Define the base class
    set myobj = CreateObject("TestClass1")    'Create the object

   myobj.Connect                                            'Do a method in
TestClass1 or set properties

  myobj.TestClass2.Colour  = "Red"              ' Set the colour in
TestClass2 to Red


Problem.

I animated this code to see what happens, the connect function was called OK
and any code would have run, but now what about the colour property ?

What do I need to do to get  myobj.TestClass2.Colour to run ?

What code should be in this property or is my structure incorrect or perhaps
my VB ?


TestClass2 could have multiple properties and methods so it would not be
correct to

    invoke TestClass2 "SetColour'' using xyz

instead it must return some sort of pointer but what and where does it go ?

Notes.

I've modified the TestClass1.if_idl file the original line commented out
The testclass1.idl file also has been modified to include

         importlib("stdole32.tlb");
        interface TestClass2;                     - This line was added.

This is the project code (NetExpress) if you want the zipped version email
me and I'll send with pleasure.


TestClass1.idl
*****************************************************
// typelib filename: testclass1.tlb

[
  // OCWIZARD - start library attributes
  uuid(E381676D-A25C-4188-89EB-10690EBC9B2B),
  version(1.0),
  helpstring("Library description for TestClass1")
  // OCWIZARD - end library attributes
]
library testclass1
{
    // TLib : OLE Automation : {00020430-0000-0000-C000-000000000046}
    importlib("stdole32.tlb");
    interface TestClass2;
    // OCWIZARD - start #include lines
    #include "TestClass1_if.idl"
    #include "TestClass2_if.idl"
    // OCWIZARD - end #include lines

TestClass1_if.idl
*****************************************************
    #include "TestClass1_if.h"
    [
    // OCWIZARD - start interface attributes
      dual,
      uuid(9FA6DACE-7C63-49AB-8265-F690D82E162D),
      helpstring("Interface description for TestClass1")
    // OCWIZARD - end interface attributes
    ]
    interface ITestClass1 : IDispatch
    {
    // OCWIZARD - start methods
        [id(DISPID_TESTCLASS1_CONNECT)] HRESULT Connect ([out, retval] long*
ret);
        [propget, id(DISPID_TESTCLASS1_GETTESTCLASS2),
        helpstring("info on class 2")]
        HRESULT TestClass2(
           [out, retval] TestClass2 ** ret);
   //     [id(DISPID_TESTCLASS1_GETTESTCLASS2), propget] HRESULT TestClass2
([out, retval] IDispatch ** Ret);

    };

    [
    // OCWIZARD - start class attributes
      uuid(DB257273-F0BE-4849-9DB5-55BAABEF647D),
     // aggregatable
    // OCWIZARD - end class attributes
    ]
    coclass TestClass1
    {
        [default] interface ITestClass1;
        interface ITestClass2;
    };

TestClass2_if.idl
*****************************************************
// Object COBOL class wizard generated file.
// This file is the IDL description of a class.
// Do not remove or alter any lines beginning with OCWIZARD.
// Do not add, delete or change any lines that appear between these
// markers, or your application may stop working.
    #include "TestClass2_if.h"
    [
    // OCWIZARD - start interface attributes
      dual,
      uuid(F24AE56E-0E26-4A78-B000-C1ACEE2067F9),
      helpstring("Interface description for TestClass2")
    // OCWIZARD - end interface attributes
    ]
    interface ITestClass2 : IDispatch
    {
    // OCWIZARD - start methods
        [id(DISPID_TESTCLASS2_SETCOLOURCODE), propput] HRESULT ColourCode (
                [in, out] BSTR * p0);
    // OCWIZARD - end methods
    };

    [
    // OCWIZARD - start class attributes
      uuid(45D55207-5CB3-48E3-B4C4-EBAE3F86B619),
      helpstring("Description for class TestClass2")
    // OCWIZARD - end class attributes
    ]
    coclass TestClass2
    {
        [default] interface ITestClass2;
    };


TestClass_if.h
*****************************************************
// OCWIZARD dispatch ids
#define DISPID_TESTCLASS1_CONNECT 0
#define DISPID_TESTCLASS1_GETTESTCLASS2 1
// OCWIZARD dispatch ids end

TestClass1Trigger.cbl
*****************************************************
      *> OLE server trigger (for in-process servers only)
      *> WARNING: Do not add further entry points to this file
      $set case
       linkage section.
       01 loadReason    pic x(4) comp-5.
       procedure division.
       entry "DllOleLoadClasses" using by value loadReason.
      *> OCWIZARD - start classes
      *> Calling the class registers it as available to OLE clients
           call "testclass1"
           call "testclass2"
      *> OCWIZARD - end classes
           exit program.

TestClass1.cbl
*****************************************************
      $set ooctrl(+p)

      *>-----------------------------------------------------------
      *> Class description
      *>-----------------------------------------------------------
       class-id. TestClass1
                 inherits from olebase.

       object section.
       class-control.
           TestClass1 is class "testclass1"
      *> OCWIZARD - start list of classes
           olebase is class "olebase"
           oleSafeArray is class "olesafea"
           oleVariant is class "olevar"
      *> OCWIZARD - end list of classes
      *>---USER-CODE. Add any additional class names below.
           TestClass2 is class "testclass2"

           .

      *>-----------------------------------------------------------
       working-storage section. *> Definition of global data
      *>-----------------------------------------------------------
      *01 anInterface           object reference.

      *>-----------------------------------------------------------
       class-object.   *> Definition of class data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard class methods
      *>-----------------------------------------------------------
      *> Return details about the class.
      *> If you have a type library, theClassId and theInterfaceId
      *> here MUST match.
      *> theProgId must match the registry entry for this class
      *>   (a zero length string implies using the class file name)
      *> theClassId must match the CLSID stored in the registry.
      *> theVersion is currently ignored (default 1 used).
      *>-----------------------------------------------------------
       method-id. queryClassInfo.
       linkage section.
       01 theProgId             pic x(256).
       01 theClassId            pic x(39).
       01 theInterfceId         pic x(39).
       01 theVersion            pic x(4) comp-5.
       01 theDescription        pic x(256).
       01 theThreadModel        pic x(20).
       procedure division using by reference theProgId
                                by reference theClassId
                                by reference theInterfceId
                                by reference theVersion
                                by reference theDescription
                                by reference theThreadModel.
        call "cbl_debugbreak"
         move z"{DB257273-F0BE-4849-9DB5-55BAABEF647D}" to theClassId
         move z"{9FA6DACE-7C63-49AB-8265-F690D82E162D}" to theInterfceId
         move z"Description for class TestClass1"
              to theDescription
         exit method.
       end method queryClassInfo.

      *>-----------------------------------------------------------
      *> Return details about the type library - delete if unused.
      *> theLocale is currently ignored (default 0 used).
      *> theLibraryName is a null terminated string used for auto
      *> registration, and supports the following values:
      *>     <no string> - Library is embedded in this binary
      *>     <number>    - As above, with this resource number
      *>     path        - Library is at this (full path) location
      *>-----------------------------------------------------------
       method-id. queryLibraryInfo.
       linkage section.
       01 theLibraryName        pic x(512).
       01 theMajorVersion       pic x(4) comp-5.
       01 theMinorVersion       pic x(4) comp-5.
       01 theLibraryId          pic x(39).
       01 theLocale             pic x(4) comp-5.
       procedure division using by reference theLibraryName
                                by reference theMajorVersion
                                by reference theMinorVersion
                                by reference theLibraryId
                                by reference theLocale.
         move 1 to theMajorVersion
         move 0 to theMinorVersion
         move z"{E381676D-A25C-4188-89EB-10690EBC9B2B}" to theLibraryId
         exit method.
       end method queryLibraryInfo.
      *>-----------------------------------------------------------

      *> OCWIZARD - end standard class methods

       end class-object.

      *>-----------------------------------------------------------
       object.         *> Definition of instance data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard instance methods
      *> OCWIZARD - end standard instance methods

      *>---------------------------------------------------------------

      *>---------------------------------------------------------------
       method-id. "Connect".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 ReturnCode             pic x(4) comp-5.

       procedure division returning ReturnCode.


       exit method.
       end method "Connect".
      *>---------------------------------------------------------------


      *>---------------------------------------------------------------
       method-id. "getTestClass2".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 anInterface       Object Reference.
       procedure division returning anInterface.

      *> I'm sure this is simple.....but what do I put in here ?

       exit method.
       end method "getTestClass2".
      *>---------------------------------------------------------------

       end object.

       end class TestClass1.

TestClass2.cbl
*****************************************************

      $set ooctrl(+p)

      *>-----------------------------------------------------------
      *> Class description
      *>-----------------------------------------------------------
       class-id. TestClass2
                 inherits from olebase.

       object section.
       class-control.
           TestClass2 is class "testclass2"
      *> OCWIZARD - start list of classes
           olebase is class "olebase"
           oleSafeArray is class "olesafea"
           oleVariant is class "olevar"


      *> OCWIZARD - end list of classes
      *>---USER-CODE. Add any additional class names below.

           .

      *>-----------------------------------------------------------
       working-storage section. *> Definition of global data
      *>-----------------------------------------------------------

      *>-----------------------------------------------------------
       class-object.   *> Definition of class data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard class methods
      *>-----------------------------------------------------------
      *> Return details about the class.
      *> If you have a type library, theClassId and theInterfaceId
      *> here MUST match.
      *> theProgId must match the registry entry for this class
      *>   (a zero length string implies using the class file name)
      *> theClassId must match the CLSID stored in the registry.
      *> theVersion is currently ignored (default 1 used).
      *>-----------------------------------------------------------
       method-id. queryClassInfo.
       linkage section.
       01 theProgId             pic x(256).
       01 theClassId            pic x(39).
       01 theInterfceId         pic x(39).
       01 theVersion            pic x(4) comp-5.
       01 theDescription        pic x(256).
       01 theThreadModel        pic x(20).
       procedure division using by reference theProgId
                                by reference theClassId
                                by reference theInterfceId
                                by reference theVersion
                                by reference theDescription
                                by reference theThreadModel.
         move z"{45D55207-5CB3-48E3-B4C4-EBAE3F86B619}" to theClassId
         move z"{F24AE56E-0E26-4A78-B000-C1ACEE2067F9}" to theInterfceId
         move z"Description for class TestClass2"
              to theDescription
         exit method.
       end method queryClassInfo.

      *>-----------------------------------------------------------
      *> Return details about the type library - delete if unused.
      *> theLocale is currently ignored (default 0 used).
      *> theLibraryName is a null terminated string used for auto
      *> registration, and supports the following values:
      *>     <no string> - Library is embedded in this binary
      *>     <number>    - As above, with this resource number
      *>     path        - Library is at this (full path) location
      *>-----------------------------------------------------------
       method-id. queryLibraryInfo.
       linkage section.
       01 theLibraryName        pic x(512).
       01 theMajorVersion       pic x(4) comp-5.
       01 theMinorVersion       pic x(4) comp-5.
       01 theLibraryId          pic x(39).
       01 theLocale             pic x(4) comp-5.
       procedure division using by reference theLibraryName
                                by reference theMajorVersion
                                by reference theMinorVersion
                                by reference theLibraryId
                                by reference theLocale.
         move z"C:\RND\test\testclass1.tlb"
                           to theLibraryName
         move 1 to theMajorVersion
         move 0 to theMinorVersion
         move z"{115106F3-5156-4EA3-8881-5514C5C58AD3}" to theLibraryId
         exit method.
       end method queryLibraryInfo.
      *>-----------------------------------------------------------

      *> OCWIZARD - end standard class methods

       end class-object.

      *>-----------------------------------------------------------
       object.         *> Definition of instance data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard instance methods
      *> OCWIZARD - end standard instance methods

      *>---------------------------------------------------------------
       method-id. "setColourCode".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 ColourCode             pic x(10).
       procedure division using by reference ColourCode.

      *>---USER-CODE. Add method implementation below.

       exit method.
       end method "setColourCode".
      *>---------------------------------------------------------------


       end object.

       end class TestClass2.

Visual Basic Project.

Create a new VB project, add a reference to the TestClass1.dll, add a
command button. Add this code to the command button.

Private Sub Command1_Click()

'I modified the type library IDL files to achive this for intellisense
'The TestClass2 get property in TestClass1 returns the interface of
TestClass2

Dim myobj As testclass1.testclass1

Set myobj = CreateObject("testclass1")

'Do a connection
myobj.Connect

'set the colour code to Red
myobj.TestClass2.ColourCode = "Red"

'Finalize the object
Set myobj = Nothing


End Sub



I await in hope


Regards

Neil
NeilH@syspro.co.za
```

#### ↳ Re: Object Model problems - NetExpress

- **From:** "David Sands" <david.sands@merant.com>
- **Date:** 2001-01-17T10:15:57
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<943vvu$rt7$1@hyperion.mfltd.co.uk>`
- **References:** `<3a5a9b80$0$234@helios.is.co.za>`

```
Hi Neil,

I think you will need an variable such as

01    mytestclass2    object reference.

in object stroage of testclass1.

In class section if testclass1

>            TestClass2 is class "testclass2"

should be

>            TestClass2 is class "$OLE$testclass2"

and then in Gettestclass2 of testclass you could have something such as:-

    if mytestclass2 = null
        invoke testclass2 "new" returning mytestclass2
    end-if
    move mytestclass2 to aninterface

I think that should work OK.

Regards
David

"Neil Hayes" <NeilH@syspro.co.za> wrote in message
news:3a5a9b80$0$234@helios.is.co.za...
> I think I'm just looking for 1 or 2 lines of code to answer this
frustrating
> problem which I don't seem to find any ole examples anywhere.
>
> I originally attached a zip file containing the project, but I was unable
to
> post it. So parts of the code appear at the end.
>
…[11 more quoted lines elided]…
>    myobj.Connect                                            'Do a method
in
> TestClass1 or set properties
>
…[6 more quoted lines elided]…
> I animated this code to see what happens, the connect function was called
OK
> and any code would have run, but now what about the colour property ?
>
> What do I need to do to get  myobj.TestClass2.Colour to run ?
>
> What code should be in this property or is my structure incorrect or
perhaps
> my VB ?
>
…[6 more quoted lines elided]…
> instead it must return some sort of pointer but what and where does it go
?
>
> Notes.
…[45 more quoted lines elided]…
>         [id(DISPID_TESTCLASS1_CONNECT)] HRESULT Connect ([out, retval]
long*
> ret);
>         [propget, id(DISPID_TESTCLASS1_GETTESTCLASS2),
…[3 more quoted lines elided]…
>    //     [id(DISPID_TESTCLASS1_GETTESTCLASS2), propget] HRESULT
TestClass2
> ([out, retval] IDispatch ** Ret);
>
…[32 more quoted lines elided]…
>         [id(DISPID_TESTCLASS2_SETCOLOURCODE), propput] HRESULT ColourCode
(
>                 [in, out] BSTR * p0);
>     // OCWIZARD - end methods
…[349 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
