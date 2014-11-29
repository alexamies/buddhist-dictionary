# Script to compute the counts of different parts of speech in the tagged
# versions of several text document and check the independence of the data.

names <- c("word")
heart <- read.table("web/corpus/tagged/heart-sutra-xuanzang-tagged.txt", 
	                header=FALSE, sep="\t", quote="\"", col.names=names, 
	                numerals ="allow.loss")
amitabha <- read.table("web/corpus/tagged/amitabha-sutra-kumarajiva-tagged.txt", 
	                header=FALSE, sep="\t", quote="\"", col.names=names, 
	                numerals ="allow.loss")
diamond <- read.table("web/corpus/tagged/diamond-sutra-taisho-tagged.txt", 
	                header=FALSE, sep="\t", quote="\"", col.names=names, 
	                numerals ="allow.loss")
pos.symbols <- c("/VA\\[", "(/VC\\[|/VE\\[)", "/VV\\[", "/NR\\[", 
	             "(/NT\\[|/NN\\[)", "(/LC\\[|/PN\\[|/DT\\[|/CD\\[|/OD\\[|/M\\[)", "/AD\\[", 
	             "(/P\\[|/CC\\[|/CS\\[|/DEC\\[|/DEG\\[|/DER\\[|/DEV\\[]|/SP\\[|/AS\\[|/ETC\\[]|/MSP\\[|/IJ\\[|/ON\\[|/PU\\[|/JJ\\[|/FW\\[|/LB\\[|/SB\\[|/BA\\[])")
heart.count <- vector(mode = "numeric", length = length(pos.symbols))
amitabha.count <- vector(mode = "numeric", length = length(pos.symbols))
diamond.count <- vector(mode = "numeric", length = length(pos.symbols))
for (i in seq(1:length(pos.symbols))) {
	heart.count[i] <- length(grep(pos.symbols[i], heart$word))
	amitabha.count[i] <- length(grep(pos.symbols[i], amitabha$word))
	diamond.count[i] <- length(grep(pos.symbols[i], diamond$word))
}
textnames <- list(c("Adjectives", "Existential Verbs", "Verbs", "Proper Nouns",
	                "Nouns", "Pronouns", "Adverbs", "Function Words"),
	              c("Heart", "Amitabha", "Diamond"))
data <- matrix(c(heart.count, amitabha.count, diamond.count), ncol = 3, 
	           dimnames = textnames)
data
chisq.test(data)