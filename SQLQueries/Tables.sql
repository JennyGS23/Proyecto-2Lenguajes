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
('carne_res', 'proteina', 'roja', 'general'),
('pollo_salsa_blanca', 'proteina', 'blanca', 'almuerzo'),
('pollo_salsa_jalapena', 'proteina', 'blanca', 'almuerzo'),
('pollo_asado', 'proteina', 'blanca', 'general'),
('pescado', 'proteina', 'marino', 'general'),
('cerdo', 'proteina', 'roja', 'almuerzo'),
('pavo', 'proteina', 'blanca', 'cena'),
('atun', 'proteina', 'marino', 'almuerzo'),
('lentejas', 'proteina', 'vegetariana', 'almuerzo'),
('salmon', 'proteina', 'marino', 'cena'),
('ternera', 'proteina', 'roja', 'cena'),
('huevo', 'proteina', 'blanca', 'desayuno'),
('tocino', 'proteina', 'roja', 'desayuno'),
('camaron', 'proteina', 'marino', 'general'),
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
('papas_asadas','acompanamiento', 'calientes', 'cena'),
('queque', 'postre', 'reposteria', 'cena'),
('fruta', 'postre', 'sin_lacteo', 'desayuno'),
('helado', 'postre', 'con_lacteo', 'cena'),
('tarta_manzana', 'postre', 'con_lacteo', 'almuerzo'),
('gelatina_frutas', 'postre', 'sin_lacteo', 'general'),
('tiramisu','postre',  'con_lacteo', 'cena'),
('flan', 'postre', 'con_lacteo', 'cena'),
('crema_cacahuate','postre',  'sin_lacteo', 'cena'),
('pudin_vainilla','postre',  'con_lacteo', 'cena'),
('tarta_fresa','postre',  'con_lacteo', 'almuerzo'),
('chocolate_caliente','postre',  'con_lacteo', 'desayuno'),
('helado_manzana','postre',  'con_lacteo', 'almuerzo');


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
(17,'carne_res', 250),
(18,'pollo_salsa_blanca', 335),
(19,'pollo_salsa_jalapena', 330),
(20,'pollo_asado', 320),
(21,'pescado', 206),
(22,'cerdo', 242),
(23,'pavo', 135),
(24,'atun',184),
(25,'lentejas', 230),
(26,'salmon', 367),
(27,'ternera', 250),
(28,'huevo', 68),
(29,'tocino', 68),
(30,'camaron', 99),
(31,'ensalada', 35),
(32,'papas_fritas', 365),
(33,'arroz', 130),
(34,'vegetal_al_vapor', 68),
(35,'ensalada_de_tomate', 78),
(36,'esparragos_gratinados', 124),
(37,'pure_de_papas',143),
(38,'macarrones_con_queso',350),
(39,'pan_integral', 80),
(40,'sopa_de_tomate', 74),
(41,'crema_de_brocoli', 103),
(42,'papas_asadas',130),
(43,'queque', 350 ),
(44,'fruta', 120 ),
(45,'helado', 207 ),
(46,'tarta_manzana', 316),
(47,'gelatina_frutas', 62),
(48,'tiramisu', 280 ),
(49,'flan', 153 ),
(50,'crema_cacahuate',400),
(51,'pudin_vainilla',174),
(52,'tarta_fresa',271),
(53,'chocolate_caliente',192),
(54,'helado_manzana',190);


SELECT * FROM ElementoComida
SELECT * FROM HealthyMeals
drop table Calorias
drop table HealthyMeals
drop table Meals

