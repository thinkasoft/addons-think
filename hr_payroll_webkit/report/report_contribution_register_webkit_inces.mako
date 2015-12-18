<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>
	%for o in objects :

	<table width="100%">
        <tr>
            <td width="30%" style="text-align:left;" style="BOLD">
                <table width="100%">
                    <tr>
                        <td rowspan="0">
                        ${helper.embed_image('jpeg',str(o.company_id.logo),120, 80)}
                        </td>
                        <td style="line-height:8pt;">
                            <FONT FACE="raro, courier" SIZE=5>${o.company_id.partner_id.name}</FONT><br/>
                            <FONT FACE="raro, courier" SIZE=1>R.I.F: ${o.company_id.partner_id.vat[2:]}</FONT><br/>
                            <FONT FACE="raro, courier" SIZE=1>${o.company_id.street}
                            ${o.company_id.street2}</FONT><br/>
                            <FONT FACE="raro, courier" SIZE=1>${o.company_id.city}
                            ${o.company_id.state_id.name}
                            ${o.company_id.country_id.name}</FONT>
                    
                        </td>
                        <td style="line-height:1pt;">REPORTE FAOV</td>
                   </tr>
                </table>
            </td>
        </tr>
	</table>
		<br/>
		<center><h2>Registro de Contribuciones (FAOV)</h2></center>
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
					<b>${formatLang(data['form']['date_to'],date=True) or ''|entity} </b>
				</td>
			</tr>
		</table>
		<br/><br/>
		<table class="list_table"  width="100%">
    		<thead>
    			<tr>
	    			<th style="text-align:left;">${_("Vat")}</th>
	    			<th style="text-align:left;">${_("Employee")}</th>
	    			<th style="text-align:left;">${_("Salario Asignado")}</th>
	    			<th style="text-align:center;">${_("R.P.V.H")}</th>
	    			<th style="text-align:right;" >${_("FAOV")}</th>
	    			<th style="text-align:right;" >${_("Monto")}</th>
    			</tr>
    		</thead>
    		<% total = 0.0%>
    		%for line in (get_payslip_lines(o)):
    			<tbody >
            	<tr>
	                <td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
	                	${line.get('payslip_employeeid') or '' |entity}</FONT>
					 </td>
            		<td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
            			${line['payslip_name'] or '' |entity} </FONT>
            		</td>
            		<td style="text-align:center;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['amount']) or 0.0 |entity} Bs.</FONT>
            		</td>
            		<td><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['rpvh']) or 0.0 |entity} Bs.</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['faov']) or 0.0 |entity} Bs.</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['mount'], currency_obj = o.company_id and o.company_id.currency_id) or 0.0} Bs.</FONT>
            		</td>
            	</tr>
            	</tbody>
            	<% total += line['mount']%>
    		%endfor
    	</table>

		<table class="list_table" width="100%" style="border-top:1px solid #ccc">
    		<thead >
    			<tr>
    				<td style="border-style:none" width="70%"></td>
    				<td style="border-top:1px solid black">
    				 <td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1><b>
	                	${_("Total :")} ${formatLang(total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0} </b></FONT>
	    			</td>
    			</tr>
    		</thead>
		</table>
		<p style="page-break-after:always"></p>		
	%endfor
</body>
</html>