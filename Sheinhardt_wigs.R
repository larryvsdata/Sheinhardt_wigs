
# Crime Rate

#Principal Component Analysis

CrimeRate <- read.csv("CrimeRate.csv", header=TRUE)



library(gclus)
my.abs     <- abs(cor(CrimeRate[,-1]))
my.colors  <- dmat.color(my.abs)
my.ordered <- order.single(cor(CrimeRate[,-1]))
cpairs(CrimeRate, my.ordered, panel.colors=my.colors, gap=0.5)


CrimeRate.pca<-princomp(CrimeRate,scores=T,cor=T)
screeplot(CrimeRate.pca,main="Scree Plot",xlab="Componets")

summary(CrimeRate.pca)

plot(CrimeRate.pca,main="Scree Plot",xlab="Componets")
biplot(CrimeRate.pca)


CrimeRate.pca$loadings

CrimeRate.fa<-factanal(CrimeRate,factors=2)
CrimeRate.fa


###############


VCR <- read.csv("VCR.csv", header=TRUE)



library(gclus)
my.abs     <- abs(cor(VCR[,-1]))
my.colors  <- dmat.color(my.abs)
my.ordered <- order.single(cor(VCR[,-1]))
cpairs(VCR, my.ordered, panel.colors=my.colors, gap=0.5)


VCR.pca<-princomp(VCR,scores=T,cor=T)
screeplot(VCR.pca,main="Scree Plot",xlab="Componets")

summary(VCR.pca)

plot(VCR.pca,main="Scree Plot",xlab="Componets")
biplot(VCR.pca)


VCR.pca$loadings

VCR.fa<-factanal(VCR,factors=2)

