Shell
=====

---

Find all duplicate files based on MD5:

`find MyFolder/  -type f -exec md5sum '{}' ';' | sort | uniq --all-repeated=separate -w 15 > duplicates.txt`
