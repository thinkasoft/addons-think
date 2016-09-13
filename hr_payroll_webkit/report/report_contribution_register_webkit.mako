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
                <strong style="font-size: 20;">LISTA DE FAOV MENSUAL</strong>
            </td>
        </tr>
    </table>
</head>
<body>
    %for o in objects :
        <center><h2>Registro de Contribuciones</h2></center>
        <table class="basic_table" width="100%" align="center" style="text-align:center">
            <tr>
                <td width="40%"> <b>${_("Register Name")} </b> </td>
                <td width="30%"> ${_("Date From")} </td>
                <td width="30%"> <b>${_("Date To")} </b> </td>
            </tr>
            <tr>
                <td> ${o.name or '' |entity}  </td>
                <td> ${formatLang(data['form']['date_from'],date=True) or ''|entity} </td>
                <td> <b>${formatLang(data['form']['date_to'],date=True) or ''|entity} </b> </td>
            </tr>
        </table>
        <br/><br/>
        <table class="list_table"  width="100%">
            <thead>
                <tr>
                <th style="text-align:left; font-size:80%;">${_("CEDULA")}</th>
                <th style="text-align:left;font-size:80%;">${_("EMPLEADO")}</th>
                <th style="text-align:right;font-size:80%;">${_("DEVENGADO")}</th>
                <th style="text-align:right;font-size:80%;">${_("1%")}</th>
                <th style="text-align:right;font-size:80%;" >${_("2%")}</th>
                <th style="text-align:right;font-size:80%;" >${_("Monto")}</th>
                </tr>
            </thead>
            <% total = 0.0%>
            %for line in (get_payslip_lines(o)):
                <tbody>
                    <tr>
                        <td style="text-align:left; font-size:80%;">
                            ${line.get('payslip_employeeid') or '' |entity}
                        </td>
                        <td style="text-align:left; font-size:80%;">
                            ${line['payslip_name'] or '' |entity}
                        </td>
                        <td style="text-align:right; font-size:80%;">
                            ${formatLang(line['amount']) or 0.0 |entity} Bs
                        </td>
                        <td style="text-align:right;font-size:80%;">
                            ${formatLang(line['rpvh']) or 0.0 |entity} Bs
                        </td>
                        <td style="text-align:right; font-size:80%;">
                            ${formatLang(line['faov']) or 0.0 |entity} Bs
                        </td>
                        <td style="text-align:right; font-size:80%;">
                            ${formatLang(line['mount'], currency_obj = o.company_id and o.company_id.currency_id) or 0.0}
                        </td>
                    </tr>
                </tbody>
                <% total += line['mount']%>
            %endfor
            <tbody>
                <tr>
                    <td style="text-align:left; font-size:80%;"></td>
                    <td style="text-align:left; font-size:80%;"></td>
                    <td style="text-align:right; font-size:80%;"></td>
                    <td style="text-align:right;font-size:80%;"></td>
                    <th style="text-align:right; font-size:80%;">TOTAL A PAGAR</th>
                    <th style="text-align:right; font-size:90%;">${formatLang(total, currency_obj = o.company_id and o.company_id.currency_id) or 0.0}</th>
                </tr>
            </tbody>
        </table>
        <p style="page-break-after:always"></p>
    %endfor
</body>
</html>
