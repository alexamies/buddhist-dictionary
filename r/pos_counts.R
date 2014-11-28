# Script to compute the counts of different parts of speech in the tagged
# corpus and compare to one of the documents using a chi squared goodness
# of fit test

names <- c("pos.tagged.text", "element.text", "word.id", "frequency")
unigram <- read.table("data/dictionary/unigram.txt", header=FALSE, sep="\t", 
	                  quote="\"", col.names=names, numerals ="allow.loss")
heart.names <- c("word")
heart <- read.table("web/corpus/tagged/heart-sutra-xuanzang-tagged.txt", 
	                header=FALSE, sep="\t", quote="\"", col.names=heart.names, 
	                numerals ="allow.loss")
pos.symbols <- c("VA", "VC", "VE", "VV", "NR", "NT", "NN", "LC", "PN", "DT", 
	             "CD", "CD", "OD", "M", "AD", "P", "CC", "CS", "DEG", "SP", 
	             "MSP", "IJ", "FW")
pos.count <- vector(mode = "numeric", length = length(pos.symbols))
heart.count <- vector(mode = "numeric", length = length(pos.symbols))
for (i in seq(1:length(pos.symbols))) {
	count <- sum(unigram[grep(pos.symbols[i], unigram$pos.tagged.text),4])
	if (count == 0) {
		# Manually extract counts that are zero
		print(pos.symbols[i])
	} else {
	    pos.count[i] <- count
	    heart.count[i] <- length(grep(pos.symbols[i], heart$word))
    }
}

pos.prob <- pos.count / sum(pos.count)
chisq.test(heart.count, p=pos.prob)