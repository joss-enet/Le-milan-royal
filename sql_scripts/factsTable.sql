CREATE TABLE Facts(idProject INT, nameProject VARCHAR(200), state ENUM('failed', 'successful', 'canceled', 'live', 'undefined', 'suspended'), backers INT, pledged FLOAT, goal FLOAT, usd_pledged FLOAT, usd_goal FLOAT, idCountry INT, CONSTRAINT fk_idCountry FOREIGN KEY (idCountry) REFERENCES Country(idCountry) ON DELETE CASCADE ON UPDATE CASCADE, idCurrency INT, CONSTRAINT fk_idCurrency FOREIGN KEY (idCurrency) REFERENCES Currency(idCurrency) ON DELETE CASCADE ON UPDATE CASCADE, idCategory INT, CONSTRAINT fk_idCategory FOREIGN KEY (idCategory) REFERENCES Category(idCategory) ON DELETE CASCADE ON UPDATE CASCADE, idMainCategory INT,  CONSTRAINT fk_idMainCategory FOREIGN KEY (idMainCategory) REFERENCES MainCategory(idMainCategory) ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY (idProject));
INSERT OR REPLACE INTO Facts VALUES (1000002330, "The Songs of Adelaide & Abullah", "failed", 0, 0.0, 1000.0, 0.0, 1533.95, 1, 1, 1, 1);
INSERT OR REPLACE INTO Facts VALUES (1000003930, "Greeting From Earth: ZGAC Arts Capsule For ET", "failed", 15, 2421.0, 30000.0, 2421.0, 30000.0, 2, 2, 2, 2);
INSERT OR REPLACE INTO Facts VALUES (1000004038, "Where is Hank?", "failed", 3, 220.0, 45000.0, 220.0, 45000.0, 2, 2, 2, 2);
INSERT OR REPLACE INTO Facts VALUES (1000007540, "ToshiCapital Rekordz Needs Help to Complete Album", "failed", 1, 1.0, 5000.0, 1.0, 5000.0, 2, 2, 3, 3);
INSERT OR REPLACE INTO Facts VALUES (1000011046, "Community Film Project: The Art of Neighborhood Filmmaking", "canceled", 14, 1283.0, 19500.0, 1283.0, 19500.0, 2, 2, 4, 2);
INSERT OR REPLACE INTO Facts VALUES (1000014025, "Monarch Espresso Bar", "successful", 224, 52375.0, 50000.0, 52375.0, 50000.0, 2, 2, 5, 4);
INSERT OR REPLACE INTO Facts VALUES (1000023410, "Support Solar Roasted Coffee & Green Energy!  SolarCoffee.co", "successful", 16, 1205.0, 1000.0, 1205.0, 1000.0, 2, 2, 6, 4);
INSERT OR REPLACE INTO Facts VALUES (1000030581, "Chaser Strips. Our Strips make Shots their B*tch!", "failed", 40, 453.0, 25000.0, 453.0, 25000.0, 2, 2, 7, 4);
INSERT OR REPLACE INTO Facts VALUES (1000034518, "SPIN - Premium Retractable In-Ear Headphones with Mic", "canceled", 58, 8233.0, 125000.0, 8233.0, 125000.0, 2, 2, 8, 5);
INSERT OR REPLACE INTO Facts VALUES (100004195, "STUDIO IN THE SKY - A Documentary Feature Film (Canceled)", "canceled", 43, 6240.57, 65000.0, 6240.57, 65000.0, 2, 2, 9, 2);