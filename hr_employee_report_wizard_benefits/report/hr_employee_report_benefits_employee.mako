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
  <p>Esta es la fecha: ${start_date}</p>
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
                  <FONT FACE="raro, courier" SIZE=1><b>Devengado Basico</b></FONT>
              </td>
              <td width="20%">
                  <FONT FACE="raro, courier" SIZE=1><b>Decengado Integral</b></FONT>
              </td>
          </tr>
  </table>
  <%total_integral = 0%>
  <table width="100%" class="bottomBorder" style="line-height:8pt;">
        %for line in (get_payslip_lines(o,start_date,stop_date)):
        <%total_integral += line['integral']%>
          % if line['month'] != 'Diciembre':
                  <tbody >
                      <tr>
                          <td style="text-align:left;">
                            ${line['month'] }
                          </td>
                          <td style="text-align:left;">
                            ${formatLang(line['basic']) } 
                          </td>
                          <td style="text-align:left;">
                            ${formatLang(line['integral']) } 
                          </td>
                      </tr>
                  </tbody>
          % else:
                  <tbody >
                      <tr>
                          <td style="text-align:left;">
                            ${line['month'] }
                          </td>
                          <td style="text-align:left;">
                            ${formatLang(o.december_salary_aprox) } 
                          </td>
                          <td style="text-align:left;">
                            ${formatLang(o.december_salary_aprox) } 
                          </td>
                      </tr>
                  </tbody>
           % endif
        %endfor
        <%total_integral += o.december_salary_aprox%>
  </table>
  <table width="100%" class="bottomBorder" style="line-height:8pt;">
          <tbody >
              <tr>
                  <td style="text-align:left;" />
                    Total: ${formatLang(total_integral, digits=2)} 
                  </td>
              </tr>
          </tbody>
  </table>
  <% value = o.number_days_benefits / 360.0000 %>
  <% calc_benefits = round(float('%.5f'%(value)),4) %>
  <% result =  total_integral*calc_benefits%>
  <table width="100%" class="bottomBorder">  
          <center><FONT FACE="raro, courier" SIZE=1><b>Utilidades ${o.number_days_benefits} Dias X ${formatLang(calc_benefits, digits=4)} =  ${formatLang(result)}</b></FONT></center>                    
  </table>
  <table width="100%" class="bottomBorder">  
          <center><FONT FACE="raro, courier" SIZE=1><b>Total Remuneraciones ${formatLang(result)}</b></FONT></center>                    
  </table>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
          <FONT FACE="raro, courier" SIZE=1>DEDUCCIONES</FONT>
  </table>
  <% inces =  result*0.005%>
  <% faov =  result*0.01%>
  <% isrl = result * (o.withholding/100)%>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>I.N.C.E.S</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${formatLang(inces)}</FONT>
                        </td>
                    </tr>
  </table>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>FAOV</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${formatLang(faov)}</FONT>
                        </td>
                    </tr>
  </table>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>ISRL</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${formatLang(isrl)}</FONT>
                        </td>
                    </tr>
  </table>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Prestamo Personal</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${o.other_benefits_deductions}</FONT>
                        </td>
                    </tr>
  </table>
  <% total_deductions =  inces + faov +  isrl + o.other_benefits_deductions%>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Total Deducciones</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${formatLang(total_deductions)}</FONT>
                        </td>
                    </tr>
  </table>
  <% pay_utilites =  result - total_deductions%>
  <table width="100%" style="border:1px solid black;border-collapse:collapse;">
                    <tr>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>Utilidades a pagar</FONT>
                        </td>
                        <td style="border:1px solid black;" width="10%">
                        <FONT FACE="raro, courier" SIZE=1>${formatLang(pay_utilites)}</FONT>
                        </td>
                    </tr>
  </table>
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
</html>
