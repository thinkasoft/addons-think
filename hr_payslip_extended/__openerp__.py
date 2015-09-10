{
    'name': "Payroll extension",
    'category': "Test",
    'version': "1.0",
    'depends': [
        "hr_payroll"
    ],
    'description': """
        fields added:
        - Period_id [many2one] [Text]""",
    'author': "www.thinkasoft.com",
    'data': [
        'wizard/hr_payslip_extended.xml',
        'report/report_hr_payslip_extended.xml'
    ],
}
