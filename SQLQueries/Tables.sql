CREATE TABLE Meals (
    id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    drink VARCHAR(255) NOT NULL,
    protein VARCHAR(255) NOT NULL,
    sideDish VARCHAR(255) NOT NULL,
    dessert VARCHAR(255) NOT NULL,
    dayMoment VARCHAR(255) NOT NULL,
    minCalories INT NOT NULL
);
