# Priorización de Vacunas
Es un pequeño ejercicio donde se identifica las condiciones de urgencia cuando se requiere que una persona sea vacunada del Covid-19.

Caso: Uno de los avances científicos que más valora la humanidad en estos tiempos, es el desarrollo oportuno de la vacuna contra el COVID19. 
Sin embargo, las empresas farmacéuticas que han logrado este hito para la humanidad se encuentran con recursos limitados y una demanda global de este producto, 
por tal razón las entregas que han hecho a los diferentes países siempre serán insuficientes para toda la población, al menos en el corto plazo. 
Por tal razón, los diferentes países han optado por realizar un esquema de vacunación en el que se les dé prioridad a las personas con mayor riesgo de 
muerte a causa del contagio. La vulnerabilidad de las personas ante el COVID19 está dada por las condiciones orgánicas que están presentes en mayor 
frecuencia en las víctimas de la enfermedad. Según la organización mundial de la salud, las personas más vulnerables tienen las siguientes condiciones:

•	Que tenga 80 años o más años.     
•	Que tenga Diabetes tipo 2. Para saber esto la prueba de hemoglobina glicosilada debe dar un resultado por encima de 7 por ciento.    
•	Que sea Obeso. Para que una persona sea obesa el índice de masa corporal debe ser igual o superior a 30.     
•	Que sea hipertenso. Para saber si la persona es hipertensa, su tensión sistólica debe ser igual o superior a 140 mmHg y la tensión diastólica 
  igual o superior a 90 mmHg.

Usted hace parte del equipo de desarrollo encargado de la priorización de las personas que recibirán las primeras dosis de vacunas que llegarán al país, 
así que debe construir el software que procesará los datos de las bases de datos en el sistema de la registraduría. 
Su misión es crear un programa en Python que permita mostrarle al Ministerio de Salud la lista de las personas que cumplen con estos requerimientos 
para ser vacunados con prioridad y por supuesto la edad de las mismas para su consideración.

Ingreso de datos:    
El ingreso de datos estará conformada por N + 1 líneas:

•	La primera línea recibirá un número N que equivale a la cantidad de registros en la base de datos de la registraduría. 
  Cada registro representa una persona que será evaluada para recibir la vacuna en el primer turno.    
•	Cada una de las siguientes N líneas estará formada por 5 números separados por espacios que representan las diferentes características de la persona. 
  Por ejemplo, la fila 85 8 31 145 92 representa una persona con 85 años de edad, 8 por ciento en su examen de hemoglobina glicosilada (con diabetes), 
  un índice de masa corporal de 31 (obesidad) y una tensión arterial de 145 (sistólica) / 92 (diastólica) lo que implica hipertensión.

Salida de datos:

•	El programa imprimirá la edad de cada una de las personas de la base de datos que cumplen con los criterios para ser vacunados con prioridad.    
•	Si no existe ningún registro en la base de datos que cumpla los criterios de vacunación prioritaria, el programa imprimirá 'NO DISPONIBLE'.

Casos de Prueba:

Ingreso de datos    

3 95 7 40 140 100 86 8 43 150 80 83 10 43 150 80    
6 82 10 40 130 110 78 5 37 150 100 95 9 40 140 90 91 7 31 150 100 79 5 31 140 90 84 6 25 140 90    
5 80 9 43 130 80 77 5 25 140 110 85 5 34 150 90 89 5 34 140 80 85 10 34 130 80    
4 96 7 37 130 90 91 10 43 140 90 88 5 37 130 110 95 7 25 130 100    
6 77 10 31 140 110 88 6 25 150 80 77 6 31 150 90 93 10 43 140 90 75 6 40 140 110 85 8 25 150 110    
6 76 8 43 140 90 81 6 28 150 110 88 8 31 140 110 96 8 25 140 110 93 8 31 150 110 76 8 25 140 90    

Salida de datos

NO DISPONIBLE    
95    
NO DISPONIBLE         
91    
93    
88.93    


