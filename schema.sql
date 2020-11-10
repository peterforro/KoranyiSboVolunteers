CREATE TABLE Accounts(
    ID SERIAL PRIMARY KEY    NOT NULL,
    FIRSTNAME    VARCHAR(100)    NOT NULL,
    LASTNAME     VARCHAR(100)    NOT NULL,
    EMAIL VARCHAR(100)  NOT NULL
);


INSERT INTO Accounts (firstname, lastname, email) VALUES('Mate', 'Balint', 'matebalint98@gmail.com');
INSERT INTO Accounts (firstname, lastname, email) VALUES('Peter', 'Forro', 'forropcs@gmail.com');