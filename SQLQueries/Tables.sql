CREATE TABLE ElementoComida (
	ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(255), 
    Tipo VARCHAR(255),
	Descripcion VARCHAR(255),
    MomentoDelDia VARCHAR(255)
);

CREATE TABLE Calorias 	(
	ID INT PRIMARY KEY,
	Nombre VARCHAR(255),
	CantidadCalorias INT
	FOREIGN KEY (ID) REFERENCES ElementoComida(ID)
);

CREATE TABLE HealthyMeals 	(
	ID			INT IDENTITY(1,1) PRIMARY KEY,
	Drink		VARCHAR(255),
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	Dessert		VARCHAR(255),
	MinCalories	VARCHAR(255)
);

CREATE TABLE ComboMeals (
	ID			INT PRIMARY KEY,
	Drink		VARCHAR(255),
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	Dessert		VARCHAR(255),
	DayMoment	VARCHAR(255)
);


CREATE TABLE ParcialMeals (
	ID			INT PRIMARY KEY,
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	DayMoment	VARCHAR(255)
);


CREATE TABLE Orders (
	Meal	    VARCHAR(255),
	Price		FLOAT
);


INSERT INTO ElementoComida(Nombre, Tipo, Descripcion, MomentoDelDia)
VALUES 
('agua', 'bebida', 'natural', 'general'),
('fresco_cas', 'bebida', 'natural', 'general'),
('fresco_tamarindo', 'bebida', 'natural', 'general'),
('fresco_guanabana', 'bebida', 'natural', 'general'),
('jugo_naranja', 'bebida', 'natural', 'general'),
('cafe', 'bebida','caliente', 'desayuno'),
('leche', 'bebida','natural', 'desayuno'),
('jugo_manzana','bebida', 'natural', 'almuerzo'),
('zumo_uva', 'bebida','natural', 'almuerzo'),
('refresco_cola', 'bebida','carbonatada', 'almuerzo'),
('te', 'bebida','caliente', 'general'),
('refresco_naranja','bebida', 'carbonatada', 'cena'),
('refresco_limon', 'bebida','carbonatada', 'cena'),
('te_verde', 'bebida','caliente', 'cena'),
('te_negro', 'bebida','caliente', 'cena'),
('leche_chocolate', 'bebida','con_lacteo', 'cena'),
('fresa_en_leche', 'bebida','con_lacteo', 'general'),
('batido_crema', 'bebida','con_lacteo', 'general'),
('te_chai_latte', 'bebida', 'caliente', 'almuerzo'),
('te_con_leche', 'bebida', 'caliente', 'cena'),
('carne_res', 'proteina', 'roja', 'general'),
('pollo_salsa_blanca', 'proteina', 'blanca', 'almuerzo'),
('pollo_salsa_jalapena', 'proteina', 'blanca', 'almuerzo'),
('pollo_asado', 'proteina', 'blanca', 'general'),
('pescado', 'proteina', 'marino', 'general'),
('cerdo', 'proteina', 'roja', 'almuerzo'),
('pavo', 'proteina', 'blanca', 'cena'),
('atun', 'proteina', 'marino', 'almuerzo'),
('salmon', 'proteina', 'marino', 'cena'),
('ternera', 'proteina', 'roja', 'cena'),
('huevo', 'proteina', 'blanca', 'desayuno'),
('tocino', 'proteina', 'roja', 'desayuno'),
('camaron', 'proteina', 'marino', 'general'),
('pasta_primavera', 'acompanamiento', 'caliente', 'almuerzo'),
('avena_con_frutas', 'acompanamiento', 'caliente', 'desayuno'),
('tostadas_de_pan', 'acompanamiento', 'caliente', 'desayuno'),
('lentejas', 'acompanamiento', 'carbohidratos', 'almuerzo'),
('ensalada', 'acompanamiento', 'vegetales', 'general'),
('papas_fritas', 'acompanamiento', 'carbohidratos', 'almuerzo'),
('arroz', 'acompanamiento', 'carbohidratos', 'general'),
('vegetal_al_vapor', 'acompanamiento', 'vegetales', 'cena'),
('ensalada_de_tomate', 'acompanamiento', 'vegetales', 'almuerzo'),
('esparragos_gratinados', 'acompanamiento', 'vegetales', 'cena'),
('pure_de_papas','acompanamiento',  'carbohidratos', 'general'),
('macarrones_con_queso', 'acompanamiento', 'carbohidratos', 'almuerzo'),
('pan_integral', 'acompanamiento', 'carbohidratos', 'desayuno'),
('sopa_de_tomate', 'acompanamiento', 'calientes', 'cena'),
('crema_de_brocoli', 'acompanamiento', 'calientes', 'cena'),
('papas_asadas','acompanamiento', 'calientes', 'general'),
('queque', 'postre', 'reposteria', 'cena'),
('fruta', 'postre', 'sin_lacteo', 'general'),
('helado', 'postre', 'con_lacteo', 'general'),
('tarta_manzana', 'postre', 'con_lacteo', 'almuerzo'),
('gelatina_frutas', 'postre', 'sin_lacteo', 'general'),
('tiramisu','postre',  'con_lacteo', 'cena'),
('flan', 'postre', 'con_lacteo', 'cena'),
('crema_cacahuate','postre',  'sin_lacteo', 'cena'),
('pudin_vainilla','postre',  'con_lacteo', 'almuerzo'),
('tarta_fresa','postre',  'con_lacteo', 'almuerzo'),
('chocolate_caliente','postre',  'con_lacteo', 'desayuno'),
('helado_manzana','postre',  'con_lacteo', 'almuerzo'),
('tostadas_con_mantequilla_de_cacahuate', 'postre', 'sin_lacteo', 'desayuno'),
('torta_de_chocolate_vegana', 'postre', 'sin_lacteo', 'desayuno'),
('batido_de_frutas_con_leche_de_almendras', 'postre', 'sin_lacteo', 'general'),
('croissant', 'postre', 'reposteria', 'desayuno'),
('donas_glaseadas', 'postre', 'reposteria', 'general');




INSERT INTO Calorias(ID, Nombre, CantidadCalorias)
VALUES 

(1,'agua', 0),
(2,'fresco_cas', 60),
(3,'fresco_tamarindo', 62),
(4,'fresco_guanabana', 70),
(5,'jugo_naranja', 120),
(6,'cafe', 2),
(7,'leche', 42),
(8,'jugo_manzana',115),
(9,'zumo_uva', 154),
(10,'refresco_cola', 140),
(11,'te',2),
(12,'refresco_naranja',150),
(13,'refresco_limon', 135),
(14,'te_verde', 2),
(15,'te_negro', 2),
(16,'leche_chocolate', 208),
(17, 'fresa_en_leche', 208),
(18, 'batido_crema', 210),
(19,'te_chai_latte', 106),
(20,'te_con_leche', 120),
(21,'carne_res', 250),
(22,'pollo_salsa_blanca', 335),
(23,'pollo_salsa_jalapena', 330),
(24,'pollo_asado', 320),
(25,'pescado', 206),
(26,'cerdo', 242),
(27,'pavo', 135),
(28,'atun',184),
(29,'salmon', 367),
(30,'ternera', 250),
(31,'huevo', 68),
(32,'tocino', 68),
(33,'camaron', 99),
(34,'pasta_primavera', 200),
(35,'avena_con_frutas', 80),
(36,'tostadas_de_pan', 10),
(37,'lentejas', 230),
(38,'ensalada', 35),
(39,'papas_fritas', 365),
(40,'arroz', 130),
(41,'vegetal_al_vapor', 68),
(42,'ensalada_de_tomate', 78),
(43,'esparragos_gratinados', 124),
(44,'pure_de_papas',143),
(45,'macarrones_con_queso',350),
(46,'pan_integral', 80),
(47,'sopa_de_tomate', 74),
(48,'crema_de_brocoli', 103),
(49,'papas_asadas',130),
(50,'queque', 350 ),
(51,'fruta', 120 ),
(52,'helado', 207 ),
(53,'tarta_manzana', 316),
(54,'gelatina_frutas', 62),
(55,'tiramisu', 280 ),
(56,'flan', 153 ),
(57,'crema_cacahuate',400),
(58,'pudin_vainilla',174),
(59,'tarta_fresa',271),
(60,'chocolate_caliente',192),
(61,'helado_manzana',190),
(62,'tostadas_con_mantequilla_de_cacahuate', 200),
(63,'torta_de_chocolate_vegana', 140),
(64,'batido_de_frutas_con_leche_de_almendras', 100),
(65,'croissant', 90),
(66,'donas_glaseadas', 120);


SELECT * FROM ElementoComida
SELECT * FROM HealthyMeals

drop table ElementoComida
drop table Calorias
drop table HealthyMeals


