Get Glottolog data for language family, macroarea,
================
Steven Moran
13 September, 2018

Glottolog languoids data
========================

``` r
# Glottolog languoids
# https://cdstar.shh.mpg.de/bitstreams/EAEA0-E7DE-FA06-8817-0/glottolog_languoid.csv.zip
glottolog.languoid.csv <- read.csv('glottolog_languoid.csv/languoid.csv', stringsAsFactors = FALSE)
```

``` r
# Have a look at the Glottolog languoid csv data
glimpse(glottolog.languoid.csv)
```

    ## Observations: 23,740
    ## Variables: 16
    ## $ id                   <chr> "aala1237", "aant1238", "aari1238", "aari...
    ## $ family_id            <chr> "aust1307", "nucl1709", "sout2845", "sout...
    ## $ parent_id            <chr> "ramo1244", "nort2920", "ahkk1235", "aari...
    ## $ name                 <chr> "Aalawa", "Aantantara", "Aari-Gayil", "Aa...
    ## $ bookkeeping          <chr> "False", "False", "False", "False", "True...
    ## $ level                <chr> "dialect", "dialect", "family", "language...
    ## $ status               <chr> "safe", "safe", "safe", "safe", "safe", "...
    ## $ latitude             <dbl> NA, NA, NA, 5.95034, NA, -4.00679, NA, NA...
    ## $ longitude            <dbl> NA, NA, NA, 36.57210, NA, 36.86480, NA, N...
    ## $ iso639P3code         <chr> "", "", "aiz", "aiw", "aay", "aas", "", "...
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0...
    ## $ child_language_count <int> 0, 0, 2, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0...
    ## $ child_dialect_count  <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0...
    ## $ country_ids          <chr> "", "", "", "ET", "IN", "TZ", "", "", "",...

``` r
# How many levels?
table(glottolog.languoid.csv$level)
```

    ## 
    ##  dialect   family language 
    ##    10920     4339     8481

``` r
# Unique language family ids. This includes all dialects, empty family_id strings, etc.
sort(table(glottolog.languoid.csv$family_id, exclude = FALSE), decreasing = TRUE)
```

    ## 
    ## atla1278 aust1307 indo1319 sino1245 afro1255 nucl1709 pama1250 aust1305 
    ##     4663     3850     2201     1666     1259      762      598      503 
    ##          book1242 otom1299 mand1469 sign1238 drav1251 cent2225 turk1311 
    ##      429      399      338      303      259      255      251      229 
    ## taik1256 nilo1247 ural1272 japo1237 tupi1275 araw1281 nakh1245 utoa1244 
    ##      223      201      185      179      157      148      144      138 
    ## pidg1258 uncl1493 nucl1708 quec1387 algi1248 cari1283 unat1236 pano1259 
    ##      129      125      117      113      103       95       89       87 
    ## timo1261 mong1329 hmon1336 sepi1257 sali1255 maya1287 tung1282 atha1245 
    ##       86       85       84       75       68       66       65       61 
    ## nucl1710 tuca1253 lowe1437 khoe1240 chib1249 mixe1287 more1255 saha1256 
    ##       61       61       60       59       58       52       50       50 
    ## dogo1299 eski1264 ijoi1239 anim1240 nort2923 gong1255 heib1242 mixe1284 
    ##       46       46       45       44       44       43       43       43 
    ## siou1252 lake1255 maba1274 anga1289 koia1260 kart1248 nubi1251 surm1244 
    ##       41       40       40       37       37       35       35       34 
    ## nduu1242 chuk1271 east2503 miwo1274 gunw1250 kadu1256 bord1247 nyul1248 
    ##       33       32       32       30       29       28       27       24 
    ## worr1236 gumu1250 kiwa1251 chap1271 kiow1265 mail1249 namb1299 song1307 
    ##       24       23       23       22       22       21       21       21 
    ## toro1256 tuuu1241 araw1282 coch1271 daju1249 goil1242 iroq1247 sout2948 
    ##       21       21       20       20       20       20       20       20 
    ## toto1251 west2434 abkh1242 grea1241 guah1252 narr1279 yano1268 bosa1245 
    ##       20       20       19       19       19       19       19       18 
    ## geel1240 tama1329 arti1236 misu1242 choc1280 daga1274 kwer1242 pomo1273 
    ##       18       18       17       17       16       16       16       16 
    ## tebe1251 west1493 yoku1255 skoo1245 huit1251 mata1289 mirn1241 musk1252 
    ##       16       16       16       15       14       14       13       13 
    ## sout1516 waka1280 cadd1255 guai1249 koma1264 manu1261 yare1250 basq1248 
    ##       13       13       12       12       12       12       12       11 
    ## east2386 kxaa1236 left1242 nucl1580 sent1261 zapa1251 east2433 katl1246 
    ##       11       11       11       11       11       11       10       10 
    ## kore1284 kwal1257 leng1261 pauw1244 saha1239 tura1263 barb1265 beto1236 
    ##       10       10       10       10       10       10        9        9 
    ## kres1240 kuna1268 mani1293 nada1235 sena1264 sout2772 spee1234 chin1490 
    ##        9        9        9        9        9        9        9        8 
    ## chum1262 iwai1246 kere1287 maoo1243 nimb1257 nort2933 rash1249 sout2845 
    ##        8        8        8        8        8        8        8        8 
    ## tang1340 tsim1258 yeni1252 bain1263 bert1248 hara1260 hata1242 jiva1245 
    ##        8        8        8        7        7        7        7        7 
    ## kamu1264 mong1343 paho1240 piaw1238 xinc1237 yawa1259 yuat1252 zamu1243 
    ##        7        7        7        7        7        7        7        7 
    ## ainu1252 arau1255 cahu1265 chon1288 east2499 huav1256 jodi1234 maib1239 
    ##        6        6        6        6        6        6        6        6 
    ## nara1262 suki1244 yele1255 ayma1253 chiq1248 dizo1235 kama1371 katu1274 
    ##        6        6        6        5        5        5        5        5 
    ## kawe1237 mang1423 timo1237 wali1264 yuka1259 baib1250 bora1262 boro1281 
    ##        5        5        5        5        5        4        4        4 
    ## chim1311 dama1272 east1459 giim1238 kaku1242 kaya1327 kolo1268 kuli1252 
    ##        4        4        4        4        4        4        4        4 
    ## kwom1263 maid1262 mair1253 peba1241 west2604 wint1258 yana1271 abun1252 
    ##        4        4        4        4        4        4        4        3 
    ## araf1243 buru1296 cand1248 char1238 come1251 fasu1242 gily1242 jarr1235 
    ##        3        3        3        3        3        3        3        3 
    ## jira1235 kala1402 lafo1243 shas1238 tequ1244 yang1287 alse1251 amto1249 
    ##        3        3        3        3        3        3        2        2 
    ## ando1256 atak1252 bayo1259 bula1259 buna1274 cofa1242 coos1248 doso1238 
    ##        2        2        2        2        2        2        2        2 
    ## east2374 fuln1247 fura1235 garr1260 haid1248 hibi1242 hrus1242 huar1251 
    ##        2        2        2        2        2        2        2        2 
    ## hurr1239 inan1242 iran1263 jara1244 jica1245 kari1254 kibi1239 kolp1236 
    ##        2        2        2        2        2        2        2        2 
    ## kond1302 laal1242 lenc1239 lepk1239 limi1242 marr1257 momb1255 monu1249 
    ##        2        2        2        2        2        2        2        2 
    ## mpur1239 naml1239 nort1442 nort1547 nyim1244 otom1276 paez1247 pala1350 
    ##        2        2        2        2        2        2        2        2 
    ## pawa1255 pele1245 puri1261 sech1236 soma1242 sout1293 tabo1241 tara1323 
    ##        2        2        2        2        2        2        2        2 
    ## taul1250 teme1251 ticu1244 timu1245 tini1245 uruc1242 west1503 xuku1239 
    ##        2        2        2        2        2        2        2        2 
    ## yuki1242 yura1255 aika1237 apma1241 pira1253 pura1257 siam1242 wadj1254 
    ##        2        2        1        1        1        1        1        1

Language families and their Glottocodes for language
====================================================

``` r
# Just family ids and Glottocodes
families.glottocodes <- glottolog.languoid.csv %>% filter(level == "language") %>% filter(family_id != "")
glimpse(families.glottocodes)
```

    ## Observations: 8,293
    ## Variables: 16
    ## $ id                   <chr> "aari1239", "aari1240", "aasa1238", "abad...
    ## $ family_id            <chr> "sout2845", "book1242", "afro1255", "aust...
    ## $ parent_id            <chr> "aari1238", "book1242", "unun9872", "west...
    ## $ name                 <chr> "Aari", "Aariya", "Aasax", "Abadi", "Abag...
    ## $ bookkeeping          <chr> "False", "True", "False", "False", "False...
    ## $ level                <chr> "language", "language", "language", "lang...
    ## $ status               <chr> "safe", "safe", "extinct", "safe", "criti...
    ## $ latitude             <dbl> 5.950340, NA, -4.006790, -9.033890, -6.12...
    ## $ longitude            <dbl> 36.57210, NA, 36.86480, 146.99200, 145.66...
    ## $ iso639P3code         <chr> "aiw", "aay", "aas", "kbt", "abg", "abf",...
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...
    ## $ child_language_count <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...
    ## $ child_dialect_count  <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 2,...
    ## $ country_ids          <chr> "ET", "IN", "TZ", "PG", "PG", "MY", "MY",...

Language families and their Glottocodes counts
==============================================

``` r
# Family ids and Glottocode counts
families.counts <- families.glottocodes %>% group_by(family_id) %>% summarize(count=n()) %>% arrange(desc(count))
dim(families.counts)
```

    ## [1] 241   2

Isolates
========

``` r
# Get language isolates
isolates <- glottolog.languoid.csv %>% filter(family_id == "") %>% filter(parent_id == "") %>% filter(level=="language")
glimpse(isolates) # 188
```

    ## Observations: 188
    ## Variables: 16
    ## $ id                   <chr> "abin1243", "abis1238", "abun1252", "adai...
    ## $ family_id            <chr> "", "", "", "", "", "", "", "", "", "", "...
    ## $ parent_id            <chr> "", "", "", "", "", "", "", "", "", "", "...
    ## $ name                 <chr> "Abinomn", "Aewa", "Abun", "Adai", "Aikan...
    ## $ bookkeeping          <chr> "False", "False", "False", "False", "Fals...
    ## $ level                <chr> "language", "language", "language", "lang...
    ## $ status               <chr> "definitely endangered", "extinct", "defi...
    ## $ latitude             <dbl> -2.922810, -0.693860, -0.570730, 31.63140...
    ## $ longitude            <dbl> 138.89100, -75.21830, 132.41600, -92.0059...
    ## $ iso639P3code         <chr> "bsa", "ash", "kgr", "xad", "tba", "aes",...
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N...
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...
    ## $ child_language_count <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...
    ## $ child_dialect_count  <int> 0, 0, 3, 0, 1, 2, 0, 2, 0, 1, 0, 0, 2, 0,...
    ## $ country_ids          <chr> "ID", "PE", "ID", "US", "BR", "US", "CO",...

Marcoareas
==========

``` r
# All languages per macroarea (and their counts) -- note names not unique
# languages.dialects.geo <- read.csv(url("https://cdstar.shh.mpg.de/bitstreams/EAEA0-E7DE-FA06-8817-0/languages_and_dialects_geo.csv"))
languages.dialects.geo <- read.csv("languages_and_dialects_geo.csv", stringsAsFactors = FALSE)
glimpse(languages.dialects.geo)
```

    ## Observations: 19,401
    ## Variables: 7
    ## $ glottocode <chr> "aala1237", "aant1238", "aari1239", "aari1240", "aa...
    ## $ name       <chr> "Aalawa", "Aantantara", "Aari", "Aariya", "Aasax", ...
    ## $ isocodes   <chr> "", "", "aiw", "aay", "aas", "", "", "", "kbt", "",...
    ## $ level      <chr> "dialect", "dialect", "language", "language", "lang...
    ## $ macroarea  <chr> "Papunesia", "Papunesia", "Africa", "Eurasia", "Afr...
    ## $ latitude   <dbl> NA, NA, 5.95034, NA, -4.00679, NA, NA, NA, -9.03389...
    ## $ longitude  <dbl> NA, NA, 36.57210, NA, 36.86480, NA, NA, NA, 146.992...

``` r
# Get Glottolog macroareas and language counts
languages.geo <- languages.dialects.geo %>% filter(level=="language") %>% filter(macroarea!="") %>% group_by(glottocode)
languages.geo
```

    ## # A tibble: 8,371 x 7
    ## # Groups:   glottocode [8,371]
    ##    glottocode name            isocodes level  macroarea latitude longitude
    ##    <chr>      <chr>           <chr>    <chr>  <chr>        <dbl>     <dbl>
    ##  1 aari1239   Aari            aiw      langu… Africa        5.95     36.6 
    ##  2 aari1240   Aariya          aay      langu… Eurasia      NA        NA   
    ##  3 aasa1238   Aasax           aas      langu… Africa       -4.01     36.9 
    ##  4 abad1241   Abadi           kbt      langu… Papunesia    -9.03    147.  
    ##  5 abag1245   Abaga           abg      langu… Papunesia    -6.12    146.  
    ##  6 abai1240   Abai Sungai     abf      langu… Papunesia     5.55    118.  
    ##  7 abai1241   Abai Tubu-Abai… ""       langu… Eurasia      NA        NA   
    ##  8 aban1242   Abanyom         abm      langu… Africa        6.31      8.63
    ##  9 abau1245   Abau            aau      langu… Papunesia    -3.97    141.  
    ## 10 abaz1241   Abaza           abq      langu… Eurasia      41.1      42.7 
    ## # ... with 8,361 more rows

``` r
table(languages.geo$macroarea)
```

    ## 
    ##        Africa     Australia       Eurasia North America     Papunesia 
    ##          2338           383          1966           784          2197 
    ## South America 
    ##           703

``` r
languages.geo.counts <- languages.geo %>% group_by(macroarea) %>% summarise(counts=n())
languages.geo.counts
```

    ## # A tibble: 6 x 2
    ##   macroarea     counts
    ##   <chr>          <int>
    ## 1 Africa          2338
    ## 2 Australia        383
    ## 3 Eurasia         1966
    ## 4 North America    784
    ## 5 Papunesia       2197
    ## 6 South America    703

``` r
save(families.glottocodes, families.counts, isolates, languages.geo, file='glottolog-families-isolates.Rdata')
```
