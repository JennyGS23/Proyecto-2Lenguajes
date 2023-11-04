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
('agua_con_gas', 'bebida', 'carbonatada', 'general'),
('limonada', 'bebida', 'natural', 'cena'),
('fresco_cas', 'bebida', 'natural', 'general'),
('fresco_tamarindo', 'bebida', 'natural', 'general'),
('fresco_guanabana', 'bebida', 'natural', 'general'),
('jugo_naranja', 'bebida', 'natural', 'general'),
('refresco', 'bebida','carbonatada', 'desayuno'),
('capucchino', 'bebida','con_lacteo', 'desayuno'),
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
('horchata', 'bebida','con_lacteo', 'almuerzo'),
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
('salmon', 'proteina', 'marino', 'desayuno'),
('ceviche', 'proteina', 'marino', 'cena'),
('ternera', 'proteina', 'roja', 'cena'),
('huevo', 'proteina', 'blanca', 'desayuno'),
('tocino', 'proteina', 'roja', 'desayuno'),
('camaron', 'proteina', 'marino', 'general'),
('pasta', 'acompanamiento', 'carbohidratos', 'cena'),
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
('tomates_cherry', 'acompanamiento', 'vegetales', 'desayuno'),
('pure_de_papas','acompanamiento',  'carbohidratos', 'general'),
('macarrones_con_queso', 'acompanamiento', 'carbohidratos', 'almuerzo'),
('pan_integral', 'acompanamiento', 'carbohidratos', 'desayuno'),
('sopa_de_tomate', 'acompanamiento', 'caliente', 'cena'),
('crema_de_brocoli', 'acompanamiento', 'caliente', 'cena'),
('papas_asadas','acompanamiento', 'caliente', 'general'),
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
('donas_glaseadas', 'postre', 'reposteria', 'general'),
('galleta_vegana','postre',  'sin_lacteo', 'almuerzo'),
('panuelo_relleno','postre',  'reposteria', 'almuerzo');




INSERT INTO Calorias(ID, Nombre, CantidadCalorias)
VALUES 

(1,'agua', 0),
(2,'agua_con_gas',0),
(3,'limonada',40),
(4,'fresco_cas', 60),
(5,'fresco_tamarindo', 62),
(6,'fresco_guanabana', 70),
(7,'jugo_naranja', 120),
(8,'refresco', 120),
(9,'capucchino', 40),
(10,'cafe', 2),
(11,'leche', 42),
(12,'jugo_manzana',115),
(13,'zumo_uva', 154),
(14,'refresco_cola', 140),
(15,'te',2),
(16,'refresco_naranja',150),
(17,'refresco_limon', 135),
(18,'te_verde', 2),
(19,'te_negro', 2),
(20,'leche_chocolate', 208),
(21, 'fresa_en_leche', 208),
(22, 'batido_crema', 100),
(23, 'horchata', 80),
(24,'te_chai_latte', 106),
(25,'te_con_leche', 120),
(26,'carne_res', 250),
(27,'pollo_salsa_blanca', 335),
(28,'pollo_salsa_jalapena', 330),
(29,'pollo_asado', 320),
(30,'pescado', 206),
(31,'cerdo', 242),
(32,'pavo', 135),
(33,'atun',184),
(34,'salmon', 100),
(35,'ceviche', 150),
(36,'ternera', 250),
(37,'huevo', 68),
(38,'tocino', 68),
(39,'camaron', 99),
(40,'pasta', 100),
(41,'pasta_primavera', 200),
(42,'avena_con_frutas', 80),
(43,'tostadas_de_pan', 10),
(44,'lentejas', 230),
(45,'ensalada', 35),
(46,'papas_fritas', 365),
(47,'arroz', 130),
(48,'vegetal_al_vapor', 68),
(49,'ensalada_de_tomate', 78),
(50,'esparragos_gratinados', 124),
(51,'tomates_cherry', 50),
(52,'pure_de_papas',143),
(53,'macarrones_con_queso',350),
(54,'pan_integral', 80),
(55,'sopa_de_tomate', 74),
(56,'crema_de_brocoli', 103),
(57,'papas_asadas',130),
(58,'queque', 350 ),
(59,'fruta', 120 ),
(60,'helado', 207 ),
(61,'tarta_manzana', 316),
(62,'gelatina_frutas', 62),
(63,'tiramisu', 280 ),
(64,'flan', 153 ),
(65,'crema_cacahuate',400),
(66,'pudin_vainilla',174),
(67,'tarta_fresa',271),
(68,'chocolate_caliente',192),
(69,'helado_manzana',190),
(70,'tostadas_con_mantequilla_de_cacahuate', 200),
(71,'torta_de_chocolate_vegana', 140),
(72,'batido_de_frutas_con_leche_de_almendras', 100),
(73,'croissant', 90),
(74,'donas_glaseadas', 150),
(75,'galleta_vegana', 130),
(76,'panuelo_relleno', 180);

SELECT * FROM ElementoComida
SELECT * FROM HealthyMeals
SELECT * FROM 



drop table ElementoComida
drop table Calorias
drop table HealthyMeals


