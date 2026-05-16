[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help on Net Express COBOL dll and calling the DLL from VB program

_4 messages · 3 participants · 2002-05 → 2002-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help on Net Express COBOL dll and calling the DLL from VB program

- **From:** aravindbabuv@yahoo.com (aravind)
- **Date:** 2002-05-28T10:44:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be69045e.0205280944.76acdd8e@posting.google.com>`

```
Hello All,
I am trying to create a COBOL DLL using NetExpress
3.1.
I have created the class and added methods and
complied.
Now I am trying to access it from VB as follows.

Private Sub Command2_Click()
Dim g As Integer
Dim p As Integer
g = Val(Text4.Text)
p = Val(Text5.Text)
Dim n As Integer

Dim obj2 As babu6.babu6  ' if this code can be
replaced by dim obj2 as
object
Set obj2 = New babu6.babu6 ' then this code will be
set obj2 =
createobject ("babu6")

Text6.Text = obj2.RetriveTotalPayCheck(g, p)

End Sub

I have used 2 input boxes and 1 output text box.
I pass values g, p to the method RetriveTotalPayCheck.
I am getting 438 Runtime Error. Object does not
support this Method or
Property

Possible reasons :
1. Late Bound applies when we used the code given in
VB comments
2. Currently it is used as early bound.

is there any way to fix the 438 run time error. or is
there any option
i should check or select when creating method. I have
used to create
cobol dll as both OLE Automation and Microsoft
Transaction Server.


Thanks
Aravind
```

#### ↳ Re: Help on Net Express COBOL dll and calling the DLL from VB program

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-05-28T18:32:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad143a029ef@enews2.newsguy.com>`
- **References:** `<be69045e.0205280944.76acdd8e@posting.google.com>`

```

"aravind" <aravindbabuv@yahoo.com> wrote in message
news:be69045e.0205280944.76acdd8e@posting.google.com...
> Hello All,
> I am trying to create a COBOL DLL using NetExpress
…[27 more quoted lines elided]…
> Property

> Possible reasons :
> 1. Late Bound applies when we used the code given in
> VB comments
> 2. Currently it is used as early bound.

It's probably something more esoteric than this.

Is your ActiveX library/server properly registered?  Even if you intend to
use late binding, you can reference the component long enough to check it
out with the object browser.  Insure that RetriveTotalPayCheck is truly
available in your component's interface.

(Just a tangential thought -- is the method also mispelled in the component?
If not, it's not surprising that it cannot be found.)
```

#### ↳ Re: Help on Net Express COBOL dll and calling the DLL from VB program

- **From:** aravind741 <member@dbforums.com>
- **Date:** 2002-06-06T06:24:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cff001c$3@usenetgateway.com>`
- **References:** `<be69045e.0205280944.76acdd8e@posting.google.com>`

```
Hi Grinder, I have a another example which is shown below. it works fine
here. But I have created similiar classes , but I get the same error.
438 Object does not support this method or property. Any suggestions

VB code Private Sub Command1_Click() Dim g As Double Dim p As Single Dim
n As Double Dim o As Object Set o = CreateObject("idoa7") g = Text1.Text
p = Text2.Text n = o.calnet7(g, p) Text3.Text = n End Sub


Net Express Code cobol dll

      $set ooctrl(+p)

      *>----------------------------------------------------------- *>
      Class description
      *>-----------------------------------------------------------
      class-id. idoa7 inherits from olebase.

       object section. class-control. idoa7 is class "idoa7" *> OCWIZARD
       - start list of classes olebase is class "olebase" oleSafeArray
       is class "olesafea" oleVariant is class "olevar" *> OCWIZARD -
       end list of classes *>---USER-CODE. Add any additional class
       names below.

           .

      *>-----------------------------------------------------------
      working-storage section. *> Definition of global data
      *>-----------------------------------------------------------

      *>-----------------------------------------------------------
      class-object. *> Definition of class data and methods
      *>-----------------------------------------------------------
      object-storage section.

      *> OCWIZARD - start standard class methods
      *>----------------------------------------------------------- *>
      Return details about the class. *> If you have a type library,
      theClassId and theInterfaceId *> here MUST match. *> theProgId
      must match the registry entry for this class *> (a zero length
      string implies using the class file name) *> theClassId must match
      the CLSID stored in the registry. *> theVersion is currently
      ignored (default 1 used).
      *>-----------------------------------------------------------
      method-id. queryClassInfo. linkage section. 01 theProgId pic
      x(256). 01 theClassId pic x(39). 01 theInterfceId pic x(39). 01
      theVersion pic x(4) comp-5. 01 theDescription pic x(256). 01
      theThreadModel pic x(20). procedure division using by reference
      theProgId by reference theClassId by reference theInterfceId by
      reference theVersion by reference theDescription by reference
      theThreadModel. move z"{FC65FB59-68CB-11D6-B317-9B901B06D928}" to
      theClassId move z"{FC65FB5A-68CB-11D6-B317-9B901B06D928}" to
      theInterfceId move z"Description for class idoa7" to
      theDescription move z"Apartment" to theThreadModel exit method.
      end method queryClassInfo.

      *> OCWIZARD - end standard class methods

       end class-object.

      *>-----------------------------------------------------------
      object. *> Definition of instance data and methods
      *>-----------------------------------------------------------
      object-storage section.

      *> OCWIZARD - start standard instance methods *> OCWIZARD - end
      standard instance methods

      *>---------------------------------------------------------------
      method-id. "calnet7". local-storage Section. 01 d11 comp-2.
      *>---USER-CODE. Add any local storage items needed below. linkage
      Section. 01 gp1 comp-2. 01 tx1 pic s9(4) comp-5. 01 np1 comp-2.

       procedure division using by value gp1 by value tx1 returning np1.
       compute d11 = (gp1 * tx1) /100 compute np1 = gp1 - d11


      *>---USER-CODE. Add method implementation below.

       exit method. end method "calnet7". *>----------------------------
       ------------------------------------


       end object.

       end class idoa7.
```

##### ↳ ↳ Re: Help on Net Express COBOL dll and calling the DLL from VB program

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-06-07T21:03:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adron402onr@enews1.newsguy.com>`
- **References:** `<be69045e.0205280944.76acdd8e@posting.google.com> <3cff001c$3@usenetgateway.com>`

```

"aravind741" <member@dbforums.com> wrote in message
news:3cff001c$3@usenetgateway.com...
> Hi Grinder, I have a another example which is shown below. it works fine
> here. But I have created similiar classes , but I get the same error.
> 438 Object does not support this method or property. Any suggestions

Look at your ActiveX library with a COM object browser -- either the one in
VB or another tool of your choice.  This will show you if the interface is
being properly exposed.

You mentioned that the library is being early bound into a VB app.  Is the
method you are trying to use, found by the VB interface as you're typing it
in?  Does the syntax you're using match that offered by VB?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
