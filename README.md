# ApoTrack
## Analysis of APOBEC RNA editing in hairpins in coding sequences

Steps:

1. Identify APOBEC hairpin sites to use, using the ``survey_hairpins_rna`` command of [ApoHP](https://github.com/alangenb/ApoHP).

2. (optional) Filter sites to remove polymorphic/noisy sites, e.g. using dbSNP or an external panel of normals.

3. Get basecall counts at the hairpin sites from your RNA-Seq BAM file(s), using the ``mpileup`` command of [samtools](http://www.htslib.org/).

4. Summarize counts to a total editing rate for each BAM, using our small utility [tallyedit](tallyedit.py).

e.g.

single-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.v1.0.bed mysample.bam | python3 tallyedit.py
```


multi-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.v1.0.bed -b bamlist.txt | python3 tallyedit.py
```



List of ApoTrack coding hairpin CAUC sites in hg19

verson 1.0:    [apotrack.sites.hg19.v1.0.bed](apotrack.sites.hg19.v1.0.bed) 

