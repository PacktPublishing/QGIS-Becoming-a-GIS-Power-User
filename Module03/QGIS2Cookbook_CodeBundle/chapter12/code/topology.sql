-- Create table with overlapping linestring geometries
CREATE TABLE lines(
  id       serial primary key,
  name     varchar(6),
  geom     geometry(LINESTRING,4326)
);


-- Add a set of linestrings to the table, like this
--
--   |      |      |
-- -------------------
--   |      |      |
-- -------------------
--   |      |      |

INSERT INTO lines VALUES(
  DEFAULT,
  'top',
  ST_Setsrid(ST_Makeline(ST_Makepoint(175,-44),ST_Makepoint(179,-44)),4326)
);

INSERT INTO lines VALUES(
  DEFAULT,
  'bottom',
  ST_Setsrid(ST_Makeline(ST_Makepoint(175,-45),ST_Makepoint(179,-45)),4326)
);

INSERT INTO lines VALUES(
  DEFAULT,
  'left',
  ST_Setsrid(ST_Makeline(ST_Makepoint(176,-43),ST_Makepoint(176,-46)),4326)
);

INSERT INTO lines VALUES(
  DEFAULT,
  'middle',
  ST_Setsrid(ST_Makeline(ST_Makepoint(177,-43),ST_Makepoint(177,-46)),4326)
);

INSERT INTO lines VALUES(
  DEFAULT,
  'right',
  ST_Setsrid(ST_Makeline(ST_Makepoint(178,-43),ST_Makepoint(178,-46)),4326)
);

-- Create new empty topology structure
SELECT CreateTopology('topo1',4326,0);

-- Add all linestrings to topology in one operation as a collection
-- Creates topology like this (X = polygons - faces, + = nodes)
--   +   +   +
--   |   |   |
-- +-+---+---+--+
--   | X | X |
-- +-+---+---+--+
--   |   |   |
--   +   +   +

SELECT ST_CreateTopoGeo('topo1',ST_Collect(geom)) FROM lines;

-- Add isolated node
SELECT AddNode('topo1', ST_Setsrid(ST_Makepoint(175.0,-43.0),4326));
