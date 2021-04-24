Get language counts from Glottolog for language family and macroarea
================
Steven Moran

24 April, 2021

This script loads the [Glottolog](https://glottolog.org) data and
extracts various counts.

``` r
library(tidyverse)
```

Get the Glottolog languoids data.

``` r
# https://cdstar.shh.mpg.de/bitstreams/EAEA0-D501-DBB8-65C4-0/glottolog_languoid.csv.zip
languoids <- read.csv("glottolog_languoid/languoid.csv", stringsAsFactors = FALSE)
```

How does it look?

``` r
glimpse(languoids)
```

    ## Rows: 25,439
    ## Columns: 15
    ## $ id                   <chr> "3adt1234", "aala1237", "aant1238", "aari1238", "…
    ## $ family_id            <chr> "afro1255", "aust1307", "nucl1709", "sout2845", "…
    ## $ parent_id            <chr> "nort3292", "ramo1244", "nort2920", "ahkk1235", "…
    ## $ name                 <chr> "3Ad-Tekles", "Aalawa", "Aantantara", "Aari-Gayil…
    ## $ bookkeeping          <chr> "False", "False", "False", "False", "False", "Tru…
    ## $ level                <chr> "dialect", "dialect", "dialect", "family", "langu…
    ## $ latitude             <dbl> NA, NA, NA, NA, 5.950340, NA, -4.006790, NA, NA, …
    ## $ longitude            <dbl> NA, NA, NA, NA, 36.57210, NA, 36.86480, NA, NA, N…
    ## $ iso639P3code         <chr> "", "", "", "aiz", "aiw", "aay", "aas", "", "", "…
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, …
    ## $ child_language_count <int> 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, …
    ## $ child_dialect_count  <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0, …
    ## $ country_ids          <chr> "", "", "", "", "ET", "IN", "TZ", "", "", "", "",…

How many levels are in `level`?

``` r
table(languoids$level)
```

    ## 
    ##  dialect   family language 
    ##    12414     4509     8516

Unique language family ids. This includes all dialects, empty family\_id
strings, etc.

``` r
sort(table(languoids$family_id, exclude = FALSE), decreasing = TRUE)
```

    ## 
    ## atla1278 aust1307 indo1319 sino1245 afro1255 nucl1709 pama1250 aust1305 
    ##     4791     3901     2922     1784     1389      800      608      514 
    ##          book1242 otom1299 mand1469 sign1238 drav1251 cent2225 turk1311 
    ##      425      392      362      319      280      266      262      250 
    ## taik1256 nilo1247 ural1272 japo1237 araw1281 nakh1245 tupi1275 utoa1244 
    ##      238      204      197      179      175      160      159      147 
    ## atha1245 quec1387 pidg1258 nucl1708 uncl1493 algi1248 sali1255 cari1283 
    ##      137      134      133      130      123      107      107       96 
    ## tung1282 mong1349 pano1259 unat1236 timo1261 hmon1336 sepi1257 khoe1240 
    ##       93       90       88       88       86       84       78       69 
    ## maya1287 tuca1253 nucl1710 chib1249 lowe1437 more1255 saha1256 eski1264 
    ##       66       64       61       58       58       50       50       48 
    ## dogo1299 ijoi1239 anim1240 nort2923 gong1255 heib1242 mixe1284 siou1252 
    ##       46       45       44       44       43       43       43       41 
    ## lake1255 maba1274 anga1289 koia1260 kart1248 nubi1251 chuk1271 surm1244 
    ##       40       40       37       37       35       35       34       34 
    ## nduu1242 tuuu1241 east2503 arti1236 miwo1274 gunw1250 kadu1256 bord1247 
    ##       33       33       32       31       30       29       28       27 
    ## iroq1247 yano1268 nyul1248 worr1236 gumu1250 kiwa1251 skoo1245 song1307 
    ##       26       26       24       24       23       23       23       23 
    ## chap1271 kiow1265 koma1264 mixe1287 namb1299 toro1256 araw1282 coch1271 
    ##       22       22       22       21       21       21       20       20 
    ## daju1249 goil1242 sout2948 toto1251 west2434 abkh1242 guah1252 mail1249 
    ##       20       20       20       20       20       19       19       19 
    ## narr1279 bosa1245 geel1240 grea1241 tama1329 misu1242 choc1280 daga1274 
    ##       19       18       18       18       18       17       16       16 
    ## kwer1242 pomo1273 sout1516 tebe1251 west1493 yoku1255 araf1243 kera1258 
    ##       16       16       16       16       16       16       15       15 
    ## kore1284 spee1234 huit1251 mata1289 east2386 mirn1241 musk1252 waka1280 
    ##       15       15       14       14       13       13       13       13 
    ## cadd1255 guai1249 kxaa1236 manu1261 nada1235 sent1261 yare1250 basq1248 
    ##       12       12       12       12       12       12       12       11 
    ## kres1240 left1242 nucl1580 yeni1252 zapa1251 east2433 katl1246 kwal1257 
    ##       11       11       11       11       11       10       10       10 
    ## leng1261 pauw1244 saha1239 tura1263 barb1265 beto1236 chin1490 kuna1268 
    ##       10       10       10       10        9        9        9        9 
    ## mani1293 sena1264 sout2772 chum1262 iwai1246 kere1287 maoo1243 nimb1257 
    ##        9        9        9        8        8        8        8        8 
    ## nort2933 rash1249 sout2845 tang1340 tsim1258 wint1258 yama1264 bain1263 
    ##        8        8        8        8        8        8        8        7 
    ## bert1248 chiq1253 hara1260 hata1242 jiva1245 kamu1264 paho1240 piaw1238 
    ##        7        7        7        7        7        7        7        7 
    ## xinc1237 yawa1259 yuat1252 zamu1243 ainu1252 arau1255 ayma1253 cahu1265 
    ##        7        7        7        7        6        6        6        6 
    ## chon1288 east2499 huav1256 jodi1234 maib1239 nara1262 nivk1234 suki1244 
    ##        6        6        6        6        6        6        6        6 
    ## yele1255 dizo1235 kama1371 katu1274 kawe1237 mang1423 timo1237 wali1264 
    ##        6        5        5        5        5        5        5        5 
    ## yuka1259 yuki1242 baib1250 bora1262 boro1281 chim1311 dama1272 east1459 
    ##        5        5        4        4        4        4        4        4 
    ## garr1260 giim1238 kaku1242 kari1254 kaya1327 kolo1268 kuli1252 kwom1263 
    ##        4        4        4        4        4        4        4        4 
    ## maid1262 mair1253 peba1241 west2604 yana1271 abun1252 buru1296 cand1248 
    ##        4        4        4        4        4        3        3        3 
    ## char1238 come1251 fasu1242 hrus1242 jarr1235 jira1235 kala1402 lafo1243 
    ##        3        3        3        3        3        3        3        3 
    ## lepk1239 shas1238 tequ1244 yang1287 alse1251 amto1249 ando1256 anem1249 
    ##        3        3        3        3        2        2        2        2 
    ## arut1244 atak1252 bayo1259 bula1259 buna1274 cofa1242 coos1248 doso1238 
    ##        2        2        2        2        2        2        2        2 
    ## east2374 fuln1247 fura1235 guam1236 haid1248 hibi1242 huar1251 hurr1239 
    ##        2        2        2        2        2        2        2        2 
    ## inan1242 iran1263 jara1244 jica1245 kaur1274 kibi1239 kolp1236 kond1302 
    ##        2        2        2        2        2        2        2        2 
    ## laal1242 lenc1239 limi1242 marr1257 momb1255 monu1249 mpur1239 naml1239 
    ##        2        2        2        2        2        2        2        2 
    ## nort1442 nort1547 nyim1244 otom1276 paez1247 pala1350 pawa1255 pele1245 
    ##        2        2        2        2        2        2        2        2 
    ## puri1261 sech1236 soma1242 sout1293 tabo1241 tall1235 tara1323 taul1250 
    ##        2        2        2        2        2        2        2        2 
    ## teme1251 ticu1244 timu1245 tini1245 uruc1242 west1503 xuku1239 yura1255 
    ##        2        2        2        2        2        2        2        2 
    ## aika1237 pira1253 pura1257 siam1242 wadj1254 
    ##        1        1        1        1        1

Get just the language level families and their glottocodes.

``` r
families_glottocodes <- languoids %>% filter(level == "language") %>% filter(family_id != "")
glimpse(families_glottocodes)
```

    ## Rows: 8,335
    ## Columns: 15
    ## $ id                   <chr> "aari1239", "aari1240", "aasa1238", "abad1241", "…
    ## $ family_id            <chr> "sout2845", "book1242", "afro1255", "aust1307", "…
    ## $ parent_id            <chr> "aari1238", "book1242", "sout3054", "west2850", "…
    ## $ name                 <chr> "Aari", "Aariya", "Aasax", "Abadi", "Abaga", "Aba…
    ## $ bookkeeping          <chr> "False", "True", "False", "False", "False", "Fals…
    ## $ level                <chr> "language", "language", "language", "language", "…
    ## $ latitude             <dbl> 5.950340, NA, -4.006790, -9.033890, -6.120280, 5.…
    ## $ longitude            <dbl> 36.57210, NA, 36.86480, 146.99200, 145.66500, 118…
    ## $ iso639P3code         <chr> "aiw", "aay", "aas", "kbt", "abg", "abf", "", "ab…
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0…
    ## $ child_language_count <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0…
    ## $ child_dialect_count  <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 2, 0, 3, 0…
    ## $ country_ids          <chr> "ET", "IN", "TZ", "PG", "PG", "MY", "MY", "NG", "…

Get language families and their glottocode counts.

``` r
families_counts <- families_glottocodes %>% group_by(family_id) %>% summarize(count = n()) %>% arrange(desc(count))
```

There are these many language families in Glottolog – that are not
language isolates.

``` r
head(families_counts)
```

    ## # A tibble: 6 x 2
    ##   family_id count
    ##   <chr>     <int>
    ## 1 atla1278   1436
    ## 2 aust1307   1276
    ## 3 indo1319    588
    ## 4 sino1245    496
    ## 5 book1242    392
    ## 6 afro1255    375

``` r
dim(families_counts)
```

    ## [1] 244   2

Get the language isolates.

``` r
isolates <- languoids %>% filter(family_id == "") %>% filter(parent_id == "") %>% filter(level == "language")
```

There are these many isolates in Glottolog.

``` r
glimpse(isolates)
```

    ## Rows: 181
    ## Columns: 15
    ## $ id                   <chr> "abin1243", "abis1238", "abun1252", "adai1235", "…
    ## $ family_id            <chr> "", "", "", "", "", "", "", "", "", "", "", "", "…
    ## $ parent_id            <chr> "", "", "", "", "", "", "", "", "", "", "", "", "…
    ## $ name                 <chr> "Abinomn", "Aewa", "Abun", "Adai", "Aikanã", "Als…
    ## $ bookkeeping          <chr> "False", "False", "False", "False", "False", "Fal…
    ## $ level                <chr> "language", "language", "language", "language", "…
    ## $ latitude             <dbl> -2.922810, -1.284096, -0.570730, 31.631400, -12.6…
    ## $ longitude            <dbl> 138.89100, -75.08441, 132.41600, -92.00590, -60.5…
    ## $ iso639P3code         <chr> "bsa", "ash", "kgr", "xad", "tba", "aes", "ana", …
    ## $ description          <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ markup_description   <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ child_family_count   <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0…
    ## $ child_language_count <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0…
    ## $ child_dialect_count  <int> 0, 0, 3, 0, 1, 2, 0, 2, 2, 2, 0, 2, 0, 11, 0, 7, …
    ## $ country_ids          <chr> "ID", "PE", "ID", "US", "BR", "US", "CO", "CO", "…

Let’s combine the isolates into the language family counts.

``` r
isolates_counts <- isolates %>% select(id) %>% rename(family_id = id)
isolates_counts$count <- 1
families_counts <- rbind(families_counts, isolates_counts)
```

There are this many language families, with isolates, reported in
Glottolog.

``` r
glimpse(families_counts)
```

    ## Rows: 425
    ## Columns: 2
    ## $ family_id <chr> "atla1278", "aust1307", "indo1319", "sino1245", "book1242", …
    ## $ count     <dbl> 1436, 1276, 588, 496, 392, 375, 316, 248, 196, 181, 156, 123…

``` r
length(unique(families_counts$family_id))
```

    ## [1] 425

Access the languages and dialects geo data from Glottolog.

``` r
# languages_and_dialects_geo <- read_csv(url("https://cdstar.shh.mpg.de/bitstreams/EAEA0-D501-DBB8-65C4-0/languages_and_dialects_geo.csv"))
languages_and_dialects_geo <- read_csv("glottolog_languoid/languages_and_dialects_geo.csv")
```

``` r
glimpse(languages_and_dialects_geo)
```

    ## Rows: 20,930
    ## Columns: 7
    ## $ glottocode <chr> "3adt1234", "aala1237", "aant1238", "aari1239", "aari1240",…
    ## $ name       <chr> "3Ad-Tekles", "Aalawa", "Aantantara", "Aari", "Aariya", "Aa…
    ## $ isocodes   <chr> NA, NA, NA, "aiw", "aay", "aas", NA, NA, NA, "kbt", NA, "ab…
    ## $ level      <chr> "dialect", "dialect", "dialect", "language", "language", "l…
    ## $ macroarea  <chr> "Africa", "Papunesia", "Papunesia", "Africa", "Eurasia", "A…
    ## $ latitude   <dbl> NA, NA, NA, 5.950340, NA, -4.006790, NA, NA, NA, -9.033890,…
    ## $ longitude  <dbl> NA, NA, NA, 36.57210, NA, 36.86480, NA, NA, NA, 146.99200, …

Get Glottolog macroareas and their language counts.

``` r
languages_geo <- languages_and_dialects_geo %>% filter(level == "language") %>% filter(macroarea != "") %>% group_by(glottocode)
```

``` r
head(languages_geo)
```

    ## # A tibble: 6 x 7
    ## # Groups:   glottocode [6]
    ##   glottocode name        isocodes level    macroarea latitude longitude
    ##   <chr>      <chr>       <chr>    <chr>    <chr>        <dbl>     <dbl>
    ## 1 aari1239   Aari        aiw      language Africa        5.95      36.6
    ## 2 aari1240   Aariya      aay      language Eurasia      NA         NA  
    ## 3 aasa1238   Aasax       aas      language Africa       -4.01      36.9
    ## 4 abad1241   Abadi       kbt      language Papunesia    -9.03     147. 
    ## 5 abag1245   Abaga       abg      language Papunesia    -6.12     146. 
    ## 6 abai1240   Abai Sungai abf      language Papunesia     5.55     118.

``` r
table(languages_geo$macroarea)
```

    ## 
    ##        Africa     Australia       Eurasia North America     Papunesia 
    ##          2348           386          1971           788          2209 
    ## South America 
    ##           711

``` r
macroarea_counts <- languages_geo %>% group_by(macroarea) %>% summarise(counts = n())
```

``` r
macroarea_counts
```

    ## # A tibble: 6 x 2
    ##   macroarea     counts
    ##   <chr>          <int>
    ## 1 Africa          2348
    ## 2 Australia        386
    ## 3 Eurasia         1971
    ## 4 North America    788
    ## 5 Papunesia       2209
    ## 6 South America    711

Save the counts.

``` r
save(families_counts, macroarea_counts, file = "glottolog-counts.RData")
```
