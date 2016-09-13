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
                        <td style="line-height:1pt;">REPORTE INCES</td>
                   </tr>
                </table>
            </td>
        </tr>
    </table>
        <br/>
        <center><h2>Registro de Contribuciones (INCES)</h2></center>
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
                    <th style="text-align:left;">${_("Monto Devengado")}</th>
                    <th style="text-align:left;">${_("INCES 0.5")}</th>
                    <th style="text-align:right;" >${_("INCES 2%")}</th>
                    <th style="text-align:right;" >${_("Monto")}</th>
                </tr>
            </thead>
            <% amount_total = faov_total = inces_total = 0.0%>
            %for line in (get_payslip_lines(o)):
                <tbody >
                <tr>
                    <td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
                        ${line.get('payslip_employeeid') or '' |entity}</FONT>
                     </td>
                    <td style="text-align:left;"><FONT FACE="raro, courier" SIZE=1>
                        ${line['payslip_namerelated'] or '' |entity} </FONT>
                    </td>
                    <td style="text-align:center;"><FONT FACE="raro, courier" SIZE=1>
                        ${formatLang(line['amount']) or 0.0 |entity} Bs.</FONT>
                    </td>
                    <td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
                        ${formatLang(line['inces_0.5']*0.005)} Bs</FONT>
                    </td>
                    <td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
                        ${formatLang(line['faov']) or 0.0 |entity} Bs</FONT>
                    </td>
                    <td style="text-align:right;"><FONT FACE="raro, courier" SIZE=1>
                        ${formatLang(line['faov'] - line['inces_0.5']*0.005)} Bs</FONT>
                    </td>
                </tr>
                </tbody>
                <% inces_total += -line['inces_0.5']*0.005%>
                <% faov_total += line['faov']%>
                <% amount_total += line['amount']%>
            %endfor
        <thead>
                        <tr>
                                <th style="text-align:left;"></th>
                                <th style="text-align:left;"></th>
                                <th style="text-align:left;">${amount_total} Bs</th>
                                <th style="text-align:left;">${inces_total} Bs</th>
                                <th style="text-align:left;" >${faov_total} Bs</th>
                                <th style="text-align:left;" >${faov_total + inces_total} Bs</th>
                        </tr>
                </thead>
        </table>
        <% TOTAL_MOUNT = amount_total + faov_total%>
        <table class="list_table" width="30%" style="border-top:1px solid #ccc">
            <thead >
                <tr>
                    <table >
                        <tr>
                            <td style="text-align:left;border-top:0px" >Nomina Total: ${amount_total}</td>
                        </tr>
                        <tr>
                            <td style="text-align:left;border-top:0px" >Ret Patronal: ${faov_total}</td>
                        </tr>
                        <tr>
                            <td style="text-align:left;border-top:0px" >Ret Empleado: ${0.0}</td>
                        </tr>
                        <tr>
                            <td style="text-align:right;border-top:0px" >Total a pagar: ${TOTAL_MOUNT} </td>
                        </tr>
                    </table>
                </tr>
            </thead>
        </table>
        <p style="page-break-after:always"></p>
    %endfor
</body>
</html>
