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
                        <td style="line-height:1pt;">RECIBO DE PAGO</td>
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
                            <FONT FACE="raro, courier" SIZE=1><b>${o.name}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                            <FONT FACE="raro, courier" SIZE=1>Cargo</FONT>
                        </td>
                        <td style="border:1px solid black;" width="30%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.job_id.name}</b></FONT>
                        </td>
                    </tr>
  </table>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Cedula No</FONT>
                        </td>
                        <td style="border:1px solid black;" width="50%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.identification_id}</b></FONT>
                        </td>
                        <td style="border:1px solid black;" width="20%">
                            <FONT FACE="raro, courier" SIZE=1>Salario por Tabulador</FONT>
                        </td>
                        <td style="border:1px solid black;" width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>${o.contract_id.wage} Bs.</b></FONT>
                        </td>
                    </tr>
  </table>
  <br/>
  <table width="100%" class="bottomBorder">
                    <tr>
                        <td width="5%">
                            <FONT FACE="raro, courier" SIZE=1><b>Mes</b></FONT>
                        </td>
                        <td width="35%">
                            <FONT FACE="raro, courier" SIZE=1><b>Monto cancelado mensual</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Salario Diario</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Alic. Utilidades</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Dias Aluc</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Bono Vacacional</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Salario Integral Diario</b></FONT>
                        </td>
                        <td width="20%">
                            <FONT FACE="raro, courier" SIZE=1><b>Dias Antiguedad</b></FONT>
                        </td>
                    </tr>
  </table>
  <table width="100%" class="bottomBorder" style="line-height:8pt;">
        %for line in (get_payslip_total_lines(o)):
            <tbody >
              <tr>
                  <td style="text-align:left;">
                      ${line['month'] }
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['integral']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['salary_daily']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['alic_benefit']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['days_alic']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['holidays_bonus']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['salary_integral']) } 
                  </td>
                  <td style="text-align:left;">
                      ${formatLang(line['hitoric_day']) } 
                  </td>
              </tr>
            </tbody>
        %endfor
  </table>
  %endfor 
</body>
</html>
</html>