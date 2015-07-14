{
	'name' : "Payroll extension",
	'category' : "Test",
	'version' : "1.0",
	'depends' : [
		"hr"
	],
	'author' : "Me",
	'description' : """\
fields added:
		- Rif [Text]
		- Retencion [integer]""",
	'data' : [
		'view/hr_employee_extended.xml',
	],
} 
