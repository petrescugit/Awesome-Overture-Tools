# Awesome-Overture-Tools
Making Overture data accessible

Downloading add data
<code>
pipx install awscli
aws configure
mkdir /mnt/f/videos
cd /mnt/f/videos
mkdir places
mkdir admins
mkdir transportation
mkdir buildings
aws s3 cp --recursive 's3://overturemaps-us-west-2/release/2023-07-26-alpha.0/theme=places/' /mnt/f/videos/places
aws s3 cp --recursive 's3://overturemaps-us-west-2/release/2023-07-26-alpha.0/theme=admins/' /mnt/h/videos/admins
aws s3 cp --recursive 's3://overturemaps-us-west-2/release/2023-07-26-alpha.0/theme=transportation/' /mnt/h/videos/transportation
aws s3 cp --recursive 's3://overturemaps-us-west-2/release/2023-07-26-alpha.0/theme=transportation/' /mnt/h/videos/buildings

</code>

**Videos** <br/>
What we know so far on the Overture Maps global dataset? (60 million places from BingMaps and Meta)  <br/>
https://www.youtube.com/watch?v=yUDt7BkYgZU <br/>
Converting Parquet files to CSV - Overture dataset (Meta and BingMaps data released)  <br/>
https://www.youtube.com/watch?v=b7WJowVFwGs <br/>

**Useful links** <br/>
Press Release: https://overturemaps.org/overture-maps-foundation-releases-first-world-wide-open-map-dataset/ <br/>
Initial Download Instructions: https://github.com/OvertureMaps/data/blob/main/README.md#how-to-access-overture-maps-data <br/>
Blog by Simon Willison: https://til.simonwillison.net/overture-maps/overture-maps-parquet <br/>
See all places on the map: https://til.simonwillison.net/overture-maps/overture-maps-parquet <br/>
