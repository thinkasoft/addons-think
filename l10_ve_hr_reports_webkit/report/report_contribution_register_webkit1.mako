<html>
<head>
    <style type="text/css">
        ${css}
    </style>
    <table class="basic_table" width="100%">
        <tr>
            <td width="30%">
                <div  style="float:left;">
                    ${helper.embed_image('jpeg',str(company.logo),180, auto)}
                </div>
            </td>
            <td style="text-align: left;">
                <strong style="font-size: 20;">${_('Registro de Contribucion') |entity}</strong>
            </td>
       </tr>
    </table>
</head>
<body>
	%for o in objects :
		<br/>
		<br/>
		<center><h2>Registro de Contribucion</h2></center>
		<br/>
		<br/>
		<table class="basic_table" width="100%" align="center" style="text-align:center">
			<tr>
				<td width="40%">
					<b>${_("Nombre de Contribucion")} </b>
				</td>
				<td width="30%">
					${_("Desde")}
				</td>
				<td width="30%">
					<b>${_("Hasta")} </b>
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
    				<th style="text-align:left;" width="10%">${_("Cedula")}</th>
	    			<th style="text-align:left;" width="25%">${_("Trabajador")}</th>
	    			<th style="text-align:left;" width="5%">${_("Codigo")}</th>
	    			<th style="text-align:right;" width="10%">${_("Cantidad")}</th>
	    			<th style="text-align:right;" width="10%">${_("R.P.V.H 1%")}</th>
	    			<th style="text-align:right;" width="10%">${_("FAOV PATRONAL")}</th>
	    			<th style="text-align:right;" width="15%">${_("Monto")}</th>
	    			<th style="text-align:right;" width="15%">${_("Total")}</th>
    			</tr>
    		</thead>
    		%for line in (get_payslip_lines(o)):
    	
    			<tbody >
            	<tr>
            		<td style="text-align:left; size:4;"><FONT FACE="raro, courier" SIZE=1>
	                	${line.get('payslip_employeeid')or '' |entity}</FONT>
					 </td>
	                <td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
	                	${line.get('payslip_namerelated') or '' |entity}</FONT>
					 </td>
            		<td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
            			${line['code'] or '' |entity}</FONT>
            		</td>
            		<td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>>
            			${formatLang(line['quantity']) or 0.0 |entity}</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['amount'])or 0.0 |entity}</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['amount'])or 0.0 |entity}</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['amount'])or 0.0 |entity}</FONT>
            		</td>
            		<td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
            			${formatLang(line['total'], currency_obj = o.company_id and o.company_id.currency_id)}</FONT>
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
	%endfor
</body>
</html>