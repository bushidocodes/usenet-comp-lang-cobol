[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COM and COBOL

_3 messages · 3 participants · 1998-10_

---

### COM and COBOL

- **From:** mitchell@inlink.com
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<702ias$esp$1@nnrp1.dejanews.com>`

```
Can someone please tell me if COBOL is or can be COM enabled?
Please reply to this address: mitchell_l_land@uhc.com

Thanks
```

#### ↳ Re: COM and COBOL

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NB5V1.823$9R2.1355295@news4.mia.bellsouth.net>`
- **References:** `<702ias$esp$1@nnrp1.dejanews.com>`

```
mitchell@inlink.com wrote:
>Can someone please tell me if COBOL is or can be COM enabled?

That would depend on the COBOL compiler.
```

##### ↳ ↳ Re: COM and COBOL

- **From:** smb@mfltdz.co.ukz (Steve Biggs)
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<704dln$tcu@hyperion.mfltd.co.uk>`
- **References:** `<702ias$esp$1@nnrp1.dejanews.com> <NB5V1.823$9R2.1355295@news4.mia.bellsouth.net>`

```
"Judson McClendon" <judmc123@bellsouth.net> wrote:
>mitchell@inlink.com wrote:
>>Can someone please tell me if COBOL is or can be COM enabled?
>
>That would depend on the COBOL compiler.

Micro Focus NetExpress provides high-level run-time/syntactical support 
for both COM automation and ActiveX controls. This will include dual 
interface support in automation servers from NetExpress 3.0.

COM itself is largely language-independant, although heavily based on the 
design of C++. Any language that can export a pointer to a table of 
virtual functions (a 'vtable'), or can dereference such a table when given 
a pointer in order to call the functions, and can supply the appropriate 
calling conventions and parameter types should be able to use COM. It 
might help if the language is OO-based, as this makes handling of multiple 
objects/vtables easier.

Micro Focus COBOL is able to do all of that, but you need a reasonable 
understanding of COM (and COBOL) to be able to do this. We provide a class 
library, to enable the calling of COM interfaces, in the NetExpress 
product in addition to the high-level support I mentioned above. Both 
require some knowledge of OO (Object) COBOL, for which we provide several 
tools within the product.

NB: This discussion doesn't include binding to COM type libraries, which 
*is* largely a compiler/linker issue.

Steve.
Micro Focus Development.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
