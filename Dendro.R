install.packages("vegan")
library(vegan)

dendata=read.delim("stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.pick.opti_mcc.shared", row.names = 2)

den2=t(dendata)
den2dist=vegdist(den2,method="bray")

denfin=hclust(den2dist,method="complete")

denfin2=as.dendrogram(denfin,edge.root="T")

pdf(file="KD_dendrogram.pdf")
plot(denfin2,ylab="Height",leaflab="none")
dev.off()

pdf(file="KD_dendrogram_labeled.pdf")
par(cex=0.5)
plot(denfin2,ylab="Height")
dev.off()


