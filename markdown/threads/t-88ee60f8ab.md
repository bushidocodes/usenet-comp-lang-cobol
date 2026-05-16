[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

_8 messages · 4 participants · 2004-11_

---

### Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2004-11-24T18:58:42+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<co2ll1$lan$1@sparta.btinternet.com>`

```
Hi,

I am seeking the help of volunteers to test some software that I've
developed which facilitates distributed two-phase commit transactions,
encompassing any resource manager (e.g. SQL/Server or Oracle) controlled by
Microsoft's Distributed Transaction Coordinator in a Windows2000
environment, with any resource manager under the control of DECdtm (e.g. Rdb
(or Oracle via the XA Veneer)) in a VMS environment.

[Yes, at some stage, I hope to sell this software and make money out of it,
so unless you have a large philanthropic streak or are simply a techie who
likes to stay on top of Windows<->VMS connectivity issues, then you may wish
to look away now. But if you do choose to participate, then rest assured
that I have no interest in your personal or company details. (Just your
work-rate :-)]

What differentiates my Transaction Manager software from existing
Transaction Monitor packages that are already in the marketplace (and why
you should be interested) is that it is based on the Transaction Internet
Protocol TIP standard. (RFC 2372) For those of you who don't know, the
beauty of TIP's "Two-Pipe" strategy is it's application-pipe (or middleware)
neutrality. Whereas most XA implementations mandate homogenous Transaction
Monitor deployments (such as Tuxedo everywhere, Encina everywhere, MQSeries
everywhere, ACMSxp everywhere and so on  . . .), hotTIP from TIER3 Software
gives you complete freedom to choose the middleware product(s) that best
suite your particular application and heterogeneous network needs.

Would  you like to talk to VMS with TIER3 Sockets, COM or DCE/RPC? BEA
MessageQ, IBM MQSeries or HTML? The choice is yours and yours alone. But
once you realize that you need to encase your critical transactions within
the ACID properties of a true Heterogeneous Two-Phase Commit then you will
come to the conclusion that you need a Transaction Manager that looks a lot
like this.

Another drawback of traditional "One-Pipe" strategies is that they preclude
the run-time determination of transaction  participants. (Functionality
which may be advantageous in a wide-area or Internet based application.)

Anyway, this is what I have: -

On the Windows side, you need absolutely *NO* additional software! I'll
reply to this note with a brief description of the COM+ and DTC functions
that you would need to invoke in order to successfully push a MTS/DTC
transaction to VMS. NB: These are standard Windows APIs that are fully
documented on MSDN.

On the VMS side, I have a VMSINSTAL saveset that (all zipped up) is some
150KB that I'm happy to e-mail to you along similar lines to the VMS
hobbyists (non-commercial use) license. I'll reply to this note with an
Internet Daemon (INETd) example of code that uses my software to cede
transactional control, over an SQL insert into a Rdb database, to MTS/DTC.
It's under 500 lines long and contains all of the DCL, 3GL, SQL required to
produce a working example of a TIP-2PC capable TCP/IP auxiliary server. This
example will insert a row into the MF_PERSONNEL.Employees table on the VMS
side in co-operation with Windows2000 MTS/DTC client that is inserting a row
into the NORTHWIND.Employee table. Commit them all or roll them all back.

So, in summary, If you'd like to volunteer to put hotTIP through it's paces
then simply reply to this mail.

Regards Richard Maher

PS. The following are a few functionality restrictions with the current
version of my software that may effect your decision to participate: -

1) Transaction has to be started/mastered/coordinated by W2K MTS/DTC
2) Transactions cannot be PULLed from VMS and must be PUSHed from W2K
3) No cluster-wide recovery.
(If a txn falls over after being prepared then you have to wait for that
specific node to become contactable again even though that lovely RDM
recovery job is sitting on another node protecting the database until my
hotTIP TM tells it to commit or abort.)
4) There is currently no Alpha or Itanium version available. The Alpha port
is currently in progress but, for the time being, you'll either need a VAX
or a VAX emulator on your PC.
```

#### ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2004-11-25T18:24:20+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<co580i$fbm$1@titan.btinternet.com>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com>`

```
From my good friend Franco Cravero. What your Windows2000 coders need to
know in order to be able to "Push" a MTS/DTC transaction to VMS. : -

Distributed Transactions with Microsoft
G.F.Cravero
Dataware Systems Ltd.
www.dataware-sys.com

Many applications use transactions to demarcate sections of processing that
involve changing data that must be consistent as a whole. A transaction
ensures that either all the data changed within its scope is saved, or none
is. In other words, it is impossible for just some of the data modified in
the transaction to be saved for later retrieval. Transactions have long been
associated with databases, where transactional capabilities to handle stored
data were first found. Commands for demarcating transactions can be found in
all database languages, and Microsoft database interfaces (ActiveX Data
Objects, OLE DB, ODBC and the older DAO) all support starting and
terminating transactions against a single database.

DTC
---

To handle cases where more than one data source on several computers is
involved in the processing, even when the source is not a database,
Microsoft provides a service called the Distributed Transaction Coordinator
(DTC).  The DTC can act as either an XA-compliant resource manager or a
transaction manager. When the DTC is acting as an XA-compliant resource
manager, it allows Microsoft� SQL Server, Microsoft Message Queuing, and
other OLE Transactions-compliant resource managers to participate in
transactions controlled by X/Open DTP XA-compliant transaction processing
monitors such as Encina, TopEnd, and Tuxedo.

When the DTC is acting as an XA-compliant transaction manager, it allows
Oracle, IBM DB/2, Sybase, Informix, and other XA-compliant resource managers
to participate in transactions controlled by the DTC.

COM
---

Microsoft also provides a Compound Object Model (COM) for specifying
binary-compatible software components that can interact and be used by
multiple applications. This object model has recently been augmented with
the transactional capabilities of what was known as the Microsoft
Transaction Server and with other facilities such as those provided by
Microsoft Message Queue to give the COM+ middle tier services. A COM object
that is registered with the Component Services Explorer (a snap-in of the
Microsoft Management Console tool ) becomes a managed service that can use
amongst others declarative distributed transactional constraints. Therefore,
DTC transactions can be started and terminated automatically by COM+ rather
than having to be handled directly by the component's code.

Code Samples
------------

Microsoft Visual C++ component of the Visual Studio suite allows COM
components to be created easily via a wizard interface, generating a lot of
ATL based code for the project. Assuming that such an object has been
created, and that a new interface method has been defined, the following
code snippets can be used within that method to manipulate distributed
transactions.

First of all, the CoGetObjectContext function can be used to check whether
an object is being run within COM+, and hence whether transactions are
handled declaratively or whether the DTC needs to be contacted directly. The
following code shows how to perform this check:

#include <ComSvcs.h>
. . .
HRESULT    hr;
IObjectContextInfo  *pObjectContextInfo;

hr = CoGetObjectContext (IID_IObjectContextInfo,(void
**)&pObjectContextInfo);

if (SUCCEEDED(hr)) {
 // object being run within COM+, get transaction if any
} else {
 // object not within COM+, start a transaction
}

The HRESULT type is declared in winnt.h, and the SUCCEEDED() macro is
declared in winerror.h, which also contains a description of most error
codes. For the sake of brevity, checks for failure against the codes
returned by any of the function calls in the following code are omitted.

To get a handle to the current transaction when run within COM+ the
following code can be used:

IUnknown   *pTransUnknown;
ITransaction   *pTransaction

hr = pObjectContextInfo->GetTransaction (&pTransUnknown);
hr = pTransUnknown->QueryInterface (IID_ITransaction,(void
**)&pTransaction);

On the other hand, to start a new distributed transaction explicitly the
code is:

#include <XoleHlp.h>  // define DTCGetTransactionManager (requires
xolehlp.lib)
. . .
ITransactionDispenser   *pTransactionDispenser;
ITransaction   *pTransaction

hr = DtcGetTransactionManager(
             NULL,                      // pszHost
             NULL,                      // pszTmName
             IID_ITransactionDispenser, // ID of the interface
             0,                         // Reserved: must be null
             0,                         // Reserved: must be null
             0,                         // Reserved: must be null
             (void **)&pTransactionDispenser  // the interface
                                );

hr = g_pTransactionDispenser->BeginTransaction (
             0,                         // Must be null
             ISOLATIONLEVEL_ISOLATED,   // Isolation level
             ISOFLAG_RETAIN_DONTCARE,   // Isolation flags
             0,                         // Transaction options
             (void **)&pTransaction);   // The transaction object

Once a handle to the transaction has been obtained, a remote transaction
manager can be contacted to enlist any remote services in the transaction.
Microsoft provides support for non-DTC transaction managers that adhere to
the Transaction Internet Protocol (TIP), as follows:

ITipTransaction         *tpTipTransaction;
Char   *remoteTxUrl;

hr = pTransaction->QueryInterface (IID_ITipTransaction,(void
**)&pTipTransaction);

hr = tpTipTransaction->Push("tip://remotehost.co.uk/",&remoteTxUrl);

Local work and remote work can then be carried out within the scope of the
transaction provided that all the data sources involved support the
transaction protocol and have a resource manager that is enlisted with each
machine's transaction manager. In this case the application would send the
remoteTxUrl over to the remote application for enlisting with its own
(remote) transaction manager. Note that there is also a Pull method for
enlisting remote transaction managers and resources in a transaction, not
covered by this document.

Note that when using ADO to perform work against a local database, only COM+
transactions can be joined as ADO automatically checks for the context and
enlists the database with the transaction manager (the DTC in this case).
Transactions that are started explicitly through the DTC cannot be joined as
the underlying OLE DB interface for doing so is not surfaced by ADO.

Once all the work is complete the transaction can be terminated by either
committing or rolling back (undoing) the changes. The following code can be
used to commit a transaction explicitly:

hr = pTransaction->Commit (FALSE, XACTTC_ASYNC, 0);

For transactions under COM+ control the composite object 'votes' for the
transaction outcome as follows:

IObjectContext  *pObjectContext;

hr = CoGetObjectContext (IID_IObjectContext,(void **)&pObjectContext);
hr = pObjectContext->SetComplete();

The COM+ services will then commit or rollback the transaction according to
how all the objects involved in the transaction have voted (a COM+
transaction can be declared to span multiple compound objects).
```

#### ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2004-11-26T19:55:12+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<co81mt$8bs$1@hercules.btinternet.com>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com>`

```
Here's the DEMO code that I promised for the VMS side. It simply doesn't get
any easier than this!

Everything except the two T3$ services is *standard* VMS code.

Enjoy!

Cheers Richard Maher.

$!
$ server_user = f$getjpi(0,"username")
$ home_dir    = f$trnlnm("sys$login","lnm$job")
$ set default 'home_dir
$!
$ create demo_tip_auxs.cob
****************************************************************************
********
*
*
*              COPYRIGHT (c) TIER3 SOFTWARE LTD. ALL RIGHTS RESERVED.
*
*
*
*    THIS SOFTWARE IS FURNISHED UNDER A LICENSE AND MAY BE USED AND COPIED
ONLY    *
*    IN ACCORDANCE  WITH THE TERMS AND CONDITIONS OF SUCH LICENSE AND  WITH
THE    *
*    THE INCLUSION  OF THE ABOVE COPYRIGHT NOTICE.  THIS SOFTWARE  OR ANY
OTHER    *
*    COPIES  THEREOF MAY NOT  BE PROVIDED  OR OTHERWISE MADE AVAILABLE  TO
ANY    *
*    OTHER  PERSON.  NO  TITLE TO  AND OWNERSHIP  OF  THE  SOFTWARE  IS
HEREBY    *
*    TRANSFERRED.
*
*
*
*    THE INFORMATION  IN THIS SOFTWARE  IS SUBJECT TO CHANGE WITHOUT NOTICE
AND    *
*    SHOULD NOT BE CONSTRUED AS A COMMITMENT BY TIER3 SOFTWARE LTD.
*
*
*
****************************************************************************
********
identification division.
program-id.    demo_tip_auxs.
data division.
working-storage section.
01  out_msg                                         pointer value   external
out_msg.
01  io$_setmode                     pic s9(9)       comp    value   external
io$_setmode.
01  io$_writevblk                   pic s9(9)       comp    value   external
io$_writevblk.
01  io$_readvblk                    pic s9(9)       comp    value   external
io$_readvblk.
01  io$_deaccess                    pic s9(9)       comp    value   external
io$_deaccess.
01  ddtm$m_nowait                   pic s9(9)       comp    value   external
ddtm$m_nowait.
01  ddtm$_aborted                   pic s9(9)       comp    value   external
ddtm$_aborted.
01  ss$_abort                       pic s9(9)       comp    value   external
ss$_abort.
01  ss$_normal                      pic s9(9)       comp    value   external
ss$_normal.
01  sys_status                      pic s9(9)       comp.
*
01  reply_addr                                      pointer.
01  reply_len                       pic 9(4)        comp.
01  out_len                         pic 9(4)        comp.
01  abort_msg                       pic x(256).
01  bintim                          pic s9(11)v9(7) comp.
*
01  msg_buff.
    03  msg_type                    pic x(2).
    03                              pic x(510).
*
01  insert_employee_msg             redefines       msg_buff.
    03  employee_msg.
        05                          pic x(2).
        05  employee_detais.
            07  EmployeeId          pic 9(10).
            07  LastName            pic x(20).
            07  FirstName           pic x(10).
            07  BirthDate           pic x(23).
            07  Address.
                09  line1           pic x(30).
                09  line2           pic x(30).
            07  City                pic x(15).
            07  Region              pic x(15).
            07  PostalCode          pic x(10).
    03  tip_txn_url                 pic x(128).
*
01  comp_status.
    03                              pic x(2)                value   "22".
    03  commit_flag                 pic x(1).
*
01  inet_chan                       pic 9(4)        comp.
01  iosb.
    03  cond_val                    pic 9(4)        comp.
    03  msg_size                    pic 9(4)        comp.
    03                              pic x(4).
*
01  create_socket.
    03                              pic s9(4)       comp    value   external
ucx$c_tcp.
    03                              pic s9(4)       comp    value   external
auxs_def.
*
01  sqlcode                         pic 9(9)        comp.
01  rdb$message_vector                                      external.
    03 rdb$lu_num_arguments         pic 9(9)        comp.
    03 rdb$lu_status                pic 9(9)        comp.
    03 rdb$alu_arguments                            occurs 18 times.
        05 rdb$lu_arguments         pic 9(9)        comp.
*
01  sql_ctx.
    03                              pic 9(9)        comp    value   1.
    03                              pic 9(9)        comp    value   1.
    03                              pic 9(9)        comp    value   16.
    03  db_tid                      pic x(16).
    03                              pic 9(9)        comp.
*
01  tip_tid                         pic x(16).
01  tip_bid                         pic x(16).
*
01  dtm_iosb.
    03  dtm_iosb_status             pic 9(4)        comp.
    03                              pic x(2).
    03  reason_code                 pic 9(9)        comp.
*
01  syi_item_list.
    03  item_nodename.
        05                          pic s9(4)       comp    value   6.
        05                          pic s9(4)       comp    value   external
syi$_nodename.
        05                                          pointer value
reference       local_node.
        05                                          pointer value
reference       local_node_len.
    03                              pic s9(9)       comp.
*
01  local_node                      pic x(6).
01  local_node_len                  pic 9(4)        comp.
*
01  syi_iosb.
    03  syi_cond                    pic s9(9)       comp.
    03                              pic x(4).
*
procedure division.
kick_off section.
00.
    call "sys$getsyiw"
        using   by value        0, 0, 0
                by reference    syi_item_list, syi_iosb
                by value        0, 0
        giving  sys_status.
    if sys_status = ss$_normal move syi_cond to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    perform open_socket.
    perform read_socket.
    perform until msg_type = "99"

        evaluate  msg_type
            when    "20"            perform insert_employee_push
            when    other           display "Unknow message type: ",
msg_type
                                    call "lib$stop" using by value ss$_abort
        end-evaluate

        perform read_socket

    end-perform.

    perform close_socket.

    stop run.
*
open_socket section.
00.
    call "sys$assign"
        using   by descriptor   "sys$net:"
                by reference    inet_chan
                by value        0, 0, 0
        giving  sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    call "sys$qiow"
        using   by value        0, inet_chan, io$_setmode
                by reference    iosb
                by value        0, 0
                by reference    create_socket
                by value        0, 0, 0, 0, 0
        giving  sys_status.
    if sys_status = ss$_normal move cond_val to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
read_socket section.
00.
    call "sys$qiow"
        using   by value        0, inet_chan, io$_readvblk
                by reference    iosb
                by value        0, 0
                by reference    msg_buff
                by value        512, 0, 0, 0, 0
        giving  sys_status.
    if sys_status = ss$_normal move cond_val to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    display "Rec = *", insert_employee_msg(1:msg_size), "*".
*
write_socket section.
00.
    call "sys$qiow"
        using   by value       0, inet_chan, io$_writevblk
                by reference   iosb
                by value       0, 0, reply_addr, reply_len, 0, 0, 0, 0
        giving  sys_status.
    if sys_status = ss$_normal move cond_val to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
close_socket section.
00.
    call    "sys$qiow"
            using   by value        0, inet_chan, io$_deaccess
                    by reference    iosb
                    by value        0, 0, 0, 0, 0, 0, 0, 0
            giving  sys_status.
    if sys_status = ss$_normal move cond_val to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    call "sys$dassgn" using by value inet_chan giving sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
insert_employee_push section.
00.
    move function upper-case (BirthDate) to BirthDate.

    call "sys$bintim"
        using   by descriptor   BirthDate
                by reference    bintim
        giving  sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    call "t3$tip_url_to_tid"
        using   by descriptor   tip_txn_url of insert_employee_msg
                                (1:(msg_size - function
length(employee_msg)))
                by reference    tip_tid, tip_bid
        giving  sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.

    call "sys$start_branchw"
        using   by value        0, 0
                by reference    dtm_iosb
                by value        0, 0
                by reference    tip_tid
                by descriptor   local_node(1:local_node_len)
                by reference    tip_bid
        giving  sys_status.
    if sys_status = ss$_normal move dtm_iosb_status to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
    move tip_tid to db_tid.
    perform the_insert.
*
    set reply_addr to reference comp_status.
    move 3 to reply_len.
    perform write_socket.

    if commit_flag = "Y"
         perform commit_trans
    else perform abort_trans.
*
fini.
*
the_insert section.
00.
    call "set_trans_rw" using sqlcode, sql_ctx.
    if rdb$lu_status not = ss$_normal
        call "sys$putmsg" using rdb$message_vector
        call "lib$stop" using by value ss$_abort.

    call "insert_employee"
        using   sqlcode,
                EmployeeId(6:5),
                LastName,
                FirstName,
                Bintim,
                line1,
                line2,
                City,
                Region,
                PostalCode,
                sql_ctx.

    if rdb$lu_status not = ss$_normal
        move "N" to commit_flag
        call "sys$putmsg"
                using   by reference    rdb$message_vector
                        by value        out_msg, 0
                        by reference    inet_chan
                giving  sys_status
        if sys_status not = ss$_normal
            call "lib$stop" using by value sys_status
        end-if
    else
        move "Y" to commit_flag.
*
fini.
*
commit_trans section.
00.
    call "sys$end_branchw"
        using   by value        0, 0
                by reference    dtm_iosb
                by value        0, 0
                by reference    tip_tid, tip_bid
        giving  sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
    if dtm_iosb_status = ss$_abort
        display "Couldn't commit - " no advancing
        if reason_code not = zeros
            call "sys$getmsg"
                using   by value        reason_code
                        by reference    out_len
                        by descriptor   abort_msg
                        by value        0,0
                giving sys_status
             if sys_status not = ss$_normal
                call "lib$stop" using by value sys_status
             end-if
             display abort_msg (1:out_len)
        else
             display "and don't know why"
    else
        if dtm_iosb_status not = ss$_normal
              call "lib$stop" using by value dtm_iosb_status.
*
abort_trans section.
00.
    call "sys$abort_transw"
        using   by value        0, ddtm$m_nowait
                by reference    dtm_iosb
                by value        0, 0
                by reference    tip_tid
                by value        ddtm$_aborted
                by reference    tip_bid
        giving  sys_status.
    if sys_status = ss$_normal move dtm_iosb_status to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
end program demo_tip_auxs.
identification division.
program-id.    out_msg.
data division.
working-storage section.
01  io$_writevblk           pic 9(9)    comp    value   external
io$_writevblk.
01  ss$_normal              pic 9(9)    comp    value   external ss$_normal.
01  sys_status              pic 9(9)    comp.
*
01  iosb.
    03  cond_val            pic s9(4)   comp.
    03                      pic x(6).
*
01  reply_addr                          pointer.
01  reply_len               pic 9(4)    comp.
*
01  reply_hdr.
    03  error_id            pic xx              value   "88".
    03  error_len           pic 9(3).
*
linkage section.
*
01  msg_desc.
    03  msg_len             pic 9(4)    comp.
    03  msg_class           pic 9(4)    comp.
    03  msg_addr                        pointer.
*
01  inet_chan               pic 9(4)    comp.
*
procedure division
        using   msg_desc,
                inet_chan
        giving  ss$_normal.
00.
    move function length(reply_hdr) to reply_len.
    move msg_len to error_len.
    set reply_addr to reference reply_hdr.
    perform write_socket.

    move msg_len to reply_len.
    move msg_addr to reply_addr.
    perform write_socket.
*
fini.
    exit program.
*
write_socket.
*
    call "sys$qiow"
        using   by value       0, inet_chan, io$_writevblk
                by reference   iosb
                by value       0, 0, reply_addr, reply_len, 0, 0, 0, 0
        giving  sys_status.
    if sys_status = ss$_normal move cond_val to sys_status.
    if sys_status not = ss$_normal call "lib$stop" using by value
sys_status.
*
end program out_msg.
$!
$ cobol/lis demo_tip_auxs.cob
$!
$ create demo_tip_auxs_def.mar

            .title          DEMO_TIP_AUXS_DEF Demo example TIP external data
;+
;  The following command can be used to create a macro library INET in your
default
;  area if one does not already exist:-
;
;           $library/create/macro inet.mlb sys$library:ucx$inetdef
;
;           .library        "sys$login:inet"
;
;           $inetsymdef     GLOBAL
;           $siocdef        GLOBAL
;           $inetacpfsymdef GLOBAL
;           $inetacpsymdef  GLOBAL
;           $ineterrdef     GLOBAL
;-
            $ddtmdef        GLOBAL
            $ddtmmsgdef     GLOBAL

            ucx$c_auxs         ==       127
            ucx$c_af_inet      ==         2
            ucx$c_tcp          ==         6
            auxs_def           ==       <ucx$c_auxs * 256 + ucx$c_af_inet>

            .end

$ macro/lis demo_tip_auxs_def.mar
$!
$ create demo_tip_auxs_sql.sqlmod

module    dist_sql
language  cobol
parameter colons

declare pers alias filename mf_personnel

procedure set_trans_rw
        sqlcode;

        set transaction read write
                reserving pers.employees for shared write;

procedure insert_employee
        sqlcode,
        :employee_id            char(5),
        :last_name              char(20),
        :first_name             char(10),
        :birthday               date vms,
        :address_data_1         char(30),
        :address_data_2         char(30),
        :city                   char(15),
        :state                  char(15),
        :postal_code            char(10)
        ;

        insert into pers.employees
                (
                employee_id,
                last_name,
                first_name,
                birthday,
                address_data_1,
                address_data_2,
                city,
                state,
                postal_code,
                middle_initial,
                sex,
                status_code
                )
        values
                (
                :employee_id,
                :last_name,
                :first_name,
                :birthday,
                :address_data_1,
                :address_data_2,
                :city,
                :state,
                :postal_code,
                ' ',
                '?',
                'N'
                )
        ;
$!
$ sqlmod:==$sql$mod
$ sqlmod/lis/context=(set_trans_rw,insert_employee)/const=immed
demo_tip_auxs_sql.sqlmod/nowarning
$!
$ define/nolog lnk$library sys$library:t3$user
$ link
demo_tip_auxs,demo_tip_auxs_def,demo_tip_auxs_sql,sys$library:sql$user/lib
$!
$ create demo_tip_auxs_input.com
$ deck
$! define mf_personnel to_where_it_lives
$  run sys$login:demo_tip_auxs
$  exit
$ eod
$!
$ ucx set service tip_inetd             -
        /port           = 303           -
        /protocol       = tcp           -
        /process        = tip_auxs      -
        /user_name      = 'server_user' -
        /file           = 'home_dir'demo_tip_auxs_input
$!
$ ucx enable service tip_inetd
$!
$ exit
```

##### ↳ ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-11-26T16:00:17-05:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<QRMpd.3164$FR3.1576@fe12.lga>`
- **In-Reply-To:** `<co81mt$8bs$1@hercules.btinternet.com>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com> <co81mt$8bs$1@hercules.btinternet.com>`

```
Hi Richard,

I'm a very slow learner.  Also, I am retired for over 20 years.
As a result, I am interested in a definition of VMS code. It looked
a lot like Cobol to me. Oh, plus some jcl.

Warren Simmons

P.S. I see the use of pointer. I have heard that this is a tricky
thing to use. Will you explain as it was not clear to me why that
was true.

Warren Simmons
wsimmons5@optonline.net

Richard Maher wrote:

> Here's the DEMO code that I promised for the VMS side. It simply doesn't get
> any easier than this!
…[544 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** Erland Sommarskog <esquel@sommarskog.se>
- **Date:** 2004-11-26T22:28:13+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<Xns95ADEE7C89478Yazorman@127.0.0.1>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com> <co81mt$8bs$1@hercules.btinternet.com> <QRMpd.3164$FR3.1576@fe12.lga>`

```
Warren Simmons (wsimmons5@optonline.net) writes:
> I'm a very slow learner.  Also, I am retired for over 20 years.
> As a result, I am interested in a definition of VMS code. It looked
> a lot like Cobol to me. Oh, plus some jcl.

Indeed. Back in my younger days, I was a lot into VMS. But this was a 
new experience. Call SYS$QIOW and others from Cobol, egads!
```

###### ↳ ↳ ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

_(reply depth: 4)_

- **From:** Steve <ThisOne@Aint.valid>
- **Date:** 2004-11-27T17:01:49+13:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<co8u7d$e6j$1@lust.ihug.co.nz>`
- **In-Reply-To:** `<Xns95ADEE7C89478Yazorman@127.0.0.1>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com> <co81mt$8bs$1@hercules.btinternet.com> <QRMpd.3164$FR3.1576@fe12.lga> <Xns95ADEE7C89478Yazorman@127.0.0.1>`

```
Erland Sommarskog wrote:
> Warren Simmons (wsimmons5@optonline.net) writes:
> 
…[8 more quoted lines elided]…
> 
... it was bad enough trying to access these fortranesque structures 
from C (:

Steve
```

###### ↳ ↳ ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

_(reply depth: 4)_

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2004-11-30T20:05:43+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<coijqm$lku$1@sparta.btinternet.com>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com> <co81mt$8bs$1@hercules.btinternet.com> <QRMpd.3164$FR3.1576@fe12.lga> <Xns95ADEE7C89478Yazorman@127.0.0.1>`

```
Hi Erland,

(Firstly, thanks for replying to my earlier questions in the SQL Server
groups some time ago.)

> Indeed. Back in my younger days, I was a lot into VMS.

Well it's high-time you got back into it! With the Itanium port coming in
December and mini-merge doing what it should, all of Sweeden is asking you
to look at a Windows2000 SQL Server front end backed up by the bullet-proof
reliability of a disaster-tolerant VMS-cluster at the back-end. Add to this
the ACID properties of a hotTIP Two-Phase Commit, and your customers are
gonna start beating down your door.

All flattery aside, you're one of the most prolific and altruistic of
posters to these newsgroups so hopefully I've sparked your interest enough
to make you want to have a look at my software and put it through it's
paces. OK, You don't do VMS anymore, but I'll write whatever you want on the
server side if you'll just tee-up a VAX/VMS server (or emulator) to test it
on. Even if your interest extends no further than pushing Microsoft to push
TIP more, so that in a few months you're talking LU6.2 MVS DB2 connectivity,
then surely it's worth the investment?

Sadly, I'm starting to believe that good software is never honoured in its
own country, so give us a plug!

> But this was a new experience. Call SYS$QIOW and others from Cobol, egads!

Maybe someone can explain what exactly it was that COM invented again :-)
VMS has *always* had the Common Language Environment and the Procedure
Calling Standard. Whatever programming language you'd like to use, makes no
difference! (Admittedly alot of people in DEC/Compaq/HP (including senior
VMS engineers) would like to change this to get some sort of street-cred but
I'm sure that, in time,  they'll grow out of it.)

Cheers Richard.

"Erland Sommarskog" <esquel@sommarskog.se> wrote in message
news:Xns95ADEE7C89478Yazorman@127.0.0.1...
> Warren Simmons (wsimmons5@optonline.net) writes:
> > I'm a very slow learner.  Also, I am retired for over 20 years.
…[11 more quoted lines elided]…
> http://www.microsoft.com/sql/techinfo/productdoc/2000/books.asp
```

###### ↳ ↳ ↳ Re: Seeking Testing Volunteers W2K MTS/DTC to VMS DECdtm Distributed 2PC Transactions

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2004-11-30T18:38:21+00:00
- **Newsgroups:** comp.databases.ms-sqlserver,comp.databases.oracle.server,comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<coiemq$dpe$1@sparta.btinternet.com>`
- **References:** `<co2ll1$lan$1@sparta.btinternet.com> <co81mt$8bs$1@hercules.btinternet.com> <QRMpd.3164$FR3.1576@fe12.lga>`

```
Hi Warren,

>  Also, I am retired for over 20 years.

Congratulations! But what the hell are you doing here? I *long* to be able
to repeat your statement! (But then, like you, I'm sure I'd still keep my
hand in.)

I'm backing VMS for 20 *more* years! (But then I have to :-)

> I am interested in a definition of VMS code. It looked
> a lot like Cobol to me. Oh, plus some jcl.

I'm sure there are many definitions of "VMS code" out there. What I gave you
was DCL (DEC Command Language as oposed to Job Control Language (Can't swear
to the acronyms, but close enough)) command file that you could AT (@) that
would create the COBOL source code, MACRO external definitions, SQL Module
Language (I much prefer it to EXEC SQL blah), then compile them all and link
'em all together as well as set up the TCP/IP INETd parameters so that
anyone on a Windows2000 box could CONNECT to port 303 (referencce to Breaker
Morant if anyone remembers the movie) and share in a 2PC transaction with
Rdb.

It was about the most straight forward example that I could come up with,
but please ask away if you want more.

> P.S. I see the use of pointer. I have heard that this is a tricky
> thing to use. Will you explain as it was not clear to me why that
> was true.

Other conferences are probably better for this question, but in a nut shell
a 'pointer' is an address. I find it essential for calling certain VMS
System Services and desirable for dealing with constructs like VMS String
Descriptors.

Cheers Richard.

"Warren Simmons" <wsimmons5@optonline.net> wrote in message
news:QRMpd.3164$FR3.1576@fe12.lga...
> Hi Richard,
>
…[15 more quoted lines elided]…
> > Here's the DEMO code that I promised for the VMS side. It simply doesn't
get
> > any easier than this!
> >
…[12 more quoted lines elided]…
> >
****************************************************************************
> > ********
> > *
…[5 more quoted lines elided]…
> > *    THIS SOFTWARE IS FURNISHED UNDER A LICENSE AND MAY BE USED AND
COPIED
> > ONLY    *
> > *    IN ACCORDANCE  WITH THE TERMS AND CONDITIONS OF SUCH LICENSE AND
WITH
> > THE    *
> > *    THE INCLUSION  OF THE ABOVE COPYRIGHT NOTICE.  THIS SOFTWARE  OR
ANY
> > OTHER    *
> > *    COPIES  THEREOF MAY NOT  BE PROVIDED  OR OTHERWISE MADE AVAILABLE
TO
> > ANY    *
> > *    OTHER  PERSON.  NO  TITLE TO  AND OWNERSHIP  OF  THE  SOFTWARE  IS
…[5 more quoted lines elided]…
> > *    THE INFORMATION  IN THIS SOFTWARE  IS SUBJECT TO CHANGE WITHOUT
NOTICE
> > AND    *
> > *    SHOULD NOT BE CONSTRUED AS A COMMITMENT BY TIER3 SOFTWARE LTD.
…[3 more quoted lines elided]…
> >
****************************************************************************
> > ********
> > identification division.
…[3 more quoted lines elided]…
> > 01  out_msg                                         pointer value
external
> > out_msg.
> > 01  io$_setmode                     pic s9(9)       comp    value
external
> > io$_setmode.
> > 01  io$_writevblk                   pic s9(9)       comp    value
external
> > io$_writevblk.
> > 01  io$_readvblk                    pic s9(9)       comp    value
external
> > io$_readvblk.
> > 01  io$_deaccess                    pic s9(9)       comp    value
external
> > io$_deaccess.
> > 01  ddtm$m_nowait                   pic s9(9)       comp    value
external
> > ddtm$m_nowait.
> > 01  ddtm$_aborted                   pic s9(9)       comp    value
external
> > ddtm$_aborted.
> > 01  ss$_abort                       pic s9(9)       comp    value
external
> > ss$_abort.
> > 01  ss$_normal                      pic s9(9)       comp    value
external
> > ss$_normal.
> > 01  sys_status                      pic s9(9)       comp.
…[28 more quoted lines elided]…
> >     03                              pic x(2)                value
"22".
> >     03  commit_flag                 pic x(1).
> > *
…[7 more quoted lines elided]…
> >     03                              pic s9(4)       comp    value
external
> > ucx$c_tcp.
> >     03                              pic s9(4)       comp    value
external
> > auxs_def.
> > *
…[25 more quoted lines elided]…
> >         05                          pic s9(4)       comp    value
external
> > syi$_nodename.
> >         05                                          pointer value
…[32 more quoted lines elided]…
> >                                     call "lib$stop" using by value
ss$_abort
> >         end-evaluate
> >
…[201 more quoted lines elided]…
> > 01  ss$_normal              pic 9(9)    comp    value   external
ss$_normal.
> > 01  sys_status              pic 9(9)    comp.
> > *
…[54 more quoted lines elided]…
> >             .title          DEMO_TIP_AUXS_DEF Demo example TIP external
data
> > ;+
> > ;  The following command can be used to create a macro library INET in
your
> > default
> > ;  area if one does not already exist:-
…[17 more quoted lines elided]…
> >             auxs_def           ==       <ucx$c_auxs * 256 +
ucx$c_af_inet>
> >
> >             .end
…[68 more quoted lines elided]…
> >
demo_tip_auxs,demo_tip_auxs_def,demo_tip_auxs_sql,sys$library:sql$user/lib
> > $!
> > $ create demo_tip_auxs_input.com
…[18 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
