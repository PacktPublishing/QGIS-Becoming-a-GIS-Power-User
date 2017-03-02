-- Chapter 11, Recipe 4 QSpatialite
SELECT "census_wake2000".'pk' AS id, "census_wake2000".'geom' AS Geometry, "census_wake2000".'area', "census_wake2000".'perimeter' FROM "census_wake2000" WHERE "census_wake2000".'perimeter > 100000;
