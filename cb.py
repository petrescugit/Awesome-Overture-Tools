import duckdb 
db = duckdb.connect()
db.execute("INSTALL spatial")
db.execute("INSTALL httpfs")
db.execute("""
LOAD spatial;
LOAD httpfs;
SET s3_region='us-west-2';
""")
db.execute("""
COPY (
    SELECT
           type,
           subType,
           localityType,
           adminLevel,
           isoCountryCodeAlpha2,
           JSON(names) AS names,
           JSON(sources) AS sources,
           ST_GeomFromWkb(geometry) AS geometry
      FROM read_parquet('s3://overturemaps-us-west-2/release/2023-07-26-alpha.0/theme=admins/type=*/*', filename=true, hive_partitioning=1)
     WHERE adminLevel = 2
       AND ST_GeometryType(ST_GeomFromWkb(geometry)) IN ('POLYGON','MULTIPOLYGON')
) TO '/tmp/countries.geojson'
WITH (FORMAT GDAL, DRIVER 'GeoJSON');
""")
