--Points to Lines
--Create table grouping points with shared stfid into lines
CREATE Table census_pts2lines AS 
SELECT stfid,MakeLine(geom) as geom 
FROM census_wake_2000_points 
GROUP BY stfid; 

--Register the new table's geometry so QGIS knows its a spatial layer
SELECT RecoverGeometryColumn('census_pts2lines','geom',3358,'LINESTRING',2);


--Lines to Polygons
--Create table grouping lines with shared stfid into polygons
CREATE Table census_line2poly AS 
SELECT stfid,ST_Polygonize(geom) as geom 
FROM census_pts2lines 
GROUP BY stfid; 
2. Register the new table as Spatial.
--Register the new table's geometry so QGIS knows its a spatial layer
SELECT RecoverGeometryColumn('census_line2poly','geom',3358,'POLYGON',2);
