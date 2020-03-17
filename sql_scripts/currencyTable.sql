CREATE TABLE Currency(idCurrency INTEGER, code VARCHAR(3), name VARCHAR(25), changeRate FLOAT, PRIMARY KEY (idCurrency));
INSERT OR REPLACE INTO Currency VALUES (1, "GBP", "Great British Pound", 1.23);
INSERT OR REPLACE INTO Currency VALUES (2, "USD", "US Dollar", 1.0);
INSERT OR REPLACE INTO Currency VALUES (3, "CAD", "Canadian Dollar", 0.72);
INSERT OR REPLACE INTO Currency VALUES (4, "AUD", "Australian Dollar", 0.61);
INSERT OR REPLACE INTO Currency VALUES (5, "NOK", "Norwegian Krone", 0.1);
INSERT OR REPLACE INTO Currency VALUES (6, "EUR", "Euro", 1.11);
INSERT OR REPLACE INTO Currency VALUES (7, "MXN", "Mexican Peso", 0.04);
INSERT OR REPLACE INTO Currency VALUES (8, "SEK", "Swedish Krona", 0.1);
INSERT OR REPLACE INTO Currency VALUES (9, "NZD", "New Zealand Dollar", 0.61);
INSERT OR REPLACE INTO Currency VALUES (10, "CHF", "Swiss Franc", 1.06);
INSERT OR REPLACE INTO Currency VALUES (11, "DKK", "Danish Krone", 0.15);
INSERT OR REPLACE INTO Currency VALUES (12, "HKD", "Hong Kong Dollar", 0.13);
INSERT OR REPLACE INTO Currency VALUES (13, "SGD", "Singapore Dollar", 0.7);
INSERT OR REPLACE INTO Currency VALUES (14, "JPY", "Japanese Yen", 0.0095);