# -*- coding: utf-8 -*-
from osv import osv, fields


curso_ingles()
    _name = 'curso.ingles'
    numAlumno = fields.Integer(int = 'NumEmp_Alumno', required=True,)
    nomAlumno = fields.Char(string = 'Nombre_Alumno')
    dni = fields.Char(string = 'Dni')
    phone = fields.Char(string ='Telefono')
    ingles = fields.Char(string = 'Nivel_de_Ingles')
    cur_ing = fields.Char (string = 'Nombre_Curso')
