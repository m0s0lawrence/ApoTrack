# ApoTrack
## Analysis of APOBEC hairpins in coding sequences

Steps:

1. Identify APOBEC hairpin sites to use, using the survey_hairpins_rna command of [ApoHP](https://github.com/alangenb/ApoHP).

2. (optional) Filter sites to remove polymorphic/noisy sites, e.g. using panel of normals.

3. get BAM counts at these sites, using the mpileup command of [samtools](http://www.htslib.org/).

4. summarize counts to a total editing rate per 1000 sites, using [tallyedit](tallyedit.py).

e.g.

single-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.bed mysample.bam | python3 tallyedit.py
```


multi-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.bed -b bamlist.txt | python3 tallyedit.py
```



List of ApoTrack coding hairpin CAUC sites in hg19

v1.0:  [apotrack.sites.hg19.v1.0.txt](apotrack.sites.hg19.v1.0.txt)

