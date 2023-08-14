-- SQLite
/* https://www.devmedia.com.br/sqlite-o-pequeno-notavel/7249 */


/* Criando Tabelas */
/* CREATE TABLE conferentes(Id integer PRIMARY KEY AUTOINCREMENT,
nome varcaher(80) NOT NULL,
lojas_id Interger NOT NULL, FOREIGN KEY (lojas_id) REFERENCES lojas(id)
); */

/* Inserindo Valores */
INSERT INTO usuarios VALUES(2,'Rodrigo', 12345, 'usuario', 'rfsier@gmail.com');

/* Comandos SELECT */
/* SELECT f.FuncNm, c.CargoNm, f.Sal, c.Max_Sal
FROM Func f
JOIN Cargos c ON (c.CargoId = f.CargoId); */

/* SELECT f.FuncNm, c.CargoNm, f.Sal, c.Max_Sal
FROM Func f
JOIN Cargos c ON (c.CargoId = f.CargoId)
WHERE f.Sal > c.Max_Sal; */