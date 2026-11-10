Sposób użycia programu:

    py local_seq_align.py NazwaPliku.fasta

LUB

    py local_seq_align.py --fasta NazwaPliku.fasta

W terminalu zostanie podany wynik score i liczba dopasowań.

Wyznaczone dopasowania zostaną zapisane w pliku output.txt.


Przykład uruchomienia 1:

Wybrane sekwencje: Hemoglobina α człowieka (Homo sapiens - P69905) i królika (Oryctolagus cuniculus - P01948)

input1.txt:

>sp|P01948|HBA_RABIT Hemoglobin subunit alpha-1/2 OS=Oryctolagus cuniculus OX=9986 PE=1 SV=2
MVLSPADKTNIKTAWEKIGSHGGEYGAEAVERMFLGFPTTKTYFPHFDFTHGSEQIKAHG
KKVSEALTKAVGHLDDLPGALSTLSDLHAHKLRVDPVNFKLLSHCLLVTLANHHPSEFTP
AVHASLDKFLANVSTVLTSKYR

>sp|P69905|HBA_HUMAN Hemoglobin subunit alpha OS=Homo sapiens OX=9606 GN=HBA1 PE=1 SV=2
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG
KKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTP
AVHASLDKFLASVSTVLTSKYR

Wynik:

    PS C:\Users\gosia\Desktop\BioinfStruktularna\Laby\Algorytm-Smitha-Watermana> py local_seq_align.py --fasta input1.fasta
    Liczba dopasowań: 1
    Score = 92

    PS C:\Users\gosia\Desktop\BioinfStruktularna\Laby\Algorytm-Smitha-Watermana> py local_seq_align.py input1.fasta        
    Liczba dopasowań: 1
    Score = 92

output1.txt:
```
MVLSPADKTNIKTAWEKIGSHGGEYGAEAVERMFLGFPTTKTYFPHFDFTHGSEQIKAHGKKVSEALTKAVGHLDDLPGALSTLSDLHAHKLRVDPVNFKLLSHCLLVTLANHHPSEFTPAVHASLDKFLANVSTVLTSKYR
|||||||||| | || | | | ||||||| ||||| ||||||||||||  ||| | | |||||  ||| || | || | ||| |||||||||||||||||||||||||||| | | ||||||||||||||| ||||||||||
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR
```
Przykład uruchomienia 2:

Wybrane sekwencje: Hemoglobina α mamuta (Mammuthus primigenius - D3U1H8) i cytochrom b aksolotla (Ambystoma mexicanum - Q70ED6)

input2.txt:

>tr|D3U1H8|D3U1H8_MAMPR Hemoglobin subunit alpha OS=Mammuthus primigenius OX=37349 GN=HBA-T2 PE=1 SV=1
MVLSDNDKTNVKATWSKVGDHASDYVAEALERMFFSFPTTKTYFPHFDLSHGSGQVKGHG
KKVGEALTQAVGHLDDLPSALSALSDLHAHKLRVDPVNFKLLSHCLLVTLSSHQPTEFTP
EVHASLDKFLSNVSTVLTSKYR

>tr|Q70ED6|Q70ED6_AMBME Cytochrome b OS=Ambystoma mexicanum OX=8296 GN=cytb PE=3 SV=1
MAHIMRKTHPLMKIINNSFIDLPTPSNISYWWNFGSLLGLCLITQILTGLFLAMHYTADT
SSAFSSVAHICRDVNYGWLMRNIHANGASFFFICIFLHIGRGMYYGSYMFKETWNIGVIL
LFLVMATAFVGYVLPWGQMSFWGATVITNLLSAIPYMGDTLVQWIWGGFSVDKATLTRFF
AFHFLFPFLIAGTSIIHLLFLHETGSNNPTGMTSNQDKISFHPYFSYKDALGFMLMFILL
MFLSLFSPNLLGDPENFSPANPLITPPHIQPEWYFLFAYAILRSIPNKLGGVIALLMSIL
ILMLIPMLHTSKQRSMMFRPLTQIMFWILVANTMILTWIGGQPVEPPFIEIGQISSILYF
SLFIIIIPMIGILENKMMKW

Wynik:

    PS C:\Users\gosia\Desktop\BioinfStruktularna\Laby\Algorytm-Smitha-Watermana> py local_seq_align.py --fasta input2.fasta
    Liczba dopasowań: 9
    Score = 3  

    PS C:\Users\gosia\Desktop\BioinfStruktularna\Laby\Algorytm-Smitha-Watermana> py local_seq_align.py input2.fasta
    Liczba dopasowań: 9
    Score = 3  

output2.txt:

```
KAT
|||
KAT

LTQ
|||
LTQ

DLP
|||
DLP

LSA
|||
LSA

DPVNF
|| ||
DPENF

LLS
|||
LLS

FLS
|||
FLS

TSK
|||
TSK

TSKYR
||| |
TSKQR
```
