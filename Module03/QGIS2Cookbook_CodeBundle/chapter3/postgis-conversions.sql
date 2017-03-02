-- Points to Lines
CREATE VIEW pts2line AS 
SELECT ROW_NUMBER() over (order by census_wake_2000_points .stfid) as id, stfid, ST_MakeLine(geom) as geom 
FROM census_wake_2000_points 
GROUP BY stfid;

-- Lines to Polygons
CREATE VIEW line2poly AS 
SELECT id,stfid,ST_MakePolygon(geom) as geom 
FROM pts2line;

-- Points to Polygons
CREATE VIEW pts2poly AS 
SELECT ROW_NUMBER() over (order by census_wake_2000_points .stfid) as id, stfid, ST_MakePolygon(ST_MakeLine(geom)) as geom 
FROM census_wake_2000_points 
GROUP BY stfid;

-- Dump points
CREATE VIEW pts AS
SELECT ROW_NUMBER() over (order by a.id_0) as id,id_0 as grpid,(a.a_geom).path[2] as path, ST_GeometryType((a.a_geom).geom), ((a.a_geom).geom) as geom
FROM (SELECT id_0,(ST_DumpPoints(geom)) as a_geom FROM "census_wake2000") as a;
