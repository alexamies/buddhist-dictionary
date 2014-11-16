# A script to generate images for statistics on the NTI Corpus

# Read the data files
names <- c("pos.tagged.text", "element.text", "word.id", "frequency")
unigram <- read.table("data/dictionary/unigram.txt", header=FALSE, sep="\t", quote="\"", col.names=names, numerals ="allow.loss")
corpusstats <- read.table("data/stats/corpus_stats.txt", sep="\t", quote="\"", numerals ="allow.loss", header=TRUE)

# Plot of a huge number of unigram word frequencies
x <- seq(1, length(unigram$frequency))
png(filename="web/images/unigram_frequency.png", width = 400, height = 400)
plot(x, unigram$frequency, xlab="", ylab="Frequency", pch=20, col="blue")
dev.off()

# Histogram highlighting the frequency of the top few words
library(showtext)
freq <- as.vector(as.matrix(unigram[4])[1:8, 1])
freq.labels <- as.vector(as.matrix(unigram[2])[1:8, 1])
png(filename="web/images/ungram_barplot.png", width = 400, height = 400)
showtext.begin()
barplot(freq, names.arg=freq.labels, ylab="Frequency", col="steelblue")
showtext.end()
dev.off()

# Plot of variation of Unique Words with Text Size
png(filename="web/images/unique_words.png", width = 400, height = 400)
plot(corpusstats$word.count, corpusstats$unique.words, xlab="Word Count", ylab="Unique Words", pch=17, col="blue")
dev.off()

# Generic plot of Binomial Distribution with Parameters n = 20 and p = 0.5
x <- seq(1, 20)
png(filename="web/images/binomial05.png", width = 400, height = 400)
plot(x, dbinom(x, 20, 0.5), xlab="x", ylab="Frequency", pch=17, col="blue")
dev.off()

# Generic plot of Poisson Distribution with λ = 3.0
x <- seq(1, 10)
png(filename="web/images/poisson_lambda3.png", width = 400, height = 400)
plot(x, dpois(x, 3.0), xlab="x", ylab="Frequency", pch=17, col="blue")
dev.off()

# Linear Regression of Log Count of Unique Words versus Log of Text Length
x <- log(corpusstats$word.count)
y <- log(corpusstats$unique.words)
unique.lm <- lm(y ~ x)
png(filename="web/images/log_unique_words.png", width = 400, height = 400)
plot(x, y, xlab="Log Word Count", ylab="Log Unique Words", pch=17, col="blue")
abline(unique.lm)
dev.off()