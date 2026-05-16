[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic SQL

_28 messages · 9 participants · 2005-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Dynamic SQL

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-18T12:21:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```
Hi,

I'm struggling with a dynamic sql execution within my cobol program.  I
keep getting these errors:

DSNH084I W     DSNHLEXC LINE 831 COL 22  UNACCEPTABLE SQL STATEMENT
DSNH084I W     DSNHLEXC LINE 833 COL 22  UNACCEPTABLE SQL STATEMENT
DSNH080I E     DSNHSM3D LINE 2049 COL 37  STRING VARIABLE "WS-SQL" IS
NOT "VARCHAR" TYPE
PREPARE SQLSTMT FROM:WS-SQL

Here is what I have:

....
WORKING-STORAGE SECTION.

01   WS-SQL      PIC X(400) VALUE SPACES.

     EXEC SQL BEGIN DECLARE SECTION END-EXEC.
01  SQLSTMT      PIC X(400).
     EXEC SQL END DECLARE SECTION END-EXEC.

.....
PROCEDURE DIVISION.
.....
    IF condition1
       create sql statement1 and STRING to ws-sql
    ELSE
       create sql statement2 and STRING to ws-sql
    END-IF.

    MOVE WS-SQL TO SQLSTMT.

    EXEC SQL
       PREPARE SQLSTMT FROM :WS-SQL
    END-EXEC.

    EXEC SQL
       DECLARE ATTCUR CURSOR FOR SQLSTMT
    END-EXEC.

    EXEC SQL
       OPEN ATTCUR
    END-EXEC.

Could someone shed me some lights?

Thanks,
Kathie
```

#### ↳ Re: Dynamic SQL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-18T12:48:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113853704.687917.241440@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```
> 01   WS-SQL      PIC X(400) VALUE SPACES.

>     EXEC SQL BEGIN DECLARE SECTION END-EXEC.
> 01  SQLSTMT      PIC X(400).
>     EXEC SQL END DECLARE SECTION END-EXEC.
>  ...

>    MOVE WS-SQL TO SQLSTMT.
>    EXEC SQL
>       PREPARE SQLSTMT FROM :WS-SQL
>    END-EXEC.

If it has a colon in front it needs to be within the BEGIN DECLARE
(though some don't need this). The target of the prepare should not be
defined.  I suspect that you meant to have:

       PREPARE execstmt FROM :SQLSTMT
       ..
       DECLARE attcur CURSOR FOR execstmt




         PREPARE
```

##### ↳ ↳ Re: Dynamic SQL

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-18T13:05:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113854727.325809.123450@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1113853704.687917.241440@o13g2000cwo.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <1113853704.687917.241440@o13g2000cwo.googlegroups.com>`

```
Hi,

I tried the code you suggested and got error " STRING VARIABLE
"execstmt" IS NOT "VARCHAR" TYPE.

If I don't use the PREPARE statement, the program compiles ok but I got
SQLCODE -514 when I run it.

Please help!!!!

Thanks,
Kathie
```

###### ↳ ↳ ↳ Re: Dynamic SQL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-18T14:08:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113857397.680855.118240@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1113854727.325809.123450@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <1113853704.687917.241440@o13g2000cwo.googlegroups.com> <1113854727.325809.123450@l41g2000cwc.googlegroups.com>`

```
You should tell us the compiler, preprocessor and system that you are
using, and versions, as all may influence what may be done.
```

#### ↳ Re: Dynamic SQL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-18T21:13:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqV8e.317613$za2.50898@news.easynews.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```
the E-level message says that "WS-SQL" is not of "type" VARCHAR.

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnaph13/2.4.3.7

for how to define a VARCHAR host variable (in COBOL - at least for IBM 
mainframes and DB2), e.g.

   01 VAR-NAME.
      49 VAR-LEN PIC S9(4) USAGE BINARY.
      49 VAR-TEXT PIC X(n).

Use of level "49" is required (as I recall) and you MUST have a binary field 
followed by the actual "data" portion.
```

##### ↳ ↳ (VMS Rdb COBOL example) Was: Re: Dynamic SQL

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2005-04-19T09:43:21+00:00
- **Newsgroups:** comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<d42jrm$o7l$1@hercules.btinternet.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com>`

```
Hi,

Didn't see the original post, but I was just looking at the following code
on an old floppy of mine as I was cleaning up my office after holidays.

FWIW

Cheers Richard Maher

PS. Obviously replace all the "#" with a space and sorry about the wrapping.
(After 20 odd years in I.T. I am simply incapable of stopping that from
happening. Or can't be arsed to find out how :-)

PPS. If you want to run multiple table scrambles in parralel then you'll
have to change the BATCH UPDATE transaction. But the performance is so
blisteringly fast I honestly wouldn't bother.

identification#division.
program-id.####dyn_test.
*
data#division.
working-storage#section.
01##rdb$_stream_eof#####################pic#9(9)########comp####value###exte
rnal####rdb$_stream_eof.
01##lib$_strtru#########################pic#9(9)########comp####value###exte
rnal####lib$_strtru.
01##ss$_abort###########################pic#9(9)########comp####value###exte
rnal####ss$_abort.
01##ss$_normal##########################pic#9(9)########comp####value###exte
rnal####ss$_normal.
01##sys_status##########################pic#9(9)########comp.
*
01##sqlcode#############################pic#9(9)########comp.
01##rdb$message_vector##########################################external.
####03#rdb$lu_num_arguments#############pic#9(9)########comp.
####03#rdb$lu_status####################pic#9(9)########comp.
####03#rdb$alu_arguments################################occurs#18#times.
########05#rdb$lu_arguments#############pic#9(9)########comp.
*
01##col_name############################pic#x(39).
01##col_count###########################pic#9(9)########comp.
*
01##cmd_string##########################pic#x(10000).
*
01##set_trans_statement.
####03##################################pic#x(39)###############value###"set
#transaction#batch#update#reserving".
####03##trans_table#####################pic#x(39).
####03##################################pic#x(21)###############value###"#fo
r#exclusive#write;".
*
01##select_statement.
####03##################################pic#x(7)################value###"sel
ect".
####03##select_list.
######04##select_array##################################occurs##256#times.
########05##select_col##################pic#x(30).
########05##select_delim################pic#x(1).
####03##################################pic#x(5)################value###"fro
m".
####03##select_table####################pic#x(39).
####03##################################pic#x(1)################value###";".
*
01##update_id###########################pic#9(9)########comp.
01##update_statement.
####03##################################pic#x(7)################value###"upd
ate".
####03##update_table####################pic#x(39).
####03##################################pic#x(5)################value###"#se
t".
####03##update_list.
######04##update_array##################################occurs##256#times.
########05##update_col##################pic#x(30).
########05##update_delim################pic#x(5).
####03##################################pic#x(22)###############value###"#wh
ere#current#of#sel;".
*
01##col_prefix_table.
####03##col_elem########################################occurs##256#times.
########05##col_prefix##################pic#x(39).
########05##col_prefix_len##############pic#9(4)########comp.
*
01##col_pfx#############################pic#x(39).
*
01##sqlda_char##########################pic#9(4)########comp####value###453.
01##sqlda_integer#######################pic#9(4)########comp####value###497.
01##sqlda_quadword######################pic#9(4)########comp####value###505.
*
01##sqlda_list.
####03##sqldaid#########################pic#x(8)################value###"SQL
DA".
####03##sqldabc#########################pic#9(9)########comp.
####03##sqln############################pic#9(4)########comp####value###256.
####03##sqld############################pic#9(4)########comp.
####03##sqlname_rec#####################################occurs##0#to####256#
########################################################depending#on#sqln#of
#sqlda_list.
########05##sqltype#####################pic#9(4)########comp.
########05##sqllen######################pic#9(4)########comp.
########05##sqldata#####################################pointer.
########05##sqlind######################################pointer.
########05##sqlname.
############07##name_len################pic#9(4)########comp.
############07##name_str################pic#x(30).
*
01##sqlda_update.
####03##sqldaid#########################pic#x(8)################value###"SQL
DA".
####03##sqldabc#########################pic#9(9)########comp.
####03##sqln############################pic#9(4)########comp####value###256.
####03##sqld############################pic#9(4)########comp.
####03##sqlname_rec#####################################occurs##0#to####256#
########################################################depending#on#sqln#of
#sqlda_update.
########05##sqltype#####################pic#9(4)########comp.
########05##sqllen######################pic#9(4)########comp.
########05##sqldata#####################################pointer.
########05##sqlind######################################pointer.
########05##sqlname.
############07##name_len################pic#9(4)########comp.
############07##name_str################pic#x(30).
*
01##col_desc.
####03##col_len#########################pic#9(9)########comp.
####03##col_addr########################################pointer.
*
01##scramble_eof########################pic#x(1).
01##unique_char#########################pic#x(65535).
01##unique_integer######################pic#s9(9)#######comp.
01##unique_quadword#####################pic#s9(18)######comp.
01##scramble_field######################pic#x(65535).
01##scramble_desc.
####03##scramble_desc_len###############pic#9(9)########comp.
####03##################################################pointer#value###refe
rence#scramble_field.
*
01##unique_id_string####################pic#x(65535).
01##unique_id_integer###################################redefines
####unique_id_string####################pic#-9(9).
01##unique_id_quadword##################################redefines
####unique_id_string####################pic#-9(18).
01##unique_id_len#######################pic#9(4)########comp.
*
01##null_indicators.
####03##null_ind########################pic#s9(4)#######comp
########################################################occurs##256#times.
*
01##task_id#############################pic#x(39)###############value###"TES
T_TABLE".
01##relation_prefix#####################pic#x(39).
01##relation_prefix_len#################pic#9(4)########comp.
01##unique_id###########################pic#x(39).
01##vm_bytes############################pic#9(9)########comp.
*
procedure#division.
kick_off#section.
00.
####perform#get_setup.

####move#set_trans_statement#to#cmd_string.
####call#"sql_execute_immediate"#using#sqlcode,#cmd_string.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"sql_prepare_select"
########using###sqlcode,
################select_statement.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"sql_describe_select"
########using###sqlcode,
################sqlda_list.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####display#"Number#of#columns#in#select#list#is#",#sqld#of#sqlda_list#with#
conversion.

####perform#varying#sqln#of#sqlda_list#from#1#by#1#until#sqln#of#sqlda_list#
=#sqld#of#sqlda_list

########if#sqltype#of#sqlda_list#(sqln#of#sqlda_list)#not#=#sqlda_char
############display#"Can#only#handle#CHAR#datatypes#",#sqltype#of#sqlda_list
#(sqln#of#sqlda_list)#with#conversion
############call#"lib$stop"#using#by#value#ss$_abort
########end-if

########move#sqllen#of#sqlda_list#(sqln#of#sqlda_list)#to#vm_bytes
########call#"lib$get_vm"#using#vm_bytes,#sqldata#of#sqlda_list#(sqln#of#sql
da_list)#giving#sys_status
########if#sys_status#not#=#ss$_normal#
############call#"lib$stop"#using#by#value#sys_status
########end-if

########set#sqlind#of#sqlda_list(sqln#of#sqlda_list)#to#reference#null_ind(s
qln#of#sqlda_list)

####end-perform.

####evaluate####sqltype#of#sqlda_list(sqln#of#sqlda_list)
########when####sqlda_char######set#sqldata#of#sqlda_list(sqln#of#sqlda_list
)#to#reference#unique_char
########when####sqlda_integer###set#sqldata#of#sqlda_list(sqln#of#sqlda_list
)#to#reference#unique_integer
########when####sqlda_quadword##set#sqldata#of#sqlda_list(sqln#of#sqlda_list
)#to#reference#unique_quadword
########when####other###########call#"lib$stop"#using#by#value#sys_status
####end-evaluate.

####move#sqlda_list#to#sqlda_update.
####subtract#1#from#####sqln#of#sqlda_update,
########################sqld#of#sqlda_update.

####call#"sql_prepare_update"
########using###sqlcode,
################update_id,
################update_statement.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"sql_open_sel"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####move#"N"#to#scramble_eof
####call#"sql_fetch_sel"#using#sqlcode,#sqlda_list.
####evaluate####rdb$lu_status
########when####rdb$_stream_eof#move#"Y"#to#scramble_eof
########when####ss$_normal######continue
########when####other###########call#"sys$putmsg"#using#rdb$message_vector#g
iving#sys_status
################################call#"lib$stop"#using#by#value#ss$_abort
####end-evaluate.

####perform#scramble_data#until#scramble_eof#=#"Y".

####call#"sql_close_sel"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"sql_commit_db"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.
*
*
fini.
####stop#run.
*
get_setup#section.
00.
####call#"sql_task_tran"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####move#task_id#to#####trans_table,
########################select_table,
########################update_table.

####call#"sql_get_scramble"
########using###sqlcode,
################relation_prefix,
################unique_id,
################task_id.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"str$trim"
########using###by#descriptor###relation_prefix,#relation_prefix
################by#reference####relation_prefix_len
########giving##sys_status.
####if#sys_status#not#=#ss$_normal#call#"lib$stop"#using#by#value#sys_status
.

####call#"sql_open_enigma"#
########using###sqlcode,
################task_id.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####move#spaces#to######select_list,
########################update_list.
####move#zeros#to#col_count.

####call#"sql_fetch_enigma"
########using###sqlcode,
################col_name,
################col_pfx.

####perform#until#rdb$lu_status#not#=#ss$_normal

########add#1#to#col_count

########move#col_pfx##to########col_prefix(col_count)
########move#col_name#to########select_col(col_count)
################################update_col(col_count)

########call#"str$trim"
############using##by#descriptor#col_prefix(col_count),#col_prefix(col_count
)
###################by#reference##col_prefix_len(col_count)
############giving#sys_status
########if#sys_status#not#=#ss$_normal#
############call#"lib$stop"#using#by#value#sys_status
########end-if

########move#","#to#select_delim(col_count)

########move#"#=#?,"#to#update_delim(col_count)

########call#"sql_fetch_enigma"
############using#######sqlcode,
########################col_name,
########################col_pfx
####end-perform.
####if#rdb$lu_status#not#=#rdb$_stream_eof
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####if#col_count#=#zeros
########display#"No#columns#to#update#for#",#task_id
########call#"lib$stop"#using#by#value#ss$_abort.

####move#space#to#update_delim(col_count)(5:1).

####add#1#to#col_count.
####move#unique_id#to#select_col(col_count).

####call#"sql_close_enigma"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.

####call#"sql_commit_db"#using#sqlcode.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.
*
scramble_data#section.
00.

####move#spaces#to#unique_id_string.
####evaluate####sqltype#of#sqlda_list(sqln#of#sqlda_list)
########when####sqlda_char######call#"str$trim"
####################################using#######by#descriptor###unique_char,
#unique_id_string
################################################by#reference####unique_id_le
n
####################################giving######sys_status
################################if#sys_status#not#=#ss$_normal#
####################################call#"lib$stop"#using#by#value#sys_statu
s
################################end-if
########when####sqlda_integer###move#unique_integer#to#unique_id_integer
################################move#10#to#unique_id_len
########when####sqlda_quadword##move#unique_quadword#to#unique_id_quadword
################################move#19#to#unique_id_len
####end-evaluate.

####perform#varying#sqln#of#sqlda_update#from#1#by#1#until#sqln#of#sqlda_upd
ate#>#sqld#of#sqlda_update

########move#spaces#to#scramble_field

########string##relation_prefix(1:relation_prefix_len),
################col_prefix(sqln#of#sqlda_update)(1:col_prefix_len(sqln#of#sq
lda_update)),
################unique_id_string(1:unique_id_len)
################delimited#by#size
########into####scramble_field

########add#####relation_prefix_len,
################col_prefix_len(sqln#of#sqlda_update),
################unique_id_len
########giving##scramble_desc_len

########move#sqllen##of#sqlda_update#(sqln#of#sqlda_update)#to#col_len
########move#sqldata#of#sqlda_update#(sqln#of#sqlda_update)#to#col_addr

########call#"lib$scopy_dxdx"#using#scramble_desc,#col_desc#giving#sys_statu
s
########if#sys_status#not#=#ss$_normal#and#lib$_strtru
############call#"lib$stop"#using#by#value#sys_status
########end-if

####end-perform.
####move#sqld#of#sqlda_update#to#sqln#of#sqlda_update.

####call#"sql_execute_stmt"
########using###sqlcode,
################sqlda_update,
################update_id.
####if#rdb$lu_status#not#=#ss$_normal
########call#"sys$putmsg"#using#rdb$message_vector#giving#sys_status
########call#"lib$stop"#using#by#value#ss$_abort.
*
fini.
####call#"sql_fetch_sel"#using#sqlcode,#sqlda_list.
####evaluate####rdb$lu_status
########when####rdb$_stream_eof#move#"Y"#to#scramble_eof
########when####ss$_normal######continue
########when####other###########call#"sys$putmsg"#using#rdb$message_vector#g
iving#sys_status
################################call#"lib$stop"#using#by#value#ss$_abort
####end-evaluate.
*
end#program#dyn_test.

module####dyn_sql
language##cobol
authorization#scram_db
parameter#colons

declare#external#scram_db#alias#filename#scram_db

declare#sel#cursor#for#sel_stmt

declare#enigma#cursor#for
########select#
################a.field_name,
################a.field_prefix
########from
################scramble_relation_fields#a
########where
################a.relation_name#=#:task_id

procedure#sql_task_tran
########sqlcode
########;

########set#transaction#read#write#reserving
################scramble_relation###############for#shared#write,
################scramble_relation_fields########for#shared#read;

procedure#sql_get_scramble
########sqlcode,
########:relation_prefix########char(39),
########:unique_id##############char(39),
########:task_id################char(39)
########;

########select
################a.relation_prefix,
################a.unique_id
########into
################:relation_prefix,
################:unique_id
########from#
################scramble_relation#a
########where
################a.relation_name#=#:task_id
########;

procedure#sql_open_enigma
########sqlcode,
########:task_id################char(39)
########;

########open#enigma;

procedure#sql_fetch_enigma
########sqlcode,
########:field_name#############char(39),
########:field_prefix###########char(39)
########;

########fetch
################enigma
########into
################:field_name,
################:field_prefix
########;

procedure#sql_close_enigma
########sqlcode
########;

########close#enigma;

procedure#sql_prepare_select
########sqlcode,
########:stmt###################char(7988)
########;

########prepare#sel_stmt#from#:stmt;

procedure#sql_describe_select
########sqlca,
########sqlda;

########describe#sel_stmt#select#list#into#sqlda;

procedure#sql_open_sel
########sqlca;

########open#sel;

procedure#sql_fetch_sel
########sqlca,
########sqlda;

########fetch#sel#using#descriptor#sqlda;

procedure#sql_close_sel
########sqlca;

########close#sel;

procedure#sql_release_stmt
########sqlca;

########release#sel_stmt;#

procedure#sql_prepare_update
########sqlcode,
########:update_id##############integer,
########:stmt###################char(9033)
########;

########prepare#:update_id#from#:stmt;

procedure#sql_execute_stmt
########sqlcode,
########:sqlda##################sqlda,
########:dyn_stmt_id############integer
########;

########execute#:dyn_stmt_id#using#descriptor#:sqlda;

procedure#sql_commit_db
########sqlcode;

########commit;

procedure#sql_execute_immediate
########sqlcode,
########:cmd_string#############char(10000)
########;

########execute#immediate#:cmd_string;


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:aqV8e.317613$za2.50898@news.easynews.com...
> the E-level message says that "WS-SQL" is not of "type" VARCHAR.
>
> See:
>
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnaph13/2.4.3.7
>
> for how to define a VARCHAR host variable (in COBOL - at least for IBM
…[6 more quoted lines elided]…
> Use of level "49" is required (as I recall) and you MUST have a binary
field
> followed by the actual "data" portion.
>
…[56 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Dynamic SQL

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-19T07:18:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113920296.443129.34830@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com>`

```
Hi,

I'm very new with mainframe and appreciate all the help I can get.  I'm
using IBM MVS COBOL with DB2.  The precompiler is DB2 SQL Version 7 Rel
1.0.  I tried the following:

In Working-storage section,

     01  WS-SQL                    PIC X(400) VALUE SPACES.

     01  WS-SQL-STR.
         49  WS-SQL-LEN    PIC 9(4) USAGE BINARY.
         49  WS-SQL-TXT    PIC X(400).

In Procedure division,

     ... A SELECT stmt is being strung into WS-SQL bases on a
conditional stmt
     ...
         MOVE WS-SQL TO WS-SQL-TXT.

         EXEC SQL
            PREPARE STRSQL FROM :WS-SQL-STR
         END-EXEC.

         EXEC SQL
            DECLARE ATTCUR CURSOR FOR STRSQL
         END-EXEC.

         EXEC SQL
            OPEN ATTCUR
         END-EXEC.

This is the error I got when compiling:

     DSNH312I E     DSNHSMUD LINE 2051 COL 36  UNDEFINED OR UNUSABLE
HOST VARIABLE "WS-SQL-STR"
     DSNH080I E     DSNHSM3D LINE 2051 COL 36  STRING VARIABLE
"WS-SQL-STR" IS NOT "VARCHAR" TYPE

I also tried

     EXEC SQL
       PREPARE STRSQL FROM :WS-SQL-TXT
     END-EXEC.

And got:
     DSNH080I E     DSNHSM3D LINE 2051 COL 36  STRING VARIABLE
"WS-SQL-TXT" IS NOT "VARCHAR" TYPE

I read somewhere that I need to declare the host variable WS-SQL-STR
within a
EXEC SQL BEGIN DECLARE SECTION END-EXEC and
EXEC SQL END DECLARE SECTION END-EXEC.

but it gave me an error

DSNH084I W     DSNHLEXC LINE 831 COL 22  UNACCEPTABLE SQL STATEMENT
DSNH084I W     DSNHLEXC LINE 835 COL 22  UNACCEPTABLE SQL STATEMENT

Thanks,
Kathie
```

###### ↳ ↳ ↳ Re: Dynamic SQL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-19T17:05:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zTa9e.380023$za2.60987@news.easynews.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com>`

```
Don't you need to have WS-SQL-STR within in an EXEC SQL DECLARE?
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 4)_

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-19T10:32:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113931974.416961.318430@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<zTa9e.380023$za2.60987@news.easynews.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <zTa9e.380023$za2.60987@news.easynews.com>`

```
Hi Bill,

I did and got an error UNACCEPTABLE SQL STATEMENT.  Did I have the
correct syntax?

Thanks,
Kathie


William M. Klein wrote:
> Don't you need to have WS-SQL-STR within in an EXEC SQL DECLARE?
>
…[7 more quoted lines elided]…
> > I'm very new with mainframe and appreciate all the help I can get.
I'm
> > using IBM MVS COBOL with DB2.  The precompiler is DB2 SQL Version 7
Rel
> > 1.0.  I tried the following:
> >
…[44 more quoted lines elided]…
> > I read somewhere that I need to declare the host variable
WS-SQL-STR
> > within a
> > EXEC SQL BEGIN DECLARE SECTION END-EXEC and
…[9 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-19T13:14:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113941667.556320.322590@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1113931974.416961.318430@z14g2000cwz.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <zTa9e.380023$za2.60987@news.easynews.com> <1113931974.416961.318430@z14g2000cwz.googlegroups.com>`

```
> I did and got an error UNACCEPTABLE SQL STATEMENT.  Did I have the
> correct syntax?

You probably need to set the length of the actual SQL statement text in
WS-SQL-Len.  That is the point of having a VARCHAR defined with a
length and  a text sub-fields.

Without setting the length then it will have some random number there
that may treat your SQL as truncated or as very long and including what
follows in memory.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-19T13:28:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113942539.737646.257990@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1113920296.443129.34830@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com>`

```
> This is the error I got when compiling:

>     DSNH312I E     DSNHSMUD LINE 2051 COL 36  UNDEFINED OR UNUSABLE
> HOST VARIABLE "WS-SQL-STR"
>     DSNH080I E     DSNHSM3D LINE 2051 COL 36  STRING VARIABLE
> "WS-SQL-STR" IS NOT "VARCHAR" TYPE

Host variables need to be inside a DECLARE section. (some don't need
this).

>     EXEC SQL
>       PREPARE STRSQL FROM :WS-SQL-TXT
>     END-EXEC.

> And got:
>     DSNH080I E     DSNHSM3D LINE 2051 COL 36  STRING VARIABLE
> "WS-SQL-TXT" IS NOT "VARCHAR" TYPE

A VARCHAR is a 'variable length character field' when the length is
specified by an integer at the start of the field followed by the text,
as in WS-SQL-STR.

> I read somewhere that I need to declare the host variable WS-SQL-STR
> within a
> EXEC SQL BEGIN DECLARE SECTION END-EXEC and
> EXEC SQL END DECLARE SECTION END-EXEC.

Host variables should be inside a DECLARE section (some preprocessers
don't need this).

> but it gave me an error
> DSNH084I W     DSNHLEXC LINE 831 COL 22  UNACCEPTABLE SQL STATEMENT
> DSNH084I W     DSNHLEXC LINE

> 835 COL 22  UNACCEPTABLE SQL STATEMENT

The other errors referred to lines 2051, this is line 831, ie 20 pages
away.  There may be many reasons for the disparity:

It is a completely unrelated problem somewhere else in the program.
It is a different program.
The last is a run-time error when the program executes and the line
numbers refer to something else, the preprocessed source perhaps.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 4)_

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-19T14:34:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113946460.571232.43660@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1113942539.737646.257990@z14g2000cwz.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com>`

```
Hi all,

Just FYI, the program I'm working on was created in 1992 by someone
else.  It has the total of 2730 lines(!!!)

I included the DECLARE STATEMENT (as Chris suggested) and it doesn't
yell on these lines.

Could someone tell me the exact syntax of how to declare the WS-SQL-STR
in the SQL DECLARE section?  I tried the

EXEC SQL BEGIN DECLARE SECTION END-EXEC  and
EXEC SQL END DECLARE SECTION END-EXEC.

then
EXEC SQL DECLARE WS-SQL-STR VARIABLE END-EXEC.

but both gave errors.  

Please help!!!

Thanks,
Kathie
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-19T22:39:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jiua615i6po91gbpq01tj6qv3joul6n9p1@4ax.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com>`

```
On 19 Apr 2005 14:34:20 -0700, "kathie" <kktbva@yahoo.com> wrote:

>Hi all,
>
…[15 more quoted lines elided]…
>but both gave errors.  
One example for Oracle. Syntax is the same for all DB's.

-----------


*****************************************************************
      * Sample Program 1:  Simple Query
*
      *
*
      * This program logs on to ORACLE, prompts the user for an
*
      * employee number, queries the database for the employee's
*
      * name, salary, and commission, then displays the result.
*
      * The program terminates when the user enters a 0.
*

*****************************************************************


       IDENTIFICATION DIVISION.
       PROGRAM-ID. QUERY.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

           EXEC SQL BEGIN DECLARE SECTION END-EXEC.
       01  USERNAME          PIC X(10) VARYING.
       01  PASSWD            PIC X(10) VARYING.
       01  EMP-REC-VARS.
           05  EMP-NAME      PIC X(10) VARYING.
           05  EMP-NUMBER    PIC S9(4) COMP VALUE ZERO.
           05  SALARY        PIC S9(5)V99 COMP-3 VALUE ZERO.
           05  COMMISSION    PIC S9(5)V99 COMP-3 VALUE ZERO.
           05  COMM-IND      PIC S9(4) COMP VALUE ZERO.
           EXEC SQL END DECLARE SECTION END-EXEC.

           EXEC SQL INCLUDE SQLCA END-EXEC.

       01  DISPLAY-VARIABLES.
           05  D-EMP-NAME    PIC X(10).
           05  D-SALARY      PIC Z(4)9.99.
           05  D-COMMISSION  PIC Z(4)9.99.
           05  D-EMP-NUMBER  PIC 9(4).

       01 D-TOTAL-QUERIED   PIC 9(4) VALUE ZERO.
        
       PROCEDURE DIVISION.
       BEGIN-PGM.
           EXEC SQL WHENEVER SQLERROR
              DO PERFORM SQL-ERROR END-EXEC.

           PERFORM LOGON.

       QUERY-LOOP.
           DISPLAY " ".
           DISPLAY "ENTER EMP NUMBER (0 TO QUIT): "
               WITH NO ADVANCING.

           ACCEPT D-EMP-NUMBER FROM CONSOLE.

           MOVE D-EMP-NUMBER TO EMP-NUMBER.
           IF (EMP-NUMBER = 0)
               PERFORM SIGN-OFF.
           MOVE SPACES TO EMP-NAME-ARR.
           EXEC SQL WHENEVER NOT FOUND GOTO NO-EMP END-EXEC.
           EXEC SQL SELECT ENAME, SAL, COMM
               INTO :EMP-NAME, :SALARY, :COMMISSION:COMM-IND
               FROM EMP
               WHERE EMPNO = :EMP-NUMBER
           END-EXEC.
           PERFORM DISPLAY-INFO.
           ADD 1 TO D-TOTAL-QUERIED.
           GO TO QUERY-LOOP.

       NO-EMP.
           DISPLAY "NOT A VALID EMPLOYEE NUMBER - TRY AGAIN.".
           GO TO QUERY-LOOP.

       LOGON.
           MOVE "SCOTT@orcl" TO USERNAME-ARR.
           MOVE 21 TO USERNAME-LEN.
           MOVE "TIGER" TO PASSWD-ARR.
           MOVE 5 TO PASSWD-LEN.
           EXEC SQL
               CONNECT :USERNAME IDENTIFIED BY :PASSWD
           END-EXEC.
           DISPLAY " ".
           DISPLAY "CONNECTED TO ORACLE AS USER: ", USERNAME-ARR.
        
       DISPLAY-INFO.
           DISPLAY " ".
           DISPLAY "EMPLOYEE    SALARY    COMMISSION".
           DISPLAY "--------    ------    ----------". 
           MOVE EMP-NAME-ARR TO D-EMP-NAME.
           MOVE SALARY TO D-SALARY.
           IF COMM-IND = -1
               DISPLAY D-EMP-NAME, D-SALARY, "          NULL"
           ELSE
               MOVE COMMISSION TO D-COMMISSION
               DISPLAY D-EMP-NAME, D-SALARY, "      ", D-COMMISSION
           END-IF.

       SIGN-OFF.
           DISPLAY " ".
           DISPLAY "TOTAL NUMBER QUERIED WAS ",
               D-TOTAL-QUERIED, ".".
           DISPLAY " ".
           DISPLAY "HAVE A GOOD DAY.".
           DISPLAY " ".
           EXEC SQL COMMIT WORK RELEASE END-EXEC.
           STOP RUN.

       SQL-ERROR.
           EXEC SQL WHENEVER SQLERROR CONTINUE END-EXEC.
           DISPLAY " ".
           DISPLAY "ORACLE ERROR DETECTED:".
           DISPLAY " ".
           DISPLAY SQLERRMC.
           EXEC SQL ROLLBACK WORK RELEASE END-EXEC.
           STOP RUN.

-----------


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-19T14:58:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113947882.820062.119050@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1113946460.571232.43660@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com>`

```
> Just FYI, the program I'm working on was created in 1992 by someone
> else.  It has the total of 2730 lines(!!!)

Did the original already have any SQL in it ?

> Could someone tell me the exact syntax of how to declare the
WS-SQL-STR
> in the SQL DECLARE section?  I tried the

> EXEC SQL BEGIN DECLARE SECTION END-EXEC  and
> EXEC SQL END DECLARE SECTION END-EXEC

These look correct, but different systems (I don't use DB2) may have
different requirements.

If you don't have a manual that you can look up then you can get pdfs
at:

http://www-306.ibm.com/software/data/db2/udb/support/manualsv8.html

for example:

ftp://ftp.software.ibm.com/ps/products/db2/info/vr8/pdf/letter/db2a1e80.pdf

Or for a html overview:

https://aurora.vcu.edu/db2help/db2s0/frame3.htm#sqls0606

  WORKING-STORAGE SECTION.
        EXEC SQL BEGIN DECLARE SECTION  END-EXEC.
  01  HV-SMINT              PIC S9(4)       COMP-4.
  01  HV-VCHAR24.
      49 HV-VCHAR24-LENGTH  PIC S9(4)       COMP-4.
      49 HV-VCHAR24-VALUE   PIC X(24).
  01  HV-DEC72              PIC S9(5)V9(2)  COMP-3.
  01 HV-BLOB-50K            USAGE SQL TYPE IS BLOB(50K).
        EXEC SQL END DECLARE SECTION  END-EXEC.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 5)_

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-20T07:14:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114006477.287484.88900@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1113946460.571232.43660@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com>`

```
Kathie,

You can go one of two ways with the declare statement:

EXEC SQL BEGIN DECLARE SECTION END-EXEC.

01  WS-SQL-STR         PIC  X(1024).
EXEC SQL VAR WS-SQL-STR IS CHARF END-EXEC.

EXEC SQL END DECLARE SECTION END-EXEC.

or

EXEC SQL BEGIN DECLARE SECTION END-EXEC.

01  WS-SQL-STR         PIC  X(1024)  VARYING.

EXEC SQL END DECLARE SECTION END-EXEC.

I use the first scenario, because it is more "friendly" to COBOL move
statements. If you go with the second scenario, you will need to move
the actual syntax to WS-SQL-STR-ARR and the length of that syntax to
WS-SQL-STR-LEN (these fields are created for you by the Oracle
precompiler).
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 6)_

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-20T11:00:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114020006.803948.327670@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1114006477.287484.88900@f14g2000cwb.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com> <1114006477.287484.88900@f14g2000cwb.googlegroups.com>`

```
Hi all,

I changed the data type of WS-SQL-LEN to PIC S9(4) COMP-5.  It compiled
OK, with warnings of "UNACCEPTABLE SQL STATEMENT" on the BEGIN DECLARE
and END DECLARE lines.  I still don't understand why.  All I know is
that I typed the commands exactly like it is listed in the SQL
reference.  When I ran the program, I got SQL error -104.  The SQLERRMC
has ' ,, FOR WITH FETCH QUERYNO OPTIMIZE ' and SQLSTATE is 42601.  I
did some research and found error -104 means syntax error in the sql
statement was detected at 'token' and the suggestion is to look at the
token list.

I have no clue where to get the "token" list.  I know that the SQL
statement runs fine if it's not a dynamic SQL

I really appreciate all the help I can get.  

Thanks,
Kathie
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 7)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-04-20T19:37:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rby9e.7622$716.7119@tornado.tampabay.rr.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com> <1114006477.287484.88900@f14g2000cwb.googlegroups.com> <1114020006.803948.327670@l41g2000cwc.googlegroups.com>`

```
 Kathie,

Token is a generic term for "a thing" in your SQL.

If you read further in the manual:
As an aid to the programmer, a partial list of valid tokens is provided in 
the SQLERRM field of the SQLCA as "<token-list>". This list assumes the 
statement is correct to that point.

In your SQLERRM you have:

' ,, FOR WITH FETCH QUERYNO OPTIMIZE '

This tells me that somewhere way at the bottom of your "built" query you 
have a delimiter or something missing because it's expecting another <token> 
and the ones listed are the last ones to be found in any query (as opposed 
to say FROM WHERE )...I'm just guessing, but based on your other posts....as 
you build your string, make sure the length is always correct for what you 
are putting in there.....

I recommend outputting the statement, and the length (or debugging) to see 
what DB2 sees.

JCE

"kathie" <kktbva@yahoo.com> wrote in message 
news:1114020006.803948.327670@l41g2000cwc.googlegroups.com...
> Hi all,
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 7)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2005-04-20T18:01:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jA9e.11105$Jg5.759237@news20.bellglobal.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com> <1114006477.287484.88900@f14g2000cwb.googlegroups.com> <1114020006.803948.327670@l41g2000cwc.googlegroups.com>`

```

Kathie, are you using STDSQL(YES) on your precompile?



"kathie" <kktbva@yahoo.com> wrote in message 
news:1114020006.803948.327670@l41g2000cwc.googlegroups.com...
> Hi all,
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 8)_

- **From:** "kathie" <kktbva@yahoo.com>
- **Date:** 2005-04-22T08:03:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114182198.676436.142630@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9jA9e.11105$Jg5.759237@news20.bellglobal.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com> <1114006477.287484.88900@f14g2000cwb.googlegroups.com> <1114020006.803948.327670@l41g2000cwc.googlegroups.com> <9jA9e.11105$Jg5.759237@news20.bellglobal.com>`

```
Hello,

No, STSQL(NO) is the setting.  Should it be set to YES?

Anyway, since I have a deadline to meet and this dynamic cursor is
still a problem, I went ahead (with hesitant!) and split it into 2
static cursors.  I would much prefer to use the dynamic one.  When I
have some free time later on, I will definitely revisit this issue and
keep you all posted.

Thanks for all your help.

Kathie



Don Leahy wrote:
> Kathie, are you using STDSQL(YES) on your precompile?
> 
>
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-20T11:13:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114020814.927377.206950@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1114006477.287484.88900@f14g2000cwb.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <1113942539.737646.257990@z14g2000cwz.googlegroups.com> <1113946460.571232.43660@l41g2000cwc.googlegroups.com> <1114006477.287484.88900@f14g2000cwb.googlegroups.com>`

```

kathie:>  I'm using IBM MVS COBOL with DB2.  The precompiler is DB2 SQL
Version 7 Rel 1.0.

Chris:> (these fields are created for you by the Oracle precompiler).

Unfortunately not all precompilers are equal. In some matters it is
necessary to actually look at the manual and see what it does.  It is
also necessary to look at what options are used because, for example,
Oracle can be used without the BEGIN DECLARE at all when certain
options are set.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2005-04-19T22:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d44010$fhs$1@nwrdmz03.dmz.ncs.ea.ibs-infra.bt.com>`
- **In-Reply-To:** `<1113920296.443129.34830@l41g2000cwc.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com>`

```
> In Working-storage section,
> 
…[15 more quoted lines elided]…
>          END-EXEC.

<snip>

Hi Kathie,

The naming convention is normally something as follows :

01 varchar1.
    49 varchar1-len        pic 9(4) comp-5.
    49 varchar1-data       pic x(200).
01 Longvarchar1.
    49 Longvarchar1-len    pic 9(4) comp.
    49 Longvarchar1-data   pic x(30000).

Note that the length and data elements have suffixes from the group 
name. Hence, in your example, you should probably code :

       01  WS-SQL-STR.
           49  WS-SQL-STR-LEN    PIC 9(4) USAGE BINARY.
           49  WS-SQL-STR-TXT    PIC X(400).

You *may* also need to set the Length element to the correct size prior 
to the PREPARE statement,

SimonT.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-04-20T06:08:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%lm9e.9892$5f.6978@tornado.tampabay.rr.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com> <d44010$fhs$1@nwrdmz03.dmz.ncs.ea.ibs-infra.bt.com>`

```
"Wiggy" <wignomore@btopenworld.com> wrote in message 
news:d44010$fhs$1@nwrdmz03.dmz.ncs.ea.ibs-infra.bt.com...
> Hi Kathie,
>
…[7 more quoted lines elided]…
>    49 Longvarchar1-data   pic x(30000).

I have yet to find any (pre)compiler that uses a naming convention - and if 
I did I would not use it.
I call things what I want to call things - with rules :-)

> Note that the length and data elements have suffixes from the group name. 
> Hence, in your example, you should probably code :
…[6 more quoted lines elided]…
> the PREPARE statement,

This is the precompiler - it's not *that* smart - but then you're not the 
only one to think  it is :-).

JCE
```

###### ↳ ↳ ↳ Re: Dynamic SQL - Your ANSWER

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-04-20T06:04:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xhm9e.7486$716.1277@tornado.tampabay.rr.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <aqV8e.317613$za2.50898@news.easynews.com> <1113920296.443129.34830@l41g2000cwc.googlegroups.com>`

```

"kathie" <kktbva@yahoo.com> wrote in message 
news:1113920296.443129.34830@l41g2000cwc.googlegroups.com...
> Hi,
>
…[10 more quoted lines elided]…
>         49  WS-SQL-TXT    PIC X(400).


49  WS-SQL-LEN    PIC S9(4) USAGE BINARY.

If all else fails COPY the manual.

Finally I have an on topic post....woo hoo

JCE
```

#### ↳ Re: Dynamic SQL

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-19T13:27:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113942430.042533.175310@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```
I think you may be missing the declaration of the statement. Not sure
if this is just an Oracle specific issue though. You may try this,
where sql-statement is defined in the DECLARE section of working
storage:

           EXEC SQL
               DECLARE csrstmnt STATEMENT
           END-EXEC.

           EXEC SQL
               PREPARE csrstmnt FROM :sql-statement
           END-EXEC.

           EXEC SQL
               DECLARE mycsr CURSOR FOR csrstmnt
           END-EXEC.

           EXEC SQL
               OPEN mycsr
           END-EXEC.


I hope that helps.

Chris
```

#### ↳ Re: Dynamic SQL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-20T19:28:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jl7d61lje0k9ni7ue5vf5a64i6gt313lul@4ax.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```

Top posting only.

Kathie,


Please create a small program with ONLY the minimum requirements to
run the SQL statement and do the open of the cursor and the fetch.

Then compile it, and try it.

Then post the FULL source (of both the original source AND the output
of the pre-compiler!!!!) here along with the error messages.

Also give the FULL sql statement used.

Regards


Frederico

On 18 Apr 2005 12:21:44 -0700, "kathie" <kktbva@yahoo.com> wrote:

>Hi,
>
…[46 more quoted lines elided]…
>Kathie
```

#### ↳ Re: Dynamic SQL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-20T19:36:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d58d615i3hon9jbmaho7bum66avh2196j5@4ax.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com>`

```
On 18 Apr 2005 12:21:44 -0700, "kathie" <kktbva@yahoo.com> wrote:

>Hi,
>
…[42 more quoted lines elided]…
>
further to my other posts the following is an example from DB2 for
windows.


*************************************************************************
      **
      ** Source File Name = dynamic.sqb
      **
      ** Licensed Materials - Property of IBM
      **
      ** (C) COPYRIGHT International Business Machines Corp. 1995,
2000 
      ** All Rights Reserved.
      **
      ** US Government Users Restricted Rights - Use, duplication or
      ** disclosure restricted by GSA ADP Schedule Contract with IBM
Corp.
      **
      **
      ** PURPOSE: This sample program demonstrates the use of a
CURSOR.
      **          The CURSOR is processed using dynamic SQL.  This
program
      **          will list all the entries in the system table
      **          sysibm.systables that do not have the value "STAFF"
in
      **          the "name" column.
      **
      ** For more information about these samples see the README file.
      **
      ** For more information on programming in COBOL, see the:
      **    -  "Programming in COBOL" section of the Application
Development Guide.
      **
      ** For more information on building COBOL applications, see the:
      **    - "Building COBOL Applications" section of the Application
Building Guide.
      **
      ** For more information on the SQL language see the SQL
Reference.
      **

*************************************************************************

       Identification Division.
       Program-ID. "dynamic".

       Data Division.
       Working-Storage Section.

           copy "sqlenv.cbl".
           copy "sql.cbl".
           copy "sqlca.cbl".

           EXEC SQL BEGIN DECLARE SECTION END-EXEC.
       01 table-name      pic x(20).
       01 st              pic x(80).
1
       01 parm-var        pic x(18).
       01 userid            pic x(8).
       01 passwd.
         49 passwd-length   pic s9(4) comp-5 value 0.
         49 passwd-name     pic x(18).
           EXEC SQL END DECLARE SECTION END-EXEC.

       77 errloc          pic x(80).

       Procedure Division.
       Main Section.
           display "Sample COBOL program: DYNAMIC".

           display "Enter your user id (default none): " 
                with no advancing.
           accept userid.

           if userid = spaces
             EXEC SQL CONNECT TO sample END-EXEC
           else
             display "Enter your password : " with no advancing
             accept passwd-name.

      * Passwords in a CONNECT statement must be entered in a VARCHAR
format
      * with the length of the input string.
           inspect passwd-name tallying passwd-length for characters
              before initial " ".

           EXEC SQL CONNECT TO sample USER :userid USING :passwd
               END-EXEC.

           move "SELECT TABNAME FROM SYSCAT.TABLES
      -       " ORDER BY 1
      -       " WHERE TABNAME <> ?" to st.
           EXEC SQL PREPARE s1 FROM :st END-EXEC.
           EXEC SQL DECLARE c1 CURSOR FOR s1 END-EXEC.

           move "STAFF" to parm-var.
           EXEC SQL OPEN c1 USING :parm-var END-EXEC.
           perform Fetch-Loop thru End-Fetch-Loop
              until SQLCODE not equal 0.

           EXEC SQL CLOSE c1 END-EXEC.
           EXEC SQL COMMIT END-EXEC.

           EXEC SQL CONNECT RESET END-EXEC.

       End-Main.
           go to End-Prog.

       Fetch-Loop Section.
           EXEC SQL FETCH c1 INTO :table-name END-EXEC.
           if SQLCODE not equal 0
              go to End-Fetch-Loop.
           display "TABLE = ", table-name.
       End-Fetch-Loop. exit.

       End-Prog.
           Goback.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Dynamic SQL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-20T13:50:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114030207.557919.209910@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d58d615i3hon9jbmaho7bum66avh2196j5@4ax.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <d58d615i3hon9jbmaho7bum66avh2196j5@4ax.com>`

```
>      01 st              pic x(80).
>
>       move "SELECT TABNAME FROM SYSCAT.TABLES
>      -       " ORDER BY 1
>      -       " WHERE TABNAME <> ?" to st.

That MOVE seems to be more than 80 characters.

Interesting that it doesn't complain about ST not being a VARCHAR,
kathie is using version 7, what is yours ?

Note that Fujitsu doesn't need the PREPARE to be from a VARCHAR either,
but some may well do.
```

###### ↳ ↳ ↳ Re: Dynamic SQL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-20T22:08:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fmgd615lsm1724r1b53n802dt778curbbf@4ax.com>`
- **References:** `<1113852104.333988.160920@f14g2000cwb.googlegroups.com> <d58d615i3hon9jbmaho7bum66avh2196j5@4ax.com> <1114030207.557919.209910@g14g2000cwa.googlegroups.com>`

```
On 20 Apr 2005 13:50:07 -0700, "Richard" <riplin@Azonic.co.nz> wrote:

>>      01 st              pic x(80).
>>
…[10 more quoted lines elided]…
>but some may well do.

Hum. You are correct. This example is supplied by IBM, so maybe there
is an option on Visual Age that is removing the spaces after TABLES,
so the string ends up being
"SELECT TABNAME FROM SYSCAT.TABLES ORDER BY 1 WHERE TABNAME <> ?"

And I am using RM/COBOL.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
