CREATE TABLE IF NOT EXISTS Отдел(
    id SERIAL PRIMARY KEY,
    название_отдела VARCHAR(40) NOT NULL
)


CREATE TABLE IF NOT EXISTS Начальник(
    id SERIAL PRIMARY KEY,
    имя VARCHAR(40) NOT NULL,
    id_отдела INTEGER NOT NULL REFERENCES Отдел(id),
)

CREATE TABLE IF NOT EXISTS Сотрудник(
    id SERIAL PRIMARY KEY,
    имя VARCHAR(40) NOT NULL,
    id_отдела INTEGER NOT NULL REFERENCES Отдел(id),
    id_начальника INTEGER NOT NULL REFERENCES Начальник(id)
)