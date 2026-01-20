{
    "name": "Hospital Management System",
    "author": "Rajesh",
    "license": "LGPL-3",
    "version": "19.0.1.0",
    "application": True,
    "sequence": -1,
    "depends":[
        'mail'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/appointment_views.xml",
        "views/doctor_views.xml",
        "views/menu.xml",
    ],
}
