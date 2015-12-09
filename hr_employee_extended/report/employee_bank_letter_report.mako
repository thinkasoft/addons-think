<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>



	<!-- The objects variable is a list of browse_record objects from OpenERP. -->
	<!-- It contains all the documents in OpenERP that you wanted to generate this report for. -->
	<!-- We loop on it in order to be able to output the information for each document -->
    %for o in objects :
	<% 
	    # Let's define a function to get the day of the week with Python. 
	    # Notice the <% and %> to open and close Python code blocks...
	    # They can also be used for 1 liners (see setLang above)
	    import time

	    def get_day():
	    	return time.strftime("%d" " de " "%B" " del " "%Y"".")
	   
	    
	%>

<table width="100%">
        <tr>
            <td width="30%" style="text-align:center;" style="BOLD">
                <table width="100%">
                    <tr>
                        <td rowspan="0">
                        ${helper.embed_image('jpeg',str(o.company_id.logo),180, 120)}
                        </td>
                        <td style="line-height:1pt;">
                            <h3>${o.company_id.partner_id.name}</h3>
                            <h6>R.I.F: ${o.company_id.partner_id.vat[2:]}</h6>
                            <h6>${o.company_id.street}
                            ${o.company_id.street2}</h6>
                            <h6>${o.company_id.city}
                            ${o.company_id.state_id.name}
                            ${o.company_id.country_id.name}</h6>
                    
                        </td>
                   </tr>
                </table>
            </td>
        </tr>
    </table>
    <hr style="color: #0056b2;" size="5" />

    <H1 style="text-align:center;">CONSTANCIA DE TRABAJO</H1>
    <H4 style="text-align:center;">A QUIEN PUEDA INTERESAR</H4>
    <br/>
     %if o.employment_benefit == True:
     	<p style="text-align:justify">Quien suscribe, Alcibiete Ricciardelli, en mi carácter de Gerente de Operaciones de la empresa ${o.company_id.partner_id.name}, por medio de la presente hago constar que los datos abajo suministrados corresponden a nuestro trabajador(a) ACTIVO por concepto de Beneficios Laborales</p>
     %else:
	    %if o.date_exit == "False":
	    	<p style="text-align:justify">Quien suscribe, Alcibiete Ricciardelli, en mi carácter de Gerente de Operaciones de la empresa ${o.company_id.partner_id.name}, por medio de la presente hago constar que los datos abajo suministrados corresponden a nuestro trabajador(a) ACTIVO:</p>
	    %else:
	    	<p style="text-align:justify">Quien suscribe, Alcibiete Ricciardelli, en mi carácter de Gerente de Operaciones de la empresa ${o.company_id.partner_id.name}, por medio de la presente hago constar que los datos abajo suministrados corresponden a nuestro trabajador(a), quién prestó sus servicios laborales para esta institución: </p>
	    %endif
    %endif
    <!-- We want to print this report out and send it to the partner, so -->
    <!-- We use the partner_id field on our object to set the translation language -->
  

    <!-- Now we write the name field of our object as the title -->
    <!-- You can access any field or function on the object like this -->
    <!-- Notice above we use the same syntax to output the css variable that was given to use by OpenERP? -->
    <br/>

    <table width="70%" style="text-align:left;" border="5" align="center">
    	<tr>
    		<td><b>NOMBRE Y APELLIDO:</b></td>
    		<td><b>${ o.name }</b></td>
    	</tr>
    	<tr>
    		<td><b>CÉDULA DE INDENTIDAD</b></td>
    		<td><b>${ o.identification_id}</b></td>
    	</tr>
    	<tr>
    		<td><b>CARGO</b></td>
    		<td><b>${ o.job_id.name }</b></td>
    	</tr>
    	%if o.date_exit == "False":
    		<tr>
    			<td><b>SALARIO MENSUAL</b></td>
    			<td><b>${ o.salary } BS.</b></td>
    		</tr>
    	%else :
    		<tr>
    			<td><b> SALARIO MENSUAL</b></td>
    			<td><b>${ o.salary } BS.</b></td>
    		</tr>
    	%endif
    	<tr>
    		<td><b>FECHA DE INGRESO</b></td>
    		<td><b>${ o.admission_date }</b></td>
    	</tr>
    	 %if o.date_exit != "False":
    		<tr>
    			<td><b>FECHA DE EGRESO</b></td>
    			<td><b>${ o.date_exit }</b></td>
    		</tr>
    	%endif

    </table>

	<br/>
	

 	<p style="text-align:justify">Se expide la presente constancia a petición de la parte interesada, en San Diego, el  ${get_day()}</p>
 	<p style="text-align:justify">Atentamente,</p>
 	<br/>
 	<br/>
 	<br/>
 	<br/>
 	<br/>
 	<br/>
 	<table width="100%" align="center" style="font-size:12px;" >
 		<td></td>
 		<td>  
 			<div ALIGN=center>________________________________________________</div>
 			<div ALIGN=center>Gerente de Recursos Humanos</div>
 			<div ALIGN=center>Emilia Ricciardelli</div>
 			<div ALIGN=center>Ofic. (0241) 871.62.36 / Celular. (0424) 888.88.88</div>
 		</td>
 		<td></td>
 			
 	</table>
 	

	

	<!-- We call our function in the same way as we ouput parameters and it will simply print the result -->
	

	<!-- We can even create variables inside Python code blocks and use them later -->
	<%
	from datetime import datetime
	time = datetime.now()
	%>

	<!-- Here, I use a similar syntax to the for loops to write an if statement -->


	<!-- Don't forget to close your loops! -->
	%endfor

</body>
</html>
