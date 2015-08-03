{
    'name': "Contract extension",
    'category': "Test",
    'version': "1.0",
    'depends': [
                "hr_contract"],
    'author': "Gerardo Medina",
    'description': """ Add field Sueldo Trimestral to IVSS calculate
                       fields added:
                       - Sueldo Trimestral [Text]""",
    'data': [
              'view/hr_contract_trimestre.xml'],
}
