[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sending Mail from MF/NetExpress Object COBOL using MAPI services

_21 messages · 9 participants · 2003-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-09T23:52:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3093282.1057794745@dbforums.com>`

```

Hi,
I am having a problem invoking a MS Outlook session from my OO Cobol
program(MicroFocus NetExpress 4.0) that uses MSMAPI.MAPISession
registered class and establishes a new outlook session.

The code looks like this:

Class-Control.
   MAPISession         is class "$OLE$MSMAPI.MAPISession"
   MAPIMessages        is class "$OLE$MSMAPI.MAPIMessages"
   CharacterArray      is class "chararry"
Working-Storage Section.
01 SessionObj               object reference.
01 MessageObj               object reference.
Procedure Division.
    invoke MapiSession  "new" returning SessionObj
    invoke MapiMessages "new" returning MessageObj
    invoke SessionObj "SignOn"
    invoke SessionObj "GetSessionID" returning plSessionID

This program is a called program from a WEB CGI program running on an MS
IIS Web Server, Windows 2000 professional environment.

The eroor I get is as follows:

Exception 65537 not trapped by the class oleexceptionmanager.
Description: "Server defined OLE exception"
(80020009): MAPI Failure: valid session ID does not exist
Hit T to terminate program. Hit any other key to continue.

Exception 65537 not trapped by the class oleexceptionmanager.
Description: "Server defined OLE exception"
(80020009): Property is read only when not using compose buffer. Set
            MsgIndex = -1

I suspect there is a security issue here, but I am not sure. I have
checked that the IIS_User has security acces to send mail, but no
luck so far.

Any ideas?

thanks

R...
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T22:09:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d3bfc_9@news.athenanews.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```
Hi,

Do you want the Outlook session for the calendar, notes, etc, or are you
using it simply to send mail, because it is a convenient
MAPI client?

The reason I ask is because there are MUCH better ways to send mail from the
environment you are using than going via Outlook (or ANY MAPI client...)

If you are interested in a (simpler) and more efficient alternative check
out:

http://groups.google.co.nz/groups?hl=en&lr=&ie=UTF-8&oe=UTF-8&selm=3edd3a97_3%40news.athenanews.com&rnum=1

In the meantime, I have made some suggested changes to your code.

Let me know how you get on.

Pete.

"Ringo950" <member30412@dbforums.com> wrote in message
news:3093282.1057794745@dbforums.com...

>
> Hi,
…[8 more quoted lines elided]…
>    MAPIMessages        is class "$OLE$MSMAPI.MAPIMessages"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Comment this  Class out.


>    CharacterArray      is class "chararry"
> Working-Storage Section.
…[3 more quoted lines elided]…
>     invoke MapiSession  "new" returning SessionObj
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Get to the "Message" by invoking it from the Session hierarchy, like this...

       invoke SessionObj "new" returning MessageObj

>     invoke SessionObj "SignOn" ^^^^^^^^^^^^^^^^ won't you need parameters
for this?
>     invoke SessionObj "GetSessionID" returning plSessionID
>

Animate the above and check that you don't have NULL object references after
the invokes...of the "new" method.


<snip>.

Pete.
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-10T13:12:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3095033.1057842770@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Originally posted by Peter E.C. Dashwood 
> Hi,
>
…[67 more quoted lines elided]…
> Pete. 


Hi Pete,
I am simply trying to send mail, nothing fancy. It works when I run it
on my locat NetExpress IDE 4.0. But when I move the code to the server
that uses MF Application server(Run Time), it does not work.

Do you have sample code for the mail method you mentioned?  I am
assuming it is cobol call to .NET, is that right?

thanks

R.
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL NOT using MAPI services

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T23:27:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e9fd0_3@news.athenanews.com>`
- **References:** `<3093282.1057794745@dbforums.com> <3095033.1057842770@dbforums.com>`

```

"Ringo950" <member30412@dbforums.com> wrote in message
news:3095033.1057842770@dbforums.com...
<snip of my original post>>
>
> Hi Pete,
…[3 more quoted lines elided]…
>

Did you try the amendments I suggested? There are different Classes in
different environments.

> Do you have sample code for the mail method you mentioned?  I am
> assuming it is cobol call to .NET, is that right?
>

No, it has nothing to do with .NET (although the .NET SMTPMail Class wraps
it...)

It is a use of Collaboration Data Objects (CDOSYS) which has now replaced
CDONTS, as CDO for NTS was called.

Here's the code...(It is Fujitsu OO COBOL but you will be able to translate
to MF pretty easily...)
(paste all the constant data (things starting with 'http://') lines exactly
as below)

* CDOSYS stuff...
 01  COMProgid   pic x(20) value "CDO.Message.1".
 01  objMail      OBJECT REFERENCE CDOSYS.
 01  COMProg02   pic x(20) value "CDO.Configuration.1".
 01  objCDOConf   OBJECT REFERENCE CDOSYS.
 01  objCDOFields    OBJECT REFERENCE CDOSYS.
 01  txtConfItem1  pic x(80) value
     'http://schemas.microsoft.com/cdo/configuration/sendusing'.
 01  txtConfItem2  pic x(80) value
     'http://schemas.microsoft.com/cdo/configuration/smtpserver'.
 01  txtConfItem3  pic x(80) value
     'http://schemas.microsoft.com/cdo/configuration/smtpserverport'.
 01  txtConfItem4  pic x(80) value
     'http://schemas.microsoft.com/cdo/configuration/sendusing'.


 01  txtSubject  pic x(50) value 'Earth, we have a problem...'.
 01  txtSender   pic x(50) value 'Joe90@Enterprise.com'.
 01  txtTo          pic x(50) value 'anybody@somewhere.com'.
 01  txtTextBody pic x(75) value
     'There is a meltdown in the core on level 37... Thank you for using
Starfleet.'. *> only if you don't

*> have one you prepared

*> earlier...

 01  HTMLMessage pic x(75) value 'Server relative path to the HTML
message\Mess.htm'.
 01  TEXTMessage pic x(75) value 'Server relative path to the TEXT
message\Mess.txt'.
 01  HTML-flag   pic x value space.
     88 sending-HTML value '1'.
     88 sending-TEXT value '0'.

The above caters for an embedded text message, an attached text message, or
an embedded HTML message. There is a problem with embedding images (like
logos, for example) into HTML mail and many people use a link back to their
server for the <img> tag. Obviously, this means the image will only appear
if the mail is read on-line... not a very useful state of affairs...

The code below uses CDOSYS to solve this problem and the result is
elegant.(Logos are embedded into the (HTML) mail and appear whether it is
read offline or not...)

This is using port 25 directly and therefore does not require a MAPI client.
Mail is sent whether the system has Outlook on it or not...

I have previously created a full letter (it is a Booking Confirmation and
has a lot of data in it),  in text or HTML format, depending on what the
user indicated on the Web Page. (Radio Button handled with JavaScript)

*------------------------------------------------------------------------ 
 Post-the-Mail   section.
 ptm000.
*
*  This section uses CDOSYS to post the mail created by Mail-WBR45CGI
*  above.
*
*  The HTML mail is sent as Body Text with no attachment.
*  Text Mail is sent with a short Message and the Confirmation
*  as a Plain Text Attachment. This is because there is no CDOSYS
*  Plain Text equivalent Method for "CreateMHTMLBody".
*
     move zero to 0-RESULT
     invoke CDOSYS "CREATE-OBJECT"
            using COMProgID
        returning objMail
     end-invoke
     invoke objMail "GET-Configuration"
            returning objCDOConf
     invoke objMail "SET-Subject"
            using  txtSubject
     end-invoke
     invoke objMail "SET-Sender"
            using  txtSender
     end-invoke
     move Email  to txtTo
     invoke objMail "SET-To"
            using  txtTo
     end-invoke
*>
*> these paths are built dynamically...replace them with your own paths to
the HTML or TEXT mail you want to send...
*>
     move 'file://C|/Inetpub/wwwroot/Scripts/WBRMailConfirms/' to
HTMLMessage
     move 'C:\Inetpub\wwwroot\Scripts\WBRMailConfirms\' to TEXTMessage

     if sending-HTML
        string
             HTMLMessage
                delimited by space
             TranID
                delimited by size
             'MailConf.htm'
                delimited by size
                   into HTMLMessage
        end-string
        invoke objMail "CreateMHTMLBody"
               using HTMLMessage
        end-invoke
     else
        string
           TEXTMessage
              delimited by space
           TranID
              delimited by size
           'MailConf.txt'
                delimited by size
                  into TEXTMessage
        end-string
        invoke objMail "AddAttachment"
               using  TEXTMessage
        end-invoke
        invoke objMail "SET-TextBody"
               using  txtTextBody
        end-invoke
     end-if
*
*  Because we are sending from a server it is necessary to configure
*  the CDO system.
*
*'==This section provides the configuration information for the remote SMTP
server.
*'==Normally you will only change the server name or IP.
*Set "sendusing"...
     move 2 to numValue
     invoke objCDOConf "SET-Fields"
            using txtConfItem1
                  numValue
     end-invoke
* Set ServerName...or IP address
     move 'localhost' to txtValue
     invoke objCDOConf "SET-Fields"
            using txtConfItem2
                  txtValue
     end-invoke
* Set Server Port (typically 25)
     move 25 to numValue
     invoke objCDOConf "SET-Fields"
            using txtConfItem3
                  numValue
     end-invoke
     invoke objCDOConf "GET-Fields"
            returning objCDOFields
     end-invoke
* Now use the "update" method to update the configuration fields
     invoke objCDOFields "Update"
     end-invoke

     invoke objMail "Send"
     end-invoke

* clean up...
     set objMail to NULL
     set objCDOConf to NULL
     set objCDOFields to NULL
     .
 ptm999.
     exit.
*------------------------------------------------------------------------

There are a number of methods available with CDO, some of which are not
shown here. Run a search on GOOGLE...

Pete.
```

###### ↳ ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL NOT using MAPI services

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-11T20:37:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307111937.23be4836@posting.google.com>`
- **References:** `<3093282.1057794745@dbforums.com> <3095033.1057842770@dbforums.com> <3f0e9fd0_3@news.athenanews.com>`

```
One (big?) Caveat - CDO is not installed by default and requires an MS
Exchange server (according to MS but I know Pete tested using an
alternate server).

Nothing further.  Go pet your pangolins.

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3f0e9fd0_3@news.athenanews.com>...
> "Ringo950" <member30412@dbforums.com> wrote in message
> news:3095033.1057842770@dbforums.com...
…[192 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL NOT using MAPI services

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-12T19:39:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0fbbdb_4@news.athenanews.com>`
- **References:** `<3093282.1057794745@dbforums.com> <3095033.1057842770@dbforums.com> <3f0e9fd0_3@news.athenanews.com> <bfdfc3e8.0307111937.23be4836@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0307111937.23be4836@posting.google.com...
> One (big?) Caveat - CDO is not installed by default and requires an MS
> Exchange server (according to MS but I know Pete tested using an
…[3 more quoted lines elided]…
>

My understanding, based on MS documents is that it is NOT installed by
default with NTServer.  It came with XP and i understand it does with Win 2K
also. I have seen conflicting statements as to the requirement for an
exchange server.

I guess the best course is simply to try it and see...

Pete.

<snipped code sample before Richard can snigger at it...<G>>
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "David Sands" <david.sands@microfocus.com>
- **Date:** 2003-07-12T09:40:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beoga8$dlv$1@hyperion.microfocus.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```
Hi R..,

I would guess permissions as well. For MAPI to work you usually needs to go
in and setup the Mail profiles using the mail applet in control panel. You
can configure to set the default profile and setup authentication so that
you are not prompted for a userid/password.

However use IUSR_machinename I don't know how you can setup the profiles
correctly so in your case it may not have a profile to use.

I would try amending the user account that IIS runs the CGI under to be one
that you know MAPI is working correctly from.

You can do this by amending the anonymous access account under Directory
Security tab on the Virtual Directory properties.

Rgds
David.


"Ringo950" <member30412@dbforums.com> wrote in message
news:3093282.1057794745@dbforums.com...
>
> Hi,
…[45 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-16T00:48:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3114994.1058316530@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com> <beoga8$dlv$1@hyperion.microfocus.com>`

```

Originally posted by David Sands 
> Hi R..,
>
…[72 more quoted lines elided]…
>     

Hi David,

I have configured the following on the server:

1 - A generic Email Account is set up and configured for Outlook(I
actually can manually send mail under that ID), the login is
automatic(password already saved)
2 - Same user name is defined as an authorized user on the server with
previlages like the "admininstrator".
3 - IIS_USER for the CGI-BIN is up as the same user that has been
defined to outlook.

I am assuming that everyone who accesses the CGI-BIN on the server will
automatically receive the same id as the outlook id. So at this point I
was hoping that I could connect to the session. But still no luck.

Maybe it is not permissions afterall. I don't know!

Any ideas?

thanks

R...
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-07-12T12:58:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uBTPa.41081$OZ2.7256@rwcrnsc54>`
- **References:** `<3093282.1057794745@dbforums.com>`

```
Ringo,
Don't know if this helps but I generate this vb script with a cobol program
and and then do a system call to run the script. The program makes  from 1
to 700 emails and just launches the scripts.
These lines are just working storage items that I modify.

Dim ToAddress
Dim FromAddress
Dim MessageSubject
Dim MessageBody
Dim MessageAttachment
Dim ol, ns, newMail
ToAddress = "BOB@email.com"
MessageSubject = "Special Announcement"
MessageBody = "Here are your leads for  07-08-2003"
MessageAttachment = "Y:\filder\folder\somefile.txt"
Set ol = WScript.CreateObject("Outlook.Application")
Set ns = ol.getNamespace("MAPI")
Set newMail = ol.CreateItem(olMailItem)
newMail.Subject = MessageSubject
newMail.Body = MessageBody & vbCrLf
newMail.RecipIents.Add(ToAddress)
newMail.Attachments.Add(MessageAttachment)
newMail.Send

Enjoy Bob fixit4you@attbi.com


"Ringo950" <member30412@dbforums.com> wrote in message
news:3093282.1057794745@dbforums.com...
>
> Hi,
…[45 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-13T17:23:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3105349.1058116998@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Not trying to offend, but I couldn't help the Fujitsu .NET COBOL
solution for sending an email:

 IDENTIFICATION DIVISION.
 PROGRAM-ID. EMAIL2.
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 REPOSITORY.
     CLASS SmtpMail AS "System.Web.Mail.SmtpMail".
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 PROCEDURE DIVISION.
     Invoke SmtpMail "Send" Using "hhinman@awebdomain.com"
                           "hhinman@hinmanconsulting.com"
                           "This is from COBOL - Test"
                           "This is a test Email from a COBOL program".

....that's it. Sends an email just fine. Why should it be any more
complicated? And any or all of the 4 literal strings may be data items
as well....
<grin>
-Howard
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "JC" <Kaos_Theory99@hotmail.com>
- **Date:** 2003-07-13T17:34:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bes56q$b15$1@sparta.btinternet.com>`
- **References:** `<3093282.1057794745@dbforums.com> <3105349.1058116998@dbforums.com>`

```
hhinman <member30421@dbforums.com> wrote in message
news:3105349.1058116998@dbforums.com...
>
> Not trying to offend, but I couldn't help the Fujitsu .NET COBOL
…[21 more quoted lines elided]…
>
Now try that in Fujitsu Net Cobol v 7

:-))
```

###### ↳ ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2003-07-14T04:13:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t5qQa.50495$sY2.25427@rwcrnsc51.ops.asp.att.net>`
- **References:** `<3093282.1057794745@dbforums.com> <3105349.1058116998@dbforums.com> <bes56q$b15$1@sparta.btinternet.com>`

```
"JC" <Kaos_Theory99@hotmail.com> wrote:
> Now try that in Fujitsu Net Cobol v 7
>
> :-))

...and then try moving it back to the .NET compiler...

Gary.
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-14T21:27:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3109534.1058218070@dbforums.com>`
- **References:** `<3105349.1058116998@dbforums.com>`

```

Originally posted by hhinman 
> Not trying to offend, but I couldn't help the Fujitsu .NET COBOL
> solution for sending an email:
…[20 more quoted lines elided]…
> -Howard 
Howard,
I am curious, do you need a licence to access System.Web.Mail.SmtpMail?
If yes, what product or products this is tied to? I assume you need an
entry in the registry before you could call this class.
I tried your code but because I don't have the System.Web.Mail.SmtpMail
defined anywhere in my environment, it didn't work.
Maybe you could give me some hints as to how this code workd.

thanks

R....
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-14T15:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3108120.1058197681@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Thanks everyone for the wonderful suggestions.

Pete, thanks for your code change suggestions. I tried it works on my
local NetExpress IDE 4.0 , but not on the server.

I truly believe it is a security issue, but I will try all the
suggestions I got from everybody and will keep you posted.

The idea about the VB code is an excellent idea too. I even thought of
creating a class for sending mail using JAVA and then calling it from
COBOL.  Similar to calling the VB, as it was suggested.

Let me experiment, and wiil let you all know.......

Thanks again for all the suggestions....

R...............
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-15T05:06:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3110832.1058245591@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Ringo,
   The SmtpMAIL class is what is being used (INVOKED/CALLed) in my
   example. It is part of the .NET framework, which can be obtained from
   Windows Update (actually called ?".NET Framework") and has no charges
   associated with it that I am aware of. This is one of the beauties of
   the .NET architecture. There are approxmately 5000 classes and API's
   provided in the .NET framework, most (all?) of which are accessible
   from COBOL. Microsoft is  moving to make the .NET framework part of
   Future Windows distributions as well.
Thanks,
-Howard
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-15T05:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3110834.1058246482@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Ringo,
   Just noticed I didn't answer the second partof your question. The
   example I posted requires that you have Visual Studio .NET (version
   7 basically) installed along with the .NET framework, and the
   Fujitsu NetCOBOL for .NET compiler installed. You can download a 30
   Day usage NetCOBOL for .NET compiler from www.netcobol.com. But
   you'll need to have the .NET Framework and Visual Studio .NET
   installed first. I've been told you can obtain a 60 or 90 day usage
   version of Visual Studio .NET from the Microsoft web site,but I jst
   had a quick look and couldn't find such. You can obtain what you
   need by purchasing a standard edition of Visual Basic .NET (which
   comes with the Framework and Visual Studio .NET) for around $99 as I
   understand. Please note that the current production Fujitsu NetCOBOL
   for .NET compiler is version 1.1 which works with Visual Studio .NET
   version 7 (actually this was the first version of Visual Studio
   .NET, but because the previous non-.NET version of Visual Studio was
   version 6, Microsoft chose to call it version 7). Microsoft have
   recently released a newer version of Visual Studio .NET called VS
   .NET 2003. If you want to work with it, I believe you will need a
   newer Fujitsu NetCOBOL for .NET compiler (version). read carefully
   on their web site about this....
Thanks,
-Howard
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-15T21:55:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3114420.1058306101@dbforums.com>`
- **References:** `<3110834.1058246482@dbforums.com>`

```

Originally posted by hhinman 
> Ringo,
>    Just noticed I didn't answer the second partof your question. The
…[20 more quoted lines elided]…
> -Howard 

Howard,

Thanks for the info, but fortunately or unfortunately, I am running
MicroFocus NetExpress 4.0. I have the visual studio installed on my
machine and also on the server, but  Fujitsu NetCOBOL  won't do.
thanks
R...
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-07-15T11:38:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3JRQa.58183$sY2.27456@rwcrnsc51.ops.asp.att.net>`
- **References:** `<3093282.1057794745@dbforums.com>`

```
I usually generate a vbscript  in working storage
such as the following and
then launch it with cscript using a system call.

E me if you need some help.
fixit4you@attbi.com

Dim ToAddress
Dim FromAddress
Dim MessageSubject
Dim MessageBody
Dim MessageAttachment
Dim ol, ns, newMail
ToAddress = "BOB@email.com"
MessageSubject = "msg goes here"
MessageBody = "Here are your leads for  07-08-2003"
MessageAttachment = "Y:\folder\folder\filename.ext"
Set ol = WScript.CreateObject("Outlook.Application")
Set ns = ol.getNamespace("MAPI")
Set newMail = ol.CreateItem(olMailItem)
newMail.Subject = MessageSubject
newMail.Body = MessageBody & vbCrLf
newMail.RecipIents.Add(ToAddress)
newMail.Attachments.Add(MessageAttachment)
newMail.Send

"Ringo950" <member30412@dbforums.com> wrote in message
news:3093282.1057794745@dbforums.com...
>
> Hi,
…[45 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-07-15T18:32:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0307151732.2438da53@posting.google.com>`
- **References:** `<3093282.1057794745@dbforums.com> <3JRQa.58183$sY2.27456@rwcrnsc51.ops.asp.att.net>`

```
"ShadowFox" <me@email.com> wrote in message news:<3JRQa.58183$sY2.27456@rwcrnsc51.ops.asp.att.net>...
> I usually generate a vbscript  in working storage
> such as the following and
…[23 more quoted lines elided]…
> 

Perhaps my post that follows may seek Off Topic....but here goes...

When I read the vbscript example posted above and the earlier comment
about calling VB from COBOL...I thought that the following chatter
might make a worth while post...

So...

- "IF" for some reason you ended up going with the .NET approach and 
- "IF" for some reason you wanted to run the code Server Side and 
- "IF" you opted to create a VB (VB.NET that is) component to call
from your COBOL code...

then, here's a VB.NET code snippet to get you started.

----------------------
Dim myattachment1 As System.Web.Mail.MailAttachment = New _
  System.Web.Mail.MailAttachment(Server.MapPath("Any File name"))
Dim MyEmailMessage As New System.Web.Mail.MailMessage()

With MyEmailMessage

  .To = "Some Text String"
  .From = "Some Text String"
  .Subject = "Some Text String"
  .BodyFormat = System.Web.Mail.MailFormat.Text
  .Body = "Some Text String"
  .Attachments.Add(myattachment1)

End With
System.Web.Mail.SmtpMail.Send(MyEmailMessage)
 ---------------------------

You will notice that this VB.NET code is similiar to the "COBOL"
sample that Howard posted else where in this thread - they both make
use of the .NET "SmtpMail" Class (and the SEND function). This
illustrates one of the nice things about the .NET Framework.
Regardless of which language you happen to choose (COBOL, VB.NET, C#,
J#, etc.), the .NET Framework Class library looks pretty much the
same.

- regards.
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-15T22:06:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3114422.1058306776@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Ringo,
    No problem. I posted an apology up front regarding such. Micto Focus
    is promising a .NET compiler sometime this year as I understand. If
    they do the job correctly, then the program I posted should be
    doable with similar syntax.....
Good Luck,
-Howard
```

#### ↳ Re: Sending Mail from MF/NetExpress Object COBOL using MAPI services

- **From:** Ringo950 <member30412@dbforums.com>
- **Date:** 2003-07-18T14:17:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3126402.1058537844@dbforums.com>`
- **References:** `<3093282.1057794745@dbforums.com>`

```

Hi Everybody,
I tried the suggestion made by Bob, calling a VB Script from Cobol from
the COMMAND-LINE and it worked both on my local workstation and on the
server. The only thing is that you have to have OUTLOOK open and active
when the mail is sent otherwise it will sit there until you activate
OUTLOOK. But it works for me. All the other suggestions were also great
and I mad myself a litte reference file for the future from all the
suggestions made.

Now here is the code (for your reference) that will execute a VB Script
or any other command from DOS command line:

       Identification Division.
       Program-ID. Email.
       Environment Division.
       DATA DIVISION.
       FILE SECTION.

       working-storage section.
       01  MENU-CMD.
           02 RUN-CMD         PIC X(80)       OCCURS 25.
           02 RES-CMD         PIC 99          COMP-X VALUE ZERO.
           02 FUN-CMD         PIC 99          COMP-X VALUE ZERO.
           02 PAR-CMD.
             03 NUM-CMD       PIC 99          COMP-X VALUE ZERO.
             03 DOS-CMD       PIC X(80)       VALUE SPACE.
           02 NAME-CMD0.
             03 NAME-CMD      PIC X           OCCURS 30.

       01  RunCmdRet          pic xxxx comp-5.
       88  Got-Ok             value 1.
       88  Got-Cancel         value 2.
      *>-------------------------------------------------------
       procedure division.
000038 RUNDOS    SECTION.
000039 RUN-DOS.
           MOVE "cscript c:\myscript.vbs" TO DOS-CMD.
000042     MOVE 0 TO RES-CMD NUM-CMD.
000044     MOVE 35 TO FUN-CMD.
000045     DISPLAY DOS-CMD UPON COMMAND-LINE.

000046     CALL X"91" USING RES-CMD FUN-CMD PAR-CMD.
000047     CANCEL X"91".
      *
000048     IF RES-CMD = 0,
              move 1 to RunCmdRet
           else
              move 0 to RunCmdRet
           end-if.
      *

000051 RUN-DOSZ.
000052     GOBACK.

I ran thins on MF Netexpress 4.0 and also on the server running MF
Application Server 4.0. It works both ways althought it is much slower
on the server.

R....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
