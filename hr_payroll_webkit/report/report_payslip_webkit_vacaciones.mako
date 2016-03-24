<html>
<head>
    <style type="text/css">
        ${css}
    </style>
    <style type="text/css">
        table.bottomBorder { 
          border-collapse: collapse; 
          }
        table.bottomBorder td, 
        table.bottomBorder th { 
          border-bottom: 1px dotted black; 
          padding:5px; 
          }
          .page-break {
                page-break-after: always;
            }
         p.saltodepagina
		    {
		    page-break-after: always;
		    }
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
                        <td style="line-height:1pt;">RECIBO DE PAGO VACACIONES</td>
                   </tr>
                </table>
            </td>
        </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
        <tr>
            <td style="border:1px solid black;" width="10%">
            <FONT FACE="raro, courier" SIZE=1>Trabajador</FONT>
            </td>
            <td style="border:1px solid black;" width="50%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.name}</b></FONT>
            </td>
            <td style="border:1px solid black;" width="10%">
                <FONT FACE="raro, courier" SIZE=1>Cargo</FONT>
            </td>
            <td style="border:1px solid black;" width="30%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.job_id.name}</b></FONT>
            </td>
        </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
        <tr>
            <td style="border:1px solid black;" width="10%">
            <FONT FACE="raro, courier" SIZE=1>Cedula No</FONT>
            </td>
            <td style="border:1px solid black;" width="50%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.identification_id}</b></FONT>
            </td>
            <td style="border:1px solid black;" width="20%">
                <FONT FACE="raro, courier" SIZE=1>Salario por Tabulador</FONT>
            </td>
            <td style="border:1px solid black;" width="20%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.contract_id.wage} Bs.</b></FONT>
            </td>
        </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
        <tr>
            <td style="border:1px solid black;" width="16%">
            <FONT FACE="raro, courier" SIZE=1>Fecha de Ingreso</FONT>
            </td>
            <td style="border:1px solid black;" width="16%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.contract_id.date_start}</b></FONT>
            </td>
            <td style="border:1px solid black;" width="16%">
                <FONT FACE="raro, courier" SIZE=1>Pago Desde</FONT>
            </td>
            <td style="border:1px solid black;" width="16%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.date_from}</b></FONT>
            </td>
            <td style="border:1px solid black;" width="16%">
                <FONT FACE="raro, courier" SIZE=1>Pago Hasta</FONT>
            </td>
            <td style="border:1px solid black;" width="20%">
                <FONT FACE="raro, courier" SIZE=1><b>${o.date_to}</b></FONT>
            </td>
        </tr>
	</table>
	<br/>
	<table width="100%" class="bottomBorder">
        <thead>
            <tr>
                <td width="5%">
                    <FONT FACE="raro, courier" SIZE=1><b>CODIGO</b></FONT>
                </td>
                <td width="35%">
                    <FONT FACE="raro, courier" SIZE=1><b>DESCRIPCION</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>CANTIDAD</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>IMPORTE</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>TOTAL</b></FONT>
                </td>
            </tr>
        </thead>
	    <tbody style="line-height:8pt;">
            %for line in (get_payslip_lines(o.line_ids)):
                %if line.code == "039" or line.code == "069" or line.code == "200":
                	<tr>
    	                <td width="5%"><b><FONT FACE="raro, courier" SIZE=1>
    	                	${line.code or ''|entity}</FONT></b>
    					 </td>
                		<td width="35%"><b><FONT FACE="raro, courier" SIZE=2>
                			${line.name or '' |entity}</FONT></b>
                		</td>
                		<td width="20%" ><b><FONT FACE="raro, courier" SIZE=1>
                			${formatLang(line.quantity) or '' |entity}</FONT></b>
                		</td>
                		<td width="20%"><b><FONT FACE="raro, courier" SIZE=1>
                			${formatLang(line.amount) or '' |entity}</FONT></b>
                		</td>
                		<td width="20%"><b><FONT FACE="raro, courier" SIZE=2>
                			${formatLang(line.total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0 |entity}</FONT></b>
                		</td>
                	</tr>
                %else:
                	<tr>
    	                <td width="5%"><FONT FACE="raro, courier" SIZE=0.5>
    	                	${line.code or ''|entity}</FONT>
    					 </td>
                		<td width="35%"><FONT FACE="raro, courier" SIZE=0.5>
                			${line.name or '' |entity}</FONT>
                		</td>
                		<td width="20%" ><FONT FACE="raro, courier" SIZE=0.5>
                			${formatLang(line.quantity) or '' |entity}</FONT>
                		</td>
                		%if line.code =="008" :
                		<td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                			</FONT>
                		</td>
                		%else :
                		<td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                			${formatLang(line.amount) or '' |entity}</FONT>
                		</td>
                		%endif
                		<td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                			${formatLang(line.total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0 |entity}</FONT>
                		</td>
                	</tr>
                %endif
    		%endfor
        </tbody>
	</table>
	</br>
	</br>
	<table width="80%" style="margin: 0 auto;">
	    <tr>
	        <td width="80%">
	            <FONT FACE="raro, courier" SIZE=1><b>Recibe Conforme: _________________________  Cedula del Trabajador: _________________________ Huella: _________________________</b></FONT>
	        </td>
	    </tr>
	</table>
	</br>
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
                        <td style="line-height:1pt;">RECIBO DE PAGO VACACIONES</td>
                   </tr>
                </table>
            </td>
        </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Trabajador</FONT>
                        </td>
                        <td style="border:1px solid black;" width="50%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.name}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                            <FONT FACE="raro, courier" SIZE=1>Cargo</FONT>
                        </td>
                        <td style="border:1px solid black;" width="30%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.job_id.name}</b></FONT>
                        </td>
                    </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Cedula No</FONT>
                        </td>
                        <td style="border:1px solid black;" width="50%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.employee_id.identification_id}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="20%">
                            <FONT FACE="raro, courier" SIZE=1>Salario por Tabulador</FONT>
                        </td>
                        <td style="border:1px solid black;" width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.contract_id.wage} Bs.</b></FONT>
                        </td>
                    </tr>
	</table>
	<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="16%">
                        <FONT FACE="raro, courier" SIZE=1>Fecha de Ingreso</FONT>
                        </td>
                        <td style="border:1px solid black;" width="16%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.contract_id.date_start}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="16%">
                            <FONT FACE="raro, courier" SIZE=1>Pago Desde</FONT>
                        </td>
                        <td style="border:1px solid black;" width="16%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.date_from}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="16%">
                            <FONT FACE="raro, courier" SIZE=1>Pago Hasta</FONT>
                        </td>
                        <td style="border:1px solid black;" width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.date_to}</b></FONT>
                        </td>
                    </tr>
	</table>
	<br/>
	<table width="100%" class="bottomBorder">
        <thead>
            <tr>
                <td width="5%">
                    <FONT FACE="raro, courier" SIZE=1><b>CODIGO</b></FONT>
                </td>
                <td width="35%">
                    <FONT FACE="raro, courier" SIZE=1><b>DESCRIPCION</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>CANTIDAD</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>IMPORTE</b></FONT>
                </td>
                <td width="20%">
                    <FONT FACE="raro, courier" SIZE=1><b>TOTAL</b></FONT>
                </td>
            </tr>
        </thead>
        <tbody style="line-height:8pt;">
            %for line in (get_payslip_lines(o.line_ids)):
                %if line.code == "039" or line.code == "069" or line.code == "200":
                    <tr>
                        <td width="5%"><b><FONT FACE="raro, courier" SIZE=1>
                            ${line.code or ''|entity}</FONT></b>
                         </td>
                        <td width="35%"><b><FONT FACE="raro, courier" SIZE=2>
                            ${line.name or '' |entity}</FONT></b>
                        </td>
                        <td width="20%" ><b><FONT FACE="raro, courier" SIZE=1>
                            ${formatLang(line.quantity) or '' |entity}</FONT></b>
                        </td>
                        <td width="20%"><b><FONT FACE="raro, courier" SIZE=1>
                            ${formatLang(line.amount) or '' |entity}</FONT></b>
                        </td>
                        <td width="20%"><b><FONT FACE="raro, courier" SIZE=2>
                            ${formatLang(line.total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0 |entity}</FONT></b>
                        </td>
                    </tr>
                %else:
                    <tr>
                        <td width="5%"><FONT FACE="raro, courier" SIZE=0.5>
                            ${line.code or ''|entity}</FONT>
                         </td>
                        <td width="35%"><FONT FACE="raro, courier" SIZE=0.5>
                            ${line.name or '' |entity}</FONT>
                        </td>
                        <td width="20%" ><FONT FACE="raro, courier" SIZE=0.5>
                            ${formatLang(line.quantity) or '' |entity}</FONT>
                        </td>
                        %if line.code =="008" :
                        <td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                            </FONT>
                        </td>
                        %else :
                        <td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                            ${formatLang(line.amount) or '' |entity}</FONT>
                        </td>
                        %endif
                        <td width="20%"><FONT FACE="raro, courier" SIZE=0.5>
                            ${formatLang(line.total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0 |entity}</FONT>
                        </td>
                    </tr>
                %endif
            %endfor
        </tbody>            
	</table>
	</br>
	</br>
	<table width="80%" style="margin: 0 auto;">
	    <tr>
	        <td width="80%">
	            <FONT FACE="raro, courier" SIZE=1><b>Recibe Conforme: _________________________  Cedula del Trabajador: _________________________ Huella: _________________________</b></FONT>
	        </td>
	    </tr>
	</table>
    <div class="page-break">&nbsp;</div>
	%endfor	

</body>
</html>