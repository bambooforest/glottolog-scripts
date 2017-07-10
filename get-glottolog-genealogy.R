# Get Glottolog genealogy
# Original code adapted from Taras Zakharko

library(phytools)  # for robust version of read.newick
glottolog.trees <- read.newick('http://glottolog.org/static/trees/tree-glottolog-newick.txt')
# Transform into a dataframe
source('https://raw.githubusercontent.com/IVS-UZH/phylo-convert/master/phylo-convert.R')
glottolog.df.tmp <- as.data.frame(glottolog.trees)
# and collect glottocodes from all possible taxonomic levels because we can't know in advance for which level we have data (glottolog resolves into dialects etc)
glottolog.df <- as.data.frame(apply(glottolog.df.tmp, 2, function(x) gsub("'","",x)))
glottolog.full.with.code <- NULL
# run though all columns and create versions with the item in that columns as the key; all lower taxons will be set to NA:
for(column.id in 1:ncol(glottolog.df))
{
  # take the full copy of data (but only if the column is not NA)
  units <- glottolog.df[!is.na(glottolog.df[, column.id]), ]
  if(nrow(units) == 0) next
  # set all the columns after 'column' to NA and make all rows unique
  # this will leave the rows which actually describe the current column
  if(column.id < ncol(glottolog.df)) units[, -(1:column.id)] <- NA
  units <- unique(units)
  units$glottolog.language <- units[, column.id]
  glottolog.full.with.code <- rbind(glottolog.full.with.code, units)
}
glottolog.full.with.code$glottocode <- gsub('^.*\\[(.+[0-9])\\].*$', '\\1', glottolog.full.with.code$glottolog.language)
head(glottolog.full.with.code); dim(glottolog.full.with.code)
save(glottolog.full.with.code, file="glottolog-full-with-code.Rdata")

# Sanity checks... damn it there are duplicates! Dropping them for now.
library(dplyr)
glottolog.full.with.code %>% filter(glottocode=="stan1295") # Level 19: Indo-European [indo1319]
glottolog.full.with.code[duplicated(glottolog.full.with.code$glottocode, fromLast = TRUE),] %>% arrange(glottocode)
glottolog.full.with.code[duplicated(glottolog.full.with.code$glottocode, fromLast = FALSE),]
glottolog.full.with.code %>% filter(glottocode=="abin1243") # Returns 2 rows.
glottolog.full.with.code %>% filter(glottocode=="kibi1239") # Returns 2 rows.
glottolog.full.with.code %>% filter(glottocode=="pele1245") # Returns 2 rows.


tmp <- glottolog.full.with.code[!duplicated(glottolog.full.with.code$glottocode),]
tmp[duplicated(tmp$glottocode),] # 0
tmp[duplicated(tmp$glottolog.language),] # 0
# These Glottolog codes don't appear in the Glottolog trees.
pcsal %>% filter(Glottocode=="stan1325") # Standard Latvian
tmp %>% filter(glottocode=="stan1325")
pcsal %>% filter(Glottocode=="ishk1246") # Ishkashimi
tmp %>% filter(glottocode=="ishk1246")
