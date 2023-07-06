# ApoTrack

[Nature (2023) ](https://doi.org/10.1038/s41586-023-06303-1)
**Therapy-induced APOBEC3A drives evolution of persistent cancer cells**

Hideko Isozaki*, Ramin Sakhtemani, Ammal Abbasi, Naveed Nikpour, Marcello Stanzione, Sunwoo Oh, Adam Langenbucher, 
Susanna Monroe, Wenjia Su, Heidie Frisco Cabanos, Faria M. Siddiqui, Nicole Phan, Pégah Jalili, Daria Timonina, 
Samantha Bilton, Maria Gomez-Caraballo, Hannah L. Archibald, Varuna Nangia, Kristin Dionne, Amanda Riley, Matthew Lawlor, 
Mandeep Kaur Banwait, Rosemary G. Cobb, Lee Zou, Nicholas J. Dyson, Christopher J. Ott, Cyril Benes, Gad Getz, 
Chang S. Chan, Alice T. Shaw, Justin F. Gainor, Jessica J. Lin, Lecia V. Sequist, Zofia Piotrowska, Beow Y. Yeap, 
Jeffrey A. Engelman, Jake June-Koo Lee, Yosef E. Maruvka, Rémi Buisson, Michael S. Lawrence* & Aaron N. Hata*

## Analysis of APOBEC RNA editing in hairpins in coding sequences



Steps:

1. Identify APOBEC hairpin sites to use, using the ``survey_hairpins_rna`` command of [ApoHP](https://github.com/alangenb/ApoHP).

2. (optional) Filter sites to remove polymorphic/noisy sites, e.g. using dbSNP or an external panel of normals.

3. Get counts at the hairpin sites from your RNA-Seq BAM file(s), using the ``mpileup`` command of [samtools](http://www.htslib.org/).

4. Summarize counts to a total editing rate for each BAM, using our small utility [tallyedit](tallyedit.py).

e.g.

single-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.v1.0.bed --max-depth 5000 mysample.bam | python3 tallyedit.py
```


multi-bam mode

```
samtools mpileup -f hg19.fa -l apotrack.sites.hg19.v1.0.bed --max-depth 5000 -b bamlist.txt | python3 tallyedit.py
```



List of ApoTrack coding hairpin CAUC sites in hg19

verson 1.0:    [apotrack.sites.hg19.v1.0.bed](apotrack.sites.hg19.v1.0.bed) 

