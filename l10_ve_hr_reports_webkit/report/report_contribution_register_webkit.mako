<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>
	%for o in objects :
		<br/>
		<br/>
		<center><h2>PaySlip Lines by Contribution Register</h2></center>
		<br/>
		<br/>
		<table class="basic_table" width="100%" align="center" style="text-align:center">
			<tr>
				<td width="40%">
					<b>${_("Register Name")} </b>
				</td>
				<td width="30%">
					${_("Date From")}
				</td>
				<td width="30%">
					<b>${_("Date To")} </b>
				</td>
			</tr>
			<tr>
				<td>
					${o.name or '' |entity} 
				</td>
				<td>
					${formatLang(data['form']['date_from'],date=True) or ''|entity}
				</td>
				<td>
					<b>${formatLang(data['form']['date_from'],date=True) or ''|entity} </b>
				</td>
			</tr>
		</table>
		<br/><br/>
		<table class="list_table"  width="100%">
    		<thead>
    			<tr>
	    			<th style="text-align:left;">${_("PaySlip Name")}</th>
	    			<th style="text-align:left;">${_("Code")}</th>
	    			<th style="text-align:left;">${_("Name")}</th>
	    			<th style="text-align:right;">${_("Quantity/Rate")}</th>
	    			<th style="text-align:right;" >${_("Amount")}</th>
	    			<th style="text-align:right;" >${_("Total")}</th>
    			</tr>
    		</thead>
    		%for line in (get_payslip_lines(o)):
    			<tbody >
            	<tr>
	                <td style="text-align:left;">
	                	${line.get('payslip_name') or '' |entity}
					 </td>
            		<td style="text-align:left;">
            			${line['code'] or '' |entity} 
            		</td>
            		<td style="text-align:left;">
            			${line['name'] or '' |entity} 
            		</td>
            		<td>
            			${formatLang(line['quantity']) or 0.0 |entity} 
            		</td>
            		<td style="text-align:right;">
            			${formatLang(line['amount'])or 0.0 |entity} 
            		</td>
            		<td style="text-align:right;">
            			${formatLang(line['total'], currency_obj = o.company_id and o.company_id.currency_id)}
            		</td>
            	</tr>
            	</tbody>
    		%endfor
    	</table>
		<table class="list_table" width="30%" style="border-top:1px solid #ccc">
    		<thead >
    			<tr>
    				<td style="border-style:none" width="70%"></td>
    				<td style="border-top:1px solid black">
    				<table  >
    				    <tr>
    				        <td style="text-align:left;border-top:0px" ><b>${_("Total :")}</b></td>
                            <td style="text-align:right;border-top:0px" >${formatLang(sum_total(), currency_obj = o.company_id and o.company_id.currency_id) or 0.0}</td>
    				    </tr>
    				</table>
	    			</td>
    			</tr>
    		</thead>
		</table>
		<p style="page-break-after:always"></p>		
	%endfor
</body>
</html>