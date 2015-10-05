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
                <strong style="font-size: 20;">${_('Listado Nomina') |entity}</strong>
            </td>
       </tr>
    </table>
    <% suma1 = 0 %>
    <% suma2 = 0 %>
    <% suma3 = 0 %>
</head>
<body>
		<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                <tr>
                    <td style="border:1px solid black; text-align: center;" width="10%">
                    <FONT FACE="raro, courier" SIZE=1><b>Doc. Identidad</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: center;" width="45%">
                        <FONT FACE="raro, courier" SIZE=1><b>Trabajador</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: center;" width="15%">
                        <FONT FACE="raro, courier" SIZE=1><b>Total Asignaciones</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: center;" width="15%">
                        <FONT FACE="raro, courier" SIZE=1><b>Total Deducciones</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: center;" width="15%">
                        <FONT FACE="raro, courier" SIZE=1><b>Total a Pagar</b></FONT>
                    </td>
                </tr>
		</table>
	%for o in objects :	
		<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                <tr>
                    <td style="border:1px solid black;" width="10%">
                    <FONT FACE="raro, courier" SIZE=1>${o.employee_id.identification_id}</FONT>
                    </td>
                    <td style="border:1px solid black;" width="45%">
                        <FONT FACE="raro, courier" SIZE=1>${o.employee_id.name}</FONT>
                    </td>
                    %for line_r in (get_details_by_rule_category(o.details_by_salary_rule_category)):
	                    %if line_r.get('code') == "039":
		                    <td style="border:1px solid black; text-align: right;" width="15%">
		                        <FONT FACE="raro, courier" SIZE=1>${formatLang(line_r.get('total')) or 0.0 |entity } Bs.</FONT>
		                    </td>
		          		<% suma1 += line_r.get('total') %>
		                %endif
		                %if line_r.get('code') == "069":
		                    <td style="border:1px solid black; text-align: right;" width="15%">
		                        <FONT FACE="raro, courier" SIZE=1>${formatLang(line_r.get('total')) or 0.0 |entity } Bs.</FONT>
		                    </td>
		                <% suma2 += line_r.get('total') %>
		                %endif
		                %if line_r.get('code') == "200":
		                    <td style="border:1px solid black; text-align: right;" width="15%">
		                        <FONT FACE="raro, courier" SIZE=1>${formatLang(line_r.get('total')) or 0.0 |entity } Bs.</FONT>
		                    </td>
		                <% suma3 += line_r.get('total') %>
		                %endif
                    %endfor
                </tr>
		</table>
	%endfor
		<table width="100%" style="border:1px solid black;border-collapse:collapse;">
                <tr>
                    <td style="border:1px solid black; text-align: center;" width="10%">
                    <FONT FACE="raro, courier" SIZE=1><b></b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: right;" width="45%">
                        <FONT FACE="raro, courier" SIZE=2><b>TOTALES</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: right;" width="15%">
                        <FONT FACE="raro, courier" SIZE=2><b>${formatLang(suma1)} Bs.</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: right;" width="15%">
                        <FONT FACE="raro, courier" SIZE=2><b>${formatLang(suma2)} Bs.</b></FONT>
                    </td>
                    <td style="border:1px solid black; text-align: right;" width="15%">
                        <FONT FACE="raro, courier" SIZE=2><b>${formatLang(suma3)} Bs.</b></FONT>
                    </td>
                </tr>
		</table>
</body>
</html>