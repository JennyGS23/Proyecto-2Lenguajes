CREATE TABLE ElementoComida (
	ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(255), 
    Tipo VARCHAR(255),
	Descripcion VARCHAR(255),
    MomentoDelDia VARCHAR(255)
);

CREATE TABLE Calorias 	(
	ID INT IDENTITY(1,1) PRIMARY KEY,
	Nombre VARCHAR(255),
	CantidadCalorias INT
);

CREATE TABLE Precio (
	ID INT IDENTITY(1,1) PRIMARY KEY,
	Nombre VARCHAR(255),
	Costo INT
);

CREATE TABLE HealthyMeals 	(
	ID			INT IDENTITY(1,1) PRIMARY KEY,
	Drink		VARCHAR(255),
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	Dessert		VARCHAR(255),
	MinCalories	INT,
	Price		INT
);

CREATE TABLE ComboMeals (
	ID			INT IDENTITY(1,1) PRIMARY KEY,
	Drink		VARCHAR(255),
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	Dessert		VARCHAR(255),
	Price		INT
);


CREATE TABLE ParcialMeals (
	ID			INT IDENTITY(1,1) PRIMARY KEY,
	Proteins	VARCHAR(255),
	SideDish	VARCHAR(255),
	Price		INT
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




INSERT INTO Calorias(Nombre, CantidadCalorias)
VALUES 

('agua', 0),
('agua_con_gas',0),
('limonada',40),
('fresco_cas', 60),
('fresco_tamarindo', 62),
('fresco_guanabana', 70),
('jugo_naranja', 120),
('refresco', 120),
('capucchino', 40),
('cafe', 2),
('leche', 42),
('jugo_manzana',115),
('zumo_uva', 154),
('refresco_cola', 140),
('te',2),
('refresco_naranja',150),
('refresco_limon', 135),
('te_verde', 2),
('te_negro', 2),
('leche_chocolate', 208),
('fresa_en_leche', 208),
('batido_crema', 100),
('horchata', 80),
('te_chai_latte', 106),
('te_con_leche', 120),
('carne_res', 250),
('pollo_salsa_blanca', 335),
('pollo_salsa_jalapena', 330),
('pollo_asado', 320),
('pescado', 206),
('cerdo', 242),
('pavo', 135),
('atun',184),
('salmon', 100),
('ceviche', 150),
('ternera', 250),
('huevo', 68),
('tocino', 68),
('camaron', 99),
('pasta', 100),
('pasta_primavera', 200),
('avena_con_frutas', 80),
('tostadas_de_pan', 10),
('lentejas', 230),
('ensalada', 35),
('papas_fritas', 365),
('arroz', 130),
('vegetal_al_vapor', 68),
('ensalada_de_tomate', 78),
('esparragos_gratinados', 124),
('tomates_cherry', 50),
('pure_de_papas',143),
('macarrones_con_queso',350),
('pan_integral', 80),
('sopa_de_tomate', 74),
('crema_de_brocoli', 103),
('papas_asadas',130),
('queque', 350 ),
('fruta', 120 ),
('helado', 207 ),
('tarta_manzana', 316),
('gelatina_frutas', 62),
('tiramisu', 280 ),
('flan', 153 ),
('crema_cacahuate',400),
('pudin_vainilla',174),
('tarta_fresa',271),
('chocolate_caliente',192),
('helado_manzana',190),
('tostadas_con_mantequilla_de_cacahuate', 200),
('torta_de_chocolate_vegana', 140),
('batido_de_frutas_con_leche_de_almendras', 100),
('croissant', 90),
('donas_glaseadas', 150),
('galleta_vegana', 130),
('panuelo_relleno', 180);


INSERT INTO Precio(Nombre, Costo)
VALUES
('agua', 500),
('agua_con_gas', 750),
('limonada', 800),
('fresco_cas', 1200),
('fresco_tamarindo', 1300),
('fresco_guanabana', 1400),
('jugo_naranja', 1000),
('refresco', 900),
('capucchino', 1500),
('cafe', 1200),
('leche', 700),
('jugo_manzana', 950),
('zumo_uva', 1100),
('refresco_cola', 950),
('te', 800),
('refresco_naranja', 900),
('refresco_limon', 950),
('te_verde', 850),
('te_negro', 850),
('leche_chocolate', 1000),
('fresa_en_leche', 1300),
('batido_crema', 1400),
('horchata', 1200),
('te_chai_latte', 1500),
('te_con_leche', 1200),
('carne_res', 2500),
('pollo_salsa_blanca', 2000),
('pollo_salsa_jalapena', 2200),
('pollo_asado', 1800),
('pescado', 2200),
('cerdo', 2200),
('pavo', 2000),
('atun', 1800),
('salmon', 2300),
('ceviche', 1500),
('ternera', 2400),
('huevo', 600),
('tocino', 1200),
('camaron', 1700),
('pasta', 1000),
('pasta_primavera', 1400),
('avena_con_frutas', 900),
('tostadas_de_pan', 800),
('lentejas', 1100),
('ensalada', 1200),
('papas_fritas', 900),
('arroz', 850),
('vegetal_al_vapor', 1100),
('ensalada_de_tomate', 950),
('esparragos_gratinados', 1400),
('tomates_cherry', 1200),
('pure_de_papas', 900),
('macarrones_con_queso', 1200),
('pan_integral', 750),
('sopa_de_tomate', 1100),
('crema_de_brocoli', 1300),
('papas_asadas', 1000),
('queque', 1200),
('fruta', 800),
('helado', 1500),
('tarta_manzana', 1400),
('gelatina_frutas', 900),
('tiramisu', 1600),
('flan', 1300),
('crema_cacahuate', 1000),
('pudin_vainilla', 1200),
('tarta_fresa', 1400),
('chocolate_caliente', 1100),
('helado_manzana', 1400),
('tostadas_con_mantequilla_de_cacahuate', 900),
('torta_de_chocolate_vegana', 1300),
('batido_de_frutas_con_leche_de_almendras', 1200),
('croissant', 1000),
('donas_glaseadas', 800),
('galleta_vegana', 900),
('panuelo_relleno', 1100);



INSERT INTO ComboMeals(Drink, Proteins, SideDish, Dessert, Price, Calories)
VALUES
('batido_crema', 'pollo_asado', 'arroz', 'gelatina_frutas', 4000, 1500),
('refresco_cola', 'ceviche', 'papas_fritas', 'helado', 5000, 800 ),
('jugo_naranja', 'tocino', 'tostadas_de_pan', 'fruta', 3000, 5000),
('te', 'cerdo', 'ensalada', 'croissant', 3000, 1900),
('refresco', 'salmon', 'pasta', 'helado_manzana', 3500, 600),
('zumo_uva', 'pollo_salsa_jalapena','ensalada_de_tomate', 'tiramisu', 4000, 745);

INSERT INTO ParcialMeals(Proteins, SideDish, Price, Calories)
VALUES
('ternera', 'ensalada', 3500, 700),
('tocino', 'tostadas', 3000, 500),
('camaron', 'vegetales_al_vapor', 4000, 500),
('pescado', 'arroz', 3500, 600),
('pavo', 'pasta', 3500, 400);


SELECT * FROM ElementoComida
SELECT * FROM HealthyMeals
SELECT * FROM ComboMeals
SELECT * FROM ParcialMeals
SELECT * FROM Calorias
SELECT * FROM Precio

drop*from ComboMeals
drop*from ParcialMeals




