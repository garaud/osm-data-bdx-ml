
-- routes
with roads as (
  select abs(osm_id) as osm_id
    , building
    , name
    , way as geom
  from planet_osm_roads
  order by st_length(way) desc
  )

select r.osm_id
  , name
  , elem
  , version
  , n_user
  , n_autocorr
  , n_corr
  , first_at
  , last_at
  , last_uid
  , last_ug
  , st_transform(r.geom, 4326) as geom
from roads as r
  join osmq.element using(osm_id)
 ;
