## spacyr example with stats
# This example aggregates sentiment flags from twits messages.
# [spacyr](https://github.com/kbenoit/spacyr) is R binding of [SpaCy](https://spacy.io/), which is Python library for NLP.
# spacyr requires Python with Spacy.

library(dplyr)
library(sparklyr)

#### Connect spark
sc <- spark_connect(master = "yarn-client", config = config)

#### Tidy dataframe
austen     <- austen_books()

#### Concatinate texts per document
#
# mutate
# paste0
# rename
#
text_with_sentiment <- twits_messages() %>%
  group_by(sentiment) %>%
  mutate(text_by_book = paste0(text, collapse = " ")) %>% 
  select(book, text_by_book) %>%
  distinct() %>%
  rename(text = text_by_book)
text_by_book$doc_id <- seq.int(nrow(text_by_book))

#### Create Spark Data Frame
twits_msg_tbl <- copy_to(sc, text_by_book, overwrite = TRUE)
