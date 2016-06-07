<html>
<head>
	<style>
		#terp_default_8 {
				text-align:left;
				font-size: 9pt;
				margin-right: 0.0pt;
				margin-left: 0.0pt;
				line-height: 11pt;
		}

		#terp_default_9 {
				text-align:left;
				font-size: 6pt;
				margin-right: 0.0pt;
				margin-left: 0.0pt;
				line-height: 11pt;
		}

		#terp_default_Right_9 {
				text-align:right;
				font-size: 8pt;
				margin-right: 0.0pt;
				margin-left: 0.0pt;
				line-height: 11pt;
		}

		#terp_default_Centre_9 {
				text-align:center;
				font-size: 8pt;
				position:absolute;
				margin-right: 0.0pt;
				margin-left: 0.0pt;
				line-height: 11pt;
		}

		#table8 {
				position:absolute;
				top: 185px;
				left: 187px;
		}

		#table9 {
				position:absolute;
				top: 154.62992126px;
				left: 17px;
		}

		#table10 {
				position:absolute;
				top: 222px;
				left: 99px;
		}
	</style>
</head>
<body>
	
	<% setLang(user.lang) %>
    %for o in objects :
    <table id='table9'>
    	<tr><td><para>Valencia ${o.date_invoice}</para></td></tr>
    </table>
    <table id='table8'>
		<tr><td style='font-size: 10.5pt; line-height:14px;'><para>${(o.partner_id and o.partner_id.title and o.partner_id.title.name) or '' + (o.partner_id and o.partner_id.name) or ''}</para></td></tr>
	</table>
    <table id='table10'>
      <tr>
        <td>
          <para id="terp_default_8"s>${o.partner_id.street}</para>
        </td>
        <td>
          <para id="terp_default_8">${o.partner_id.street2 + o.partner_id.city + " " + o.partner_id.zip + " Venezuela"}</para>
        </td>
      </tr>
    </table>
    <!--<table>
		<tr>
			<td id='terp_default_8' style='background-color: yellow;padding-left: 153px;'><para><b>${(o.payment_term and o.payment_term.note and format(o.payment_term and o.payment_term.note)) or removeParentNode('para') }</b></para></td>
		</tr>
		<tr>
			<td id='terp_default_8' style='background-color: blue;padding-left: 148px;'><para><b>${o.partner_id.phone}</b></para></td>
		</tr>
		<tr>
			<td id='terp_default_8' style='background-color: red;text-align:right;'><para><b>${(o.partner_id.vat and ('        %s-%s-%s'%(o.partner_id.vat[2:3], o.partner_id.vat[3:11],o.partner_id.vat[11:12])) or removeParentNode('para'))}</b></para></td>
		</tr>
	</table>
	<table>
      %for line in o.invoice_line:
        <tr>
          <td id="terp_default_Centre_9"><para>${format(line.name)}</para></td>
          <td id="terp_default_Right_9"><para>${formatLang(line.quantity)}</para></td>
          <td id="terp_default_Right_9"><para>${formatLang(line.price_unit)}</para></td>
          <td id="terp_default_Right_9"><para>${formatLang(line.price_subtotal)}</para></td>
        </tr>
      %endfor
    </table>
    <table>
      	<tr><td><para >${formatLang(o.amount_untaxed)}</para></td></tr>
      	<tr><td><para>0.00</para></td></tr>
      	<tr><td><para >0.00</para></td></tr>
        <tr><td><para >${formatLang(o.amount_untaxed)}</para></td></tr>
      	<tr><td><para >${formatLang( o.amount_tax)}</para></td></tr>
    	<tr><td><para ><b>${formatLang(o.amount_total)}</b></para></td></tr>
    </table>-->
    %endfor
</body>
</html>