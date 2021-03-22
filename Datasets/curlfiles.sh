# Bash File for curl operations

#pwd
cd ..
#pwd
python -c "import FindingAProteinMotif; FindingAProteinMotif.file_manipulation1()"
# python FindingAProteinMotif.py

cd Datasets
#pwd
curl -L $(cat tobedown.txt) > download.txt

cd ..
#pwd
python -c "import FindingAProteinMotif; FindingAProteinMotif.check_protein_motif(\"Datasets/download.txt\")"

cd Datasets
rm tobedown.txt download.txt