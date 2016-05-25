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
    <% setLang(user.lang) %>
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
                                <FONT FACE="raro, courier" SIZE=1>${o.company_id.street} ${o.company_id.street2}</FONT><br/>
                                <FONT FACE="raro, courier" SIZE=1>${o.company_id.city} ${o.company_id.state_id.name} ${o.company_id.country_id.name}</FONT>
                            </td>
                            <td style="line-height:1pt;">${_("PAYSLIP")}</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        <table width="100%" style="border:1px solid black;border-collapse:collapse;">
            <tr>
                <td style="border:1px solid black;" width="10%">
                    <FONT FACE="raro, courier" SIZE=1>${_("Partner")}</FONT>
                </td>
                <td style="border:1px solid black;" width="50%">
                    <FONT FACE="raro, courier" SIZE=1><b>${o.name}</b></FONT>
                </td>
            </tr>
        </table>
        <table width="100%" class="bottomBorder">
            <thead>
                <tr>
                    <td>
                        <FONT FACE="raro, courier" SIZE=1><b>${_("Suppliers")}</b></FONT>
                    </td>
                    <td>
                        <FONT FACE="raro, courier" SIZE=1><b>${_("Product")}</b></FONT>
                    </td>
                    <td>
                        <FONT FACE="raro, courier" SIZE=1><b>${_("Quantity")}</b></FONT>
                    </td>
                    <td>
                        <FONT FACE="raro, courier" SIZE=1><b>${_("Price Unit")}</b></FONT>
                    </td>
                    <td>
                        <FONT FACE="raro, courier" SIZE=1><b>${_("Amount")}</b></FONT>
                    </td>
                </tr>
            </thead>
            <%total = iva_total = sub_total = 0%>
            <tbody >
                %for line in (get_supplier_invoice_line(start_days, stop_days, o)):
                    <%sub_total += line['sub_total']%>
                    <%iva_total += line['sub_total']*line['iva_amount']%>
                    <%total += line['sub_total'] + (line['sub_total']*line['iva_amount'])%>
                    <tr>
                        <td style="text-align:left;"> ${line['name_supplier']} </td>
                        <td style="text-align:left;"> ${line['name_product']} </td>
                        <td style="text-align:left;"> ${line['quantity']} </td>
                        <td style="text-align:left;"> ${formatLang(line['price_unit'])} </td>
                        <td style="text-align:left;"> ${formatLang(line['sub_total'])} </td>
                        <!-- TAX Amount * (1 + TAX.amount ) 
                        <td style="text-align:left;"> ${formatLang(line['sub_total']*(1 + line['iva_amount']))} </td>-->
                    </tr>
                %endfor
            </tbody>
            <table width="100%" class="bottomBorder" style="line-height:8pt;">
                <tr> <td style="text-align:right;" /> ${_("Subtotal")}: ${formatLang(sub_total)}</td> </tr>
                <tr> <td style="text-align:right;" /> ${_("Tax")}: ${formatLang(iva_total)} </td> </tr>
                <tr> <td style="text-align:right;" /> ${_("Total")}: ${formatLang(total)} </td> </tr>
            </table>
        </table>
        <table width="80%" style="margin: 0 auto;" xml:space="preserve">
            <tr>
                <td width="80%">
                <FONT FACE="raro, courier" SIZE=1><b> ${_("Receipt")}: _________________________ </FONT>
                </td>
            </tr>
        </table>
        <div class="page-break">&nbsp;</div>
    %endfor
</body>
</html>