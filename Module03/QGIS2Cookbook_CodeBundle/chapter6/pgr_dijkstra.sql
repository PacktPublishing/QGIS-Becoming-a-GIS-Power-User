SELECT seq, id1 AS node, id2 AS edge, di.cost, the_geom
  FROM pgr_dijkstra(
    'SELECT id, source, target, cost FROM network_pgr',
    16, 9, false, false
  ) as di
JOIN network_pgr as net 
ON di.id2 = net.id