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
                            %if o.company_id.partner_id.vat != False:
                                <FONT FACE="raro, courier" SIZE=1>R.I.F: ${o.company_id.partner_id.vat[2:]}</FONT><br/>
                            %endif
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
        <thead>
            <tr>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Mes</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Monto cancelado mensual</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Salario Diario</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Alic. Utilidades</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Dias Aluc</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Bono Vacacional</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Salario Integral Diario</b></FONT>
                </th>
                <th>
                    <FONT FACE="raro, courier" SIZE=1><b>Dias Antiguedad</b></FONT>
                </th>
                <th>
                  <FONT FACE="raro, courier" SIZE=1><b>Prest. del Mes</b></FONT>
                </th>
                <th style="text-align:right;">
                  <FONT FACE="raro, courier" SIZE=1 ><b>Adelanto de Prest.</b></FONT>
                </th>
                <th style="text-align:right;">
                  <FONT FACE="raro, courier" SIZE=1 ><b>Prest. Acumulado</b></FONT>
                </th>
            </tr>
        </thead>
        <tbody >
        <% amount_total = loan_mont = 0.0%>
        <% loan_acum = o.acum_social_benefits %>
        %for line in (get_payslip_total_lines(o)):
          <% loan_mont = line['salary_integral'] * line['hitoric_day']%>
          <% loan_acum += loan_mont - line['advancement']%>
          <tr>
              <td width="9%">
                  ${line['month'] }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['integral']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['salary_daily']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['alic_benefit']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['days_alic']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['holidays_bonus']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['salary_integral']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['hitoric_day']) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(loan_mont) }
              </td>
              <td style="text-align:center;">
                  ${formatLang(line['advancement']) }
              </td>
              <td style="text-align:right;">
                  ${formatLang(loan_acum) }
              </td>
          </tr>
        %endfor
        </tbody>
  </table>
  <table class="list_table" width="100%" style="border-top:1px solid #ccc">
    <thead>
      <tr>
        <td style="text-align:right;border-top:0px" >Total a pagar: ${formatLang(loan_acum) }</td>
      </tr>
    </thead>
  </table>
  %endfor
</body>
</html>
</html>
